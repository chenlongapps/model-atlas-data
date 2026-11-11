import test from 'node:test';
import assert from 'node:assert/strict';
import { modelLab, labLogoUrl, routeFor, parseRoute, filterModels, filterBenchmarks, sortEntries, sortBenchmarkResults, buildIndex, description, loadData } from '../web/data.mjs';
import { messages, resolveLanguage, descriptionLocale } from '../web/i18n.mjs';
import { readFile } from 'node:fs/promises';
import { createSelect } from '../web/select.mjs';
import { groupModalities, renderModalities } from '../web/modalities.mjs';
import { hasBenchmarkCost, releaseTimestamp, costOptions, defaultChartAxis, chartPoints, conditionKey, comparisonGroups, scoreDomain, frontierUnavailable, paretoFront, median, numericDomain, axisTicks, formatTick, costAxis, formatCostTick, placeLabels, labColor } from '../web/chart-data.mjs';
import { createBenchmarkChart } from '../web/chart.mjs';

const models = {
  'lab/A': { name: 'Alpha', open_weights: true, release_date: '2025-01-01' },
  'lab/b': { name: 'Beta', open_weights: false, release_date: '2026-01-01' },
  'other/c': { name: 'Gamma' },
};
const definition = { name: 'Bench', version: '1', metric: 'accuracy', category: 'reasoning', organization: 'Org' };
const result = { name: 'Bench', version: '1', metric: 'accuracy', score: 42, dataset: 'set A', variant: 'no tools' };

test('modality grouping preserves MIME formats and unknown values', () => {
  assert.deepEqual(groupModalities(['text', 'text/plain', 'image/png', 'image/jpeg', 'image/png', 'application/pdf', 'pdf', 'embedding', 'audio/wav', 'video/mp4']), [
    { type: 'text', formats: ['text', 'text/plain'] },
    { type: 'image', formats: ['image/png', 'image/jpeg'] },
    { type: 'pdf', formats: ['application/pdf', 'pdf'] },
    { type: 'embedding', formats: ['embedding'] },
    { type: 'audio', formats: ['audio/wav'] },
    { type: 'video', formats: ['video/mp4'] },
  ]);
  assert.deepEqual(groupModalities(undefined), []);
  assert.deepEqual(groupModalities([]), []);
});

test('modality icons provide translated accessible labels and unknown types remain visible', () => {
  class Element {
    constructor() { this.children = []; this.attributes = {}; }
    setAttribute(name, value) { this.attributes[name] = value; }
    append(child) { this.children.push(child); }
  }
  const previousDocument = globalThis.document;
  globalThis.document = { createElement: () => new Element(), createElementNS: () => new Element() };
  try {
    assert.equal(renderModalities([], messages.en.modalityLabels), '—');
    const rendered = renderModalities(['image/png', 'image/jpeg', 'embedding', 'decision', 'reranking', 'future-type'], messages['zh-CN'].modalityLabels);
    assert.equal(rendered.children[0].attributes['aria-label'], '图片: image/png, image/jpeg');
    assert.equal(rendered.children[0].attributes.title, '图片: image/png, image/jpeg');
    assert.equal(rendered.children[0].children[0].attributes['aria-hidden'], 'true');
    for (const [index, label] of [[1, '嵌入'], [2, '决策'], [3, '重排序']]) {
      assert.equal(rendered.children[index].className, 'modality-icon');
      assert.equal(rendered.children[index].attributes['aria-label'], label);
      assert.equal(rendered.children[index].children.length, 1);
    }
    assert.equal(rendered.children[4].textContent, 'future-type');
    assert.equal(rendered.children[4].attributes['aria-label'], 'future-type');
  } finally { globalThis.document = previousDocument; }
});

test('lab logo URLs stay on the expected host and reject invalid IDs', () => {
  assert.equal(labLogoUrl('anthropic'), 'https://models.dev/logos/anthropic.svg');
  assert.equal(labLogoUrl('aion-labs'), 'https://models.dev/logos/aion-labs.svg');
  for (const lab of ['', '../anthropic', 'a/b', 'a?x', 'https://evil.example', null]) assert.equal(labLogoUrl(lab), null);
});

test('model IDs and encoded hash routes round-trip safely', () => {
  assert.equal(modelLab('lab/A'), 'lab');
  assert.equal(routeFor('models', 'lab/A'), '#/models/lab%2FA');
  assert.deepEqual(parseRoute('#/models/lab%2FA'), { kind: 'models', id: 'lab/A' });
  assert.deepEqual(parseRoute(routeFor('benchmarks', 'bench.1')), { kind: 'benchmarks', id: 'bench.1' });
  assert.deepEqual(parseRoute(''), { kind: 'models' });
  for (const hash of ['#/models/%ZZ', '#/models/invalid', '#/models/lab/A', '#/bad']) assert.equal(parseRoute(hash).kind, 'notfound');
});
test('model search, filters, missing weights and date sorting', () => {
  assert.deepEqual(filterModels(models, { query: 'LAB/A' }).map(([id]) => id), ['lab/A']);
  assert.deepEqual(filterModels(models, { query: 'ALPHA' }).map(([id]) => id), ['lab/A']);
  assert.deepEqual(filterModels(models, { lab: 'lab', weights: 'closed' }).map(([id]) => id), ['lab/b']);
  assert.deepEqual(filterModels(models, { weights: 'unknown' }).map(([id]) => id), ['other/c']);
  assert.deepEqual(filterModels(models, { lab: 'lab', sort: 'oldest' }).map(([id]) => id), ['lab/A', 'lab/b']);
  assert.deepEqual(filterModels(models).map(([id]) => id), ['lab/b', 'lab/A', 'other/c']);
});
test('benchmark search and dynamic category filter', () => {
  const defs = { b1: definition, b2: { ...definition, name: 'Other', category: 'coding' } };
  assert.deepEqual(filterBenchmarks(defs, { query: 'org', category: 'coding' }).map(([id]) => id), ['b2']);
  assert.deepEqual(filterBenchmarks(defs, { query: 'B1' }).map(([id]) => id), ['b1']);
  assert.deepEqual(filterBenchmarks(defs, { query: 'reasoning' }).map(([id]) => id), ['b1']);
});
test('benchmarks default to descending popularity, then name and ID without mutating definitions', () => {
  const defs = {
    missing: { ...definition, name: 'A missing' },
    zero: { ...definition, name: 'Zero', popularity: 0 },
    z: { ...definition, name: 'Beta', popularity: 0.8 },
    b: { ...definition, name: 'Alpha', popularity: 0.8 },
    a: { ...definition, name: 'Alpha', popularity: 0.8 },
    top: { ...definition, name: 'Z top', popularity: 1 },
  };
  const original = JSON.stringify(defs);
  assert.deepEqual(filterBenchmarks(defs).map(([id]) => id), ['top', 'a', 'b', 'z', 'zero', 'missing']);
  assert.equal(JSON.stringify(defs), original);
  assert.deepEqual(filterBenchmarks({ z: { name: 'Beta' }, a: { name: 'Alpha' } }).map(([id]) => id), ['a', 'z']);
  assert.deepEqual(filterBenchmarks({ b: {}, a: {} }).map(([id]) => id), ['a', 'b']);
});
test('benchmark search and category filtering preserve popularity order while table sorting overrides it', () => {
  const defs = {
    low: { ...definition, name: 'Alpha', popularity: 0.1 },
    high: { ...definition, name: 'Beta', popularity: 0.9 },
    other: { ...definition, name: 'Other', category: 'coding', popularity: 1 },
  };
  const filtered = filterBenchmarks(defs, { query: 'org', category: 'reasoning' });
  assert.deepEqual(filtered.map(([id]) => id), ['high', 'low']);
  assert.deepEqual(sortEntries(filtered, ([, item]) => item.name).map(([id]) => id), ['low', 'high']);
});
test('invalid or missing benchmark popularity stays behind explicit zero', () => {
  const values = [undefined, null, '', NaN, Infinity, -Infinity, '0.9', true, false, -0.1, 1.1];
  const defs = Object.fromEntries(values.map((popularity, i) => [String(i), { name: `Invalid ${i}`, popularity }]));
  defs.zero = { name: 'Zero', popularity: 0 };
  const sorted = filterBenchmarks(defs);
  assert.equal(sorted[0][0], 'zero');
  assert.equal(sorted.length, values.length + 1);
});
test('table sorting keeps missing values last in either direction without mutating entries', () => {
  const entries = [['c', {}], ['b', { n: 2 }], ['a', { n: 10 }]];
  assert.deepEqual(sortEntries(entries, ([, item]) => item.n).map(([id]) => id), ['b', 'a', 'c']);
  assert.deepEqual(sortEntries(entries, ([, item]) => item.n, 'desc').map(([id]) => id), ['a', 'b', 'c']);
  assert.deepEqual(entries.map(([id]) => id), ['c', 'b', 'a']);
});
test('benchmark results follow the scoring direction, keep ties stable and never drop records', () => {
  const entries = [
    { modelId: 'lab/z', result: { ...result, score: 0 } },
    { modelId: 'lab/b', result: { ...result, score: 42.12, effort: 'xhigh' } },
    { modelId: 'lab/a', result: { ...result, score: 42.12 } },
    { modelId: 'lab/b', result: { ...result, score: 42.12, effort: 'Adaptive/Max' } },
    { modelId: 'lab/c', result: { ...result, score: -1.5 } },
  ];
  const original = [...entries];
  assert.deepEqual(sortBenchmarkResults(entries, { higher_is_better: true }), [entries[2], entries[1], entries[3], entries[0], entries[4]]);
  assert.deepEqual(sortBenchmarkResults(entries, { higher_is_better: false }), [entries[4], entries[0], entries[2], entries[1], entries[3]]);
  assert.deepEqual(entries, original);
  assert.deepEqual(sortBenchmarkResults([], { higher_is_better: true }), []);
  for (const definition of [undefined, {}, { higher_is_better: 'false' }]) {
    assert.deepEqual(sortBenchmarkResults(entries, definition), original);
  }
});
test('benchmark sorting leaves missing or invalid scores last rather than treating them as zero', () => {
  const entries = [undefined, null, '', NaN, Infinity, '99', 0, -2, 1.25].map((score, i) => ({ modelId: `lab/${i}`, result: { score } }));
  for (const higher of [true, false]) {
    const sorted = sortBenchmarkResults(entries, { higher_is_better: higher });
    assert.deepEqual(sorted.slice(0, 3).map(entry => entry.result.score), higher ? [1.25, 0, -2] : [-2, 0, 1.25]);
    assert.deepEqual(sorted.slice(3), entries.slice(0, 6));
  }
});
test('exact association requires explicit version and metric and preserves every record', () => {
  const withoutVersion = { ...result }; delete withoutVersion.version;
  const withoutMetric = { ...result }; delete withoutMetric.metric;
  const differentMetric = { ...result, metric: 'other' };
  const anotherCondition = { ...result, variant: 'with tools', harness: 'H', future: { budget: 2 } };
  const input = { 'lab/a': { benchmarks: [result, withoutVersion, withoutMetric, differentMetric, anotherCondition] } };
  const index = buildIndex(input, { b1: definition });
  assert.deepEqual(index.byModel.get('lab/a').map(r => r.status), ['matched', 'unmatched', 'unmatched', 'unmatched', 'matched']);
  assert.equal(index.byBenchmark.get('b1').length, 2);
  assert.equal(index.byBenchmark.get('b1')[1].result, anotherCondition);
  assert.equal(index.byBenchmark.get('b1')[0].result.variant, 'no tools');
  assert.equal(index.byModel.get('lab/a')[1].result.version, undefined);
});
test('declared compatible benchmark versions map to the same definition', () => {
  const compatibleDefinition = { ...definition, version: '4.0.0', compatible_versions: ['4.0'] };
  const results = [
    { ...result, version: '4.0.0' },
    { ...result, version: '4.0' },
  ];
  const index = buildIndex({ 'lab/a': { benchmarks: results } }, { terminalBench: compatibleDefinition });
  assert.deepEqual(index.byModel.get('lab/a').map(entry => entry.status), ['matched', 'matched']);
  assert.deepEqual(index.byBenchmark.get('terminalBench').map(entry => entry.result), results);
});
test('multiple exact candidates remain ambiguous', () => {
  const index = buildIndex({ 'lab/a': { benchmarks: [result] } }, { b1: definition, b2: { ...definition } });
  assert.equal(index.byModel.get('lab/a')[0].status, 'ambiguous');
  assert.equal(index.byModel.get('lab/a')[0].benchmarkId, undefined);
  assert.equal(index.byBenchmark.get('b1').length, 0);
});
test('optional effort stays separate from variant and does not change definition association', () => {
  const results = [result, { ...result, effort: 'xhigh' }, { ...result, effort: 'Adaptive/Max' }];
  const index = buildIndex({ 'lab/a': { benchmarks: results } }, { b1: definition });
  assert.deepEqual(index.byModel.get('lab/a').map(r => r.status), ['matched', 'matched', 'matched']);
  assert.deepEqual(index.byBenchmark.get('b1').map(r => r.result), results);
  assert.equal(Object.hasOwn(results[0], 'effort'), false);
  assert.deepEqual(results.map(r => r.variant), ['no tools', 'no tools', 'no tools']);
});
test('benchmark model counts deduplicate conditions and exclude unmatched or ambiguous records', () => {
  const ambiguous = { ...definition, name: 'Ambiguous' };
  const defs = { b1: definition, empty: { ...definition, version: '2' }, a1: ambiguous, a2: { ...ambiguous } };
  const index = buildIndex({
    'lab/a': { benchmarks: [result, { ...result, effort: 'xhigh' }, { ...result, source: 'https://example.com' }] },
    'lab/b': { benchmarks: [result] },
    'lab/c': { benchmarks: [{ ...result, version: undefined }, { ...result, metric: 'other' }, { ...result, name: 'Ambiguous' }] },
    'lab/d': {},
  }, defs);
  assert.equal(index.byBenchmark.get('b1').length, 4);
  assert.deepEqual([...index.modelCountByBenchmark], [['b1', 2], ['empty', 0], ['a1', 0], ['a2', 0]]);
  assert.equal(buildIndex().modelCountByBenchmark.size, 0);
  assert.deepEqual(sortEntries(Object.entries(defs), ([id]) => index.modelCountByBenchmark.get(id), 'desc').map(([id]) => id), ['b1', 'a1', 'a2', 'empty']);
});
test('empty input and missing localization fall back', () => {
  assert.deepEqual(filterModels(), []);
  assert.deepEqual(filterBenchmarks(), []);
  assert.equal(buildIndex().byModel.size, 0);
  assert.equal(description({}, 'model', 'lab/a', 'original'), 'original');
  assert.equal(description({ model: { descriptions: { 'lab/a': '中文' } } }, 'model', 'lab/a', 'original'), '中文');
  assert.equal(description({}, 'benchmark', 'b', undefined), '');
});
test('optional manifest and locale failures do not block the page; required errors do', async () => {
  const calls = [];
  const fetcher = async path => {
    calls.push(path);
    if (path.includes('manifest')) throw new Error('offline');
    if (path.includes('i18n')) return { ok: false, status: 404 };
    return { ok: true, json: async () => ({}) };
  };
  const loaded = await loadData(fetcher);
  assert.equal(loaded.manifest, null);
  assert.deepEqual(loaded.locale, {});
  assert.equal(loaded.index.byModel.size, 0);
  assert.equal(calls.length, 4);
  await assert.rejects(loadData(async () => ({ ok: false, status: 500 })), /models.json/);
});
test('language preference overrides browser languages; unsupported languages fall back', () => {
  assert.equal(resolveLanguage('en', ['zh-CN']), 'en');
  assert.equal(resolveLanguage('zh-CN', ['en-US']), 'zh-CN');
  assert.equal(resolveLanguage(null, ['fr-FR', 'zh-Hans']), 'zh-CN');
  assert.equal(resolveLanguage('invalid', ['fr', 'en-GB']), 'en');
  assert.equal(resolveLanguage(null, ['fr-FR']), 'en');
  assert.equal(resolveLanguage(null), 'en');
});
test('both languages cover all UI message keys and static HTML references', async () => {
  const keys = Object.keys(messages.en).sort();
  assert.deepEqual(Object.keys(messages['zh-CN']).sort(), keys);
  for (const key of keys) {
    assert.equal(typeof messages.en[key], typeof messages['zh-CN'][key], key);
    assert.ok(messages.en[key] && messages['zh-CN'][key], key);
  }
  const html = await readFile(new URL('../web/index.html', import.meta.url), 'utf8');
  for (const [, key] of html.matchAll(/data-i18n(?:-aria|-placeholder)?="([^"]+)"/g)) {
    assert.equal(typeof messages.en[key], 'string', key);
  }
  const app = await readFile(new URL('../web/app.mjs', import.meta.url), 'utf8');
  for (const [, key] of app.matchAll(/\bT\.([A-Za-z][A-Za-z0-9]*)/g)) assert.ok(Object.hasOwn(messages.en, key), key);
  const chart = await readFile(new URL('../web/chart.mjs', import.meta.url), 'utf8');
  for (const [, key] of chart.matchAll(/\bT\.([A-Za-z][A-Za-z0-9]*)/g)) assert.ok(Object.hasOwn(messages.en, key), key);
  for (const reason of ['costOnly', 'direction', 'empty']) assert.equal(typeof messages.en[`chartFrontier_${reason}`], 'string');
});
test('descriptions follow the selected language and preserve fallback', () => {
  const locale = { model: { descriptions: { 'lab/a': '中文' } }, benchmark: { description: { b: '评测' } } };
  assert.equal(description(descriptionLocale('zh-CN', locale), 'model', 'lab/a', 'original'), '中文');
  assert.equal(description(descriptionLocale('en', locale), 'model', 'lab/a', 'original'), 'original');
  assert.equal(description(descriptionLocale('zh-CN', locale), 'benchmark', 'b', 'benchmark'), '评测');
  assert.equal(description(descriptionLocale('en', locale), 'benchmark', 'b', 'benchmark'), 'benchmark');
  assert.equal(description(descriptionLocale('zh-CN', {}), 'model', 'lab/a', 'original'), 'original');
});

test('detail pages preserve results, optional prices and parameter provenance', async t => {
  class Element {
    constructor(tag = '') { this.tag = tag; this.children = []; this.attributes = {}; this.dataset = {}; this.handlers = {}; this.classList = { toggle() {} }; }
    setAttribute(name, value) { this.attributes[name] = value; }
    removeAttribute(name) { delete this.attributes[name]; }
    append(...children) { this.children.push(...children); }
    replaceChildren(...children) { this.children = children; }
    addEventListener(name, handler) { this.handlers[name] = handler; }
    querySelectorAll() { return []; }
    querySelector(tag) { return this.children.filter(child => child instanceof Element).map(child => child.tag === tag ? child : child.querySelector(tag)).find(Boolean); }
    focus() {}
    set textContent(value) { this.children = [String(value)]; }
    get textContent() { return this.children.map(child => child instanceof Element ? child.textContent : String(child)).join(''); }
  }
  const nodes = new Map();
  const select = selector => {
    if (!nodes.has(selector)) nodes.set(selector, new Element());
    return nodes.get(selector);
  };
  const handlers = {};
  let rendered;
  const ready = new Promise(resolve => { rendered = resolve; });
  select('.page-scroll').scrollTo = rendered;
  const ambiguousDefinition = { ...definition, name: 'Ambiguous bench' };
  const defs = { b1: { ...definition, higher_is_better: true, popularity: 0.9 }, b2: ambiguousDefinition, b3: { ...ambiguousDefinition }, b4: { ...definition, name: 'Matched bench', popularity: 0.5 } };
  const fixture = {
    'lab/a': { name: 'Alpha', release_date: '2026-01-01', benchmarks: [{ ...result, score: 10 }] },
    'lab/b': { name: 'Beta', release_date: '2026-02-01', benchmarks: [{ ...result, score: 20, effort: 'Adaptive/Max', harness: 'H', future: { budget: 2 } }] },
    'lab/c': { name: 'Gamma', benchmarks: [
      { ...result, name: 'Zulu', score: 99 },
      { ...result, name: 'Matched bench', score: 2, effort: 'xhigh' },
      { ...result, name: 'Alpha', score: 1 },
      { ...result, name: 'Matched bench', score: 3, effort: 'Adaptive/Max' },
      { ...result, name: 'Ambiguous bench', score: 4 },
    ] },
  };
  const globals = {
    Node: Element,
    document: { createElement: tag => new Element(tag), createElementNS: (_, tag) => new Element(tag), createTextNode: String, querySelector: select, querySelectorAll: () => [], addEventListener() {}, documentElement: new Element() },
    window: { addEventListener: (name, handler) => { handlers[name] = handler; } },
    location: { hash: '#/benchmarks/b1' },
    navigator: { languages: ['en'] },
    localStorage: { getItem: () => null },
    fetch: async path => ({ ok: true, json: async () => path === './models.json' ? fixture : path === './benchmarks.json' ? defs : null }),
  };
  const previous = new Map(Object.keys(globals).map(key => [key, Object.getOwnPropertyDescriptor(globalThis, key)]));
  const find = (node, tag) => node.tag === tag ? node : node.children.filter(child => child instanceof Element).map(child => find(child, tag)).find(Boolean);
  const resultTable = () => find(select('#main'), 'table');
  const cells = row => row.children.map(cell => cell.textContent);
  try {
    for (const [key, value] of Object.entries(globals)) Object.defineProperty(globalThis, key, { configurable: true, writable: true, value });
    await import('../web/app.mjs');
    await ready;
    await t.test('benchmark listing defaults to popularity and allows manual model-count sorting including zero', () => {
      globals.location.hash = '#/benchmarks';
      handlers.hashchange();
      const headers = find(resultTable(), 'thead').children[0].children;
      assert.equal(headers[5].textContent, 'Included models ↕');
      const counts = () => find(resultTable(), 'tbody').children.map(row => cells(row)[5]);
      assert.deepEqual(counts(), ['2', '1', '0', '0']);
      assert.deepEqual(find(resultTable(), 'tbody').children.map(row => find(row.children[0], 'a').attributes.href),
        ['#/benchmarks/b1', '#/benchmarks/b4', '#/benchmarks/b2', '#/benchmarks/b3']);
      find(headers[5], 'button').handlers.click();
      assert.deepEqual(counts(), ['0', '0', '1', '2']);
      assert.equal(find(resultTable(), 'thead').children[0].children[5].attributes['aria-sort'], 'ascending');
      find(find(resultTable(), 'thead').children[0].children[5], 'button').handlers.click();
      assert.deepEqual(counts(), ['2', '1', '0', '0']);
      assert.equal(find(resultTable(), 'thead').children[0].children[5].attributes['aria-sort'], 'descending');
      globals.location.hash = '#/benchmarks/b1';
      handlers.hashchange();
    });
    assert.deepEqual(cells(find(resultTable(), 'thead').children[0]), ['Model', 'Score', 'Effort', 'Metric', 'Version', 'Test conditions', 'Source']);
    const rows = find(resultTable(), 'tbody').children;
    assert.deepEqual(cells(rows[0]).slice(0, 5), ['Beta', '20.0', 'Adaptive/Max', 'accuracy', '1']);
    assert.equal(cells(rows[1])[1], '10.0');
    assert.equal(cells(rows[1])[2], '—');
    assert.match(cells(rows[0])[5], /variant: no tools/);
    assert.match(cells(rows[0])[5], /harness: H/);
    assert.match(cells(rows[0])[5], /future: \{"budget":2\}/);
    assert.doesNotMatch(cells(rows[0])[5], /effort|Adaptive\/Max/);
    assert.ok(select('#main').textContent.includes(messages.en.sortedResultNote));

    defs.b1.higher_is_better = false;
    handlers.hashchange();
    assert.equal(cells(find(resultTable(), 'tbody').children[0])[0], 'Alpha');

    fixture['lab/a'].benchmarks[0].score = 10.11;
    fixture['lab/b'].benchmarks[0].score = 10.14;
    defs.b1.higher_is_better = true;
    handlers.hashchange();
    assert.deepEqual(find(resultTable(), 'tbody').children.map(row => cells(row).slice(0, 2)), [['Beta', '10.1'], ['Alpha', '10.1']]);
    assert.equal(fixture['lab/a'].benchmarks[0].score, 10.11);
    assert.equal(fixture['lab/b'].benchmarks[0].score, 10.14);

    const pricedResult = fixture['lab/b'].benchmarks[0];
    Object.assign(pricedResult, { cost: 0.28440671352465285, cost_unit: 'USD/weighted task', cost_source: 'https://example.com/cost' });
    const originalPricedResult = structuredClone(pricedResult);
    handlers.hashchange();
    assert.deepEqual(cells(find(resultTable(), 'thead').children[0]), ['Model', 'Score', 'Price', 'Effort', 'Metric', 'Version', 'Test conditions', 'Source']);
    let pricedRows = find(resultTable(), 'tbody').children;
    assert.deepEqual(pricedRows.map(row => cells(row).slice(0, 2)), [['Beta', '10.1'], ['Alpha', '10.1']]);
    assert.ok(cells(pricedRows[0])[2].startsWith('$0.28'));
    assert.doesNotMatch(cells(pricedRows[0])[2], /USD|weighted task|0\.2844/);
    const priceDisplay = find(pricedRows[0].children[2], 'span');
    assert.equal(priceDisplay.attributes.title, '0.28440671352465285 USD/weighted task');
    assert.equal(priceDisplay.attributes['aria-label'], priceDisplay.attributes.title);
    assert.equal(find(pricedRows[0].children[2], 'a').attributes.href, pricedResult.cost_source);
    assert.equal(cells(pricedRows[1])[2], '—');
    assert.doesNotMatch(cells(pricedRows[0])[6], /cost|USD\/weighted task/);
    assert.match(cells(pricedRows[0])[6], /variant: no tools/);
    assert.match(cells(pricedRows[0])[6], /future: \{"budget":2\}/);
    assert.deepEqual(pricedResult, originalPricedResult);

    delete pricedResult.cost_source;
    pricedResult.cost = 0;
    pricedResult.cost_unit = 'USD/test';
    pricedResult.source = 'https://example.com/result';
    handlers.hashchange();
    pricedRows = find(resultTable(), 'tbody').children;
    assert.ok(cells(pricedRows[0])[2].startsWith('$0.00'));
    assert.doesNotMatch(cells(pricedRows[0])[2], /USD|\/test/);
    assert.equal(find(pricedRows[0].children[2], 'a').attributes.href, pricedResult.source);
    assert.equal(find(pricedRows[0].children[7], 'a').attributes.href, pricedResult.source);

    pricedResult.cost_source = 'javascript:alert(1)';
    handlers.hashchange();
    const unlinkedCost = find(resultTable(), 'tbody').children[0].children[2];
    assert.equal(unlinkedCost.textContent, '$0.00');
    assert.equal(find(unlinkedCost, 'a'), undefined);
    assert.equal(find(unlinkedCost, 'span').attributes.title, '0 USD/test');

    for (const [cost, unit, expected] of [
      [12, 'CNY/task', '¥12.00'],
      [12.346, 'USD/evaluation', '$12.35'],
      [0.001, 'USD/test', '$0.00'],
      [12.3, 'JPY/task', '¥12.30'],
      [12.3, 'EUR/task', '€12.30'],
      [12.3, 'GBP/task', '£12.30'],
      [12.3, 'KRW/task', '₩12.30'],
      [12.3, 'INR/task', '₹12.30'],
      [12.3, 'XYZ/task', 'XYZ 12.30'],
    ]) {
      pricedResult.cost = cost;
      pricedResult.cost_unit = unit;
      const original = structuredClone(pricedResult);
      handlers.hashchange();
      const cell = find(resultTable(), 'tbody').children[0].children[2];
      assert.equal(cell.textContent, expected);
      assert.equal(find(cell, 'span').attributes.title, `${cost} ${unit}`);
      assert.deepEqual(pricedResult, original);
    }

    globals.location.hash = '#/benchmarks/b4';
    handlers.hashchange();
    assert.ok(!cells(find(resultTable(), 'thead').children[0]).includes('Price'));
    globals.location.hash = '#/benchmarks/b1';
    delete pricedResult.cost;
    delete pricedResult.cost_unit;
    delete pricedResult.cost_source;
    handlers.hashchange();
    assert.ok(!cells(find(resultTable(), 'thead').children[0]).includes('Price'));

    globals.location.hash = '#/models/lab%2Fb';
    handlers.hashchange();
    assert.deepEqual(cells(find(resultTable(), 'thead').children[0]), ['Benchmark', 'Score', 'Effort', 'Metric', 'Version', 'Test conditions', 'Source']);
    assert.equal(cells(find(resultTable(), 'tbody').children[0])[2], 'Adaptive/Max');
    assert.doesNotMatch(cells(find(resultTable(), 'tbody').children[0])[5], /effort|Adaptive\/Max/);
    assert.ok(select('#main').textContent.includes(messages.en.resultNote));
    for (const [score, displayed] of [[42, '42.0'], [42.16, '42.2'], [0, '0.0'], [-1.26, '-1.3']]) {
      fixture['lab/b'].benchmarks[0].score = score;
      handlers.hashchange();
      assert.equal(cells(find(resultTable(), 'tbody').children[0])[1], displayed);
      assert.equal(fixture['lab/b'].benchmarks[0].score, score);
    }

    const originalResults = structuredClone(fixture['lab/c'].benchmarks);
    globals.location.hash = '#/models/lab%2Fc';
    handlers.hashchange();
    const modelRows = find(resultTable(), 'tbody').children;
    assert.deepEqual(modelRows.map(row => cells(row).slice(0, 3)), [
      ['Alpha', '1.0', '—'],
      [`Ambiguous bench ${messages.en.ambiguous}`, '4.0', '—'],
      ['Matched bench', '2.0', 'xhigh'],
      ['Matched bench', '3.0', 'Adaptive/Max'],
      ['Zulu', '99.0', '—'],
    ]);
    assert.doesNotMatch(resultTable().textContent, /Unmatched/);
    assert.equal(find(modelRows[0].children[0], 'a'), undefined);
    assert.equal(find(modelRows[1].children[0], 'a'), undefined);
    assert.equal(find(modelRows[2].children[0], 'a').attributes.href, '#/benchmarks/b4');
    for (const row of modelRows) assert.doesNotMatch(cells(row)[5], /effort|xhigh|Adaptive\/Max/);
    assert.deepEqual(fixture['lab/c'].benchmarks, originalResults);
    globals.location.hash = '#/models/lab%2Fa';
    handlers.hashchange();
    globals.location.hash = '#/models/lab%2Fc';
    handlers.hashchange();
    assert.deepEqual(find(resultTable(), 'tbody').children.map(cells), modelRows.map(cells));

    await t.test('model parameters keep precision, independent components and safe provenance links', () => {
      const model = fixture['lab/a'];
      globals.location.hash = '#/models/lab%2Fa';
      const parameterSection = () => select('#main').children.find(node => find(node, 'h2')?.textContent === messages.en.modelParameters);
      const counts = () => find(parameterSection(), 'dl').children.map(fact => find(fact, 'dd').textContent);
      const sources = node => {
        const links = [];
        const visit = child => {
          if (!(child instanceof Element)) return;
          if (child.tag === 'a') links.push(child);
          child.children.forEach(visit);
        };
        visit(node);
        return links;
      };
      handlers.hashchange();
      assert.equal(parameterSection().children[1].textContent, messages.en.noParameters);
      assert.equal(find(parameterSection(), 'table'), undefined);

      model.metadata = { modelatlas: { parameters: {
        total_billion: 671, active_billion: 37,
        sources: ['https://example.com/full', 'https://example.com/paper'], notes: 'Reported approximate counts.',
      } } };
      const parameters = model.metadata.modelatlas.parameters;
      let original = structuredClone(parameters);
      handlers.hashchange();
      assert.equal(select('#main').children[2], parameterSection());
      assert.deepEqual(counts(), ['671 B', '37 B']);
      assert.ok(parameterSection().textContent.includes(parameters.notes));
      assert.ok(parameterSection().textContent.includes(messages.en.parameterUnit));
      assert.deepEqual(sources(parameterSection()).map(link => link.attributes.href), parameters.sources);
      for (const link of sources(parameterSection())) {
        assert.equal(link.attributes.target, '_blank');
        assert.equal(link.attributes.rel, 'noopener noreferrer');
      }
      assert.deepEqual(parameters, original);

      for (const value of [0.35, 8.123456789, 0.000001, 1000]) {
        parameters.total_billion = value;
        delete parameters.active_billion;
        handlers.hashchange();
        assert.deepEqual(counts(), [`${value} B`, '—']);
        assert.equal(find(parameterSection(), 'table'), undefined);
      }
      delete parameters.total_billion;
      parameters.active_billion = 3;
      handlers.hashchange();
      assert.deepEqual(counts(), ['—', '3 B']);
      delete parameters.active_billion;
      delete parameters.sources;
      parameters.notes = 'Only component counts are disclosed.';
      parameters.components = [
        { name: 'Multimodal Decoder', total_billion: 12, active_billion: 3, sources: ['https://example.com/decoder'], notes: 'Decoder only.' },
        { name: 'Vision Encoder', total_billion: 0.4, sources: ['https://example.com/encoder'], notes: 'Vision weights only.' },
        { name: 'Active component', active_billion: 0.1, sources: ['https://example.com/active'] },
      ];
      original = structuredClone(parameters);
      handlers.hashchange();
      assert.deepEqual(counts(), ['—', '—']);
      let componentTable = find(parameterSection(), 'table');
      assert.deepEqual(cells(find(componentTable, 'thead').children[0]), ['Component', 'Total parameters', 'Active parameters per token']);
      const rows = find(componentTable, 'tbody').children;
      assert.deepEqual(rows.map(row => cells(row).slice(1)), [['12 B', '3 B'], ['0.4 B', '—'], ['—', '0.1 B']]);
      rows.forEach((row, index) => {
        const component = parameters.components[index];
        assert.ok(row.children[0].textContent.startsWith(component.name));
        if (component.notes) assert.ok(row.children[0].textContent.includes(component.notes));
        assert.deepEqual(sources(row).map(link => link.attributes.href), component.sources);
      });
      assert.deepEqual(parameters, original);

      parameters.total_billion = 20;
      parameters.sources = ['https://example.com/full', 'javascript:alert(1)', 'data:text/html,unsafe', 'not a URL'];
      parameters.notes = '<script>untrusted notes</script>';
      handlers.hashchange();
      assert.deepEqual(counts(), ['20 B', '—']);
      assert.deepEqual(sources(parameterSection()).map(link => link.attributes.href), ['https://example.com/full', ...parameters.components.flatMap(component => component.sources)]);
      assert.ok(parameterSection().textContent.includes(parameters.notes));
      assert.equal(find(parameterSection(), 'script'), undefined);

      // Use the actual language selector to check translated labels and rerendering.
      const languagePicker = select('#language').children[0];
      languagePicker.children[1].children[1].handlers.click();
      const translated = select('#main').children[2];
      assert.equal(find(translated, 'h2').textContent, messages['zh-CN'].modelParameters);
      assert.deepEqual(find(translated, 'dl').children.map(fact => find(fact, 'dt').textContent), [messages['zh-CN'].totalParameters, messages['zh-CN'].activeParameters]);
      assert.deepEqual(find(translated, 'dl').children.map(fact => find(fact, 'dd').textContent), ['20 B', '—']);
      componentTable = find(translated, 'table');
      assert.deepEqual(cells(find(componentTable, 'thead').children[0]), ['组件', '总参数量', '每 token 激活参数量']);
      assert.ok(translated.textContent.includes(parameters.notes));
      assert.ok(translated.textContent.includes(messages['zh-CN'].parameterUnit));
      delete model.metadata;
      handlers.hashchange();
      assert.equal(select('#main').children[2].children[1].textContent, messages['zh-CN'].noParameters);
    });
  } finally {
    for (const [key, descriptor] of previous) {
      if (descriptor) Object.defineProperty(globalThis, key, descriptor); else delete globalThis[key];
    }
  }
});

const deepDefinition = { name: 'DeepSWE', version: '1.1', metric: 'pass@1', unit: 'percent', higher_is_better: true };
const deepResult = {
  name: 'DeepSWE', version: '1.1', metric: 'pass@1', score: 50, cost: 1.234567891, cost_unit: 'USD/task',
  dataset: '113 tasks', harness: 'mini-swe-agent', effort: 'high',
  variant: '4 whole-benchmark passes; 113 tasks attempted; 452 scored attempts; provider/verifier/network errors excluded',
  source: 'https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json',
};

test('chart costs keep exact bases, finite values, true zero and source precision', () => {
  for (const cost of [0, 0.0000001, 1.234567891]) assert.equal(hasBenchmarkCost({ cost, cost_unit: 'USD/task' }), true);
  for (const cost of [undefined, null, '', '1', -1, NaN, Infinity]) assert.equal(hasBenchmarkCost({ cost, cost_unit: 'USD/task' }), false);
  for (const cost_unit of [undefined, '', ' ', null, 1]) assert.equal(hasBenchmarkCost({ cost: 1, cost_unit }), false);
  const results = [deepResult, { ...deepResult, cost: 0 }, { ...deepResult, cost_unit: 'USD/test' }, { ...deepResult, cost_unit: 'USD/task ' }, { ...deepResult, score: NaN }, { ...deepResult, cost: -1 }];
  const entries = results.map(result => ({ modelId: 'lab/A', result }));
  const original = structuredClone(entries);
  assert.deepEqual(costOptions(entries), [['USD/task', 2], ['USD/task ', 1], ['USD/test', 1]]);
  assert.deepEqual(chartPoints(entries, models, 'cost', 'USD/task').map(point => point.x), [1.234567891, 0]);
  assert.deepEqual(chartPoints(entries, models, 'cost'), []);
  assert.deepEqual(chartPoints(entries, models, 'other', 'USD/task'), []);
  assert.deepEqual(entries, original);
});

test('bar defaults include costless results without requiring release dates or inventing scores', () => {
  const entries = [
    { modelId: 'lab/a', result: { ...result, score: 0 } },
    { modelId: 'lab/a', result: { ...result, score: 42.123456789, cost: 0, cost_unit: 'USD/task' } },
    { modelId: 'lab/b', result: { ...result, score: '43 ± 1' } },
    { modelId: 'lab/c', result: { ...result, score: null } },
    { modelId: 'lab/d', result: { ...result, score: NaN } },
  ];
  const original = structuredClone(entries);
  assert.equal(defaultChartAxis(entries), 'score');
  assert.equal(defaultChartAxis(entries.slice(0, 1)), 'score');
  assert.equal(defaultChartAxis(entries.slice(1)), 'cost'); // Non-numeric scores do not have chart coordinates.
  assert.equal(defaultChartAxis([]), 'score');
  assert.equal(defaultChartAxis(entries.slice(2)), 'score');
  const points = chartPoints(entries, {}, 'score');
  assert.deepEqual(points.map(point => point.y), [0, 42.123456789]);
  assert.ok(points.every(point => point.release === undefined));
  assert.equal(new Set(points.map(point => point.id)).size, 2);
  assert.deepEqual(entries, original);
});

test('bar condition filters include singleton groups without merging original configurations', () => {
  const entries = [
    { modelId: 'lab/a', result: { ...result, score: 2, source: 'https://example.com/a' } },
    { modelId: 'lab/b', result: { ...result, score: 3, source: 'https://example.com/a' } },
    { modelId: 'lab/a', result: { ...result, score: 4, source: 'https://example.com/a', effort: 'default' } },
    { modelId: 'lab/c', result: { ...result, score: 5, source: 'https://example.com/b' } },
    { modelId: 'lab/a', result: { ...result, score: 2, source: 'https://example.com/a', cost: 1, cost_unit: 'USD/test' } },
    { modelId: 'lab/a', result: { ...result, score: 6, source: 'https://example.com/a', future: { budget: 8 } } },
  ];
  const points = chartPoints(entries, {}, 'score');
  const original = structuredClone(points);
  const groups = comparisonGroups(points, { includeSingletons: true });
  assert.equal(groups.length, 4);
  assert.equal(groups.flatMap(group => group.points).length, points.length);
  assert.equal(new Set(groups.flatMap(group => group.points.map(point => point.id))).size, points.length);
  assert.deepEqual(points, original);
  assert.deepEqual(scoreDomain([0]), [0, 1]);
  assert.deepEqual(scoreDomain([]), [0, 1]);
  assert.equal(scoreDomain([2, 3])[0], 0);
  assert.equal(scoreDomain([-3, -1])[1], 0);
  assert.ok(scoreDomain([-3, 5])[0] < -3);
  assert.ok(scoreDomain([-3, 5])[1] > 5);
});

test('release coordinates use strict UTC model dates, not result dates or normalized invalid dates', () => {
  assert.equal(releaseTimestamp('1970-01-01'), 0);
  assert.equal(releaseTimestamp('2024-02-29'), Date.UTC(2024, 1, 29));
  for (const value of ['2026-02-29', '2026-04-31', '2026-13-01', '2026-00-01', '2026-1-01', '2026-01', '2026-01-01T00:00:00Z', undefined]) assert.equal(releaseTimestamp(value), undefined);
  const entries = [{ modelId: 'lab/A', result: { ...deepResult, date: '2020-01-01' } }, { modelId: 'other/c', result: deepResult }];
  const points = chartPoints(entries, models, 'release');
  assert.equal(points.length, 1);
  assert.equal(points[0].x, Date.UTC(2025, 0, 1));
  assert.equal(points[0].release, '2025-01-01');
});

test('Pareto front uses strict improvements, preserves tied observations and both scoring directions', () => {
  const points = [[0, 0], [1, 2], [1, 2], [1, 1], [2, 2], [3, 3], [4, -1]].map(([x, y], i) => ({ x, y, id: i }));
  const original = structuredClone(points);
  assert.deepEqual(paretoFront(points, true).map(point => point.id), [0, 1, 2, 5]);
  assert.deepEqual(paretoFront(points, false).map(point => point.id), [0, 6]);
  assert.deepEqual(paretoFront(points, undefined), []);
  assert.deepEqual(paretoFront([], true), []);
  assert.deepEqual(paretoFront([{ x: -1, y: 99 }, { x: Infinity, y: 99 }, { x: 0, y: NaN }], true), []);
  assert.deepEqual(points, original);
  // Compare the optimized algorithm against the definition of dominance.
  const sample = Array.from({ length: 80 }, (_, i) => ({ x: (i * 7) % 13, y: (i * 19) % 23, id: i }));
  for (const higher of [true, false]) {
    const expected = sample.filter(a => !sample.some(b => b.x <= a.x && (higher ? b.y >= a.y : b.y <= a.y) && (b.x < a.x || b.y !== a.y)));
    assert.deepEqual(new Set(paretoFront(sample, higher).map(point => point.id)), new Set(expected.map(point => point.id)));
  }
});

test('exploratory frontier needs only cost coordinates and a known scoring direction, even for one model', () => {
  const entries = ['lab/A', 'lab/b'].map(modelId => ({ modelId, result: { ...deepResult } }));
  const points = chartPoints(entries, models, 'cost', 'USD/task');
  assert.equal(frontierUnavailable(points, deepDefinition, 'cost'), null);
  assert.equal(frontierUnavailable(points, deepDefinition, 'release'), 'costOnly');
  assert.equal(frontierUnavailable(points, {}, 'cost'), 'direction');
  assert.equal(frontierUnavailable(points.slice(0, 1), deepDefinition, 'cost'), null);
  assert.equal(frontierUnavailable([], deepDefinition, 'cost'), 'empty');
  for (const changes of [{ source: 'https://example.com' }, { source: 'https://deepswe.datacurve.ai/other' }, { effort: undefined }, { effort: 'High' }, { harness: 'other' }, { dataset: '111 tasks' }, { variant: '4 runs' }, { date: '2026-01-01' }, { future: { tools: true } }]) {
    const changed = structuredClone(points);
    Object.assign(changed[0].result, changes);
    assert.equal(frontierUnavailable(changed, deepDefinition, 'cost'), null, JSON.stringify(changes));
  }
  const future = points.map(point => ({ ...point, result: { ...point.result, unknown_condition: true } }));
  assert.equal(frontierUnavailable(future, deepDefinition, 'cost'), null);
  assert.notEqual(conditionKey({ ...deepResult, effort: undefined }), conditionKey({ ...deepResult, effort: 'default' }));
  assert.notEqual(conditionKey(deepResult), conditionKey({ ...deepResult, cost_source: 'https://example.com', future: 1 }));
  assert.equal(conditionKey(deepResult), conditionKey({ ...deepResult, cost: 99, score: 20, cost_source: 'https://example.com' }));
  assert.equal(conditionKey({ nested: { b: 1, a: 2 } }), conditionKey({ nested: { a: 2, b: 1 } }));
});

test('mixed efforts and conditions share one exploratory frontier without altering optional exact filters', () => {
  const entries = [
    { modelId: 'lab/A', result: { ...deepResult, cost: 1, score: 40 } },
    { modelId: 'lab/b', result: { ...deepResult, cost: 3, score: 60 } },
    { modelId: 'lab/A', result: { ...deepResult, effort: 'low', cost: 2, score: 30 } },
    { modelId: 'lab/b', result: { ...deepResult, effort: 'low', cost: 4, score: 50 } },
    { modelId: 'other/c', result: { ...deepResult, harness: 'unknown agent', cost: 0, score: 100 } },
    { modelId: 'other/c', result: { ...deepResult, effort: 'max', cost: 1, score: 90 } },
    { modelId: 'other/c', result: { ...deepResult, effort: 'max', cost: 2, score: 95 } },
  ];
  const original = structuredClone(entries);
  const points = chartPoints(entries, models, 'cost', 'USD/task');
  const groups = comparisonGroups(points);
  assert.equal(frontierUnavailable(points, deepDefinition, 'cost'), null);
  assert.equal(groups.length, 3);
  assert.deepEqual(groups.map(group => group.points.length), [2, 2, 2]);
  assert.ok(groups.every(group => group.points.every(point => conditionKey(point.result) === group.key)));
  assert.deepEqual(paretoFront(points, true).map(point => point.modelId), ['other/c']);
  assert.equal(frontierUnavailable(points.slice(4), deepDefinition, 'cost'), null);
  assert.equal(frontierUnavailable(points, deepDefinition, 'release'), 'costOnly');
  assert.deepEqual(paretoFront(points.slice(5), true).map(point => point.y), [90, 95]); // Two configurations of one model can form a line.
  assert.deepEqual(entries, original);
});

test('axis domains, medians and organization colors are stable without changing observations', () => {
  assert.equal(median([3, 1, 2]), 2);
  assert.equal(median([4, 1, 3, 2]), 2.5);
  assert.equal(median([]), undefined);
  for (const values of [[0], [50], [-10, 10], [0.0000001, 0.0000003]]) {
    const domain = numericDomain(values);
    assert.ok(domain[0] < Math.min(...values));
    assert.ok(domain[1] > Math.max(...values));
    assert.ok(axisTicks(domain).every(Number.isFinite));
    assert.ok(axisTicks(domain).length > 0);
  }
  assert.deepEqual(numericDomain([30, 40], { min: 0, max: 100 }), [0, 100]);
  assert.equal(numericDomain([0], { zero: true })[0], 0);
  const closeTicks = axisTicks(numericDomain([50.0001, 50.0002]));
  assert.equal(new Set(closeTicks.map(value => formatTick(value, closeTicks, 'en'))).size, closeTicks.length);
  assert.equal(labColor('openai'), labColor('openai'));
  assert.equal(labColor('new-lab'), labColor('new-lab'));
  assert.notEqual(labColor('openai'), labColor('google'));
});

test('logarithmic cost coordinates preserve orders, precision and real zeros without epsilon substitution', () => {
  const values = [0.005, 0.05, 0.5, 5], original = [...values];
  const log = costAxis(values);
  assert.equal(log.kind, 'log');
  assert.equal(log.fallback, false);
  const gaps = values.slice(1).map((value, i) => log.position(value) - log.position(values[i]));
  assert.ok(gaps.every(gap => Math.abs(gap - gaps[0]) < 1e-12));
  assert.ok(log.ticks.length > 2);
  assert.ok(log.ticks.every(tick => tick > 0 && Number.isFinite(tick) && tick >= log.domain[0] && tick <= log.domain[1]));
  assert.equal(new Set(log.ticks).size, log.ticks.length);
  for (const values of [[0], [0, 0.005, 5]]) {
    const axis = costAxis(values);
    assert.equal(axis.kind, 'linear');
    assert.equal(axis.fallback, true);
    assert.equal(axis.position(0), 0);
    assert.ok(values.every(value => Number.isFinite(axis.position(value))));
  }
  assert.equal(costAxis(values, 'linear').fallback, false);
  assert.equal(costAxis(values, 'linear').kind, 'linear');
  for (const values of [[1], [0.00001], [2.001, 2.002], [0.000001, 100000]]) {
    const axis = costAxis(values);
    assert.ok(axis.domain[0] > 0 && axis.domain[1] > axis.domain[0]);
    assert.ok(axis.ticks.length > 0);
    assert.ok(values.every(value => Number.isFinite(axis.position(value))));
  }
  assert.deepEqual(values, original);
  assert.equal(formatCostTick(0.005, [0.005, 0.01, 0.02], 'USD/task', 'en'), '$0.005');
  assert.equal(formatCostTick(5, [1, 2, 5], 'EUR/test', 'en'), '€5');
  assert.equal(formatCostTick(5, [1, 2, 5], 'XYZ/task', 'en'), 'XYZ 5');
});

test('annotation layout avoids collisions and clips long labels without moving source coordinates', () => {
  const labels = [{ x: 100, y: 100, text: 'Alpha (high)' }, { x: 105, y: 100, text: 'Beta (max)' }];
  const original = structuredClone(labels), bounds = { left: 10, top: 10, right: 580, bottom: 280 };
  const placed = placeLabels(labels, bounds);
  assert.equal(placed.length, 2);
  const [a, b] = placed.map(label => label.box);
  assert.ok(a.x + a.width <= b.x || b.x + b.width <= a.x || a.y + a.height <= b.y || b.y + b.height <= a.y);
  for (const { box } of placed) assert.ok(box.x >= bounds.left && box.y >= bounds.top && box.x + box.width <= bounds.right && box.y + box.height <= bounds.bottom);
  const blocked = [{ x: 0, y: 0, width: 600, height: 300 }];
  assert.deepEqual(placeLabels(labels, bounds, blocked), []);
  const required = placeLabels([{ ...labels[0], text: 'Very long model name '.repeat(30), required: true }], bounds, blocked);
  assert.equal(required.length, 1);
  assert.match(required[0].text, /…$/);
  assert.equal(required[0].x, labels[0].x);
  assert.equal(required[0].y, labels[0].y);
  const crowded = placeLabels(Array.from({ length: 7 }, (_, i) => ({ x: 100, y: 100, text: `Frontier model ${i} (high)`, required: true })), bounds, blocked);
  assert.equal(crowded.length, 7);
  for (const [i, { box: a }] of crowded.entries()) {
    for (const { box: b } of crowded.slice(i + 1)) assert.ok(a.x + a.width <= b.x || b.x + b.width <= a.x || a.y + a.height <= b.y || b.y + b.height <= a.y);
  }
  assert.deepEqual(labels, original);
});

test('interactive chart preserves records, isolates costs and supports search, legend, touch and keyboard', async t => {
  let chartWidth = 820;
  class Element {
    constructor(tag) {
      this.tag = tag; this.children = []; this.attributes = {}; this.handlers = {}; this.className = ''; this.isConnected = true;
      this.clientWidth = chartWidth;
      this.classList = { toggle: (name, enabled) => {
        const classes = new Set(this.className.split(' ').filter(Boolean));
        if (enabled) classes.add(name); else classes.delete(name);
        this.className = [...classes].join(' ');
      } };
    }
    setAttribute(name, value) { this.attributes[name] = value; if (name === 'class') this.className = value; }
    removeAttribute(name) { delete this.attributes[name]; }
    getAttribute(name) { return this.attributes[name]; }
    append(...children) { this.children.push(...children); }
    replaceChildren(...children) { this.children = children; }
    contains(target) { return this === target || this.children.some(child => child instanceof Element && child.contains(target)); }
    addEventListener(name, handler) { this.handlers[name] = handler; }
    focus() { globalThis.document.activeElement = this; this.handlers.focus?.(); }
    dispatch(name, options = {}) { const event = { target: this, preventDefault() {}, ...options }; this.handlers[name]?.(event); }
    set textContent(value) { this.children = [String(value)]; }
    get textContent() { return this.children.map(child => child instanceof Element ? child.textContent : String(child)).join(''); }
  }
  const previous = globalThis.document;
  globalThis.document = { createElement: tag => new Element(tag), createElementNS: (_, tag) => new Element(tag), addEventListener() {} };
  const all = (node, predicate) => [node, ...node.children.filter(child => child instanceof Element).flatMap(child => all(child, () => true))].filter(predicate);
  const byClass = (root, name) => all(root, node => node.className.split(' ').includes(name));
  const choose = (root, label, text) => {
    const select = all(root, node => node.attributes.role === 'combobox' && node.attributes['aria-label'] === label)[0];
    const list = all(root, node => node.id === select.attributes['aria-controls'])[0];
    const option = list.children.find(node => node.textContent.startsWith(text));
    assert.ok(option, `${label}: ${text}`);
    option.dispatch('click');
  };
  const chartModels = { 'lab/a': { name: 'Alpha', release_date: '2026-01-01' }, 'google/b': { name: 'Beta', release_date: '2026-01-01' }, 'other/c': { name: 'Gamma', release_date: '2026-02-01' }, 'other/d': { name: 'Delta', release_date: 'invalid' } };
  const entries = Object.keys(chartModels).map((modelId, i) => ({ modelId, result: { ...deepResult, ...(i > 1 ? { cost: i + 1, score: i === 2 ? 60 : 55 } : {}) } }));
  const original = structuredClone(entries);
  const make = (options = {}) => createBenchmarkChart({ id: 'deepswe-v1.1', definition: deepDefinition, entries, models: chartModels, manifest: { published_at: '2026-11-07T00:00:00Z' }, language: 'en', T: messages.en, ...options });
  try {
    await t.test('costless and partial-cost charts default to bars; switching explicitly discloses omitted costs', () => {
      const mixed = entries.map((entry, i) => ({ ...entry, result: i === 0 ? { ...deepResult, cost: undefined } : entry.result }));
      const state = {}, root = make({ entries: mixed, state });
      assert.equal(state.axis, 'score');
      assert.equal(byClass(root, 'chart-bar').length, 4);
      assert.equal(byClass(root, 'chart-dot').length, 0);
      assert.equal(byClass(root, 'chart-svg')[0].attributes['data-scale'], 'score');
      assert.ok(all(root, node => node.attributes.type === 'checkbox').every(toggle => toggle.disabled && !toggle.checked));
      assert.equal(byClass(root, 'chart-switches')[0].children[1].hidden, true);
      assert.ok(root.textContent.includes(messages.en.chartBarNote));
      choose(root, messages.en.chartView, messages.en.chartCostScatter);
      assert.equal(byClass(root, 'chart-bar').length, 0);
      assert.match(byClass(root, 'chart-status')[0].textContent, /1 records omitted because evaluation cost is missing/);
      choose(root, messages.en.chartView, messages.en.chartBars);
      assert.equal(byClass(root, 'chart-bar').length, 4);
      assert.doesNotMatch(byClass(root, 'chart-status')[0].textContent, /evaluation cost is missing/);
      const translated = make({ entries: mixed, state, language: 'zh-CN', T: messages['zh-CN'] });
      assert.equal(byClass(translated, 'chart-bar').length, 4);
      assert.ok(translated.textContent.includes(messages['zh-CN'].chartBarNote));
      const noCosts = make({ entries: mixed.map(entry => ({ ...entry, result: { score: entry.result.score } })), models: {} });
      assert.equal(byClass(noCosts, 'chart-bar').length, 4);
      assert.equal(byClass(noCosts, 'chart-bar-score').length, 4);
    });
    await t.test('bars preserve precise labels, zero and negative scores on desktop and mobile', () => {
      const scores = [0, -2.123456789, 42.123456789, 'not numeric'];
      const input = entries.map((entry, i) => ({ ...entry, result: { ...entry.result, score: scores[i], cost: undefined } }));
      const original = structuredClone(input);
      try {
        for (const width of [820, 360]) {
          chartWidth = width;
          const root = make({ entries: input, models: {} });
          assert.equal(byClass(root, 'chart-bar').length, 3);
          assert.deepEqual(byClass(root, 'chart-bar-score').map(label => label.children[0]), ['42.123456789', '0', '-2.123456789']);
          const fills = byClass(root, 'chart-bar-fill');
          assert.equal(Number(fills[1].attributes.height), 0);
          assert.equal(byClass(root, 'chart-bar-zero').length, 1);
          assert.ok(Number(fills[2].attributes.y) > Number(fills[0].attributes.y));
          assert.ok(fills.every(fill => Number(fill.attributes.height) >= 0));
          assert.ok(fills.every(fill => Number(fill.attributes.width) <= 52));
          const logos = all(root, node => node.tag === 'image');
          assert.equal(logos.length, 3);
          assert.ok(logos.every(logo => logo.attributes.href.startsWith('https://models.dev/logos/')));
          assert.ok(byClass(root, 'chart-bar-name').every(label => label.attributes.transform.endsWith('rotate(-60)')));
          if (width === 360) assert.ok(Number(byClass(root, 'chart-svg')[0].attributes.viewBox.split(' ')[2]) >= width);
          assert.match(byClass(root, 'chart-status')[0].textContent, /3 displayed records.*1 records missing valid coordinates/);
          const unknown = make({ entries: input, definition: { ...deepDefinition, higher_is_better: undefined } });
          assert.deepEqual(byClass(unknown, 'chart-bar-score').map(label => label.children[0]), ['0', '-2.123456789', '42.123456789']);
          const lower = make({ entries: input, definition: { ...deepDefinition, higher_is_better: false } });
          assert.deepEqual(byClass(lower, 'chart-bar-score').map(label => label.children[0]), ['-2.123456789', '0', '42.123456789']);
          const zeros = make({ entries: input.slice(0, 1) });
          assert.equal(Number(byClass(zeros, 'chart-bar-fill')[0].attributes.height), 0);
          assert.doesNotMatch(byClass(zeros, 'chart-svg')[0].textContent, /NaN|Infinity/);
        }
      } finally { chartWidth = 820; }
      assert.deepEqual(input, original);
    });
    await t.test('bar search, condition and lab filters, keyboard, touch and pinned details retain original records', () => {
      const input = [
        ...entries.map(entry => ({ ...entry, result: { ...entry.result, cost: undefined } })),
        { ...entries[0], result: { ...deepResult, cost: undefined, effort: 'low', score: 99, harness: 'other agent' } },
      ];
      const root = make({ entries: input });
      assert.equal(byClass(root, 'chart-bar').length, 5);
      const search = all(root, node => node.attributes.type === 'search')[0];
      search.dispatch('input', { target: { value: 'Alpha' } });
      assert.equal(byClass(root, 'chart-bar').length, 5);
      assert.equal(byClass(root, 'chart-bar').filter(bar => bar.className.includes('is-match')).length, 2);
      const bars = byClass(root, 'chart-bar');
      bars[0].dispatch('pointerdown', { pointerType: 'touch' });
      bars[0].focus();
      assert.equal(byClass(root, 'chart-detail')[0].hidden, true);
      bars[0].dispatch('click');
      assert.equal(byClass(root, 'chart-record').length, 1);
      assert.equal(bars[0].attributes['aria-pressed'], 'true');
      bars[1].dispatch('pointerenter', { pointerType: 'mouse' });
      assert.equal(bars[0].attributes['aria-pressed'], 'true');
      search.dispatch('input', { target: { value: '' } });
      assert.equal(byClass(root, 'chart-bar')[0].attributes['aria-pressed'], 'true');
      byClass(root, 'chart-bar')[0].dispatch('keydown', { key: 'End' });
      const last = byClass(root, 'chart-bar').at(-1);
      assert.equal(document.activeElement, last);
      last.dispatch('keydown', { key: 'Enter' });
      assert.match(byClass(root, 'chart-detail-body')[0].textContent, /Alpha/);
      assert.match(byClass(root, 'chart-detail-body')[0].textContent, /50/);
      root.dispatch('keydown', { key: 'Escape' });
      assert.equal(byClass(root, 'chart-detail')[0].hidden, true);
      choose(root, messages.en.conditions, input[4].result.source + ' · ' + messages.en.effort + ': low');
      assert.equal(byClass(root, 'chart-bar').length, 1); // Singleton condition groups can be selected too.
      choose(root, messages.en.conditions, messages.en.chartAllConditions);
      const lab = all(root, node => node.tag === 'button' && node.attributes['data-lab'] === 'lab')[0];
      lab.dispatch('click');
      assert.equal(byClass(root, 'chart-bar').length, 2); // Both configurations of Alpha, not only its best score.
      byClass(root, 'chart-show-all')[0].dispatch('click');
      choose(root, messages.en.effort, 'low');
      assert.equal(byClass(root, 'chart-bar').length, 1);
    });
    await t.test('quadrants and eligible frontiers default on without overriding explicit preferences', () => {
      const state = {}, root = make({ state });
      const toggles = all(root, node => node.attributes.type === 'checkbox');
      assert.ok(toggles.every(toggle => toggle.checked && !toggle.disabled));
      assert.equal(byClass(root, 'chart-quadrants').length, 1);
      assert.equal(byClass(root, 'chart-frontier').length, 1);
      assert.equal(byClass(root, 'chart-thresholds')[0].hidden, false);
      choose(root, messages.en.chartView, messages.en.chartReleaseScatter);
      assert.ok(toggles.every(toggle => !toggle.checked && toggle.disabled));
      assert.equal(state.quadrants, true);
      assert.equal(state.frontier, true);
      choose(root, messages.en.chartView, messages.en.chartCostScatter);
      assert.ok(toggles.every(toggle => toggle.checked && !toggle.disabled));
      for (const toggle of toggles) toggle.dispatch('change', { target: { checked: false } });
      assert.equal(byClass(root, 'chart-quadrants').length, 0);
      assert.equal(byClass(root, 'chart-frontier').length, 0);
      assert.equal(byClass(root, 'chart-thresholds')[0].hidden, true);
      const translated = make({ state, language: 'zh-CN', T: messages['zh-CN'] });
      assert.ok(all(translated, node => node.attributes.type === 'checkbox').every(toggle => !toggle.checked && !toggle.disabled));
      assert.equal(byClass(translated, 'chart-quadrants').length, 0);
      assert.equal(byClass(translated, 'chart-frontier').length, 0);
    });
    await t.test('point details include all overlapping records and exact numbers; pinning survives hover', () => {
      const root = make();
      const dots = byClass(root, 'chart-dot');
      assert.equal(dots.length, 3);
      assert.equal(byClass(root, 'chart-frontier').length, 1);
      assert.match(byClass(root, 'chart-frontier')[0].attributes.d, /^M.* L/);
      assert.doesNotMatch(byClass(root, 'chart-frontier')[0].attributes.d, /[CHVQS]/);
      assert.equal(byClass(root, 'chart-detail')[0].hidden, true);
      const labels = byClass(root, 'chart-point-label');
      assert.deepEqual(new Set(labels.map(label => label.children[0])), new Set(['Alpha (high)', 'Beta (high)', 'Gamma (high)']));
      assert.equal(labels.find(label => label.children[0] === 'Alpha (high)').attributes.fill, labColor('lab'));
      assert.equal(labels.find(label => label.children[0] === 'Beta (high)').attributes.fill, labColor('google'));
      dots[0].dispatch('pointerenter', { pointerType: 'mouse' });
      assert.equal(byClass(root, 'chart-detail')[0].hidden, false);
      assert.match(byClass(root, 'chart-detail')[0].attributes.style, /left:.*top:.*max-height:/);
      const body = byClass(root, 'chart-detail-body')[0];
      assert.equal(byClass(root, 'chart-record').length, 2);
      assert.match(body.textContent, /Alpha/);
      assert.match(body.textContent, /Beta/);
      assert.match(body.textContent, /1\.234567891 USD\/task/);
      assert.ok(all(body, node => node.attributes.href === '#/models/lab%2Fa').length);
      dots[0].dispatch('click');
      assert.equal(dots[0].attributes['aria-pressed'], 'true');
      byClass(root, 'chart-layout')[0].dispatch('pointerleave');
      assert.equal(byClass(root, 'chart-detail')[0].hidden, false);
      dots[1].dispatch('pointerenter', { pointerType: 'mouse' });
      assert.match(body.textContent, /Alpha/);
      assert.match(byClass(root, 'chart-detail-heading')[0].textContent, /Pinned/);
      root.dispatch('keydown', { key: 'Escape' });
      assert.equal(dots[0].attributes['aria-pressed'], 'false');
      assert.equal(byClass(root, 'chart-detail')[0].hidden, true);
      assert.equal(body.textContent, messages.en.chartInspectHint);
      dots[1].dispatch('pointerenter', { pointerType: 'touch' });
      assert.equal(body.textContent, messages.en.chartInspectHint);
      dots[1].dispatch('pointerdown', { pointerType: 'touch' });
      dots[1].focus();
      assert.equal(byClass(root, 'chart-detail')[0].hidden, true);
      dots[1].dispatch('click');
      assert.match(body.textContent, /Gamma/);
      dots[1].dispatch('keydown', { key: 'End' });
      assert.equal(document.activeElement, dots[2]);
      dots[2].dispatch('keydown', { key: 'Enter' });
      assert.match(body.textContent, /Delta/);
      assert.equal(dots[2].attributes['aria-pressed'], 'true');
      assert.ok(root.textContent.includes('Package generated: 2026-11-07T00:00:00Z'));
    });
    await t.test('compact filters, logarithmic toggle and zero fallback keep every original observation', () => {
      const root = make();
      assert.equal(byClass(root, 'chart-filter-panel')[0].hidden, true);
      byClass(root, 'chart-filter-button')[0].dispatch('click');
      assert.equal(byClass(root, 'chart-filter-panel')[0].hidden, false);
      assert.equal(byClass(root, 'chart-filter-button')[0].attributes['aria-expanded'], 'true');
      assert.equal(byClass(root, 'chart-svg')[0].attributes['data-scale'], 'log');
      const positions = byClass(root, 'chart-dot').map(dot => dot.attributes.transform);
      choose(root, messages.en.chartScale, messages.en.chartLinear);
      assert.equal(byClass(root, 'chart-svg')[0].attributes['data-scale'], 'linear');
      assert.equal(byClass(root, 'chart-dot').length, 3);
      choose(root, messages.en.chartScale, messages.en.chartLog);
      assert.deepEqual(byClass(root, 'chart-dot').map(dot => dot.attributes.transform), positions);
      const withZero = make({ entries: entries.map((entry, i) => i ? entry : { ...entry, result: { ...entry.result, cost: 0 } }) });
      assert.equal(byClass(withZero, 'chart-svg')[0].attributes['data-scale'], 'linear');
      assert.equal(byClass(withZero, 'chart-scale-notice')[0].hidden, false);
      assert.equal(byClass(withZero, 'chart-dot').length, 4);
      const positiveLab = all(withZero, node => node.attributes['data-lab'] === 'google' && node.tag === 'button')[0];
      positiveLab.dispatch('click');
      assert.equal(byClass(withZero, 'chart-svg')[0].attributes['data-scale'], 'log');
      assert.equal(byClass(withZero, 'chart-scale-notice')[0].hidden, true);
    });
    await t.test('search only highlights; legend filters recompute the displayed frontier and counts', () => {
      const root = make();
      const path = byClass(root, 'chart-frontier')[0].attributes.d;
      const search = all(root, node => node.attributes.type === 'search')[0];
      search.dispatch('input', { target: { value: 'Alpha' } });
      assert.equal(byClass(root, 'chart-dot').length, 3);
      assert.equal(byClass(root, 'chart-dot').filter(node => node.className.includes('is-match')).length, 1);
      assert.equal(byClass(root, 'chart-frontier')[0].attributes.d, path);
      assert.match(byClass(root, 'chart-status')[0].textContent, /1 highlighted records/);
      const lab = all(root, node => node.tag === 'button' && node.attributes['data-lab'] === 'other')[0];
      lab.dispatch('click');
      assert.equal(lab.attributes['aria-pressed'], 'true');
      assert.match(byClass(root, 'chart-status')[0].textContent, /2 displayed records \/ 2 models/);
      assert.equal(byClass(root, 'chart-frontier').length, 0); // Gamma dominates Delta in the selected institution.
      assert.equal(byClass(root, 'chart-frontier-halo').length, 1); // A singleton frontier remains visible without inventing a line.
      const labels = byClass(root, 'chart-point-label').map(label => label.children[0]);
      assert.deepEqual(new Set(labels), new Set(['Gamma (high)', 'Delta (high)']));
      assert.ok(byClass(root, 'chart-dot').every(dot => !/Alpha|Beta/.test(dot.attributes['aria-label'])));
      byClass(root, 'chart-show-all')[0].dispatch('click');
      assert.equal(byClass(root, 'chart-frontier')[0].attributes.d, path);
      const quadrant = all(root, node => node.attributes.type === 'checkbox')[0];
      quadrant.dispatch('change', { target: { checked: true } });
      assert.equal(byClass(root, 'chart-quadrants').length, 1);
      assert.ok(root.textContent.includes(messages.en.chartMedianNote));
    });
    await t.test('institution focus labels all models, including overlaps and more than the overview label limit', () => {
      const state = {}, focusedModels = { ...chartModels };
      const focusedEntries = Array.from({ length: 25 }, (_, i) => {
        const modelId = `lab/focus-${i}`;
        focusedModels[modelId] = { name: `Focus ${i}`, release_date: '2026-01-01' };
        return { modelId, result: { ...deepResult, cost: i < 2 ? 1 : i + 1, score: i < 2 ? 40 : 20 + i, harness: 'unverified agent' } };
      });
      const input = [...focusedEntries, { ...entries[1], result: { ...entries[1].result, cost_unit: 'USD/test' } }];
      const original = structuredClone(input);
      const root = make({ entries: input, models: focusedModels, state });
      const institution = all(root, node => node.tag === 'button' && node.attributes['data-lab'] === 'lab')[0];
      institution.dispatch('click');
      assert.equal(root.attributes['data-lab'], 'lab');
      assert.equal(institution.attributes['aria-pressed'], 'true');
      assert.equal(byClass(root, 'chart-point-label').length, 25);
      assert.deepEqual(new Set(byClass(root, 'chart-point-label').map(label => label.children[0])), new Set(focusedEntries.map((_, i) => `Focus ${i} (high)`)));
      assert.equal(byClass(root, 'chart-dot').length, 24); // Both overlapping model names are still labelled.
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
      const translated = make({ entries: input, models: focusedModels, state, language: 'zh-CN', T: messages['zh-CN'] });
      assert.equal(translated.attributes['data-lab'], 'lab');
      assert.equal(byClass(translated, 'chart-point-label').length, 25);
      institution.dispatch('click');
      assert.equal(root.attributes['data-lab'], '');
      assert.equal(byClass(root, 'chart-show-all')[0].attributes['aria-pressed'], 'true');
      institution.dispatch('click');
      choose(root, messages.en.chartCostUnit, 'USD/test');
      assert.equal(byClass(root, 'chart-svg').length, 0);
      assert.equal(institution.hidden, false); // The selected zero-count institution remains clearable.
      byClass(root, 'chart-show-all')[0].dispatch('click');
      assert.match(byClass(root, 'chart-status')[0].textContent, /1 displayed records/);
      assert.deepEqual(input, original);
    });
    await t.test('quadrant shading follows scoring direction without moving points or rounding boundaries', () => {
      for (const higher_is_better of [true, false]) {
        const root = make({ definition: { ...deepDefinition, higher_is_better } });
        const before = byClass(root, 'chart-dot').map(dot => dot.attributes.transform);
        all(root, node => node.attributes.type === 'checkbox')[0].dispatch('change', { target: { checked: true } });
        const good = byClass(root, 'chart-quadrant-good')[0], bad = byClass(root, 'chart-quadrant-bad')[0];
        assert.equal(Number(good.attributes.y) < Number(bad.attributes.y), higher_is_better);
        assert.deepEqual(byClass(root, 'chart-dot').map(dot => dot.attributes.transform), before);
        const caption = byClass(root, 'chart-thresholds')[0];
        assert.match(caption.textContent, /≈/);
        assert.ok(caption.title.includes(`${median(entries.map(entry => entry.result.cost))} USD/task`));
      }
    });
    await t.test('axis, unit and exact effort filters never infer defaults or combine bases', () => {
      const mixed = [...entries, { modelId: 'lab/a', result: { ...deepResult, cost_unit: 'USD/test', effort: 'default' } }, { modelId: 'google/b', result: { ...deepResult, cost_unit: 'USD/test', effort: undefined } }];
      delete mixed[5].result.effort;
      const root = make({ entries: mixed });
      choose(root, messages.en.chartCostUnit, 'USD/test');
      assert.match(byClass(root, 'chart-status')[0].textContent, /2 displayed records/);
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
      choose(root, messages.en.effort, 'default');
      assert.match(byClass(root, 'chart-status')[0].textContent, /1 displayed records/);
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
      assert.equal(byClass(root, 'chart-frontier-halo').length, 1);
      assert.equal(byClass(root, 'chart-frontier').length, 0);
      choose(root, messages.en.effort, '—');
      assert.match(byClass(root, 'chart-status')[0].textContent, /1 displayed records/);
      choose(root, messages.en.effort, messages.en.chartAllEfforts);
      choose(root, messages.en.chartView, messages.en.chartReleaseScatter);
      assert.match(byClass(root, 'chart-status')[0].textContent, /5 displayed records/);
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[0].disabled, true);
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, true);
    });
    await t.test('all conditions participate by default; explicit filters survive a language rerender', () => {
      const mixed = [...entries, { modelId: 'lab/a', result: { ...deepResult, harness: 'different agent', score: 99 } }];
      const state = {};
      const root = make({ entries: mixed, state });
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
      assert.equal(byClass(root, 'chart-frontier').length, 0); // The different-agent record dominates all others.
      assert.equal(byClass(root, 'chart-frontier-halo').length, 1);
      assert.match(byClass(root, 'chart-frontier-info')[0].textContent, /all 5 visible records, not a verified comparable ranking/);
      assert.ok(!byClass(root, 'chart-point-label').some(label => label.children[0].includes('+')));
      choose(root, messages.en.conditions, deepResult.source);
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
      assert.match(byClass(root, 'chart-status')[0].textContent, /4 displayed records/);
      assert.equal(byClass(root, 'chart-frontier').length, 1);
      const translated = make({ entries: mixed, state, language: 'zh-CN', T: messages['zh-CN'] });
      assert.equal(all(translated, node => node.attributes.type === 'checkbox')[1].disabled, false);
      assert.match(byClass(translated, 'chart-status')[0].textContent, /展示 4 条记录/);
      assert.ok(translated.textContent.includes(messages['zh-CN'].chartFrontierNote));
      const unknown = make({ definition: { ...deepDefinition, higher_is_better: undefined } });
      assert.equal(all(unknown, node => node.attributes.type === 'checkbox')[0].disabled, true);
      assert.equal(all(unknown, node => node.attributes.type === 'checkbox')[1].disabled, true);
    });
    await t.test('different efforts and harnesses share one frontier, in either scoring direction', () => {
      for (const higher_is_better of [true, false]) {
        const cohortModels = { ...chartModels, 'lab/e': { name: 'Epsilon' } };
        const cohortEntries = [
          { modelId: 'lab/a', result: { ...deepResult, cost: 1, score: 40 } },
          { modelId: 'google/b', result: { ...deepResult, cost: 3, score: 60 } },
          { modelId: 'other/c', result: { ...deepResult, effort: 'low', cost: 2, score: 30 } },
          { modelId: 'other/d', result: { ...deepResult, effort: 'low', cost: 4, score: 50 } },
          { modelId: 'lab/e', result: { ...deepResult, harness: 'unknown agent', cost: 0.1, score: 20 } },
        ].map(entry => ({ ...entry, result: { ...entry.result, score: entry.result.score * (higher_is_better ? 1 : -1) } }));
        const original = structuredClone(cohortEntries);
        const root = make({ entries: cohortEntries, models: cohortModels, definition: { ...deepDefinition, higher_is_better } });
        assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
        assert.equal(byClass(root, 'chart-dot').length, 5);
        assert.equal(byClass(root, 'chart-frontier-halo').length, 3);
        const paths = byClass(root, 'chart-frontier');
        assert.equal(paths.length, 1);
        const dots = byClass(root, 'chart-dot');
        const position = index => dots[index].attributes.transform.match(/^translate\((\S+) (\S+)\)$/).slice(1).join(',');
        assert.equal(paths[0].attributes.d, `M${position(4)} L${position(0)} L${position(1)}`);
        assert.deepEqual(new Set(byClass(root, 'chart-point-label').map(label => label.children[0])), new Set(['Epsilon (high)', 'Alpha (high)', 'Beta (high)']));
        assert.match(byClass(root, 'chart-frontier-info')[0].textContent, /3 models \/ 3 configurations.*all 5 visible records/);
        assert.equal(byClass(root, 'chart-frontier-legend').length, 0);
        choose(root, messages.en.effort, 'low');
        assert.equal(byClass(root, 'chart-frontier').length, 1);
        assert.match(byClass(root, 'chart-status')[0].textContent, /2 displayed records/);
        assert.equal(byClass(root, 'chart-filter-button')[0].textContent, 'Filters (1)');
        assert.deepEqual(cohortEntries, original);
      }
    });
    await t.test('AA Index draws one line across all visible configurations, without mixing cost bases or filling missing costs', () => {
      const aaDefinition = { name: 'Artificial Analysis Intelligence Index', version: '5.0.1', metric: 'index score', unit: 'points', higher_is_better: true };
      const aaResult = { name: aaDefinition.name, version: aaDefinition.version, metric: aaDefinition.metric, cost_unit: 'USD/weighted task' };
      const aaEntries = [
        { modelId: 'lab/a', result: { ...aaResult, cost: 1, score: 40, effort: 'low' } },
        { modelId: 'lab/a', result: { ...aaResult, cost: 3, score: 60, effort: 'high' } },
        { modelId: 'google/b', result: { ...aaResult, cost: 2, score: 30, effort: 'default' } },
        { modelId: 'other/c', result: { ...aaResult, cost: 4, score: 70 } },
        { modelId: 'other/d', result: { ...aaResult, score: 99 } },
        { modelId: 'other/d', result: { ...aaResult, cost: 0.1, cost_unit: 'USD/test', score: 99 } },
      ];
      const original = structuredClone(aaEntries);
      const root = make({ id: 'artificial-analysis-intelligence-index-v5', definition: aaDefinition, entries: aaEntries, state: { axis: 'cost' } });
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
      assert.equal(byClass(root, 'chart-dot').length, 4);
      assert.equal(byClass(root, 'chart-frontier').length, 1);
      assert.equal(byClass(root, 'chart-frontier-halo').length, 3);
      const dots = byClass(root, 'chart-dot');
      const position = index => dots[index].attributes.transform.match(/^translate\((\S+) (\S+)\)$/).slice(1).join(',');
      assert.equal(byClass(root, 'chart-frontier')[0].attributes.d, `M${position(0)} L${position(1)} L${position(3)}`);
      assert.deepEqual(new Set(byClass(root, 'chart-point-label').map(label => label.children[0])), new Set(['Alpha (low)', 'Alpha (high)', 'Gamma']));
      assert.match(byClass(root, 'chart-frontier-info')[0].textContent, /2 models \/ 3 configurations.*all 4 visible records/);
      assert.match(byClass(root, 'chart-status')[0].textContent, /2 records missing valid coordinates or using another cost basis/);
      assert.deepEqual(aaEntries, original);
    });
    await t.test('every frontier model is labelled on desktop and mobile, including ties, beyond optional limits', () => {
      const frontierModels = { ...chartModels };
      const frontierEntries = Array.from({ length: 26 }, (_, i) => {
        const modelId = `lab/front-${i}`;
        frontierModels[modelId] = { name: `Front ${i}` };
        return { modelId, result: { ...deepResult, cost: i < 2 ? 1 : i + 1, score: i < 2 ? 0 : i } };
      });
      // Every tied observation participates, even with a different harness.
      frontierEntries.push({ modelId: 'other/c', result: { ...deepResult, cost: 1, score: 0, harness: 'unknown agent' } });
      const original = structuredClone(frontierEntries);
      const expected = new Set(Array.from({ length: 26 }, (_, i) => `Front ${i} (high)`));
      expected.add('Gamma (high)');
      try {
        for (const width of [820, 360]) {
          chartWidth = width;
          const root = make({ entries: frontierEntries, models: frontierModels });
          const names = () => byClass(root, 'chart-point-label').map(label => label.children[0]);
          assert.equal(names().length, 27);
          assert.deepEqual(new Set(names()), expected);
          assert.equal(byClass(root, 'chart-frontier-halo').length, 25);
          assert.ok(Number(byClass(root, 'chart-svg')[0].attributes.viewBox.split(' ')[3]) > 420);
          const search = all(root, node => node.attributes.type === 'search')[0];
          const path = byClass(root, 'chart-frontier')[0].attributes.d;
          search.dispatch('input', { target: { value: 'Front 25' } });
          assert.deepEqual(new Set(names()), expected);
          assert.equal(byClass(root, 'chart-frontier')[0].attributes.d, path);
          search.dispatch('input', { target: { value: '' } });
          const frontier = all(root, node => node.attributes.type === 'checkbox')[1];
          frontier.dispatch('change', { target: { checked: false } });
          assert.equal(byClass(root, 'chart-frontier').length, 0);
          assert.equal(byClass(root, 'chart-frontier-halo').length, 0);
          assert.equal(byClass(root, 'chart-frontier-info')[0].hidden, true);
          assert.deepEqual(names(), []);
          frontier.dispatch('change', { target: { checked: true } });
          assert.deepEqual(new Set(names()), expected);
        }
      } finally { chartWidth = 820; }
      assert.deepEqual(frontierEntries, original);
    });
    await t.test('empty charts, unsafe provenance, unknown conditions and translated labels remain safe', () => {
      const empty = make({ entries: [], manifest: null });
      assert.equal(byClass(empty, 'chart-svg').length, 0);
      assert.ok(empty.textContent.includes(messages.en.chartUpdateUnknown));
      const unsafe = entries.map(entry => ({ ...entry, result: { ...entry.result, source: 'javascript:alert(1)', cost_source: 'data:text/html,unsafe', future: { budget: 2 }, variant: '<script>unsafe</script>' } }));
      const root = make({ entries: unsafe, language: 'zh-CN', T: messages['zh-CN'] });
      assert.equal(all(root, node => node.attributes.type === 'checkbox')[1].disabled, false);
      assert.equal(byClass(root, 'chart-frontier-info')[0].hidden, false);
      assert.equal(byClass(root, 'chart-frontier-info')[0].textContent, messages['zh-CN'].chartFrontierSummary(3, 3, 4));
      byClass(root, 'chart-dot')[0].dispatch('click');
      assert.match(byClass(root, 'chart-detail-body')[0].textContent, /<script>unsafe<\/script>/);
      assert.match(byClass(root, 'chart-detail-body')[0].textContent, /"budget":2/);
      assert.equal(all(root, node => node.tag === 'script').length, 0);
      assert.equal(all(root, node => node.tag === 'a' && /^(javascript|data):/.test(node.attributes.href)).length, 0);
      assert.ok(root.textContent.includes(messages['zh-CN'].chartTitle));
      const noCosts = make({ entries: entries.map(entry => ({ ...entry, result: { name: 'B', score: 0 } })) });
      assert.ok(byClass(noCosts, 'chart-svg').length);
      choose(noCosts, messages.en.chartView, messages.en.chartCostScatter);
      assert.ok(noCosts.textContent.includes(messages.en.chartNoCosts));
    });
    assert.deepEqual(entries, original);
  } finally { globalThis.document = previous; }
});

test('custom selects support keyboard, selection, dismissal and a single open list', () => {
  class Element {
    constructor() {
      this.children = []; this.attributes = {}; this.handlers = {}; this.style = {};
      this.classList = { toggle() {} }; this.isConnected = true;
      this.offsetTop = 0; this.offsetHeight = 20; this.scrollTop = 0; this.clientHeight = 100;
    }
    setAttribute(name, value) { this.attributes[name] = value; }
    getAttribute(name) { return this.attributes[name]; }
    removeAttribute(name) { delete this.attributes[name]; }
    append(...children) { this.children.push(...children); }
    contains(target) { return this === target || this.children.some(child => child.contains(target)); }
    addEventListener(name, handler) { this.handlers[name] = handler; }
    dispatch(name, properties = {}) {
      const event = { target: this, preventDefault() { this.defaultPrevented = true; }, stopPropagation() {}, ...properties };
      this.handlers[name]?.(event);
      return event;
    }
    focus() { this.focused = true; }
    getBoundingClientRect() { return { left: 20, right: 200 }; }
  }
  const handlers = {};
  const previousDocument = globalThis.document, previousWindow = globalThis.window;
  globalThis.document = { createElement: () => new Element(), addEventListener: (name, handler) => { handlers[name] = handler; } };
  globalThis.window = { innerWidth: 800 };
  try {
    const changes = [];
    const root = createSelect('Filter', [['', 'All'], ['a', 'Alpha'], ['b', 'Beta']], '', value => changes.push(value));
    const [trigger, list] = root.children;
    assert.equal(list.dispatch('mousedown').defaultPrevented, true);
    assert.equal(trigger.getAttribute('role'), 'combobox');
    assert.equal(trigger.getAttribute('aria-label'), 'Filter');
    assert.equal(trigger.children[0].textContent, 'All');
    assert.equal(list.hidden, true);
    trigger.dispatch('keydown', { key: 'ArrowDown' });
    assert.equal(trigger.getAttribute('aria-expanded'), 'true');
    assert.equal(trigger.getAttribute('aria-activedescendant'), list.children[0].id);
    trigger.dispatch('keydown', { key: 'End' });
    assert.equal(trigger.getAttribute('aria-activedescendant'), list.children[2].id);
    assert.equal(trigger.dispatch('keydown', { key: 'Enter' }).defaultPrevented, true);
    assert.deepEqual(changes, ['b']);
    assert.equal(trigger.children[0].textContent, 'Beta');
    assert.equal(list.children[2].getAttribute('aria-selected'), 'true');
    assert.equal(list.hidden, true);
    assert.equal(trigger.focused, true);
    trigger.dispatch('click');
    trigger.dispatch('keydown', { key: 'ArrowUp' });
    trigger.dispatch('keydown', { key: 'Escape' });
    assert.deepEqual(changes, ['b']);
    assert.equal(trigger.children[0].textContent, 'Beta');
    assert.equal(list.hidden, true);
    trigger.dispatch('click');
    trigger.dispatch('keydown', { key: 'b' });
    assert.equal(trigger.getAttribute('aria-activedescendant'), list.children[2].id);
    list.children[1].dispatch('click');
    assert.deepEqual(changes, ['b', 'a']);
    trigger.dispatch('click');
    handlers.pointerdown({ target: new Element() });
    assert.equal(list.hidden, true);
    trigger.dispatch('click');
    handlers.focusin({ target: new Element() });
    assert.equal(list.hidden, true);
    trigger.dispatch('click');
    const other = createSelect('Other', [['x', 'X']], 'x', () => {});
    other.children[0].dispatch('click');
    assert.equal(list.hidden, true);
    assert.equal(other.children[1].hidden, false);
    other.children[0].dispatch('keydown', { key: 'Tab' });
    assert.equal(other.children[1].hidden, true);
  } finally {
    globalThis.document = previousDocument;
    globalThis.window = previousWindow;
  }
});
