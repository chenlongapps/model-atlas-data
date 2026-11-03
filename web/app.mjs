import { modelLab, labLogoUrl, routeFor, parseRoute, filterModels, filterBenchmarks, sortEntries, description, loadData } from './data.mjs';
import { messages, resolveLanguage, descriptionLocale } from './i18n.mjs';
import { createSelect } from './select.mjs';
import { renderModalities } from './modalities.mjs';

let savedLanguage;
try { savedLanguage = localStorage.getItem('model-atlas-language'); } catch { /* Optional preference. */ }
let language = resolveLanguage(savedLanguage, navigator.languages || [navigator.language]);
let T = messages[language];

const main = document.querySelector('#main');
const footer = document.querySelector('#data-info');
let data;
let loadError;
const state = { models: { query: '', lab: '', weights: '', sort: 'newest', page: 1, sortField: '', direction: 'asc' }, benchmarks: { query: '', category: '', page: 1, sortField: '', direction: 'asc' } };
const pageSize = 50;

function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [name, value] of Object.entries(attrs)) {
    if (name === 'class') node.className = value;
    else if (name.startsWith('on')) node.addEventListener(name.slice(2), value);
    else if (value !== undefined && value !== null) node.setAttribute(name, String(value));
  }
  for (const child of children.flat(Infinity)) {
    if (child === null || child === undefined) continue;
    node.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
  return node;
}
function text(value) {
  if (value === undefined || value === null || value === '') return '—';
  if (typeof value === 'boolean') return value ? T.yes : T.no;
  if (typeof value === 'object') return JSON.stringify(value);
  return String(value);
}
function external(url, label) {
  try {
    const parsed = new URL(url);
    if (!['http:', 'https:'].includes(parsed.protocol)) return null;
    return el('a', { href: parsed.href, target: '_blank', rel: 'noopener noreferrer' }, label, ' ↗', el('span', { class: 'sr-only' }, T.external));
  } catch { return null; }
}
function compact(value) {
  if (typeof value !== 'number') return text(value);
  const result = new Intl.NumberFormat(language, { notation: 'compact', maximumFractionDigits: 1 }).format(value);
  return el('span', { title: value.toLocaleString(language), 'aria-label': value.toLocaleString(language) }, result);
}
function internal(kind, id, name, className = '') {
  return el('a', { href: routeFor(kind, id), class: className }, name);
}
function badge(value) {
  return el('span', { class: `pill${value === true ? ' open' : ''}` }, value === true ? T.open : value === false ? T.closed : T.unknown);
}
function labLabel(id) {
  const lab = modelLab(id), url = labLogoUrl(lab);
  const logo = url && el('img', { class: 'lab-logo', alt: '', width: '20', height: '20', loading: 'lazy', referrerpolicy: 'no-referrer', onerror: event => event.currentTarget.remove(), src: url });
  return el('span', { class: 'lab-label' }, logo, lab);
}
function heading(title, intro, count) {
  return el('div', { class: 'page-heading' }, el('h1', {}, title), el('span', { class: 'count' }, count), el('p', { class: 'sr-only' }, intro));
}
function section(title, content, subtitle = '') {
  return el('section', { class: 'detail-section' }, el('div', { class: 'section-heading' }, el('h2', {}, title), subtitle && el('p', {}, subtitle)), content);
}
function facts(entries) {
  return el('dl', { class: 'facts' }, entries.map(([label, value]) => el('div', { class: 'fact' }, el('dt', {}, label), el('dd', {}, value instanceof Node ? value : text(value)))));
}
function table(headers, rows, className = '', sorting = null) {
  if (!rows.length) return el('p', { class: 'state' }, T.empty);
  return el('div', { class: 'table-wrap', tabindex: '0', role: 'region', 'aria-label': headers.join(', ') }, el('table', { class: className },
    el('thead', {}, el('tr', {}, headers.map((h, i) => {
      const field = sorting?.fields[i];
      const active = field && sorting.state.sortField === field;
      return el('th', { scope: 'col', ...(active ? { 'aria-sort': sorting.state.direction === 'asc' ? 'ascending' : 'descending' } : {}) }, field
        ? el('button', { class: 'sort-button', 'data-sort': field, type: 'button', onclick: () => sorting.change(field) }, h, el('span', { 'aria-hidden': 'true' }, active ? (sorting.state.direction === 'asc' ? ' ↑' : ' ↓') : ' ↕')) : h);
    }))),
    el('tbody', {}, rows.map(row => el('tr', {}, row.map(cell => el('td', {}, cell instanceof Node ? cell : text(cell))))))));
}
function search(placeholder, current, change) {
  const input = el('input', { type: 'search', placeholder, 'aria-label': placeholder, oninput: event => change(event.target.value) });
  input.value = current;
  return el('div', { class: 'search-wrap' }, el('span', { class: 'search-icon', 'aria-hidden': 'true' }, '⌕'), input,
    el('button', { type: 'button', 'aria-label': T.clear, onclick: () => { input.value = ''; change(''); input.focus(); } }, '×'));
}
function pagination(total, s, update) {
  const pages = Math.max(1, Math.ceil(total / pageSize));
  s.page = Math.min(s.page, pages);
  return el('div', { class: 'pagination' }, el('span', { 'aria-live': 'polite' }, `${T.countResults(total.toLocaleString(language))} · ${s.page} / ${pages}`),
    el('div', {}, el('button', { type: 'button', ...(s.page === 1 ? { disabled: '' } : {}), onclick: () => { s.page--; update(); } }, T.previous),
      el('button', { type: 'button', ...(s.page === pages ? { disabled: '' } : {}), onclick: () => { s.page++; update(); } }, T.next)));
}
function listing(kind) {
  const isModel = kind === 'models', s = state[kind];
  const collection = isModel ? data.models : data.benchmarks;
  const output = el('div');
  const update = () => {
    let items = isModel ? filterModels(collection, s) : filterBenchmarks(collection, s);
    const values = isModel ? {
      name: ([id, item]) => item.name || id, lab: ([id]) => modelLab(id), release: ([, item]) => item.release_date,
      weights: ([, item]) => typeof item.open_weights === 'boolean' ? (item.open_weights ? 'open' : 'closed') : undefined,
      context: ([, item]) => item.limit?.context, results: ([id]) => (data.index.byModel.get(id) || []).length,
    } : { name: ([id, item]) => item.name || id, version: ([, item]) => item.version, category: ([, item]) => item.category, metric: ([, item]) => item.metric, unit: ([, item]) => item.unit };
    if (s.sortField && values[s.sortField]) items = sortEntries(items, values[s.sortField], s.direction);
    const pager = pagination(items.length, s, update);
    const rows = items.slice((s.page - 1) * pageSize, s.page * pageSize).map(([id, item]) => isModel ? [
      el('div', {}, internal('models', id, item.name || id, 'primary'), el('span', { class: 'sub mono' }, id)),
      labLabel(id), item.release_date, badge(item.open_weights), renderModalities(item.modalities?.input, T.modalityLabels), renderModalities(item.modalities?.output, T.modalityLabels), compact(item.limit?.context), (data.index.byModel.get(id) || []).length,
    ] : [
      el('div', {}, internal('benchmarks', id, item.name || id, 'primary'), el('span', { class: 'sub mono' }, id)),
      item.version, item.category, item.metric, item.unit,
      el('div', { class: 'description-cell' }, text(description(descriptionLocale(language, data.locale), 'benchmark', id, item.description))),
    ]);
    const sorting = { state: s, fields: isModel ? ['name', 'lab', 'release', 'weights', null, null, 'context', 'results'] : ['name', 'version', 'category', 'metric', 'unit', null], change: field => {
      s.direction = s.sortField === field && s.direction === 'asc' ? 'desc' : 'asc'; s.sortField = field; s.page = 1; update();
      output.querySelector(`[data-sort="${field}"]`)?.focus({ preventScroll: true });
    } };
    output.replaceChildren(table(isModel ? [T.model, T.organization, T.release, T.weights, T.input, T.output, T.context, T.results] : [T.benchmark, T.version, T.category, T.metric, T.unit, T.description], rows, '', sorting), pager);
  };
  const change = field => value => { s[field] = value; if (field === 'sort') s.sortField = ''; s.page = 1; update(); };
  const choices = isModel ? [...new Set(Object.keys(collection).map(modelLab))].sort() : [...new Set(Object.values(collection).map(d => d.category).filter(Boolean))].sort();
  const controls = [search(isModel ? T.searchModels : T.searchBenchmarks, s.query, change('query'))];
  if (isModel) controls.push(createSelect(T.organization, [['', T.allLabs], ...choices.map(v => [v, v])], s.lab, change('lab')),
    createSelect(T.weights, [['', T.allWeights], ['open', T.open], ['closed', T.closed], ['unknown', T.unknown]], s.weights, change('weights')),
    createSelect(T.release, [['newest', T.newest], ['oldest', T.oldest]], s.sort, change('sort')));
  else controls.push(createSelect(T.category, [['', T.allCategories], ...choices.map(v => [v, v])], s.category, change('category')));
  main.replaceChildren(heading(isModel ? T.models : T.benchmarks, isModel ? T.modelIntro : T.benchmarkIntro, (isModel ? T.countModels : T.countBenchmarks)(Object.keys(collection).length.toLocaleString(language))), el('div', { class: 'toolbar' }, controls), output);
  update();
}
function resultTable(entries, forModel) {
  if (!entries.length) return el('p', { class: 'state' }, T.noResults);
  const rows = entries.map(entry => {
    const r = entry.result;
    const name = forModel ? (entry.status === 'matched' ? internal('benchmarks', entry.benchmarkId, r.name, 'primary') : el('span', {}, r.name, ' ', el('span', { class: 'pill' }, entry.status === 'ambiguous' ? T.ambiguous : T.unmatched))) : internal('models', entry.modelId, data.models[entry.modelId]?.name || entry.modelId, 'primary');
    // Keep every present/future result field, including nested test conditions.
    const extra = Object.entries(r).filter(([key]) => !['name', 'score', 'metric', 'version', 'source'].includes(key));
    const conditions = el('div', { class: 'conditions' }, extra.length ? extra.map(([key, value]) => el('span', { class: 'condition' }, el('b', {}, `${key}: `), text(value))) : '—');
    return [name, r.score, r.metric, r.version, conditions, external(r.source, T.source) || text(r.source)];
  });
  return table([forModel ? T.benchmark : T.model, T.score, T.metric, T.version, T.conditions, T.source], rows, 'result-table');
}
function detailHeader(kind, id, title, desc) {
  const copy = el('button', { class: 'copy-button', type: 'button', 'aria-label': T.copyId, onclick: async () => {
    try { await navigator.clipboard.writeText(id); copy.textContent = T.copied; } catch { copy.textContent = T.copyUnavailable; }
  } }, T.copy);
  return el('div', { class: 'detail-header' }, el('div', { class: 'breadcrumbs' }, el('a', { href: routeFor(kind) }, kind === 'models' ? T.models : T.benchmarks), ' / ', kind === 'models' ? modelLab(id) : T.definition),
    el('h1', {}, title), desc && el('p', {}, desc), el('div', { class: 'code-line' }, el('code', {}, id), copy));
}
function modelDetail(id) {
  if (!Object.hasOwn(data.models, id)) return notFound();
  const m = data.models[id];
  const links = [...(m.links || []), ...(m.weights || [])].map(link => external(link.url, link.label || link.type || link.url)).filter(Boolean);
  const caps = Object.entries(m.capabilities || {}).map(([key, value]) => [key,
    value && typeof value === 'object' && Object.keys(value).length === 1 && 'supported' in value ? text(value.supported) : text(value)]);
  const modalities = Object.entries(m.modalities || {}).map(([key, value]) => [T.modalities(key), Array.isArray(value) ? value.join(', ') : text(value)]);
  const limitNames = { context: T.contextWindow, input: T.maxInput, output: T.maxOutput, request_bytes: T.requestBytes };
  const limits = Object.entries(m.limit || {}).map(([key, value]) => [limitNames[key] || key, compact(value)]);
  const entries = data.index.byModel.get(id) || [];
  main.replaceChildren(detailHeader('models', id, m.name, description(descriptionLocale(language, data.locale), 'model', id, m.description)),
    section(T.overview, facts([[T.modelId, id], [T.organization, labLabel(id)], [T.family, m.family], [T.release, m.release_date], [T.weights, badge(m.open_weights)], [T.license, m.license]])),
    section(T.sourcesLinks, links.length ? el('div', { class: 'external-links' }, links) : el('p', {}, T.noLinks)),
    section(T.capabilities, facts([...modalities, ...caps].length ? [...modalities, ...caps] : [[T.information, '—']])),
    section(T.limits, facts(limits.length ? limits : [[T.information, '—']])),
    section(T.results, el('div', {}, el('p', { class: 'note' }, T.matchNote, ' ', T.resultNote), resultTable(entries, true)), T.countRecords(entries.length.toLocaleString(language))));
}
function benchmarkDetail(id) {
  if (!Object.hasOwn(data.benchmarks, id)) return notFound();
  const b = data.benchmarks[id];
  const links = [external(b.url, T.website), external(b.methodology, T.methodLink)].filter(Boolean);
  const entries = data.index.byBenchmark.get(id) || [];
  main.replaceChildren(detailHeader('benchmarks', id, b.name, description(descriptionLocale(language, data.locale), 'benchmark', id, b.description)),
    section(T.overview, facts([[T.benchmarkId, id], [T.version, b.version], [T.category, b.category], [T.organization, b.organization]])),
    section(T.definition, facts([[T.metric, b.metric], [T.unit, b.unit], [T.higherBetter, b.higher_is_better], [T.minScore, b.min_score], [T.maxScore, b.max_score]])),
    section(T.methodology, links.length ? el('div', { class: 'external-links' }, links) : el('p', {}, T.noLinks)),
    section(T.modelResults, el('div', {}, el('p', { class: 'note' }, T.matchNote, ' ', T.resultNote), resultTable(entries, false)), T.countRecords(entries.length.toLocaleString(language))));
}
function notFound() {
  main.replaceChildren(el('p', { class: 'eyebrow' }, T.dataExplorer), el('h1', {}, T.notFound), el('p', {}, T.notFoundText), el('a', { href: routeFor('models') }, T.backModels));
}
function render(scroll = true) {
  if (!data) return;
  const route = parseRoute(location.hash);
  document.querySelectorAll('[data-nav]').forEach(link => {
    const active = link.dataset.nav === route.kind;
    link.classList.toggle('active', active);
    if (active) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current');
  });
  if (route.kind === 'notfound') notFound();
  else if (route.id === undefined) listing(route.kind);
  else if (route.kind === 'models') modelDetail(route.id);
  else benchmarkDetail(route.id);
  if (scroll === true) document.querySelector('.page-scroll').scrollTo(0, 0);
}
function showManifest(manifest) {
  if (!manifest) return footer.replaceChildren(el('span', {}, T.manifestMissing));
  footer.replaceChildren(...[[T.dataVersion, manifest.data_version], [T.published, manifest.published_at], [T.commit, manifest.git_commit]].map(([label, value]) => el('span', {}, `${label}: ${text(value)}`)));
}
async function start() {
  loadError = undefined;
  main.replaceChildren(el('p', { class: 'state', role: 'status' }, T.loading));
  try {
    data = await loadData();
    showManifest(data.manifest);
    render();
  } catch (error) {
    loadError = error;
    showError();
    showManifest(null);
  }
}
function showError() {
  main.replaceChildren(el('div', { class: 'state', role: 'alert' }, el('p', {}, T.error), el('p', { class: 'mono' }, loadError.message), el('button', { type: 'button', onclick: start }, T.retry)));
}
const themeButton = document.querySelector('#theme');
let theme = 'system';
try { theme = localStorage.getItem('model-atlas-theme') || 'system'; } catch { /* Storage can be disabled. */ }
if (!['system', 'light', 'dark'].includes(theme)) theme = 'system';
function applyTheme() {
  if (theme === 'system') delete document.documentElement.dataset.theme; else document.documentElement.dataset.theme = theme;
  const name = T[{ system: 'themeSystem', light: 'themeLight', dark: 'themeDark' }[theme]];
  themeButton.textContent = `${T.themeLabel}: ${name}`;
  themeButton.setAttribute('aria-label', `${T.changeTheme}: ${name}`);
}
themeButton.addEventListener('click', () => {
  theme = ({ system: 'light', light: 'dark', dark: 'system' })[theme];
  try { localStorage.setItem('model-atlas-theme', theme); } catch { /* Optional preference. */ }
  applyTheme();
});
applyTheme();
const searchDialog = document.querySelector('#search-dialog');
const searchInput = document.querySelector('#global-search');
const searchResults = document.querySelector('#search-results');
const searchCount = document.querySelector('#search-count');
const menu = document.querySelector('#mobile-menu');
function updateGlobalSearch() {
  const query = searchInput.value.trim().toLowerCase();
  if (!data) { searchCount.textContent = T.dataUnavailable; searchResults.replaceChildren(); return; }
  if (!query) { searchCount.textContent = T.searchHint; searchResults.replaceChildren(); return; }
  const models = filterModels(data.models, { query }).map(([id, item]) => ({ kind: 'models', id, name: item.name || id }));
  const benchmarks = filterBenchmarks(data.benchmarks, { query }).map(([id, item]) => ({ kind: 'benchmarks', id, name: item.name || id }));
  const results = [...models, ...benchmarks];
  searchCount.textContent = `${T.countResults(results.length.toLocaleString(language))}${results.length > 50 ? ` · ${T.first50}` : ''}`;
  searchResults.replaceChildren(...results.slice(0, 50).map(item => el('a', { class: 'search-result', href: routeFor(item.kind, item.id), onclick: () => searchDialog.close() },
    el('span', { class: 'search-result-title' }, item.name), el('span', { class: 'search-kind' }, item.kind === 'models' ? T.model : T.benchmark), el('span', { class: 'mono search-id' }, item.id))));
}
function openSearch() {
  if (!searchDialog.open) searchDialog.showModal();
  updateGlobalSearch();
  searchInput.focus();
}
document.querySelector('#search-trigger').addEventListener('click', openSearch);
document.addEventListener('keydown', event => {
  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); if (menu.open) menu.close(); openSearch(); }
});
searchInput.addEventListener('input', updateGlobalSearch);
document.querySelector('#menu-trigger').addEventListener('click', () => menu.showModal());
menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => menu.close()));
document.querySelectorAll('[data-close]').forEach(button => button.addEventListener('click', () => document.getElementById(button.dataset.close).close()));
document.querySelector('.skip').addEventListener('click', event => { event.preventDefault(); main.focus(); });
window.addEventListener('hashchange', () => render());
const languageSelect = document.querySelector('#language');
function applyLanguage() {
  T = messages[language];
  document.documentElement.lang = language;
  document.title = T.title;
  document.querySelector('meta[name="description"]').content = T.metaDescription;
  document.querySelectorAll('[data-i18n]').forEach(node => { node.textContent = T[node.dataset.i18n]; });
  document.querySelectorAll('[data-i18n-aria]').forEach(node => node.setAttribute('aria-label', T[node.dataset.i18nAria]));
  document.querySelectorAll('[data-i18n-placeholder]').forEach(node => node.setAttribute('placeholder', T[node.dataset.i18nPlaceholder]));
  languageSelect.replaceChildren(createSelect(T.language, [['en', 'English'], ['zh-CN', '中文']], language, value => {
    language = value;
    try { localStorage.setItem('model-atlas-language', language); } catch { /* Optional preference. */ }
    applyLanguage();
    languageSelect.querySelector('button').focus({ preventScroll: true });
  }));
  applyTheme();
  if (data) { render(false); showManifest(data.manifest); }
  else if (loadError) { showError(); showManifest(null); }
  else { main.replaceChildren(el('p', { class: 'state', role: 'status' }, T.loading)); footer.textContent = T.loadingRelease; }
  if (searchDialog.open) updateGlobalSearch();
}
applyLanguage();
start();
