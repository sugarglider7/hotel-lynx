/* Hôtel Lynx — style demo switcher ("Try different styles"): palette × typography on <html>
   (data-look / data-font), kept for the tab in sessionStorage. Vanilla, no deps. */
(function () {
  'use strict';
  var d = document, html = d.documentElement;
  var panel = d.getElementById('looks'), tr = d.querySelector('.looks-tr');
  if (!panel || !tr || !('popover' in panel)) return;

  var KEY = 'lynx-look';
  var LOOKS = ['original', 'green', 'blue', 'rose'], FONTS = ['original', 'modern', 'boutique', 'soft'];
  var SPECS = { modern: ['1em Manrope'], boutique: ['1em "Cormorant Garamond"', '1em Manrope'], soft: ['1em Quicksand', '1em "DM Sans"'] };
  var noop = function () {};
  var pick = function (list, v) { return list.indexOf(v) > -1 ? v : 'original'; };

  /* ---- fonts: warm all demo faces once the visitor reaches for the switcher, never on plain page load ---- */
  var warmed = false;
  function warm() {
    if (warmed || !d.fonts) return;
    warmed = true;
    ['1em Manrope', '1em "Cormorant Garamond"', '1em Quicksand', '1em "DM Sans"'].forEach(function (s) { d.fonts.load(s).catch(noop); });
  }
  function fontsFor(f) {
    var specs = SPECS[f];
    if (!specs || !d.fonts) return null;
    return Promise.all(specs.map(function (s) { return d.fonts.load(s); })).catch(noop);
  }
  function fontsReady(f) { return !SPECS[f] || !d.fonts || SPECS[f].every(function (s) { return d.fonts.check(s); }); }

  /* ---- maps (your Agadir page): the OSM base maps are images, so each palette has its own tinted copy (tools/build.py) ---- */
  var maps = d.querySelectorAll('img[src*="/assets/img/map-"]'), decoded = {};
  var MAP_RE = /(\/map-(?:door|city-m|city))(?:-(?:green|blue|rose))?\.svg/;
  function mapSrc(img, c) { return img.getAttribute('src').replace(MAP_RE, '$1' + (c === 'original' ? '' : '-' + c) + '.svg'); }
  function idle(img, c) { var s = mapSrc(img, c); return s === img.getAttribute('src') || decoded[s] || img.loading === 'lazy' && !img.complete; }
  function mapsReady(c) { return [].every.call(maps, function (img) { return idle(img, c); }); }
  function mapsFor(c) {
    // decode the target tints before the switch so the maps change in the same frame as the colours
    return Promise.all([].map.call(maps, function (img) {
      if (idle(img, c)) return null;
      var src = mapSrc(img, c), pre = new Image(); pre.src = src;
      return (pre.decode ? pre.decode() : Promise.resolve()).then(function () { decoded[src] = true; }, noop);
    }));
  }
  function setMaps(c) { [].forEach.call(maps, function (img) { var s = mapSrc(img, c); if (s !== img.getAttribute('src')) img.setAttribute('src', s); }); }

  /* ---- state ---- */
  function radios(name) { return panel.querySelectorAll('input[name="' + name + '"]'); }
  function sync(c, f) {
    radios('look').forEach(function (r) { r.checked = r.value === c; });
    radios('font').forEach(function (r) { r.checked = r.value === f; });
  }
  function themeColor() {
    var m = d.querySelector('meta[name="theme-color"]'), ink = getComputedStyle(html).getPropertyValue('--ink').trim();
    if (m && ink) m.setAttribute('content', ink);
  }
  function commit(c, f) {
    if (c === 'original') html.removeAttribute('data-look'); else html.setAttribute('data-look', c);
    if (f === 'original') html.removeAttribute('data-font'); else html.setAttribute('data-font', f);
    setMaps(c);
    sync(c, f);
    try { sessionStorage.setItem(KEY, JSON.stringify({ c: c, f: f })); } catch (e) { /* storage off: this page only */ }
    themeColor();
  }
  // colours cross-fade for 200 ms while a choice lands (.looks-anim in looks.css). Not a View Transition: during
  // one, clicks hit <html>, which light-dismisses the panel and swallows rapid choices.
  var animT, token = 0;
  function animate() {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    html.classList.add('looks-anim');
    clearTimeout(animT);
    animT = setTimeout(function () { html.classList.remove('looks-anim'); }, 300);
  }
  function apply(c, f) {
    c = pick(LOOKS, c); f = pick(FONTS, f);
    var mine = ++token;
    var land = function () {
      if (mine !== token) return; // a later choice superseded this one while it loaded
      animate();
      commit(c, f);
    };
    // the usual case once the panel has been open a moment: everything is loaded, switch in this very frame
    if (fontsReady(f) && mapsReady(c)) return land();
    // otherwise wait (≤ 3 s) for the mode's faces and the palette's maps, so the switch lands in one frame, no fallback flash
    Promise.race([Promise.all([fontsFor(f), mapsFor(c)]), new Promise(function (r) { setTimeout(r, 3000); })]).then(land);
  }
  function checked(name) { var r = panel.querySelector('input[name="' + name + '"]:checked'); return r ? r.value : 'original'; }

  panel.addEventListener('change', function (e) {
    if (e.target.name === 'look' || e.target.name === 'font') apply(checked('look'), checked('font'));
  });
  panel.querySelector('.looks-reset').addEventListener('click', function () { apply('original', 'original'); });

  /* ---- trigger fit: only ever take the header's free space, so nothing else in the row moves ---- */
  var SLACK = 24, ICON = 44; // slack absorbs the wider demo faces (Manrope/DM Sans) in the rest of the row
  var row = tr.closest('.hd-in'), act = tr.parentNode, label = tr.querySelector('.looks-tr-l').textContent;
  function fit() {
    tr.removeAttribute('data-fit'); // label styling, out of flow and hidden: measure the row without the trigger
    var full = tr.offsetWidth, right = 0;
    for (var el = act.previousElementSibling; el; el = el.previousElementSibling) {
      if (el.getClientRects().length) right = Math.max(right, el.getBoundingClientRect().right);
    }
    var actLeft = act.getBoundingClientRect().left;
    var free = actLeft - right - (parseFloat(getComputedStyle(row).columnGap) || 0);
    var gap = parseFloat(getComputedStyle(act).columnGap) || 0;
    var mode = free >= full + gap + SLACK ? 'label' : free >= ICON + gap + SLACK ? 'icon' : 'hang';
    tr.setAttribute('data-fit', mode);
    // the hanging tab starts under the action group (from 48rem): clear of the blade sign at the photo's right edge
    if (mode === 'hang' && tr.offsetParent) tr.style.setProperty('--lx-hang', Math.round(actLeft - tr.offsetParent.getBoundingClientRect().left) + 'px');
    if (mode === 'icon') tr.title = label; else tr.removeAttribute('title');
  }
  fit();
  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(fit);
    ro.observe(row);
    [].forEach.call(row.children, function (el) { if (el !== act) ro.observe(el); });
    [].forEach.call(act.children, function (el) { if (el !== tr) ro.observe(el); });
    var ul = row.querySelector('.hd-nav ul');
    if (ul) ro.observe(ul);
  } else {
    addEventListener('resize', fit);
  }

  /* ---- panel: anchored under the trigger at the right on desktop; a bottom sheet on phones (CSS) ---- */
  var desk = matchMedia('(min-width: 40rem)');
  function place() {
    if (!desk.matches) return;
    var r = tr.getBoundingClientRect(), vw = html.clientWidth;
    var w = Math.min(parseFloat(getComputedStyle(panel).width) || 352, vw - 16);
    var left = Math.max(8, Math.min(r.right - w, vw - w - 8));
    panel.style.setProperty('--lx-top', Math.round(r.bottom + 8) + 'px');
    panel.style.setProperty('--lx-left', Math.round(left) + 'px');
  }
  panel.addEventListener('beforetoggle', function (e) {
    if (e.newState === 'open') { warm(); place(); }
  });
  panel.addEventListener('toggle', function (e) {
    tr.setAttribute('aria-expanded', String(e.newState === 'open'));
  });
  addEventListener('resize', function () { if (panel.matches(':popover-open')) place(); });
  ['pointerenter', 'focus', 'touchstart'].forEach(function (t) { tr.addEventListener(t, warm, { passive: true }); });

  /* ---- init: the boot script in <head> already set the tab's choice on <html> ---- */
  var c0 = pick(LOOKS, html.getAttribute('data-look')), f0 = pick(FONTS, html.getAttribute('data-font'));
  sync(c0, f0);
  setMaps(c0);
  if (c0 !== 'original' || f0 !== 'original') themeColor();
})();
