import { routeFor, labLogoUrl, sortBenchmarkResults } from './data.mjs';
import { createSelect } from './select.mjs';
import { costOptions, defaultChartAxis, chartPoints, conditionKey, comparisonGroups, scoreDomain, frontierUnavailable, paretoFront, median, numericDomain, axisTicks, formatTick, costAxis, formatCostTick, placeLabels, labColor, hasBenchmarkCost } from './chart-data.mjs';

function node(tag, attrs = {}, ...children) {
  const element = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (key === 'class') element.className = value;
    else if (key.startsWith('on')) element.addEventListener(key.slice(2), value);
    else if (value !== undefined) element.setAttribute(key, String(value));
  }
  element.append(...children.flat(Infinity).filter(child => child !== undefined && child !== null));
  return element;
}
function svg(tag, attrs = {}, ...children) {
  const element = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const [key, value] of Object.entries(attrs)) element.setAttribute(key, String(value));
  element.append(...children);
  return element;
}
function link(url, label, externalLabel) {
  try {
    const parsed = new URL(url);
    if (['http:', 'https:'].includes(parsed.protocol)) return node('a', { href: parsed.href, target: '_blank', rel: 'noopener noreferrer', 'aria-label': `${label}${externalLabel}` }, label, ' ↗');
  } catch { /* Unknown or unsafe provenance remains plain text. */ }
  return node('span', {}, label);
}
const valueText = value => value === undefined || value === null || value === '' ? '—' : typeof value === 'object' ? JSON.stringify(value) : String(value);
const effortKey = result => Object.hasOwn(result, 'effort') ? JSON.stringify([result.effort]) : 'missing';
const pointColor = lab => lab === 'openai' ? 'var(--chart-openai)' : labColor(lab);
const modelLabel = point => `${point.name}${point.result.effort ? ` (${point.result.effort})` : ''}`;
const pointLabels = points => [...new Map(points.map(point => [modelLabel(point), { text: modelLabel(point), color: pointColor(point.lab) }])).values()];

// A self-contained card: it never mutates source entries or filters the raw table.
// Only its small preference object survives page/language re-renders.
export function createBenchmarkChart({ id, definition, entries, models, manifest, language, T, state = {} }) {
  const units = costOptions(entries);
  const missingCostCount = entries.filter(({ result }) => Number.isFinite(result.score) && !hasBenchmarkCost(result)).length;
  if (!['score', 'cost', 'release'].includes(state.axis)) state.axis = defaultChartAxis(entries);
  if (!units.some(([unit]) => unit === state.unit)) state.unit = units[0]?.[0] || '';
  state.group ??= '';
  state.effort ??= '';
  state.query ??= '';
  const labs = [...new Set(entries.map(entry => entry.modelId.split('/')[0]))].sort();
  if (!labs.includes(state.lab)) state.lab = '';
  state.frontier ??= true;
  state.quadrants ??= true;
  if (!['log', 'linear'].includes(state.scale)) state.scale = 'log';
  state.filtersOpen ??= false;
  const dateFormat = new Intl.DateTimeFormat(language, { year: 'numeric', month: '2-digit', day: '2-digit', timeZone: 'UTC' });
  let available = [], groups = [], displayed = [], marks = [], activeKey, pinned = false, clearing = false;
  let updateLabels = () => {}, scaleSignature;

  const root = node('section', { class: 'benchmark-chart', 'aria-label': T.chartTitle });
  const unitControl = node('div'), groupControl = node('div'), scaleControl = node('div');
  const plot = node('div', { class: 'chart-scroll', tabindex: '0', role: 'region', 'aria-label': T.chartTitle });
  const info = node('div', { class: 'chart-info' });
  const status = node('p', { class: 'chart-status', role: 'status', 'aria-live': 'polite' });
  const scaleNotice = node('span', { class: 'chart-scale-notice', role: 'status' });
  const thresholds = node('p', { class: 'chart-thresholds' });
  const frontierInfo = node('div', { class: 'chart-frontier-info' });
  const detailBody = node('div', { class: 'chart-detail-body' });
  const detailLabel = node('span', {}, T.chartInspect);
  const close = node('button', { type: 'button', 'aria-label': T.chartClearSelection, onclick: () => clearSelection(true) }, '×');
  close.hidden = true;
  const detailId = `chart-detail-${id}`;
  const details = node('aside', { id: detailId, class: 'chart-detail', 'aria-label': T.chartDetails }, node('div', { class: 'chart-detail-heading' }, detailLabel, close), detailBody);
  details.hidden = true;
  const layout = node('div', { class: 'chart-layout' }, plot, details);
  layout.addEventListener('pointerleave', () => { if (!pinned) clearSelection(); });
  plot.addEventListener('click', event => { if (!marks.some(mark => mark.element.contains(event.target))) clearSelection(); });
  plot.addEventListener('scroll', () => {
    const active = marks.find(mark => mark.key === activeKey);
    if (active) positionDetails(active);
  });

  function toggle(label, key) {
    const input = node('input', { type: 'checkbox', onchange: event => { state[key] = event.target.checked; draw(true); } });
    return { input, element: node('label', { class: 'chart-toggle' }, input, label) };
  }
  const quadrants = toggle(T.chartQuadrants, 'quadrants'), frontier = toggle(T.chartFrontier, 'frontier');
  const comparisonBadge = node('span', { class: 'chart-comparison-badge' });
  const controls = node('div', { class: 'chart-switches' }, comparisonBadge, quadrants.element, frontier.element);
  const direction = typeof definition.higher_is_better === 'boolean' ? (definition.higher_is_better ? T.chartHigher : T.chartLower) : T.chartUnknownDirection;
  root.append(node('div', { class: 'chart-heading' }, node('div', {}, node('h2', {}, T.chartTitle), node('p', {}, `${definition.name} · ${definition.version} · ${definition.metric} (${definition.unit}) · ${direction}`)), controls));

  const input = node('input', { type: 'search', 'aria-label': T.chartSearch, placeholder: T.chartSearch, oninput: event => { state.query = event.target.value; draw(true); } });
  input.value = state.query;
  const search = node('div', { class: 'chart-search' }, input, node('button', { type: 'button', 'aria-label': T.clear, onclick: () => { state.query = ''; input.value = ''; draw(true); input.focus(); } }, '×'));
  const axis = createSelect(T.chartView, [['score', T.chartBars], ['cost', T.chartCostScatter], ['release', T.chartReleaseScatter]], state.axis, value => { state.axis = value; state.group = ''; refresh(); });
  unitControl.append(createSelect(T.chartCostUnit, units.length ? units.map(([unit, count]) => [unit, `${unit} (${count})`]) : [['', T.chartNoCosts]], state.unit, value => { state.unit = value; state.group = ''; refresh(); }));
  const efforts = [...new Map(entries.map(entry => [effortKey(entry.result), valueText(entry.result.effort)])).entries()].sort(([, a], [, b]) => a.localeCompare(b));
  if (!efforts.some(([key]) => key === state.effort)) state.effort = '';
  const effort = createSelect(T.effort, [['', T.chartAllEfforts], ...efforts], state.effort, value => { state.effort = value; state.group = ''; refresh(); });
  const filterPanel = node('div', { id: `chart-filters-${id}`, class: 'chart-filter-panel' }, effort, groupControl);
  const filterButton = node('button', { type: 'button', class: 'chart-filter-button', 'aria-controls': `chart-filters-${id}`, onclick: () => { state.filtersOpen = !state.filtersOpen; syncFilters(); } });
  function syncFilters() {
    filterPanel.hidden = !state.filtersOpen;
    filterButton.setAttribute('aria-expanded', String(state.filtersOpen));
    const count = Number(Boolean(state.effort)) + Number(Boolean(state.group));
    filterButton.textContent = `${T.chartFilters}${count ? ` (${count})` : ''}`;
    filterButton.classList.toggle('has-filters', count > 0);
  }
  root.append(node('div', { class: 'chart-toolbar' }, axis, unitControl, scaleControl, search, filterButton, scaleNotice), filterPanel);

  const legendButtons = new Map();
  const legend = node('div', { class: 'chart-legend', 'aria-label': T.organization });
  for (const lab of labs) {
    const count = node('span', { class: 'chart-legend-count' });
    const button = node('button', { type: 'button', 'data-lab': lab, 'aria-pressed': String(state.lab === lab), onclick: () => {
      state.lab = state.lab === lab ? '' : lab;
      draw();
    } }, node('span', { class: 'chart-swatch', style: `--lab-color: ${pointColor(lab)}`, 'aria-hidden': 'true' }), lab, count);
    legendButtons.set(lab, { button, count });
    legend.append(button);
  }
  const showAll = node('button', { type: 'button', class: 'chart-show-all', onclick: () => { state.lab = ''; draw(); } }, T.chartShowAll);
  legend.append(showAll);
  const limitation = node('p', { class: 'chart-note' });
  root.append(layout, thresholds, frontierInfo, legend, status, node('details', { class: 'chart-notes' }, node('summary', {}, T.chartNotes), limitation), info);
  root.addEventListener('keydown', event => {
    if (event.key === 'Escape' && activeKey !== undefined) { event.preventDefault(); clearSelection(true); }
  });

  function groupLabel(group) {
    const r = group.result;
    const extras = Object.entries(r).filter(([key]) => !['name', 'version', 'metric', 'score', 'cost', 'cost_unit', 'cost_source', 'source', 'effort', 'dataset', 'harness', 'variant'].includes(key));
    return `${valueText(r.source)} · ${T.effort}: ${valueText(r.effort)} · ${T.chartDataset}: ${valueText(r.dataset)} · ${T.chartHarness}: ${valueText(r.harness)} · ${T.conditions}: ${valueText(r.variant)}${extras.map(([key, value]) => ` · ${key}: ${valueText(value)}`).join('')} · ${T.countRecords(group.points.length)}`;
  }
  const effortPoints = () => available.filter(point => !state.effort || effortKey(point.result) === state.effort);
  function refresh() {
    unitControl.hidden = state.axis !== 'cost';
    available = chartPoints(entries, models, state.axis, state.unit);
    groups = comparisonGroups(effortPoints(), { includeSingletons: state.axis === 'score' });
    if (!groups.some(group => group.key === state.group)) state.group = '';
    groupControl.replaceChildren(createSelect(T.conditions, [['', T.chartAllConditions], ...groups.map(group => [group.key, groupLabel(group)])], state.group, value => { state.group = value; draw(); }));
    draw();
  }
  function registerMark(mark) {
    const { element } = mark, index = marks.length;
    marks.push(mark);
    let touching = false;
    element.addEventListener('pointerenter', event => { if (event.pointerType !== 'touch') inspect(mark); });
    element.addEventListener('pointerdown', event => { touching = event.pointerType === 'touch'; });
    element.addEventListener('pointercancel', () => { touching = false; });
    element.addEventListener('focus', () => {
      if (!touching && !clearing) {
        element.scrollIntoView?.({ block: 'nearest', inline: 'nearest' });
        inspect(mark);
      }
    });
    element.addEventListener('click', () => { touching = false; inspect(mark, true); });
    element.addEventListener('keydown', event => {
      if (['Enter', ' '].includes(event.key)) { event.preventDefault(); inspect(mark, true); }
      if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Home', 'End'].includes(event.key)) {
        event.preventDefault();
        const target = event.key === 'Home' ? 0 : event.key === 'End' ? marks.length - 1 : (index + (['ArrowRight', 'ArrowDown'].includes(event.key) ? 1 : -1) + marks.length) % marks.length;
        marks[target].element.focus({ preventScroll: true });
        if (!pinned) inspect(marks[target]);
        marks.forEach((item, i) => item.element.setAttribute('tabindex', i === target ? '0' : '-1'));
      }
    });
  }

  function drawBars(viewportWidth, matches, term) {
    // Like the raw table, this is a score-ordered view of original observations,
    // not a comparable ranking. Never collapse a model's different records.
    const points = sortBenchmarkResults(displayed, definition);
    const narrow = viewportWidth < 600, left = 48, edge = 24, top = 38;
    const width = Math.max(viewportWidth, points.length * 66 + left + edge);
    const height = narrow ? 520 : 580, bottom = height - 230;
    const step = (width - left - edge) / points.length, barWidth = Math.min(52, step - 20);
    const domain = scoreDomain(points.map(point => point.y));
    const y = value => bottom - (value - domain[0]) / (domain[1] - domain[0]) * (bottom - top);
    const baseline = y(0);
    const canvas = svg('svg', { viewBox: `0 0 ${width} ${height}`, style: `width: ${width}px`, class: 'chart-svg chart-bars', 'data-scale': 'score', role: 'group', 'aria-label': `${T.chartBars}: ${definition.name}. ${T.chartKeyboardHint}` }, svg('title', {}, `${definition.name} · ${definition.metric}`));
    const ticks = axisTicks(domain, 4);
    const grid = svg('g', { class: 'chart-grid', 'aria-hidden': 'true' });
    for (const tick of ticks) grid.append(svg('line', { x1: left, x2: width - edge, y1: y(tick), y2: y(tick) }),
      svg('text', { x: left - 12, y: y(tick) + 4, 'text-anchor': 'end' }, formatTick(tick, ticks, language)));
    grid.append(svg('line', { class: 'chart-zero-axis', x1: left, x2: width - edge, y1: baseline, y2: baseline }));
    canvas.append(grid, svg('text', { class: 'chart-axis-label', x: left, y: 18 }, `${definition.metric} (${definition.unit})`));
    points.forEach((point, index) => {
      const label = modelLabel(point), score = String(point.y), isMatch = Boolean(term && matches(point));
      const cx = left + step * (index + 0.5), color = pointColor(point.lab);
      const barTop = Math.min(y(point.y), baseline), barHeight = Math.abs(y(point.y) - baseline);
      const scoreInside = barHeight >= 32;
      const scoreY = scoreInside ? barTop + barHeight / 2 : point.y < 0 ? y(point.y) + 16 : y(point.y) - 12;
      const element = svg('g', { class: `chart-bar${isMatch ? ' is-match' : term ? ' is-dimmed' : ''}`, tabindex: marks.length ? '-1' : '0', role: 'button', 'aria-pressed': 'false', 'aria-expanded': 'false', 'aria-controls': detailId, 'aria-label': `${label}, ${T.score}: ${score}. ${groupLabel({ result: point.result, points: [point] })}. ${T.chartPointHint}` });
      element.append(svg('rect', { class: 'chart-hit', x: cx - step / 2 + 2, y: top, width: step - 4, height: height - top - 12 }),
        svg('rect', { class: 'chart-bar-fill', x: cx - barWidth / 2, y: barTop, width: barWidth, height: barHeight, rx: 7, fill: color }),
        svg('rect', { class: 'chart-bar-base', x: cx - barWidth / 2, y: point.y < 0 ? baseline : baseline - Math.min(7, barHeight / 2), width: barWidth, height: Math.min(7, barHeight / 2), fill: color }));
      if (point.y === 0) element.append(svg('line', { class: 'chart-bar-zero', x1: cx - barWidth / 2, x2: cx + barWidth / 2, y1: baseline, y2: baseline, stroke: color }));
      // Keep the original number even when it needs a smaller font to fit.
      element.append(svg('text', { class: `chart-bar-score${scoreInside ? ' is-inside' : ''}`, x: cx, y: scoreY, 'text-anchor': 'middle', 'dominant-baseline': 'central', style: `font-size: ${Math.min(22, (barWidth - 8) / (score.length * 0.62))}px${scoreInside && point.lab === 'openai' ? '; fill: var(--bg)' : ''}` }, score));
      const logoY = bottom + 18;
      const fallback = svg('text', { class: 'chart-bar-logo-fallback', x: cx, y: logoY + 17, 'text-anchor': 'middle' }, point.lab.slice(0, 2).toUpperCase());
      const logoUrl = labLogoUrl(point.lab);
      if (logoUrl) {
        const logo = svg('image', { href: logoUrl, x: cx - 12, y: logoY, width: 24, height: 24, 'aria-hidden': 'true' });
        logo.addEventListener('error', () => logo.replaceWith(fallback));
        element.append(svg('rect', { x: cx - 12, y: logoY, width: 24, height: 24, rx: 3, fill: '#fff', 'aria-hidden': 'true' }), logo);
      } else element.append(fallback);
      const name = svg('text', { class: 'chart-bar-name', transform: `translate(${cx + 4} ${bottom + 62}) rotate(-60)`, 'text-anchor': 'end' });
      // Wrap before rotating so long model names remain readable, not clipped.
      const lines = [''];
      for (const word of label.split(/\s+/)) {
        const last = lines.length - 1;
        if (lines[last] && (lines[last].length + word.length > 22)) lines.push(word);
        else lines[last] += `${lines[last] ? ' ' : ''}${word}`;
      }
      lines.slice(0, 3).forEach((line, i) => name.append(svg('tspan', { x: 0, dy: i ? 17 : 0 }, line.length > 24 ? `${line.slice(0, 23)}…` : line)));
      name.append(svg('title', {}, label));
      element.append(name);
      registerMark({ key: point.id, points: [point], element, cx, cy: scoreY, width, height });
      canvas.append(element);
    });
    return canvas;
  }

  function finishPlot(canvas, previousKey, wasPinned, restoreFocus) {
    plot.replaceChildren(canvas);
    const previous = marks.find(mark => mark.key === previousKey);
    if (previous) {
      inspect(previous, wasPinned);
      if (restoreFocus) previous.element.focus({ preventScroll: true });
    }
  }
  function clearSelection(focus = false) {
    clearing = true;
    const active = marks.find(mark => mark.key === activeKey);
    if (focus) active?.element.focus({ preventScroll: true });
    activeKey = undefined;
    pinned = false;
    for (const mark of marks) {
      mark.element.classList.toggle('is-active', false);
      mark.element.setAttribute('aria-pressed', 'false');
      mark.element.setAttribute('aria-expanded', 'false');
    }
    close.hidden = true;
    detailLabel.textContent = T.chartInspect;
    detailBody.replaceChildren(node('p', {}, T.chartInspectHint));
    details.hidden = true;
    details.setAttribute('data-pinned', 'false');
    clearing = false;
    updateLabels();
  }
  function positionDetails(mark) {
    const width = layout.clientWidth || mark.width;
    const cx = mark.cx - (plot.scrollLeft || 0);
    const cardWidth = Math.min(328, width - 24);
    const fitsRight = cx + cardWidth + 30 < width, fitsLeft = cx - cardWidth - 30 > 0;
    let topLimit = 12, bottomLimit = mark.height - 12;
    const rect = layout.getBoundingClientRect?.();
    if (rect && typeof window !== 'undefined' && Number.isFinite(window.innerHeight)) {
      const header = document.querySelector?.('.site-header')?.getBoundingClientRect?.();
      const viewportTop = (header?.bottom || 0) + 12 - rect.top;
      topLimit = Math.max(topLimit, viewportTop);
      bottomLimit = Math.min(bottomLimit, window.innerHeight - rect.top - 12);
      // At the very edge of the viewport a floating card may extend above the
      // plot, rather than being squeezed to an unreadable height below it.
      if (bottomLimit - topLimit < 160) topLimit = viewportTop;
    }
    const above = mark.cy - topLimit - 16, below = bottomLimit - mark.cy - 16;
    // On narrow screens the card cannot sit beside the point. Limit its height
    // to the larger vertical gap instead of covering the click/touch target.
    const maxHeight = Math.min(360, fitsRight || fitsLeft ? bottomLimit - topLimit : Math.max(above, below));
    details.setAttribute('style', `width: ${cardWidth}px; max-height: ${maxHeight}px`);
    const cardHeight = details.offsetHeight || Math.min(280, maxHeight);
    const left = Math.max(12, Math.min(width - cardWidth - 12, fitsRight ? cx + 18 : cx - cardWidth - 18));
    const placeBelow = fitsRight || fitsLeft ? mark.cy + cardHeight + 30 < mark.height : below >= above;
    const top = Math.max(topLimit, Math.min(bottomLimit - cardHeight, placeBelow ? mark.cy + 18 : mark.cy - cardHeight - 18));
    details.setAttribute('style', `left: ${left}px; top: ${top}px; width: ${cardWidth}px; max-height: ${maxHeight}px`);
  }
  function inspect(mark, pin = false) {
    if (clearing || pinned && !pin) return;
    pinned = pin ? !(pinned && activeKey === mark.key) : false;
    activeKey = mark.key;
    for (const item of marks) {
      item.element.classList.toggle('is-active', item === mark);
      item.element.setAttribute('tabindex', item === mark ? '0' : '-1');
      item.element.setAttribute('aria-pressed', String(item === mark && pinned));
      item.element.setAttribute('aria-expanded', String(item === mark));
    }
    close.hidden = false;
    details.hidden = false;
    details.setAttribute('data-pinned', String(pinned));
    detailLabel.textContent = `${pinned ? T.chartPinned : T.chartDetails}${mark.points.length > 1 ? ` · ${T.chartOverlap(mark.points.length)}` : ''}`;
    detailBody.replaceChildren(...mark.points.map(point => {
      const r = point.result;
      const facts = [[T.organization, point.lab], [T.score, String(r.score)], [T.chartCost, hasBenchmarkCost(r) ? `${r.cost} ${r.cost_unit}` : '—'], [T.release, valueText(point.release)]];
      // Preserve unknown conditions just as the raw result table does.
      for (const [key, value] of Object.entries(r)) {
        if (!['name', 'score', 'cost', 'cost_unit', 'cost_source', 'source'].includes(key)) facts.push([({ effort: T.effort, metric: T.metric, version: T.version, dataset: T.chartDataset, harness: T.chartHarness, variant: T.conditions })[key] || key, valueText(value)]);
      }
      return node('article', { class: 'chart-record' }, node('a', { class: 'primary', href: routeFor('models', point.modelId) }, point.name), node('span', { class: 'sub mono' }, point.modelId),
        node('dl', {}, facts.map(([label, value]) => node('div', {}, node('dt', {}, label), node('dd', {}, value)))),
        node('div', { class: 'chart-record-links' }, r.source ? link(r.source, T.source, T.external) : null,
          hasBenchmarkCost(r) && (r.cost_source || r.source) ? link(r.cost_source ?? r.source, T.chartCostSource, T.external) : null));
    }));
    positionDetails(mark);
    updateLabels(mark);
  }

  function draw(keepSelection = false) {
    syncFilters();
    const inGroup = state.group ? effortPoints().filter(point => conditionKey(point.result) === state.group) : effortPoints();
    displayed = inGroup.filter(point => !state.lab || point.lab === state.lab);
    root.setAttribute('data-lab', state.lab);
    legend.classList.toggle('is-focused', Boolean(state.lab));
    showAll.setAttribute('aria-pressed', String(!state.lab));
    const term = state.query.trim().toLowerCase();
    const matches = point => `${point.name} ${point.modelId} ${point.lab}`.toLowerCase().includes(term);
    for (const [lab, { button, count }] of legendButtons) {
      button.setAttribute('aria-pressed', String(state.lab === lab));
      button.title = state.lab === lab ? T.chartShowAll : T.chartFocusLab(lab);
      const total = inGroup.filter(point => point.lab === lab).length;
      count.textContent = String(total);
      button.hidden = total === 0 && state.lab !== lab;
    }
    const reason = frontierUnavailable(displayed, definition, state.axis);
    quadrants.element.hidden = frontier.element.hidden = state.axis !== 'cost';
    frontier.input.disabled = reason !== null;
    frontier.input.checked = reason === null && state.frontier;
    frontier.element.title = reason ? T[`chartFrontier_${reason}`] : T.chartFrontierNote;
    const front = frontier.input.checked ? paretoFront(displayed, definition.higher_is_better) : [];
    const frontIds = new Set(front.map(point => point.id));
    frontierInfo.hidden = state.axis !== 'cost' || (!reason && !frontier.input.checked);
    frontierInfo.replaceChildren(node('p', {}, reason ? T[`chartFrontier_${reason}`] : T.chartFrontierSummary(new Set(front.map(point => point.modelId)).size, front.length, displayed.length)));
    comparisonBadge.hidden = reason === null || state.axis !== 'cost';
    comparisonBadge.textContent = T.chartDistribution;
    comparisonBadge.title = reason ? T[`chartFrontier_${reason}`] : '';
    const canQuadrant = state.axis === 'cost' && typeof definition.higher_is_better === 'boolean' && displayed.length > 1;
    quadrants.input.disabled = !canQuadrant;
    quadrants.input.checked = canQuadrant && state.quadrants;
    limitation.textContent = state.axis === 'score' ? T.chartBarNote : `${T.chartComparisonNote} ${reason ? T[`chartFrontier_${reason}`] : T.chartFrontierNote}${canQuadrant && state.quadrants ? ` ${T.chartMedianNote}` : ''}`;
    const costs = costAxis(state.axis === 'cost' ? displayed.map(point => point.x) : [], state.scale, (plot.clientWidth || 820) < 600 ? 4 : 10);
    scaleControl.hidden = state.axis !== 'cost';
    const signature = JSON.stringify([costs.kind, costs.fallback, state.scale]);
    if (signature !== scaleSignature) {
      scaleSignature = signature;
      scaleControl.replaceChildren(createSelect(T.chartScale, costs.fallback ? [['linear', T.chartLinear]] : [['log', T.chartLog], ['linear', T.chartLinear]], costs.kind, value => {
        state.scale = value;
        scaleSignature = JSON.stringify([value, false, value]);
        draw(true);
      }));
    }
    scaleNotice.hidden = state.axis !== 'cost' || !costs.fallback;
    scaleNotice.textContent = T.chartZeroLinear;
    thresholds.hidden = !quadrants.input.checked;
    const medianCost = median(displayed.map(point => point.x)), medianScore = median(displayed.map(point => point.y));
    const approximate = value => `≈${new Intl.NumberFormat(language, { maximumSignificantDigits: 5 }).format(value)}`;
    thresholds.textContent = quadrants.input.checked ? T.chartMedians(`${approximate(medianCost)} ${state.unit}`, `${approximate(medianScore)}${definition.unit === 'percent' ? '%' : ` ${definition.unit}`}`) : '';
    thresholds.title = `${T.chartMedians(`${medianCost} ${state.unit}`, `${medianScore} ${definition.unit}`)}. ${T.chartMedianNote}`;
    status.textContent = [T.chartCounts(displayed.length, new Set(displayed.map(point => point.modelId)).size),
      ...(state.axis === 'cost' && missingCostCount ? [T.chartMissingCosts(missingCostCount)] : []),
      ...(entries.length > available.length ? [T.chartOmitted(entries.length - available.length)] : []),
      ...(available.length > displayed.length ? [T.chartFiltered(available.length - displayed.length)] : []),
      ...(term ? [T.chartMatches(displayed.filter(matches).length)] : [])].join(' · ');
    const urls = [...new Set(displayed.flatMap(point => [point.result.source, point.result.cost_source]).filter(Boolean))].sort();
    info.replaceChildren(node('span', {}, manifest?.published_at ? `${T.published}: ${manifest.published_at}` : T.chartUpdateUnknown),
      node('details', {}, node('summary', {}, `${T.source} (${urls.length})`), node('div', { class: 'chart-sources' }, urls.map(url => link(url, url, T.external)))));
    const previousKey = keepSelection ? activeKey : undefined, wasPinned = pinned;
    const restoreFocus = keepSelection && marks.some(mark => mark.element === document.activeElement);
    marks = [];
    updateLabels = () => {};
    clearSelection();
    if (!displayed.length) {
      plot.replaceChildren(node('p', { class: 'state' }, state.axis === 'cost' && !units.length ? T.chartNoCosts : T.chartEmpty));
      return;
    }
    const width = Math.max(300, Math.round(plot.clientWidth || 820));
    if (state.axis === 'score') {
      finishPlot(drawBars(width, matches, term), previousKey, wasPinned, restoreFocus);
      return;
    }
    const narrow = width < 600, baseHeight = narrow ? 360 : Math.min(560, Math.max(420, Math.round(width * 0.36)));
    const left = narrow ? 52 : 64, right = width - (narrow ? 24 : 36), top = 44;
    const labelCount = new Set((state.lab ? displayed : front).map(point => JSON.stringify([point.x, point.y, modelLabel(point)]))).size;
    const labelColumns = Math.max(1, Math.floor((right - left) / 300));
    // Frontier names and institution-focused models are mandatory annotations.
    // Give narrow screens room rather than dropping or stacking their labels.
    const height = Math.max(baseHeight, Math.ceil(labelCount / labelColumns) * 40 + 140);
    const bottom = height - 64;
    const xDomain = state.axis === 'cost' ? costs.domain : numericDomain(displayed.map(point => point.x));
    // A single release date gets a meaningful day range, not a timestamp-sized pad.
    if (state.axis === 'release' && new Set(displayed.map(point => point.x)).size === 1) { xDomain[0] = displayed[0].x - 86400000; xDomain[1] = displayed[0].x + 86400000; }
    const yDomain = numericDomain(displayed.map(point => point.y));
    // Show the observed score range, but do not pad beyond known scoring bounds.
    if (Number.isFinite(definition.min_score) && definition.min_score <= Math.min(...displayed.map(point => point.y))) yDomain[0] = Math.max(yDomain[0], definition.min_score);
    if (Number.isFinite(definition.max_score) && definition.max_score >= Math.max(...displayed.map(point => point.y))) yDomain[1] = Math.min(yDomain[1], definition.max_score);
    if (yDomain[0] === yDomain[1]) { yDomain[0] -= 0.5; yDomain[1] += 0.5; }
    const x = value => left + (state.axis === 'cost' ? costs.position(value) : (value - xDomain[0]) / (xDomain[1] - xDomain[0])) * (right - left);
    const y = value => bottom - (value - yDomain[0]) / (yDomain[1] - yDomain[0]) * (bottom - top);
    const canvas = svg('svg', { viewBox: `0 0 ${width} ${height}`, class: 'chart-svg', 'data-scale': state.axis === 'cost' ? costs.kind : 'time', role: 'group', 'aria-label': `${T.chartTitle}: ${definition.name}. ${T.chartKeyboardHint}` }, svg('title', {}, `${definition.name} · ${definition.metric}`));
    if (quadrants.input.checked) {
      const mx = x(median(displayed.map(point => point.x))), my = y(median(displayed.map(point => point.y)));
      const high = definition.higher_is_better;
      canvas.append(svg('g', { class: 'chart-quadrants', 'aria-hidden': 'true' },
        svg('rect', { class: 'chart-quadrant-good', x: left, y: high ? top : my, width: mx - left, height: high ? my - top : bottom - my }),
        svg('rect', { class: 'chart-quadrant-bad', x: mx, y: high ? my : top, width: right - mx, height: high ? bottom - my : my - top })));
    }
    const grid = svg('g', { class: 'chart-grid', 'aria-hidden': 'true' });
    const yTicks = axisTicks(yDomain, narrow ? 4 : 5);
    for (const tick of yTicks) grid.append(svg('line', { x1: left, x2: right, y1: y(tick), y2: y(tick) }), svg('text', { x: left - 12, y: y(tick) + 4, 'text-anchor': 'end' }, formatTick(tick, yTicks, language)));
    const intervals = narrow ? 2 : 4;
    const xTicks = state.axis === 'cost' ? costs.ticks : Array.from({ length: intervals + 1 }, (_, i) => Math.round((xDomain[0] + (xDomain[1] - xDomain[0]) * i / intervals) / 86400000) * 86400000);
    for (const tick of [...new Set(xTicks)].filter(tick => tick >= xDomain[0] && tick <= xDomain[1])) grid.append(svg('line', { class: 'chart-axis-tick', x1: x(tick), x2: x(tick), y1: bottom, y2: bottom + 6 }), svg('text', { x: x(tick), y: bottom + 26, 'text-anchor': 'middle' }, state.axis === 'cost' ? formatCostTick(tick, xTicks, state.unit, language) : dateFormat.format(tick)));
    canvas.append(grid, svg('text', { class: 'chart-axis-label', x: left, y: 18 }, `${definition.metric} (${definition.unit})`),
      svg('text', { class: 'chart-axis-label', x: (left + right) / 2, y: height - 12, 'text-anchor': 'middle' }, state.axis === 'cost' ? `${T.chartCost} (${state.unit}) · ${costs.kind === 'log' ? T.chartLog : T.chartLinear}` : T.release));
    const uniqueFront = front.filter((point, i) => !i || point.x !== front[i - 1].x || point.y !== front[i - 1].y);
    // A single non-dominated position still has its halo and all model names;
    // never invent a segment to a dominated point or an unobserved endpoint.
    if (uniqueFront.length > 1) canvas.append(svg('path', { class: 'chart-frontier', 'aria-label': T.chartFrontierNote, d: uniqueFront.map((point, i) => `${i ? 'L' : 'M'}${x(point.x)},${y(point.y)}`).join(' ') }, svg('title', {}, T.chartFrontierNote)));

    const positions = new Map();
    for (const point of displayed) {
      const key = JSON.stringify([point.x, point.y]);
      if (!positions.has(key)) positions.set(key, []);
      positions.get(key).push(point);
    }
    for (const [key, points] of positions) {
      const first = points.find(point => term && matches(point)) || points[0], isMatch = Boolean(term && points.some(matches));
      const label = `${modelLabel(first)}${points.length > 1 ? ` +${points.length - 1}` : ''}`;
      const isFront = points.some(point => frontIds.has(point.id));
      const element = svg('g', { class: `chart-dot${isFront ? ' is-frontier' : ''}${isMatch ? ' is-match' : term ? ' is-dimmed' : ''}`, transform: `translate(${x(first.x)} ${y(first.y)})`, tabindex: marks.length ? '-1' : '0', role: 'button', 'aria-pressed': 'false', 'aria-expanded': 'false', 'aria-controls': detailId, 'aria-label': `${points.map(point => `${point.name}, ${T.score}: ${point.y}, ${state.axis === 'cost' ? `${T.chartCost}: ${point.x} ${state.unit}` : `${T.release}: ${point.release}`}, ${T.effort}: ${valueText(point.result.effort)}`).join('; ')}. ${T.chartPointHint}` });
      element.append(svg('circle', { r: 14, class: 'chart-hit' }));
      if (isFront) element.append(svg('circle', { r: 10, class: 'chart-frontier-halo' }));
      const labs = [...new Set(points.map(point => point.lab))];
      const radius = narrow ? 5.5 : 6.5;
      element.append(svg('circle', { r: radius, fill: pointColor(labs[0]), class: 'chart-marker' }));
      if (labs.length > 1) labs.forEach((lab, i) => {
        const start = i * Math.PI * 2 / labs.length, end = (i + 1) * Math.PI * 2 / labs.length;
        element.append(svg('path', { fill: pointColor(lab), d: `M0,0 L${radius * Math.cos(start)},${radius * Math.sin(start)} A${radius},${radius} 0 0,1 ${radius * Math.cos(end)},${radius * Math.sin(end)} Z`, 'aria-hidden': 'true' }));
      });
      if (points.length > 1) element.append(svg('text', { class: 'chart-overlap-count', x: 9, y: 12, 'aria-hidden': 'true' }, String(points.length)));
      const mark = { key, points, element, cx: x(first.x), cy: y(first.y), width, height, label, labels: pointLabels(points), frontLabels: pointLabels(points.filter(point => frontIds.has(point.id))), color: pointColor(first.lab), isFront, isMatch };
      registerMark(mark);
      canvas.append(element);
    }
    const annotations = svg('g', { class: 'chart-annotations', 'aria-hidden': 'true' });
    canvas.append(annotations);
    updateLabels = active => {
      const rank = mark => mark === active ? 0 : mark.isFront ? 1 : 2;
      let optionalCount = 0;
      const candidates = marks.filter(mark => state.lab || mark === active || mark.isFront || mark.isMatch).sort((a, b) => rank(a) - rank(b) || a.cx - b.cx)
        .filter(mark => state.lab || mark === active || mark.isFront || optionalCount++ < (narrow ? 8 : 20));
      const obstacles = marks.map(mark => ({ x: mark.cx - 9, y: mark.cy - 9, width: 18, height: 18 }));
      const labels = placeLabels(candidates.flatMap(mark => (state.lab || mark === active ? mark.labels : mark.isFront ? mark.frontLabels : [{ text: mark.label, color: mark.color }]).map(({ text, color }) => ({ mark, color, x: mark.cx, y: mark.cy, text, fullText: text, required: Boolean(state.lab) || mark.isFront || mark === active }))), { left: left + 4, right: right - 4, top: 24, bottom: bottom - 4 }, obstacles);
      annotations.replaceChildren(...labels.flatMap(({ mark, color, text, fullText, box }) => {
        const tx = Math.max(box.x, Math.min(box.x + box.width, mark.cx)), ty = Math.max(box.y, Math.min(box.y + box.height, mark.cy));
        const leader = Math.hypot(tx - mark.cx, ty - mark.cy) > 20 ? svg('line', { class: 'chart-label-leader', x1: mark.cx, y1: mark.cy, x2: tx, y2: ty }) : null;
        return [leader, svg('text', { class: 'chart-point-label', x: box.x + 5, y: box.y + 13, fill: color }, text, svg('title', {}, fullText))].filter(Boolean);
      }));
    };
    updateLabels();
    finishPlot(canvas, previousKey, wasPinned, restoreFocus);
  }
  refresh();
  // Match SVG coordinates to CSS pixels so axis text stays legible on phones.
  // Disconnect when an app/language re-render removes this card.
  if (typeof ResizeObserver !== 'undefined') {
    let measuredWidth = 0;
    const observer = new ResizeObserver(([entry]) => {
      if (!root.isConnected) { if (measuredWidth) observer.disconnect(); return; }
      const width = Math.round(entry.contentRect.width);
      if (width > 0 && width !== measuredWidth) { measuredWidth = width; draw(true); }
    });
    observer.observe(plot);
  }
  return root;
}
