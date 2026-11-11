// Pure data helpers shared by the explorer and its Node tests.
export function modelLab(id) {
  return id.split('/')[0];
}

export function labLogoUrl(lab) {
  // Match the model-path slug validation; never let data change the host or path.
  return typeof lab === 'string' && /^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(lab)
    ? `https://models.dev/logos/${lab}.svg` : null;
}

export function routeFor(kind, id) {
  return `#/${kind}${id === undefined ? '' : `/${encodeURIComponent(id)}`}`;
}

export function parseRoute(hash) {
  if (!hash || hash === '#' || hash === '#/') return { kind: 'models' };
  const match = /^#\/(models|benchmarks)(?:\/([^/]+))?\/?$/.exec(hash);
  if (!match) return { kind: 'notfound' };
  try {
    const id = match[2] === undefined ? undefined : decodeURIComponent(match[2]);
    if (id !== undefined && (!id || (match[1] === 'models' && !/^[^/]+\/[^/]+$/.test(id)))) return { kind: 'notfound' };
    return { kind: match[1], id };
  } catch { return { kind: 'notfound' }; }
}

export function filterModels(models, { query = '', lab = '', weights = '', sort = 'newest' } = {}) {
  const term = query.trim().toLowerCase();
  return Object.entries(models || {}).filter(([id, model]) =>
    `${model.name || ''} ${id} ${modelLab(id)}`.toLowerCase().includes(term) &&
    (!lab || modelLab(id) === lab) &&
    (!weights || (weights === 'unknown' ? typeof model.open_weights !== 'boolean' : model.open_weights === (weights === 'open')))
  ).sort(([idA, a], [idB, b]) => {
    const dateA = a.release_date || '', dateB = b.release_date || '';
    if (!dateA !== !dateB) return dateA ? -1 : 1;
    return (sort === 'oldest' ? dateA.localeCompare(dateB) : dateB.localeCompare(dateA)) || idA.localeCompare(idB);
  });
}

export function filterBenchmarks(definitions, { query = '', category = '' } = {}) {
  const term = query.trim().toLowerCase();
  return Object.entries(definitions || {}).filter(([id, d]) =>
    `${id} ${d.name || ''} ${d.category || ''} ${d.organization || ''}`.toLowerCase().includes(term) &&
    (!category || d.category === category)
  ).sort(([a, x], [b, y]) => {
    // Editorial display priority, not a benchmark result; missing values stay last.
    const hasX = Number.isFinite(x.popularity) && x.popularity >= 0 && x.popularity <= 1;
    const hasY = Number.isFinite(y.popularity) && y.popularity >= 0 && y.popularity <= 1;
    if (hasX !== hasY) return hasX ? -1 : 1;
    return (hasX ? y.popularity - x.popularity : 0) ||
      (x.name || a).localeCompare(y.name || b) || a.localeCompare(b);
  });
}

// Missing values remain last in both directions; ties have a stable ID order.
export function sortEntries(entries, valueOf, direction = 'asc') {
  return [...entries].sort((a, b) => {
    const x = valueOf(a), y = valueOf(b);
    const missingX = x === undefined || x === null || x === '';
    const missingY = y === undefined || y === null || y === '';
    if (missingX !== missingY) return missingX ? 1 : -1;
    if (missingX) return a[0].localeCompare(b[0]);
    const comparison = typeof x === 'number' && typeof y === 'number' ? x - y : String(x).localeCompare(String(y), undefined, { numeric: true, sensitivity: 'base' });
    return (direction === 'desc' ? -comparison : comparison) || a[0].localeCompare(b[0]);
  });
}

// Display order only: matching a definition does not establish comparability.
export function sortBenchmarkResults(entries, definition) {
  if (typeof definition?.higher_is_better !== 'boolean') return [...entries];
  return sortEntries(entries.map(entry => [entry.modelId, entry]),
    ([, entry]) => Number.isFinite(entry.result.score) ? entry.result.score : undefined,
    definition.higher_is_better ? 'desc' : 'asc').map(([, entry]) => entry);
}

const key = d => JSON.stringify([d.name, d.version, d.metric]);

export function buildIndex(models = {}, definitions = {}) {
  const lookup = new Map(), byModel = new Map(), byBenchmark = new Map();
  for (const [id, definition] of Object.entries(definitions)) {
    const k = key(definition);
    if (!lookup.has(k)) lookup.set(k, []);
    lookup.get(k).push(id);
    byBenchmark.set(id, []);
  }
  for (const [modelId, model] of Object.entries(models)) {
    const results = (Array.isArray(model.benchmarks) ? model.benchmarks : []).map(result => {
      const candidates = result.name && result.version && result.metric ? (lookup.get(key(result)) || []) : [];
      const status = candidates.length === 1 ? 'matched' : candidates.length > 1 ? 'ambiguous' : 'unmatched';
      const entry = { modelId, result, status, benchmarkId: status === 'matched' ? candidates[0] : undefined };
      if (entry.benchmarkId) byBenchmark.get(entry.benchmarkId).push(entry);
      return entry;
    });
    byModel.set(modelId, results);
  }
  // Multiple efforts, sources or other conditions still count as one model.
  const modelCountByBenchmark = new Map([...byBenchmark].map(([id, entries]) =>
    [id, new Set(entries.map(entry => entry.modelId)).size]));
  return { byModel, byBenchmark, modelCountByBenchmark };
}

export function description(locale, type, id, original) {
  const translated = type === 'model' ? locale?.model?.descriptions?.[id] : locale?.benchmark?.description?.[id];
  return translated || original || '';
}

// Optional resources fail independently; required data failures are surfaced to the UI.
export async function loadData(fetcher = fetch) {
  async function json(path) {
    const response = await fetcher(path);
    if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
    return response.json();
  }
  const [models, benchmarks, locale, manifest] = await Promise.all([
    json('./models.json'), json('./benchmarks.json'),
    json('./i18n/zh-CN.json').catch(() => ({})), json('./manifest.json').catch(() => null),
  ]);
  return { models, benchmarks, locale, manifest, index: buildIndex(models, benchmarks) };
}
