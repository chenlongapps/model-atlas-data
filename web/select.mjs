// A single open list at a time, including across page re-renders.
let openSelect;
let listeningDocument;
let nextId = 0;

function listenForDismissal() {
  if (listeningDocument === document) return;
  listeningDocument = document;
  document.addEventListener('pointerdown', event => {
    if (openSelect && !openSelect.root.contains(event.target)) openSelect.close();
  });
  document.addEventListener('focusin', event => {
    if (openSelect && !openSelect.root.contains(event.target)) openSelect.close();
  });
}

export function createSelect(label, options, current, change) {
  listenForDismissal();
  const id = `select-list-${++nextId}`;
  const root = document.createElement('div');
  root.className = 'custom-select';
  const trigger = document.createElement('button');
  trigger.type = 'button';
  trigger.className = 'select-trigger';
  trigger.setAttribute('role', 'combobox');
  trigger.setAttribute('aria-label', label);
  trigger.setAttribute('aria-haspopup', 'listbox');
  trigger.setAttribute('aria-expanded', 'false');
  trigger.setAttribute('aria-controls', id);
  const valueLabel = document.createElement('span');
  valueLabel.className = 'select-value';
  const arrow = document.createElement('span');
  arrow.className = 'select-arrow';
  arrow.setAttribute('aria-hidden', 'true');
  trigger.append(valueLabel, arrow);
  const list = document.createElement('div');
  list.id = id;
  list.className = 'select-options';
  list.setAttribute('role', 'listbox');
  list.setAttribute('aria-label', label);
  list.hidden = true;
  // Keep focus on the combobox until the option's click is handled. Otherwise
  // the document focusin listener can dismiss the list before selection.
  list.addEventListener('mousedown', event => event.preventDefault());
  root.append(trigger, list);

  let selected = Math.max(0, options.findIndex(([value]) => value === current));
  let active = selected;
  let searchText = '';
  let lastTyped = 0;
  const items = options.map(([value, name], index) => {
    const item = document.createElement('div');
    item.id = `${id}-option-${index}`;
    item.className = 'select-option';
    item.setAttribute('role', 'option');
    const nameNode = document.createElement('span');
    nameNode.textContent = name;
    const check = document.createElement('span');
    check.className = 'select-check';
    check.setAttribute('aria-hidden', 'true');
    check.textContent = '✓';
    item.append(nameNode, check);
    item.addEventListener('pointermove', event => {
      if (event.pointerType !== 'touch') activate(index);
    });
    item.addEventListener('click', () => choose(index));
    list.append(item);
    return item;
  });

  function sync() {
    valueLabel.textContent = options[selected][1];
    items.forEach((item, index) => {
      item.setAttribute('aria-selected', String(index === selected));
      item.classList.toggle('is-active', index === active);
    });
  }
  function activate(index) {
    active = Math.max(0, Math.min(index, items.length - 1));
    sync();
    trigger.setAttribute('aria-activedescendant', items[active].id);
    const item = items[active];
    if (item.offsetTop < list.scrollTop) list.scrollTop = item.offsetTop;
    else if (item.offsetTop + item.offsetHeight > list.scrollTop + list.clientHeight) list.scrollTop = item.offsetTop + item.offsetHeight - list.clientHeight;
  }
  function close() {
    list.hidden = true;
    searchText = '';
    trigger.setAttribute('aria-expanded', 'false');
    trigger.removeAttribute('aria-activedescendant');
    if (openSelect?.root === root) openSelect = undefined;
  }
  function open() {
    if (openSelect) openSelect.close();
    openSelect = { root, close };
    list.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    list.style.transform = '';
    const bounds = list.getBoundingClientRect();
    const shift = bounds.right > window.innerWidth - 12 ? window.innerWidth - 12 - bounds.right : bounds.left < 12 ? 12 - bounds.left : 0;
    if (shift) list.style.transform = `translateX(${shift}px)`;
    activate(selected);
  }
  function choose(index) {
    const changed = selected !== index;
    selected = index;
    sync();
    close();
    if (changed) change(options[index][0]);
    if (trigger.isConnected) trigger.focus({ preventScroll: true });
  }
  trigger.addEventListener('click', () => list.hidden ? open() : close());
  trigger.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !list.hidden) {
      event.preventDefault();
      event.stopPropagation();
      close();
    } else if (['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(event.key)) {
      event.preventDefault();
      const wasHidden = list.hidden;
      if (wasHidden) open();
      if (event.key === 'Home') activate(0);
      else if (event.key === 'End') activate(items.length - 1);
      else if (!wasHidden) activate(active + (event.key === 'ArrowDown' ? 1 : -1));
    } else if ((event.key === 'Enter' || event.key === ' ') && !list.hidden) {
      event.preventDefault();
      choose(active);
    } else if (event.key === 'Tab' && !list.hidden) close();
    else if (event.key.length === 1 && event.key !== ' ' && !event.ctrlKey && !event.metaKey && !event.altKey) {
      const now = Date.now();
      searchText = (now - lastTyped > 700 ? '' : searchText) + event.key.toLocaleLowerCase();
      lastTyped = now;
      const match = options.findIndex(([, name]) => name.toLocaleLowerCase().startsWith(searchText));
      if (match >= 0) {
        event.preventDefault();
        if (list.hidden) open();
        activate(match);
      }
    }
  });
  sync();
  return root;
}
