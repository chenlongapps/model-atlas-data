import test from 'node:test';
import assert from 'node:assert/strict';
import { modelLab, labLogoUrl, routeFor, parseRoute, filterModels, filterBenchmarks, sortEntries, sortBenchmarkResults, buildIndex, description, loadData } from '../web/data.mjs';
import { messages, resolveLanguage, descriptionLocale } from '../web/i18n.mjs';
import { readFile } from 'node:fs/promises';
import { createSelect } from '../web/select.mjs';
import { groupModalities, renderModalities } from '../web/modalities.mjs';

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
});
test('descriptions follow the selected language and preserve fallback', () => {
  const locale = { model: { descriptions: { 'lab/a': '中文' } }, benchmark: { description: { b: '评测' } } };
  assert.equal(description(descriptionLocale('zh-CN', locale), 'model', 'lab/a', 'original'), '中文');
  assert.equal(description(descriptionLocale('en', locale), 'model', 'lab/a', 'original'), 'original');
  assert.equal(description(descriptionLocale('zh-CN', locale), 'benchmark', 'b', 'benchmark'), '评测');
  assert.equal(description(descriptionLocale('en', locale), 'benchmark', 'b', 'benchmark'), 'benchmark');
  assert.equal(description(descriptionLocale('zh-CN', {}), 'model', 'lab/a', 'original'), 'original');
});

test('detail tables sort results, show effort and optional benchmark prices separately and hide only unmatched labels', async () => {
  class Element {
    constructor(tag = '') { this.tag = tag; this.children = []; this.attributes = {}; this.dataset = {}; this.handlers = {}; this.classList = { toggle() {} }; }
    setAttribute(name, value) { this.attributes[name] = value; }
    append(...children) { this.children.push(...children); }
    replaceChildren(...children) { this.children = children; }
    addEventListener(name, handler) { this.handlers[name] = handler; }
    querySelectorAll() { return []; }
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
  const defs = { b1: { ...definition, higher_is_better: true }, b2: ambiguousDefinition, b3: { ...ambiguousDefinition }, b4: { ...definition, name: 'Matched bench' } };
  const fixture = {
    'lab/a': { name: 'Alpha', benchmarks: [{ ...result, score: 10 }] },
    'lab/b': { name: 'Beta', benchmarks: [{ ...result, score: 20, effort: 'Adaptive/Max', harness: 'H', future: { budget: 2 } }] },
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
    document: { createElement: tag => new Element(tag), createTextNode: String, querySelector: select, querySelectorAll: () => [], addEventListener() {}, documentElement: new Element() },
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
  } finally {
    for (const [key, descriptor] of previous) {
      if (descriptor) Object.defineProperty(globalThis, key, descriptor); else delete globalThis[key];
    }
  }
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
