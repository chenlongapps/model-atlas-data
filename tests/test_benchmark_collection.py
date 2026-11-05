import unittest
from unittest.mock import patch
import sys

from scripts import benchmark_collection
from scripts.benchmark_collection import matches


class BenchmarkCollectionTests(unittest.TestCase):
    def test_unspecified_definition_matches_omitted_or_explicit_sentinel_version(self):
        definition = {"name": "Humanity's Last Exam", "version": "unspecified", "metric": "accuracy"}
        omitted = {"name": "Humanity's Last Exam", "metric": "accuracy"}
        explicit = {"name": "Humanity's Last Exam", "version": "unspecified", "metric": "accuracy"}
        other_version = {"name": "Humanity's Last Exam", "version": "1.0", "metric": "accuracy"}
        wrong_metric = {"name": "Humanity's Last Exam", "metric": "score"}
        model = {"benchmarks": [omitted, explicit, other_version, wrong_metric]}

        self.assertEqual(matches(model, definition), [omitted, explicit])

    def test_declared_compatible_index_patch_version_matches_v5_family(self):
        definition = {
            "name": "Artificial Analysis Intelligence Index",
            "version": "5.0",
            "compatible_versions": ["5.0.1"],
            "metric": "index score",
        }
        exact = {"name": "Artificial Analysis Intelligence Index", "version": "5.0", "metric": "index score"}
        compatible = {"name": "Artificial Analysis Intelligence Index", "version": "5.0.1", "metric": "index score"}
        unsupported = {"name": "Artificial Analysis Intelligence Index", "version": "5.1", "metric": "index score"}
        model = {"benchmarks": [exact, compatible, unsupported]}

        self.assertEqual(matches(model, definition), [exact, compatible])

    def test_init_model_refreshes_global_progress_documents(self):
        with patch.object(sys, "argv", ["benchmark_collection.py", "--init-model", "lab/model"]), \
             patch.object(benchmark_collection, "initialize_model") as initialize, \
             patch.object(benchmark_collection, "refresh") as refresh:
            self.assertEqual(benchmark_collection.main(), 0)

        initialize.assert_called_once()
        refresh.assert_called_once()


if __name__ == "__main__":
    unittest.main()
