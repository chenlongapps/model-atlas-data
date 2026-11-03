// SVG designs adapted from models.dev/packages/web/src/shared.ts.
// Copyright (c) 2025 models.dev, MIT license; see LICENSE.models-dev.
const icons = {
  text: '<polyline points="4,7 4,4 20,4 20,7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line>',
  image: '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>',
  audio: '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="m19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>',
  video: '<path d="m22 8-6 4 6 4V8Z"></path><rect width="14" height="12" x="2" y="6" rx="2" ry="2"></rect>',
  pdf: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14,2 14,8 20,8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10,9 9,9 8,9"></polyline>',
  decision: '<path d="m14 13-8.5 8.5a2.12 2.12 0 0 1-3-3L11 10"></path><path d="m16 16 6-6M8 8l6-6M9 7l8 8M21 11l-8-8"></path>',
  embedding: '<path d="m12 2 5 3v5l-5 3-5-3V5z"></path><path d="m7 5 5 3 5-3M12 8v5"></path><path d="m7 10 5 3v6l-5 3-5-3v-6z"></path><path d="m2 13 5 3 5-3M7 16v6"></path><path d="m17 10 5 3v6l-5 3-5-3v-6z"></path><path d="m12 13 5 3 5-3M17 16v6"></path>',
  reranking: '<path d="M8 20V4m-4 4 4-4 4 4M16 4v16m-4-4 4 4 4-4"></path>',
};

export function groupModalities(values) {
  const groups = new Map();
  for (const value of Array.isArray(values) ? values : []) {
    if (typeof value !== 'string' || !value) continue;
    const type = value === 'application/pdf' ? 'pdf' : /^(text|image|audio|video)\//.exec(value)?.[1] || value;
    if (!groups.has(type)) groups.set(type, []);
    if (!groups.get(type).includes(value)) groups.get(type).push(value);
  }
  return [...groups].map(([type, formats]) => ({ type, formats }));
}

export function renderModalities(values, labels) {
  const groups = groupModalities(values);
  if (!groups.length) return '—';
  const container = document.createElement('div');
  container.className = 'modalities';
  for (const { type, formats } of groups) {
    const item = document.createElement('span');
    const label = labels[type] || type;
    const detail = formats.length === 1 && formats[0] === type ? label : `${label}: ${formats.join(', ')}`;
    item.className = icons[type] ? 'modality-icon' : 'modality-unknown';
    item.setAttribute('title', detail);
    item.setAttribute('role', 'img');
    item.setAttribute('aria-label', detail);
    if (icons[type]) {
      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      for (const [key, value] of Object.entries({ width: '16', height: '16', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'aria-hidden': 'true' })) svg.setAttribute(key, value);
      svg.innerHTML = icons[type]; // Static SVG markup only; dataset values never enter HTML.
      item.append(svg);
    } else item.textContent = type;
    container.append(item);
  }
  return container;
}
