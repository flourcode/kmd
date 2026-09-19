/* kill.js: the five-question engine behind Kill My Rep, Partner and Territory.
   Each page passes a config: five questions, weights, a verdict function,
   attack lines and moves per pillar, a DM template and a hand-off.
   Kill My Deal keeps its own script (it has Boss Mode). See HANDOFF.md §16. */
'use strict';
(function () {
  const kmd = (n) => { if (typeof window.kmd === 'function') window.kmd(n); else (window.kmdQ = window.kmdQ || []).push(n); };
  const esc = (s) => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const el = () => document.getElementById('screen');
  const show = (html) => { const e = el(); e.classList.remove('enter'); e.innerHTML = html; void e.offsetWidth; e.classList.add('enter'); window.scrollTo({ top: 0 }); };
  const VAL = { yes: 92, sort: 50, no: 8 };
  const CODE = { yes: 'y', sort: 's', no: 'n' }, UNCODE = { y: 'yes', s: 'sort', n: 'no' };
  const WORD = { yes: 'Yes', sort: 'Sort of', no: 'No' };
  const clearHash = () => { try { history.replaceState(null, '', location.pathname); } catch {} };

  function copyText(text) {
    try {
      const ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0;font-size:16px;';
      document.body.appendChild(ta);
      if (/iP(hone|ad|od)/.test(navigator.userAgent)) {
        ta.contentEditable = 'true'; ta.readOnly = false;
        const r = document.createRange(); r.selectNodeContents(ta);
        const sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
        ta.setSelectionRange(0, text.length);
      } else { ta.select(); }
      const ok = document.execCommand('copy');
      document.body.removeChild(ta);
      if (ok) return Promise.resolve();
    } catch (e) {}
    if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(text);
    return Promise.reject(new Error('no clipboard'));
  }

  window.KillMy = function (cfg) {
    const P = cfg.questions;
    let answers = {}, lastScore = null, shared = false;
    const INTRO_HTML = el().innerHTML;

    function score(a) {
      let total = 0, wsum = 0;
      P.forEach(p => { total += VAL[a[p.k]] * cfg.weights[p.k]; wsum += cfg.weights[p.k]; });
      total = Math.round(total / wsum);
      if (cfg.capOnNo !== false && P.some(p => a[p.k] === 'no')) total = Math.min(total, 74);
      const ranked = P.slice().sort((x, y) => (VAL[a[x.k]] - VAL[a[y.k]]) || (cfg.weights[y.k] - cfg.weights[x.k]));
      const weak = ranked[0];
      const v = cfg.verdict(a, total, weak);
      const moves = ranked.filter(p => a[p.k] !== 'yes').slice(0, 3).map(p => cfg.moves[p.k]);
      // The literal count: yes is one, sort of is a half. This is the number people see.
      const proven = P.reduce((n, p) => n + (a[p.k] === 'yes' ? 1 : a[p.k] === 'sort' ? .5 : 0), 0);
      const provenText = (proven % 1 ? Math.floor(proven) + '½' : String(proven)) + ' of ' + P.length + ' ' + (cfg.countNoun || 'proven');
      const meta = (cfg.count === false ? '' : provenText + '. ') + 'Weakest: ' + weak.n.toLowerCase() + '.';
      return Object.assign({ total, weak, moves, answers: a, proven, provenText, meta }, v);
    }
    const encode = () => P.map(p => CODE[answers[p.k]]).join('');
    function readHash() {
      const h = (location.hash || '').replace(/^#/, '');
      if (!/^[ysn]{5}$/.test(h)) return false;
      answers = {}; P.forEach((p, i) => answers[p.k] = UNCODE[h[i]]); return true;
    }
    const shareLink = () => (location.origin && location.origin !== 'null' ? location.origin + location.pathname : cfg.url) + '#' + encode();
    function shareBlock(s) {
      const dots = { yes: '●', sort: '◐', no: '○' };
      return `${cfg.name} · ${s.label}\n${s.meta}\n` + P.map(p => dots[answers[p.k]]).join(' ') + '\n' + P.map(p => p.n).join(' · ')
        + `\n\n${s.attack}\n${shareLink()}`;
    }

    function home() { answers = {}; clearHash(); show(INTRO_HTML); bind(); }
    function bind() { const b = document.getElementById('prep'); if (b) b.onclick = () => { kmd(cfg.slug + '_start'); ask(0); }; }

    function ask(i) {
      const p = P[i];
      show(`
    <div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="${P.length}" aria-valuenow="${i + 1}">${P.map((_, j) => `<i class="${j <= i ? 'done' : ''}"></i>`).join('')}</div>
    <span class="overline">${p.n} · question ${i + 1} of ${P.length}</span>
    <div class="question">${esc(p.q)}</div>
    <div class="choice-group" role="group" aria-label="${esc(p.q)}">
      <button class="choice" data-v="yes" type="button">Yes</button>
      <button class="choice" data-v="sort" type="button">Sort of</button>
      <button class="choice" data-v="no" type="button">No</button>
    </div>
    ${i > 0 ? '<button class="btn btn-text" id="back" type="button">← Back</button>' : ''}`);
      el().querySelectorAll('.choice').forEach(b => b.onclick = () => {
        answers[p.k] = b.dataset.v;
        if (navigator.vibrate) navigator.vibrate(8);
        setTimeout(() => (i + 1 < P.length ? ask(i + 1) : result(false)), 120);
      });
      const back = document.getElementById('back'); if (back) back.onclick = () => ask(i - 1);
    }

    function result(isShared) {
      const s = score(answers); lastScore = s;
      kmd(cfg.slug + (isShared ? '_verdict_shared' : '_verdict'));
      const firstMove = s.moves[0] || cfg.noMove;
      show(`
    ${isShared ? `<div class="banner">Someone sent you this verdict. <button id="runMine" type="button">Run your own →</button></div>` : ''}
    <div class="verdict verdict-${s.cls}">
      <div class="verdict-word">${esc(s.label)}</div>
      <div class="verdict-meta">${esc(s.meta)}</div>
      <div class="verdict-attack">${esc(s.attack)}</div>
      ${s.sub ? `<div class="verdict-sub">${esc(s.sub)}</div>` : ''}
    </div>
    <div class="list" aria-label="Your answers">
      ${P.map(p => `<div class="list-item compact"><span class="headline">${p.n}</span><span class="trailing${answers[p.k] === 'no' ? ' v-no' : ''}">${WORD[answers[p.k]]}</span></div>`).join('')}
    </div>
    <div class="card">
      <span class="overline">${esc(cfg.askedBy)}</span>
      <p class="lede">“${esc(cfg.grill[s.weak.k])}”</p>
      <span class="overline" style="margin-top:16px;">Do this first</span>
      <p class="lede">${esc(firstMove)}</p>
    </div>
    ${cfg.handoff ? `<div class="card card-accent">
      <span class="overline">${esc(cfg.handoff.overline)}</span>
      <p class="lede">${esc(cfg.handoff.text)}</p>
      <a class="btn btn-tonal btn-full" href="${cfg.handoff.href}" style="margin-top:14px;">${esc(cfg.handoff.label)}</a>
    </div>` : ''}
    <div class="btn-row center" style="margin-top:8px;">
      <button class="btn btn-text" id="copy" type="button">Share</button>
      <button class="btn btn-text" id="again" type="button">Start over</button>
    </div>
    <div class="card" style="margin-top:24px;">
      <h3>${esc(cfg.mark.title(s))}</h3>
      <p>${esc(cfg.mark.body)}</p>
      <div class="preview mono" title="Tap to select">${esc(cfg.dm(s))}</div>
      <button class="btn btn-primary btn-lg btn-full" id="dmBtn" type="button" style="margin-top:14px;">Copy this &amp; DM me</button>
      <div class="btn-row center" style="margin-top:4px;">
        <a class="btn btn-text" href="https://calendly.com/markflournoy/chat-with-mark?utm_source=killmydeal&utm_medium=${cfg.slug}&utm_content=after_score" target="_blank" rel="noopener">Or book 20 minutes</a>
      </div>
      <p class="fine" style="text-align:center;margin:4px 0 0;">Free either way. I answer LinkedIn faster than email.</p>
    </div>`);
      const rm = document.getElementById('runMine'); if (rm) rm.onclick = () => { answers = {}; clearHash(); ask(0); };
      document.getElementById('again').onclick = () => { answers = {}; clearHash(); ask(0); };
      document.getElementById('copy').onclick = (e) => {
        const btn = e.currentTarget; kmd(cfg.slug + '_share');
        try { history.replaceState(null, '', '#' + encode()); } catch {}
        copyText(shareBlock(s)).then(() => { btn.textContent = 'Copied ✓'; }).catch(() => { btn.textContent = "Couldn't copy"; });
      };
      document.getElementById('dmBtn').onclick = (e) => {
        const btn = e.currentTarget; kmd(cfg.slug + '_dm_copy');
        copyText(cfg.dm(s)).then(() => { btn.textContent = 'Copied ✓'; window.open('https://www.linkedin.com/in/markflournoy/', '_blank', 'noopener'); })
          .catch(() => { btn.textContent = "Couldn't copy"; });
      };
      el().querySelector('.preview').onclick = (e) => { const r = document.createRange(); r.selectNodeContents(e.currentTarget); const sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r); };
    }

    /* Boot */
    document.getElementById('logoHome').onclick = home;
    bind();
    if (readHash()) result(true);
    window.addEventListener('hashchange', () => { if (readHash()) result(true); });
    window.KMD_TEST = { score, P };
  };
})();
