import { modelLab } from './data.mjs';

// Chart coordinates always use the original numbers, never table display rounding.
export function hasBenchmarkCost(result) {
  return Number.isFinite(result.cost) && result.cost >= 0 && typeof result.cost_unit === 'string' && result.cost_unit.trim() !== '';
}

export function releaseTimestamp(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return undefined;
  const timestamp = Date.parse(`${value}T00:00:00Z`);
  return Number.isFinite(timestamp) && new Date(timestamp).toISOString().slice(0, 10) === value ? timestamp : undefined;
}

export function costOptions(entries) {
  const counts = new Map();
  for (const { result } of entries) {
    if (Number.isFinite(result.score) && hasBenchmarkCost(result)) counts.set(result.cost_unit, (counts.get(result.cost_unit) || 0) + 1);
  }
  return [...counts].sort(([a, n], [b, m]) => m - n || a.localeCompare(b));
}

export function chartPoints(entries, models, axis, costUnit) {
  return entries.flatMap(({ modelId, result }, index) => {
    if (!Number.isFinite(result.score)) return [];
    const model = models[modelId] || {};
    const date = releaseTimestamp(model.release_date);
    // An explicit, exact unit is mandatory. Never silently combine cost bases.
    const x = axis === 'cost' ? (hasBenchmarkCost(result) && result.cost_unit === costUnit ? result.cost : undefined)
      : axis === 'release' ? date : undefined;
    return x === undefined ? [] : [{ id: `${modelId}:${index}`, modelId, name: model.name || modelId, lab: modelLab(modelId), release: model.release_date, result, x, y: result.score }];
  });
}

// Include every non-measurement field, including future/nested conditions. Missing
// fields remain absent and are never interpreted as a default experiment setting.
function canonical(value) {
  if (Array.isArray(value)) return value.map(canonical);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort().map(key => [key, canonical(value[key])]));
  return value;
}
export function conditionKey(result) {
  return JSON.stringify(canonical(Object.fromEntries(Object.entries(result).filter(([key]) => !['score', 'cost', 'cost_unit', 'cost_source'].includes(key)))));
}

// This is an exploratory envelope of the displayed coordinates, not a verified
// comparable ranking. chartPoints keeps cost bases separate before this step.
export function frontierUnavailable(points, definition, axis) {
  if (axis !== 'cost') return 'costOnly';
  if (typeof definition.higher_is_better !== 'boolean') return 'direction';
  if (!points.length) return 'empty';
  return null;
}

// Exact-condition groups are optional filters, not proof of comparability and
// not automatic boundaries for the exploratory frontier.
export function comparisonGroups(points) {
  const groups = new Map();
  for (const point of points) {
    const key = conditionKey(point.result);
    if (!groups.has(key)) groups.set(key, { key, points: [], result: point.result });
    groups.get(key).points.push(point);
  }
  return [...groups.values()].filter(group => group.points.length > 1)
    .sort((a, b) => b.points.length - a.points.length || a.key.localeCompare(b.key));
}

// Weak dominance with at least one strict improvement. Identical coordinates are
// all retained; equal performance at a higher cost is dominated. No averaging.
export function paretoFront(points, higherIsBetter) {
  if (typeof higherIsBetter !== 'boolean') return [];
  const sorted = points.filter(point => Number.isFinite(point.x) && point.x >= 0 && Number.isFinite(point.y))
    .sort((a, b) => a.x - b.x || (higherIsBetter ? b.y - a.y : a.y - b.y));
  const front = [];
  let best;
  for (let i = 0; i < sorted.length;) {
    let end = i + 1;
    while (end < sorted.length && sorted[end].x === sorted[i].x) end++;
    const score = sorted[i].y;
    if (best === undefined || (higherIsBetter ? score > best : score < best)) {
      for (let j = i; j < end && sorted[j].y === score; j++) front.push(sorted[j]);
      best = score;
    }
    i = end;
  }
  return front;
}

export function median(values) {
  if (!values.length) return undefined;
  const sorted = [...values].sort((a, b) => a - b), mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[mid] : sorted[mid - 1] / 2 + sorted[mid] / 2;
}

export function numericDomain(values, { zero = false, min, max } = {}) {
  let low = Math.min(...values), high = Math.max(...values);
  if (!values.length) { low = 0; high = 1; }
  const span = high - low || Math.abs(high) * 0.2 || 1;
  low = zero ? 0 : low - span * 0.08;
  high += span * 0.08;
  if (Number.isFinite(min) && min <= Math.min(...values)) low = min;
  if (Number.isFinite(max) && max >= Math.max(...values)) high = max;
  return low < high ? [low, high] : [low - 0.5, high + 0.5];
}

export function axisTicks([low, high], count = 5) {
  const raw = (high - low) / count;
  const magnitude = 10 ** Math.floor(Math.log10(raw));
  const step = [1, 2, 2.5, 5, 10].map(n => n * magnitude).find(n => n >= raw);
  const ticks = [];
  for (let i = Math.ceil(low / step); i * step <= high && ticks.length < 20; i++) ticks.push(Number((i * step).toPrecision(12)));
  return ticks;
}

export function formatTick(value, ticks, language) {
  const step = ticks.length > 1 ? Math.abs(ticks[1] - ticks[0]) : Math.abs(value) || 1;
  const digits = Math.max(0, Math.ceil(-Math.log10(step)) + 1);
  return new Intl.NumberFormat(language, digits > 20 ? { notation: 'scientific', maximumSignificantDigits: 8 } : { maximumFractionDigits: digits }).format(value);
}

// Logarithms change only the visual scale, never the stored costs. A real zero
// forces a linear axis rather than disappearing or being replaced by an epsilon.
export function costAxis(values, preferred = 'log', count = 8) {
  const fallback = preferred === 'log' && values.some(value => value === 0);
  const kind = preferred === 'log' && !fallback && values.length ? 'log' : 'linear';
  if (kind === 'linear') {
    const domain = numericDomain(values, { zero: true });
    return { kind, fallback, domain, ticks: axisTicks(domain, count), position: value => (value - domain[0]) / (domain[1] - domain[0]) };
  }
  const logs = numericDomain(values.map(Math.log10));
  const domain = [Math.max(Number.MIN_VALUE, 10 ** logs[0]), Math.min(Number.MAX_VALUE, 10 ** logs[1])];
  const low = Math.log10(domain[0]), high = Math.log10(domain[1]);
  const candidates = [];
  const factors = high - low < 1 ? [1, 2, 3, 4, 5, 6, 7, 8, 9] : [1, 2, 5];
  for (let exponent = Math.floor(low); exponent <= Math.ceil(high); exponent++) {
    for (const factor of factors) {
      const value = Number((factor * 10 ** exponent).toPrecision(12));
      if (value >= domain[0] && value <= domain[1] && Number.isFinite(value)) candidates.push(value);
    }
  }
  const ticks = candidates;
  // Narrow ranges may not contain a power-of-ten tick at all.
  if (ticks.length < 2) ticks.splice(0, ticks.length, ...axisTicks(domain, count));
  const spaced = [];
  for (const tick of ticks) if (!spaced.length || Math.log10(tick) - Math.log10(spaced.at(-1)) >= (high - low) / count * 0.7) spaced.push(tick);
  return { kind, fallback, domain, ticks: spaced, position: value => (Math.log10(value) - low) / (high - low) };
}

export function formatCostTick(value, ticks, unit, language) {
  const currency = unit.split('/')[0].trim();
  const symbols = { USD: '$', CNY: '¥', JPY: '¥', EUR: '€', GBP: '£', KRW: '₩', INR: '₹' };
  return `${Object.hasOwn(symbols, currency) ? symbols[currency] : `${currency} `}${formatTick(value, ticks, language)}`;
}

// Place annotations, not observations. Approximate text bounds include padding;
// Labels that cannot fit are omitted unless required by the frontier, inspection
// or institution focus.
export function placeLabels(labels, bounds, obstacles = []) {
  const occupied = [], placed = [];
  const charWidth = char => /[^\x00-\xff]/.test(char) ? 13 : /[ilI.,' ]/.test(char) ? 4 : /[MW@]/.test(char) ? 11 : 7.5;
  const textWidth = text => [...text].reduce((sum, char) => sum + charWidth(char), 0);
  const intersects = (a, b) => a.x < b.x + b.width + 5 && a.x + a.width + 5 > b.x && a.y < b.y + b.height + 4 && a.y + a.height + 4 > b.y;
  for (const label of labels) {
    const maxWidth = Math.min(280, bounds.right - bounds.left - 12);
    const characters = [];
    let measured = 0;
    for (const char of label.text) {
      if (measured + charWidth(char) + 12 > maxWidth) break;
      characters.push(char);
      measured += charWidth(char);
    }
    let text = characters.join('');
    if (text !== label.text) { characters.pop(); text = `${characters.join('')}…`; }
    const width = Math.min(maxWidth, textWidth(text) + 10), height = 18;
    const offsets = [[14, -28], [-width - 14, -28], [14, 16], [-width - 14, 16], [-width / 2, -52], [-width / 2, 40], [20, -76], [-width - 20, -76], [20, 64], [-width - 20, 64],
      [-width / 2, -100], [-width / 2, 90], [-width / 2, -128], [-width / 2, 118], [-width / 2, -156], [-width / 2, 146]];
    const candidates = offsets.map(([dx, dy]) => ({ x: Math.max(bounds.left, Math.min(bounds.right - width, label.x + dx)), y: Math.max(bounds.top, Math.min(bounds.bottom - height, label.y + dy)), width, height }));
    const blocked = [...occupied, ...obstacles];
    let box = candidates.find(candidate => !blocked.some(other => intersects(candidate, other)));
    if (!box && label.required) {
      let obstruction = Infinity, distance = Infinity;
      const anchor = { x: label.x - 10, y: label.y - 10, width: 20, height: 20 };
      // Prefer a distant empty slot and a leader line. If observations occupy
      // every slot, minimize marker overlap instead of stacking required names;
      // the annotation's own point and all other labels remain protected.
      for (let y = bounds.top; y + height <= bounds.bottom; y += height + 8) {
        for (let x = bounds.left; x + width <= bounds.right; x += 24) {
          const candidate = { x, y, width, height };
          if (occupied.some(other => intersects(candidate, other)) || intersects(candidate, anchor)) continue;
          const overlaps = obstacles.filter(other => intersects(candidate, other)).length;
          const d = Math.hypot(x + width / 2 - label.x, y + height / 2 - label.y);
          if (overlaps < obstruction || overlaps === obstruction && d < distance) { box = candidate; obstruction = overlaps; distance = d; }
        }
      }
      box ||= candidates[0];
    }
    if (!box) continue;
    occupied.push(box);
    placed.push({ ...label, text, box });
  }
  return placed;
}

const colors = {
  openai: '#303633', anthropic: '#cc8569', google: '#39a65c', deepseek: '#4b64ee', alibaba: '#8c72ce',
  moonshotai: '#ba8749', zhipuai: '#d25393', xai: '#7d899f', meta: '#229bc1', minimax: '#d35858',
  mistral: '#b69426', xiaomi: '#e48131', tencent: '#239c9a', nvidia: '#79a335',
};
export function labColor(lab) {
  if (Object.hasOwn(colors, lab)) return colors[lab];
  let hash = 0;
  for (const char of lab) hash = (hash * 31 + char.charCodeAt(0)) >>> 0;
  return `hsl(${hash % 360} 52% 49%)`;
}
