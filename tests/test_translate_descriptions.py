import io
import json
import subprocess
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from scripts import translate_descriptions as tr
from scripts.sync_models import check_staged, sync_models
from tests import test_sync_models as fixtures

MODEL = fixtures.MODEL


class TranslationTests(unittest.TestCase):
    def test_protected_fragments_round_trip_and_damage_is_rejected(self):
        source = 'Example 1.5 supports `code` at https://example.com and {user}.'
        protected, saved = tr.protect(source, 'Example')
        translated = protected.replace('supports', '支持').replace('at', '位于').replace('and', '和')
        result = tr.restore(translated, source, saved)
        for original in saved.values():
            self.assertIn(original, result)
        with self.assertRaisesRegex(tr.TranslationError, 'protected'):
            tr.restore(translated.replace(next(iter(saved)), 'broken'), source, saved)
        with self.assertRaisesRegex(tr.TranslationError, 'numbers'):
            tr.restore(translated + ' 100', source, saved)

    def test_conventional_translation_keeps_natural_text_and_validates_fragments(self):
        source = 'Example model with 128K context.'
        _, saved = tr.protect(source, 'Example')
        result = tr.restore('Example 模型，具有 128K 上下文。', source, saved, masked=False)
        self.assertIn('128K', result)
        with self.assertRaisesRegex(tr.TranslationError, 'protected'):
            tr.restore('示例模型，具有 128K 上下文。', source, saved, masked=False)
        candidates = {'lab/new': {'name': 'Example', 'description': source}}
        with patch.object(tr, 'run_worker', side_effect=[tr.TranslationError('failed'), result]) as worker:
            self.assertEqual(tr.translate_candidates(candidates)[1], {'lab/new': 'google'})
            self.assertEqual(worker.call_args_list[1].args[1], source)

    def test_empty_unchanged_and_non_chinese_are_rejected(self):
        for result in ('', 'Original', 'Different English text'):
            with self.subTest(result=result), self.assertRaises(tr.TranslationError):
                tr.restore(result, 'Original', {})

    def test_order_and_short_circuit(self):
        candidates = {'lab/new': {'name': 'Example', 'description': 'A language model.'}}
        with patch.object(tr, 'run_worker', side_effect=[tr.TranslationError('offline'), '语言模型。']) as worker:
            accepted, providers, failures = tr.translate_candidates(candidates)
        self.assertEqual(providers, {'lab/new': 'google'})
        self.assertEqual(accepted, {'lab/new': '语言模型。'})
        self.assertEqual([c.args[0] for c in worker.call_args_list], ['index', 'google'])
        self.assertEqual(failures, {'lab/new': {'index': 'offline'}})
        with patch.object(tr, 'run_worker', return_value='语言模型。') as worker:
            self.assertEqual(tr.translate_candidates(candidates)[1], {'lab/new': 'index'})
            self.assertEqual(worker.call_count, 1)

    def test_validation_failure_reaches_argos_and_total_failure_is_reported(self):
        candidates = {'lab/new': {'name': 'Example', 'description': 'A language model.'}}
        with patch.object(tr, 'run_worker', side_effect=['', 'Untranslated', '语言模型。']):
            self.assertEqual(tr.translate_candidates(candidates)[1], {'lab/new': 'argos'})
        with patch.object(tr, 'run_worker', side_effect=tr.TranslationError('unavailable')):
            accepted, providers, failures = tr.translate_candidates(candidates)
        self.assertEqual(accepted, {})
        self.assertEqual(set(failures['lab/new']), {'index', 'google', 'argos'})

    def test_disabled_backend_is_not_repeated_for_each_model(self):
        candidates = {f'lab/{i}': {'name': 'Example', 'description': 'A model.'} for i in range(2)}
        def call(backend, text, timeout):
            if backend == 'index':
                raise tr.TranslationError('access restriction', disable=True)
            return '模型。'
        with patch.object(tr, 'run_worker', side_effect=call) as worker:
            accepted, providers, failures = tr.translate_candidates(candidates)
        self.assertEqual(len(accepted), 2)
        self.assertEqual([c.args[0] for c in worker.call_args_list], ['index', 'google', 'google'])

    def test_exhausted_budget_skips_requests(self):
        candidates = {'lab/new': {'name': 'Example', 'description': 'A model.'}}
        with patch.object(tr.time, 'monotonic', side_effect=[0, 241, 300, 421, 500, 621]), patch.object(tr, 'run_worker') as worker:
            self.assertFalse(tr.translate_candidates(candidates)[0])
            worker.assert_not_called()

    def test_worker_enforces_timeout_and_does_not_send_text_as_argument(self):
        with patch.object(tr.subprocess, 'run', side_effect=subprocess.TimeoutExpired('worker', 1)) as run:
            with self.assertRaisesRegex(tr.TranslationError, 'timed out'):
                tr.run_worker('google', 'private source', 1)
        self.assertNotIn('private source', run.call_args.args[0])
        self.assertEqual(json.loads(run.call_args.kwargs['input']), {'text': 'private source'})
        self.assertEqual(run.call_args.kwargs['timeout'], 1)

    def response(self, data):
        response = io.BytesIO(json.dumps(data).encode())
        response.headers = {'Content-Type': 'application/json'}
        return response

    def test_index_configuration_and_truncation_retry(self):
        replies = [self.response({'choices': [{'finish_reason': 'length'}]}),
                   self.response({'choices': [{'finish_reason': 'stop', 'message': {'content': '模型。'}}]})]
        with patch.object(tr.request, 'urlopen', side_effect=replies) as request:
            self.assertEqual(tr.index_translate('A model.'), '模型。')
        payloads = [json.loads(c.args[0].data) for c in request.call_args_list]
        self.assertEqual([p['max_tokens'] for p in payloads], [1024, 2048])
        self.assertEqual(payloads[0]['chat_template_kwargs'], {'enable_thinking': False})
        self.assertFalse(payloads[0]['stream'])
        self.assertEqual(payloads[0]['temperature'], 0)
        self.assertNotIn('Authorization', dict(request.call_args.args[0].header_items()))

    def test_index_retries_rate_limits_and_stops_auth_failure(self):
        rate = HTTPError(tr.ENDPOINT, 429, 'rate limited', {'Retry-After': '3'}, None)
        with patch.object(tr.request, 'urlopen', side_effect=[rate] * 3), patch.object(tr.time, 'sleep') as sleep:
            with self.assertRaises(tr.TranslationError) as caught:
                tr.index_translate('text')
            self.assertTrue(caught.exception.disable)
            self.assertEqual(sleep.call_count, 2)
            sleep.assert_called_with(3)
        denied = HTTPError(tr.ENDPOINT, 403, 'denied', {}, None)
        with patch.object(tr.request, 'urlopen', side_effect=denied) as request:
            with self.assertRaises(tr.TranslationError):
                tr.index_translate('text')
            self.assertEqual(request.call_count, 1)

    def test_index_rejects_bad_responses(self):
        for data in ({}, [], {'choices': []}, {'choices': [{'finish_reason': 'stop', 'message': {}}]},
                     {'choices': [{'finish_reason': 'length'}]}):
            with self.subTest(data=data), patch.object(tr.request, 'urlopen', side_effect=lambda *a, **k: self.response(data)):
                with self.assertRaises(tr.TranslationError):
                    tr.index_translate('text')

    def test_index_html_and_invalid_json_are_failures(self):
        html = io.BytesIO(b'<html>challenge</html>')
        html.headers = {'Content-Type': 'text/html'}
        with patch.object(tr.request, 'urlopen', return_value=html):
            with self.assertRaises(tr.TranslationError) as caught:
                tr.index_translate('text')
            self.assertTrue(caught.exception.disable)
        broken = io.BytesIO(b'{')
        broken.headers = {'Content-Type': 'application/json'}
        with patch.object(tr.request, 'urlopen', return_value=broken):
            with self.assertRaisesRegex(tr.TranslationError, 'invalid JSON'):
                tr.index_translate('text')

    def test_invalid_worker_json_shape_is_a_backend_failure(self):
        with patch.object(tr.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '[]')):
            with self.assertRaises(tr.TranslationError):
                tr.run_worker('google', 'text', 1)


class LocalizationTests(unittest.TestCase):
    setUp = fixtures.SyncTests.setUp
    write = fixtures.SyncTests.write
    git = fixtures.SyncTests.git
    init_git = fixtures.SyncTests.init_git
    def translate(self, result=None, dry_run=False):
        self.write(self.upstream, 'models/lab/new.toml')
        value = result if result is not None else ({'lab/new': '示例模型。'}, {'lab/new': 'google'}, {})
        with patch('scripts.sync_models.translate_candidates', return_value=value) as translate:
            report = sync_models(self.upstream, self.root, dry_run, True)
        return report, translate

    def test_translation_appends_and_staged_guard_protects_old_entries(self):
        original = '[model.descriptions]\n# Keep this comment.\n"lab/existing" = "已有模型。"\n\n[benchmark.description]\n"bench" = "评测。"\n'
        locale = self.write(self.root, 'i18n/zh-CN.toml', original.encode())
        self.write(self.root, 'models/lab/existing.toml')
        self.init_git()
        report, _ = self.translate()
        self.assertEqual((self.root / 'models/lab/new.toml').read_bytes(), MODEL)
        self.assertIn('# Keep this comment.', locale.read_text())
        self.git('add', 'models/', 'i18n/')
        check_staged(self.root, report)
        content = locale.read_text().replace('已有模型。', '篡改模型。').encode()
        locale.write_bytes(content)
        self.git('add', 'i18n/')
        import hashlib
        report['translations']['files']['i18n/zh-CN.toml']['after'] = hashlib.sha256(content).hexdigest()
        with self.assertRaisesRegex(ValueError, 'unrelated'):
            check_staged(self.root, report)

    def test_failure_imports_model_without_writing_locale(self):
        report, _ = self.translate(({}, {}, {'lab/new': {'index': 'failed', 'google': 'missing', 'argos': 'missing'}}))
        self.assertTrue((self.root / 'models/lab/new.toml').exists())
        self.assertFalse((self.root / 'i18n').exists())
        self.assertEqual(report['translations']['accepted'], {})

    def test_dry_run_never_calls_translator(self):
        report, translate = self.translate(dry_run=True)
        translate.assert_not_called()
        self.assertEqual(report['translations']['pending'], ['lab/new'])
        self.assertFalse((self.root / 'models').exists())

    def test_repeat_and_existing_translation_do_not_trigger_backend_requests(self):
        self.translate()
        with patch('scripts.sync_models.translate_candidates', return_value=({}, {}, {})) as translate:
            report = sync_models(self.upstream, self.root, False, True)
            translate.assert_called_once_with({})
        self.assertEqual(report['added'], {})

    def test_locale_creation_passes_guard(self):
        self.init_git()
        report, _ = self.translate()
        self.git('add', 'models/', 'i18n/')
        check_staged(self.root, report)
        self.assertEqual(report['translations']['files']['i18n/zh-CN.toml']['before'], None)

    def test_preexisting_translation_is_never_overwritten(self):
        original = b'[model.descriptions]\n"lab/new" = "Keep"\n'
        locale = self.write(self.root, 'i18n/zh-CN.toml', original)
        self.write(self.upstream, 'models/lab/new.toml')
        with patch('scripts.sync_models.translate_candidates', return_value=({}, {}, {})) as translate:
            sync_models(self.upstream, self.root, False, True)
            translate.assert_called_once_with({})
        self.assertEqual(locale.read_bytes(), original)

    def test_guard_rejects_missing_file_report_and_unrelated_model_id(self):
        self.init_git()
        report, _ = self.translate()
        self.git('add', 'models/', 'i18n/')
        files = report['translations']['files']
        report['translations']['files'] = {}
        with self.assertRaisesRegex(ValueError, 'missing locale'):
            check_staged(self.root, report)
        report['translations']['files'] = files
        files['i18n/zh-CN.toml']['added'] = ['lab/not-added']
        with self.assertRaisesRegex(ValueError, 'not added'):
            check_staged(self.root, report)
