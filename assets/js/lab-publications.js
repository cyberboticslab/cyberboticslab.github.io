// All papers remain readable without JavaScript; controls enhance the archive.
document.querySelectorAll('[data-publication-browser]').forEach((browser) => {
  const controls = browser.querySelector('[data-publication-controls]');
  const search = controls.querySelector('[data-publication-search]');
  const year = controls.querySelector('[data-publication-year]');
  const type = controls.querySelector('[data-publication-type]');
  const reset = controls.querySelector('[data-publication-reset]');
  const count = browser.querySelector('[data-publication-count]');
  const empty = browser.querySelector('[data-publication-empty]');
  const groups = Array.from(browser.querySelectorAll('[data-publication-group]'));
  const normalize = (text) => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const records = Array.from(browser.querySelectorAll('[data-publication]')).map((element) => ({
    element,
    year: element.dataset.year,
    types: element.dataset.types.split(/\s+/),
    text: normalize(element.dataset.search),
  }));
  // Keep saved links from the theme's earlier type filter working.
  const legacyType = () => {
    const value = window.location.hash.slice(1);
    return /^\d+$/.test(value) && Array.from(type.options).some((option) => option.value === value)
      ? value : null;
  };

  const filter = () => {
    const words = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    let visible = 0;
    records.forEach((record) => {
      const matches = (year.value === 'all' || record.year === year.value)
        && (type.value === 'all' || record.types.includes(type.value))
        && words.every((word) => record.text.includes(word));
      record.element.hidden = !matches;
      if (matches) visible += 1;
    });
    groups.forEach((group) => {
      group.hidden = !group.querySelector('[data-publication]:not([hidden])');
    });
    count.textContent = `Showing ${visible} of ${records.length} papers · newest first`;
    empty.hidden = visible !== 0;
    reset.disabled = !search.value && year.value === 'all' && type.value === 'all';
  };

  search.addEventListener('input', filter);
  year.addEventListener('change', filter);
  type.addEventListener('change', filter);
  reset.addEventListener('click', () => {
    search.value = '';
    year.value = 'all';
    type.value = 'all';
    if (legacyType()) {
      window.history.replaceState(null, '', `${window.location.pathname}${window.location.search}`);
    }
    filter();
    search.focus();
  });
  const savedType = legacyType();
  if (savedType) type.value = savedType;
  filter();
  controls.hidden = false;
});
