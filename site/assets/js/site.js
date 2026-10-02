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

  /* ---- sticky call/ask bar: after the page head, never over a form, a CTA band or the footer ---- */
  var bar = d.querySelector('[data-sticky]');
  if (bar && 'IntersectionObserver' in window) {
    var hero = d.querySelector('.hero, .nf, .ph'), blockers = d.querySelectorAll('#ask, .ft, .band');
    var state = { hero: !!hero, block: new Set() };
    var paint = function () { bar.classList.toggle('on', !state.hero && state.block.size === 0); };
    if (hero) new IntersectionObserver(function (es) { state.hero = es[0].isIntersecting; paint(); }).observe(hero);
    var bo = new IntersectionObserver(function (es) {
      es.forEach(function (e) { e.isIntersecting ? state.block.add(e.target) : state.block.delete(e.target); });
      paint();
    });
    blockers.forEach(function (b) { bo.observe(b); });
  }

  /* ---- maps: on narrow screens the wide map starts centred on the hotel ---- */
  d.querySelectorAll('.map-scroll').forEach(function (s) {
    var pin = s.querySelector('.mp-pin');
    if (pin && s.scrollWidth > s.clientWidth) s.scrollLeft = pin.offsetLeft - s.clientWidth / 2;
  });

  /* ---- dates: shared helpers ---- */
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  var today = new Date(); today.setHours(0, 0, 0, 0);
  var iso = function (dt) { return dt.getFullYear() + '-' + pad(dt.getMonth() + 1) + '-' + pad(dt.getDate()); };
  var parse = function (v) { var p = v.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); };
  var isDate = function (v) { return /^\d{4}-\d{2}-\d{2}$/.test(v) && !isNaN(parse(v)); };
  // arrival ≥ today; departure defaults to the next day and never sits before arrival
  var pairDates = function (arr, dep) {
    arr.min = iso(today); dep.min = iso(today);
    arr.addEventListener('change', function () {
      if (!isDate(arr.value)) return;
      var a = parse(arr.value), n = new Date(a); n.setDate(a.getDate() + 1);
      dep.min = iso(n);
      if (!isDate(dep.value) || parse(dep.value) <= a) dep.value = iso(n);
    });
  };

  /* ---- homepage mini form: plain GET to the ask page; JS only helps with dates ---- */
  var mini = d.getElementById('ask-mini');
  if (mini) {
    pairDates(mini.elements.arrival, mini.elements.departure);
    mini.addEventListener('submit', function () {
      // drop empty fields so the ask page URL stays clean
      ['arrival', 'departure'].forEach(function (n) { if (!mini.elements[n].value) mini.elements[n].disabled = true; });
      setTimeout(function () { mini.elements.arrival.disabled = mini.elements.departure.disabled = false; }, 0);
    });
  }

  /* ---- availability request → composed email ---- */
  var form = d.getElementById('ask-form');
  if (!form) return;
  var T = JSON.parse(d.getElementById('ask-i18n').textContent);
  var done = d.getElementById('ask-done'), retry = d.getElementById('ask-retry');
  var copied = d.getElementById('ask-copied');
  var el = function (n) { return form.elements[n]; };
  pairDates(el('arrival'), el('departure'));

  // prefill from the URL: ?room=double, or the homepage mini form (?arrival=…&departure=…&guests=…)
  var q = new URLSearchParams(location.search);
  if (q.get('room') && T.rooms[q.get('room')]) el('room').value = q.get('room');
  if (isDate(q.get('arrival') || '') && parse(q.get('arrival')) >= today) {
    el('arrival').value = q.get('arrival');
    el('arrival').dispatchEvent(new Event('change'));
  }
  if (isDate(q.get('departure') || '') && el('arrival').value && parse(q.get('departure')) > parse(el('arrival').value)) el('departure').value = q.get('departure');
  var g = parseInt(q.get('guests'), 10);
  if (g >= 1 && g <= 12) el('guests').value = g;

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
    ok.push(setErr('arrival', !a ? E.required : !isDate(a) ? E.required : parse(a) < today ? E.past : ''));
    ok.push(setErr('departure', !dp ? E.required : !isDate(dp) ? E.required : (isDate(a) && parse(dp) <= parse(a)) ? E.order : ''));
    var gs = parseInt(v('guests'), 10);
    ok.push(setErr('guests', !v('guests') ? E.required : (isNaN(gs) || gs < 1 || gs > 12) ? E.guests : ''));
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
    var guests = String(parseInt(v('guests'), 10));
    var subject = M.subject.replace('{arrival}', fmt(a)).replace('{departure}', fmt(dp))
      .replace('{guests}', guests).replace('{room}', room);
    var L = [M.hello, '', M.ask_line, '',
      M.arrival + ': ' + fmt(a, true),
      M.departure + ': ' + fmt(dp, true) + ' (' + nights + ' ' + M.nights + ')',
      M.guests + ': ' + guests,
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
    d.getElementById('done-subject').textContent = last.subject;
    d.getElementById('done-body').textContent = last.body;
    copied.textContent = '';
    form.hidden = true;
    done.hidden = false;
    done.focus();
    done.scrollIntoView({ block: 'start', behavior: reduce ? 'auto' : 'smooth' });
    window.location.href = last.href;
  });
  d.getElementById('ask-edit').addEventListener('click', function () {
    done.hidden = true;
    form.hidden = false;
    el('arrival').focus();
  });

  // copy: clipboard API on https, textarea + execCommand elsewhere; otherwise the text stays on screen to select
  var copy = function (txt, okMsg) {
    var show = function (m) { copied.textContent = m; };
    var fallback = function () {
      var ta = d.createElement('textarea'); ta.value = txt; ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.top = '0'; ta.style.opacity = '0'; d.body.appendChild(ta);
      ta.select(); ta.setSelectionRange(0, txt.length);
      var ok = false;
      try { ok = d.execCommand('copy'); } catch (x) { ok = false; }
      ta.remove();
      show(ok ? okMsg : T.copy_fail);
    };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(txt).then(function () { show(okMsg); }, fallback);
    else fallback();
  };
  done.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy]');
    if (!b || !last) return;
    if (b.getAttribute('data-copy') === 'email') copy(T.email, T.copied_email);
    else copy(last.subject + '\n\n' + last.body, T.copied);
  });
})();
