/* Hôtel Lynx — menu, sticky action bar, reveal, availability email composer. Vanilla, no deps. */
(function () {
  'use strict';
  var d = document, html = d.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- mobile menu ---- */
  var btn = d.querySelector('.hd-menu'), menu = d.getElementById('menu');
  if (btn && menu) {
    var setOpen = function (open, focusBack) {
      btn.setAttribute('aria-expanded', String(open));
      menu.hidden = !open;
      html.classList.toggle('menu-open', open);
      if (open) { var f = menu.querySelector('a'); if (f) f.focus(); }
      else if (focusBack) btn.focus();
    };
    btn.addEventListener('click', function () { setOpen(btn.getAttribute('aria-expanded') !== 'true'); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') setOpen(false, true);
    });
    matchMedia('(min-width: 64rem)').addEventListener('change', function (m) { if (m.matches) setOpen(false); });
  }

  /* ---- reveal on scroll ---- */
  var rv = d.querySelectorAll('.rv, .line');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---- sticky call/ask bar: after the hero, never over the form or footer ---- */
  var bar = d.querySelector('[data-sticky]');
  if (bar && 'IntersectionObserver' in window) {
    var hero = d.querySelector('.hero, .nf'), blockers = d.querySelectorAll('#ask, .ft');
    var state = { hero: true, block: new Set() };
    var paint = function () { bar.classList.toggle('on', !state.hero && state.block.size === 0); };
    if (hero) new IntersectionObserver(function (es) { state.hero = es[0].isIntersecting; paint(); }).observe(hero);
    var bo = new IntersectionObserver(function (es) {
      es.forEach(function (e) { e.isIntersecting ? state.block.add(e.target) : state.block.delete(e.target); });
      paint();
    });
    blockers.forEach(function (b) { bo.observe(b); });
  }

  /* ---- availability request → composed email ---- */
  var form = d.getElementById('ask-form');
  if (!form) return;
  var T = JSON.parse(d.getElementById('ask-i18n').textContent);
  var done = d.getElementById('ask-done'), retry = d.getElementById('ask-retry');
  var copyBtn = d.getElementById('ask-copy'), copied = d.getElementById('ask-copied');
  var el = function (n) { return form.elements[n]; };
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  var today = new Date(); today.setHours(0, 0, 0, 0);
  var iso = function (dt) { return dt.getFullYear() + '-' + pad(dt.getMonth() + 1) + '-' + pad(dt.getDate()); };
  var parse = function (v) { var p = v.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); };
  el('arrival').min = iso(today);
  el('departure').min = iso(today);
  el('arrival').addEventListener('change', function () {
    if (!el('arrival').value) return;
    var a = parse(el('arrival').value), n = new Date(a); n.setDate(a.getDate() + 1);
    el('departure').min = iso(n);
    if (!el('departure').value || parse(el('departure').value) <= a) el('departure').value = iso(n);
  });

  // room links elsewhere on the page preselect the room
  d.addEventListener('click', function (e) {
    var a = e.target.closest('[data-room]');
    if (a && el('room')) el('room').value = a.getAttribute('data-room');
  });

  var fmt = function (v, long) {
    try {
      return parse(v).toLocaleDateString(T.lang, long ? { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' } : { day: 'numeric', month: 'short' });
    } catch (x) { return v; }
  };

  var setErr = function (name, msg) {
    var f = el(name), wrap = f.closest('.fld'), id = 'err-' + name, p = d.getElementById(id);
    if (msg) {
      if (!p) { p = d.createElement('p'); p.className = 'err'; p.id = id; wrap.appendChild(p); }
      p.textContent = msg;
      wrap.classList.add('bad');
      f.setAttribute('aria-invalid', 'true');
      f.setAttribute('aria-describedby', id);
    } else {
      if (p) p.remove();
      wrap.classList.remove('bad');
      f.removeAttribute('aria-invalid');
      f.removeAttribute('aria-describedby');
    }
    return !msg;
  };

  var validate = function () {
    var ok = [], E = T.err, v = function (n) { return el(n).value.trim(); };
    var a = v('arrival'), dp = v('departure');
    ok.push(setErr('arrival', !a ? E.required : parse(a) < today ? E.past : ''));
    ok.push(setErr('departure', !dp ? E.required : (a && parse(dp) <= parse(a)) ? E.order : ''));
    var g = parseInt(v('guests'), 10);
    ok.push(setErr('guests', !v('guests') ? E.required : (isNaN(g) || g < 1 || g > 12) ? E.guests : ''));
    ok.push(setErr('name', v('name') ? '' : E.required));
    var m = v('email');
    ok.push(setErr('email', !m ? E.required : /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(m) ? '' : E.email));
    return ok.every(Boolean);
  };

  var compose = function () {
    var M = T.mail, v = function (n) { return el(n).value.trim(); };
    var a = v('arrival'), dp = v('departure');
    var nights = Math.round((parse(dp) - parse(a)) / 864e5);
    var room = v('room') ? T.rooms[v('room')] : T.room_any;
    var subject = M.subject.replace('{arrival}', fmt(a)).replace('{departure}', fmt(dp))
      .replace('{guests}', v('guests')).replace('{room}', room);
    var L = [M.hello, '', M.ask_line, '',
      M.arrival + ': ' + fmt(a, true),
      M.departure + ': ' + fmt(dp, true) + ' (' + nights + ' ' + M.nights + ')',
      M.guests + ': ' + v('guests'),
      M.room + ': ' + room,
      M.balcony + ': ' + (el('balcony').checked ? M.yes : M.no),
      M.parking + ': ' + (el('parking').checked ? M.yes : M.no),
      M.time + ': ' + v('time'), '',
      M.name + ': ' + v('name'),
      M.email + ': ' + v('email')];
    if (v('phone')) L.push(M.phone + ': ' + v('phone'));
    if (v('message')) L.push('', M.message + ':', v('message'));
    L.push('', M.close, '', M.sign, v('name'));
    var body = L.join('\n');
    return { subject: subject, body: body,
      href: 'mailto:' + T.email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body) };
  };

  var last = null;
  form.addEventListener('input', function (e) { if (e.target.closest('.bad')) setErr(e.target.name, ''); });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!validate()) { var b = form.querySelector('[aria-invalid="true"]'); if (b) b.focus(); return; }
    last = compose();
    retry.href = last.href;
    form.hidden = true;
    done.hidden = false;
    done.focus();
    window.location.href = last.href;
  });
  copyBtn.addEventListener('click', function () {
    if (!last) return;
    var txt = last.subject + '\n\n' + last.body;
    var show = function () { copied.hidden = false; };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(txt).then(show, fallback);
    else fallback();
    function fallback() {
      var ta = d.createElement('textarea'); ta.value = txt; ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.opacity = '0'; d.body.appendChild(ta); ta.select();
      try { d.execCommand('copy'); show(); } catch (x) { /* text stays selectable in the email app fallback */ }
      ta.remove();
    }
  });
})();
