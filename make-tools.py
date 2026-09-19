#!/usr/bin/env python3
"""Builds rep/index.html, partner/index.html and territory/index.html from one template.
Run from the web root after editing copy below. Kill My Deal and Kill My Pipeline are hand-written."""
import json, os, re

BUILD = '2026-09-22.0900'
TOOLS = [
    ('/', 'Kill My Deal', 'Is this deal real?'),
    ('/pipeline/', 'Kill My Pipeline', 'Do I have enough real pipeline?'),
    ('/rep/', 'Kill My Rep', 'Is it the rep, or the patch?'),
    ('/partner/', 'Kill My Partner', 'Is this partner real, or a logo?'),
    ('/territory/', 'Kill My Territory', 'Can this patch make the number?'),
]

def menu(current):
    items = ''.join(f'<a href="{h}"{" class=\"current\"" if h == current else ""}>{n}<small>{d}</small></a>' for h, n, d in TOOLS)
    return f'<details class="menu"><summary><span class="chip">Tools ▾</span></summary><div class="menu-list">{items}</div></details>'

MARK = open('index.html').read()
MARK = MARK[MARK.index('<section class="band" id="mark"'):MARK.index('<section class="band" id="faq"')]
MARK = MARK.replace('src="mark.jpg"', 'src="../mark.jpg"')

def page(t):
    faq_html = ''.join(f'''    <details class="exp"><summary>{q}</summary>
      <div class="body">{a}</div></details>
''' for q, a in t['faq'])
    faq_ld = ',\n'.join(json.dumps({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}}) for q, a in t['faq'])
    bands = ''.join(f'''<section class="band" id="{i}">
  <div class="band-inner">
    <h2>{h}</h2>
{body}
  </div>
</section>

''' for i, h, body in t['bands'])
    mark = MARK.replace('utm_medium=page', f'utm_medium={t["slug"]}')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="canonical" href="https://killmydeal.com/{t['slug']}/">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="icon" type="image/png" sizes="64x64" href="../favicon.png">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://killmydeal.com/{t['slug']}/">
<meta property="og:title" content="{t['name']}: {t['h1']}">
<meta property="og:description" content="{t['ogdesc']}">
<meta property="og:site_name" content="Kill My Deal">
<meta property="og:image" content="https://killmydeal.com/card-{t['slug']}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{t['name']}: {t['h1']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t['name']}: {t['h1']}">
<meta name="twitter:description" content="{t['ogdesc']}">
<meta name="twitter:image" content="https://killmydeal.com/card-{t['slug']}.jpg">
<meta name="twitter:image:alt" content="{t['name']}: {t['h1']}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#F9FCFF">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#101418">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebApplication",
      "name": "{t['name']}",
      "url": "https://killmydeal.com/{t['slug']}/",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Any",
      "description": "{t['desc']}",
      "image": "https://killmydeal.com/card-{t['slug']}.jpg",
      "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "USD" }},
      "isPartOf": {{ "@type": "WebSite", "name": "Kill My Deal", "url": "https://killmydeal.com/" }},
      "author": {{ "@id": "https://killmydeal.com/#mark" }}
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
{faq_ld}
      ]
    }}
  ]
}}
</script>
<link rel="stylesheet" href="../kmd.css">
<script src="../analytics.js" defer></script>
</head>
<body>

<div class="wrap">
  <header class="appbar">
    <button class="logo" id="logoHome" type="button" aria-label="{t['name']}, start over"><picture><source srcset="../bluebird-dark.png" media="(prefers-color-scheme: dark)"><img class="brandmark" src="../bluebird.png" alt="" width="38" height="32"></picture> {t['name']}</button>
    {menu('/' + t['slug'] + '/')}
  </header>
  <div id="screen">
    <h1>{t['h1']}</h1>
    <p class="dek">{t['dek']}</p>
    <button class="btn btn-primary btn-lg btn-full" id="prep" type="button">{t['cta']}</button>
    <p class="pillars">{' · '.join(q['n'].title() for q in t['questions'])}</p></div>
</div>

{bands}{mark}<section class="band" id="faq" aria-labelledby="faq-h">
  <div class="band-inner">
    <h2 id="faq-h">Questions</h2>
{faq_html}  </div>
</section>

<footer class="sitefoot">
  <p>{t['name']} is one of the <a href="/">Kill My Deal</a> tools by
    <a href="https://www.linkedin.com/in/markflournoy/" target="_blank" rel="noopener">Mark Flournoy</a>,
    who also builds <a href="https://fedhoo.com" target="_blank" rel="noopener">fedhoo</a>.</p>
  <p>Not affiliated with the U.S. government.</p>
</footer>
<script src="../kill.js"></script>
<script>
'use strict';
window.KMD_BUILD = '{BUILD}';
{t['config']}
</script>
</body>
</html>
'''

# ────────────────────────────── KILL MY REP ──────────────────────────────
REP = dict(
    slug='rep', name='Kill My Rep',
    title='Is It the Rep or the Territory? Five Questions for Sales Managers | Kill My Rep',
    desc='Five questions that separate a performance problem from a territory, comp or pipeline problem wearing a performance costume. For sales managers. One minute, no names, nothing stored.',
    ogdesc='Before you write them up, figure out what is actually wrong. Five questions, one minute, no names.',
    h1='Before you write them up, figure out what is actually wrong.',
    dek='Five questions that separate a performance problem from a territory, comp or pipeline problem wearing a performance costume. For managers. One minute. No names.',
    cta='Kill my rep',
    questions=[
        dict(k='customers', n='CUSTOMERS', q='Are they in front of customers every week, not just in internal meetings?'),
        dict(k='pipeline', n='PIPELINE', q='Are they creating new pipeline this quarter, not just working what they inherited?'),
        dict(k='territory', n='TERRITORY', q='Could a good rep make this number in this territory?'),
        dict(k='comp', n='COMP', q='Is there still something meaningful for them to earn this year?'),
        dict(k='belief', n='BELIEF', q='Do they still think the year can be won?'),
    ],
    bands=[
        ('how', 'Five questions, four different problems', '''    <p class="lede">A team can be behind plan for a lot of reasons, and the fix for one makes another worse.</p>
    <p><strong>CUSTOMERS: Are they in front of customers every week?</strong> Lots of internal meetings, marketing
      projects and partner activity is how a rep stays busy without selling. If the calendar is full and the
      customer meetings are not, that is the first thing to look at, and the easiest to fix.</p>
    <p><strong>PIPELINE: Are they creating anything new?</strong> Some sellers have a perfectly respectable year
      because the existing business is good. Separate what they inherited from what they are actually creating.
      A rep who is making the number on renewals alone has a problem you will not see until next year.</p>
    <p><strong>TERRITORY: Could a good rep make this number here?</strong> Be honest. If the answer is no, nothing
      you do to the rep matters. Fix the patch or fix the number. Writing them up fixes neither, and it costs you
      the rep.</p>
    <p><strong>COMP: Is there still something to earn?</strong> Telling somebody to stay motivated does not do much
      when the plan stopped paying in June. Look at whether there is still a meaningful check to chase this year.
      If there is not, you are managing for next year whether you admit it or not.</p>
    <p><strong>BELIEF: Do they think the year can be won?</strong> A rep who has decided the year is over stops
      doing the things that would have saved it. The activity goes first, then the pipeline, then the rep. This
      is a conversation, and it has to happen this week.</p>'''),
        ('leave', 'Sometimes the answer is leave them alone', '''    <p>If they are producing and the forecast is good, do not invent a management problem because they do not
      love one-on-ones. Figure out what visibility you actually need and leave the rest alone. The tool will tell
      you that, too. It is the one verdict managers argue with, and it is usually right.</p>
    <p>Nothing here is a substitute for the conversation. It is the five minutes before it, so you walk in knowing
      which problem you are there to talk about.</p>'''),
    ],
    faq=[
        ('Does anything I enter leave my device?', 'No. The five answers are scored in your browser. No account, no CRM connection, no API call. The site counts page views with Google Analytics and never sends your answers. Nothing else leaves the page unless you choose to share a result.'),
        ('Why does it never ask the rep\'s name?', 'Because it does not need it, and because a tool that stores judgments about named people is a different kind of tool. Run it, have the conversation, and nothing about it is written down anywhere.'),
        ('What do the verdicts mean?', "<strong>They're fine:</strong> leave them alone; decide what visibility you need. <strong>The patch:</strong> the territory cannot produce the number. <strong>The plan:</strong> comp stopped paying. <strong>Checked out:</strong> they have decided the year is over. <strong>The rep:</strong> the territory works and the plan pays; they are not doing the job. <strong>Not sure:</strong> too many sort-ofs; go find out."),
        ('Can I run it on myself?', 'Yes, and sellers should. If the territory answer is no, <a href="/territory/">Kill My Territory</a> is the tool that makes that case to your manager.'),
    ],
    config='''KillMy({
  slug: 'rep', name: 'Kill My Rep', url: 'https://killmydeal.com/rep/',
  questions: [
    { k: 'customers', n: 'CUSTOMERS', q: 'Are they in front of customers every week, not just in internal meetings?' },
    { k: 'pipeline',  n: 'PIPELINE',  q: 'Are they creating new pipeline this quarter, not just working what they inherited?' },
    { k: 'territory', n: 'TERRITORY', q: 'Could a good rep make this number in this territory?' },
    { k: 'comp',      n: 'COMP',      q: 'Is there still something meaningful for them to earn this year?' },
    { k: 'belief',    n: 'BELIEF',    q: 'Do they still think the year can be won?' },
  ],
  weights: { customers: 24, pipeline: 22, territory: 22, comp: 16, belief: 16 },
  capOnNo: false,
  // A diagnosis, not a score. Order matters: structural causes first.
  verdict(a) {
    const no = (k) => a[k] === 'no', yes = (k) => a[k] === 'yes';
    if (['customers','pipeline','territory','comp','belief'].every(yes))
      return { label: "They're fine", cls: 'ready', attack: 'Leave them alone.', sub: "Don't invent a management problem because they don't love one-on-ones. Decide what visibility you actually need." };
    if (no('territory'))
      return { label: 'The patch', cls: 'prove', attack: "It's the territory, not the person.", sub: 'Nobody makes a number in a territory that cannot produce one. Fix the patch or fix the number. Writing them up fixes neither.' };
    if (no('belief') && no('customers'))
      return { label: 'Checked out', cls: 'dont', attack: "They've decided the year is over.", sub: 'The activity stopped because the hope did. The conversation about whether there is still a reason to care has to happen this week.' };
    if (no('comp'))
      return { label: 'The plan', cls: 'proof', attack: "It's the comp plan, not the person.", sub: "Telling somebody to stay motivated when the plan stopped paying does not work. Find something they can still win this year." };
    if (no('customers') || no('pipeline'))
      return { label: 'The rep', cls: 'dont', attack: "It's a performance problem.", sub: "The territory works and the plan pays. They're not doing the job. Get specific: which customers, which weeks, what has to happen by when." };
    return { label: 'Not sure', cls: 'proof', attack: "You don't know yet.", sub: "You can't fix a problem you haven't named. Pick the weakest answer below and go find out this week." };
  },
  count: false,
  askedBy: 'Your VP will ask',
  grill: {
    customers: 'How many customer meetings did they have last week, and with whom?',
    pipeline: 'What have they created this quarter that they did not inherit?',
    territory: 'Has anyone ever made this number in that territory?',
    comp: 'What are they still getting paid for this year?',
    belief: 'Have you asked them whether they think the year is winnable?',
  },
  moves: {
    customers: 'Ask for next week\\'s customer meetings by name. Not activity, meetings.',
    pipeline: 'Split their pipeline into inherited and created. Put the created number on paper.',
    territory: 'Size the patch yourself before the next one-on-one. If it cannot produce the number, say so up the chain.',
    comp: 'Find the one thing still worth winning this year and put it in front of them.',
    belief: 'Ask them directly, this week, whether they think the year can be won. Listen to the answer.',
  },
  noMove: 'Nothing. Tell them the forecast looks good and ask what they need.',
  handoff: { overline: 'If the answer was territory', text: 'Send them Kill My Territory. It makes the case for them, without the argument.', href: '/territory/', label: 'Kill my territory' },
  mark: { title: (s) => 'Not sure it\\'s ' + s.weak.n.toLowerCase() + '?', body: "I'm Mark. I have managed the rep who wanted space, the one who thought the year was over, and the one whose territory could never have produced the number. Send me one line. No names." },
  dm: (s) => `Mark, ran a rep through Kill My Rep. Verdict: ${s.label.toLowerCase()}. Weakest answer was ${s.weak.n.toLowerCase()}. Not sure I've got the right problem. Worth 20 minutes?`,
});''',
)

# ────────────────────────────── KILL MY PARTNER ──────────────────────────────
PARTNER = dict(
    slug='partner', name='Kill My Partner',
    title='Is This Partnership Real? Five Questions for Partner Managers | Kill My Partner',
    desc='Five questions that separate a partner who sells with you from a logo on a slide. For partner managers, alliance leads and anyone who owns a co-sell number. One minute, no names, nothing stored.',
    ogdesc='Before you renew the partnership, try to kill it. Five questions, one minute, no names.',
    h1='Before you renew the partnership, try to kill it.',
    dek='Five questions that separate a partner who sells with you from a logo on a slide. For partner managers and anyone who owns a co-sell number. One minute. No names.',
    cta='Kill my partner',
    questions=[
        dict(k='sourced', n='SOURCED', q="Have they brought you an opportunity you didn't find yourself?"),
        dict(k='accounts', n='ACCOUNTS', q='Is there a named account both sides are working right now?'),
        dict(k='owner', n='OWNER', q='Does someone on their side carry a number that includes you?'),
        dict(k='plan', n='PLAN', q='Is there a co-sell plan with dates on it, not a deck?'),
        dict(k='pull', n='PULL', q='Would they call you if you stopped calling them?'),
    ],
    bands=[
        ('how', 'The five questions, and what each one disproves', '''    <p class="lede">Everybody gets along. There have been plenty of meetings, maybe a joint slide deck. The question
      is whether anyone can point to the account where the two companies are actually trying to win something together.</p>
    <p><strong>SOURCED: Have they brought you anything?</strong> A partner who has never handed you an opportunity
      you did not already have is a partner you are working for. One sourced deal is worth a year of joint webinars.</p>
    <p><strong>ACCOUNTS: Is there a named account, right now?</strong> Not a target list. A customer, a requirement,
      two sellers who know each other's names. If nobody can name one, the partnership exists on a slide.</p>
    <p><strong>OWNER: Does someone on their side get paid when you win?</strong> Partnerships run on comp plans, not
      goodwill. If nobody at the partner carries a number that includes you, your deals are a favor, and favors do
      not scale.</p>
    <p><strong>PLAN: Is there a plan with dates?</strong> A deck says what the partnership could be. A plan says three
      accounts, two dates, and who owns each one. If it does not fit on a page, it is a deck.</p>
    <p><strong>PULL: Would they call you first?</strong> Stop calling for two weeks and see what happens. A real
      partner notices. The rest of them were waiting for you to do the work.</p>'''),
        ('verdicts', 'Four kinds of partner', '''    <p><strong>Real.</strong> Deals are moving with both names on them. Feed it.</p>
    <p><strong>All talk.</strong> Lots of activity, no deals. Everybody is busy and nothing closes. Most
      partnerships live here, and most of them never leave.</p>
    <p><strong>Neighbors.</strong> You get along. That is all that is happening.</p>
    <p><strong>Logo swap.</strong> They are on your slide, you are on theirs, and that is the partnership. Stop
      spending time on it and say so.</p>'''),
    ],
    faq=[
        ('Does anything I enter leave my device?', 'No. The five answers are scored in your browser. No account, no CRM connection, no API call. The site counts page views with Google Analytics and never sends your answers. Nothing else leaves the page unless you choose to share a result.'),
        ('Does this work for the partner running it on me?', 'Yes, and that is the best use. Run it on each other, compare, and the gap between the two verdicts is the conversation you should have been having.'),
        ('What about a partner that is strategic but not producing yet?', 'Then the answer to SOURCED and ACCOUNTS is no, and the tool will say so. Strategic is what people call a partnership before it has produced anything. The question is how long you are willing to say it.'),
        ('Can I use it on a distributor or an SI?', 'Yes. The questions do not care which direction the paper flows. They care whether anyone on the other side is accountable for a deal with your name on it.'),
    ],
    config='''KillMy({
  slug: 'partner', name: 'Kill My Partner', url: 'https://killmydeal.com/partner/',
  questions: [
    { k: 'sourced',  n: 'SOURCED',  q: "Have they brought you an opportunity you didn't find yourself?" },
    { k: 'accounts', n: 'ACCOUNTS', q: 'Is there a named account both sides are working right now?' },
    { k: 'owner',    n: 'OWNER',    q: 'Does someone on their side carry a number that includes you?' },
    { k: 'plan',     n: 'PLAN',     q: 'Is there a co-sell plan with dates on it, not a deck?' },
    { k: 'pull',     n: 'PULL',     q: 'Would they call you if you stopped calling them?' },
  ],
  weights: { sourced: 24, owner: 22, accounts: 20, pull: 18, plan: 16 },
  verdict(a, total) {
    if (total >= 75) return { label: 'Real', cls: 'ready', attack: 'This one is real. Feed it.', sub: 'Protect the time you spend here from the partners below.' };
    if (total >= 55) return { label: 'All talk', cls: 'proof', attack: 'Lots of activity. No deals.', sub: 'Everybody is busy. Nothing closes. Most partnerships live here forever.' };
    if (total >= 35) return { label: 'Neighbors', cls: 'prove', attack: "You get along. That's all that's happening.", sub: 'Pick one account and one date, or stop pretending this is a partnership.' };
    return { label: 'Logo swap', cls: 'dont', attack: "They're on your slide. You're on theirs.", sub: 'That is the whole partnership. Say so, and put the time somewhere that produces.' };
  },
  askedBy: 'Your boss will ask',
  grill: {
    sourced: "What have they brought us that we didn't find ourselves?",
    accounts: "Name one account where we're both working the same deal.",
    owner: 'Who on their side gets paid when we win?',
    plan: "What's on the co-sell plan that has a date on it?",
    pull: 'When did they last call you first?',
  },
  moves: {
    sourced: 'Ask them for one opportunity this month. Their answer is the diagnosis.',
    accounts: 'Pick three accounts, get both sellers on one call, agree who does what by when.',
    owner: 'Find out whose comp plan includes you. If the answer is nobody, that is the problem.',
    plan: 'Replace the deck with one page: three accounts, two dates, one owner each.',
    pull: 'Stop calling for two weeks. See what happens.',
  },
  noMove: 'Keep doing what you are doing, and write down why it works before someone changes it.',
  handoff: { overline: 'Is there a deal inside this partnership?', text: 'Run it through Kill My Deal. A real partner deal survives the same five questions any deal does.', href: '/', label: 'Kill my deal' },
  mark: { title: (s) => 'Stuck on ' + s.weak.n.toLowerCase() + '?', body: "I'm Mark. I ran partner sales at AWS for six years and sat on the other side of the table before that. I have seen every version of the partnership that looks great in the QBR and produces nothing. Send me one line. No partner names." },
  dm: (s) => `Mark, ran a partner through Kill My Partner. ${s.label[0] + s.label.slice(1).toLowerCase()}, ${s.provenText}, weakest is ${s.weak.n.toLowerCase()}. Not sure what to do with it. Worth 20 minutes?`,
});''',
)

# ────────────────────────────── KILL MY TERRITORY ──────────────────────────────
TERRITORY = dict(
    slug='territory', name='Kill My Territory',
    title='Can This Territory Make the Number? Five Questions for Sellers | Kill My Territory',
    desc='Five questions that tell you whether the patch can make the number, or whether you are being asked to grow where nobody could. For sellers. One minute, no account names, nothing stored.',
    ogdesc='Before you sign up for the number, try to kill the territory. Five questions, one minute, no account names.',
    h1='Before you sign up for the number, try to kill the territory.',
    dek='Five questions that tell you whether the patch can make the number, or whether you are being asked to grow where nobody could. For sellers. One minute. No account names.',
    cta='Kill my territory',
    questions=[
        dict(k='spend', n='SPEND', q='Is there enough addressable spend in the territory to make the number twice over?'),
        dict(k='accounts', n='ACCOUNTS', q="Can you name ten accounts you'd expect to buy this year?"),
        dict(k='base', n='BASE', q='Is there existing business to grow, not just logos to win?'),
        dict(k='access', n='ACCESS', q='Do you have a way in: relationships, partners, contract vehicles?'),
        dict(k='history', n='HISTORY', q='Has anyone made this number in this territory before?'),
    ],
    bands=[
        ('how', 'The five questions, and what each one disproves', '''    <p class="lede">A quota is a claim about a territory. Before you accept it, check whether the territory agrees.</p>
    <p><strong>SPEND: Is the money there twice over?</strong> Agency budgets, program lines, contract ceilings.
      If the total addressable spend is not at least double the number, you are not selling, you are hoping for
      share you have no reason to expect.</p>
    <p><strong>ACCOUNTS: Can you name ten?</strong> Not a list from the CRM. Ten accounts you personally expect to
      buy this year, with a reason for each. If you cannot get to ten, your manager should hear that in January,
      not October.</p>
    <p><strong>BASE: Is there anything to grow?</strong> A territory with installed base has a floor. A territory that
      is all new logos has a ceiling and no floor. Know which one you have, and put the inherited number on paper
      so nobody counts it twice.</p>
    <p><strong>ACCESS: Can you get in the door?</strong> A relationship, a partner who owns the account, a contract
      vehicle they already buy through. One route per account. Without one, the account is a name.</p>
    <p><strong>HISTORY: Has anyone done it?</strong> Find the last person who had the patch. If nobody has ever made
      this number here, you are the experiment, and you should be paid like one.</p>'''),
        ('now', 'What to do with the verdict', '''    <p>A bad territory verdict is not an excuse. It is a document. Take it to your manager in the first month, with
      the sizing behind it, and ask for one of three things: a different patch, a different number, or a different
      plan for how the gap gets filled. Managers respect the seller who does the math in January. They have no
      patience for the one who discovers it in Q4.</p>
    <p>A good verdict is worse news. The number is there. Now it is on you.</p>'''),
    ],
    faq=[
        ('Does anything I enter leave my device?', 'No. The five answers are scored in your browser. No account, no CRM connection, no API call. The site counts page views with Google Analytics and never sends your answers. Nothing else leaves the page unless you choose to share a result.'),
        ('Is this just a way to argue about quota?', 'It is a way to argue about quota with evidence instead of feelings, which is the only version of that argument anyone has ever won.'),
        ('What if I am new and do not know the territory yet?', 'Then most answers will be sort of, and the verdict will say so. Run it again in 60 days. The gap between the two runs is what you learned.'),
        ('What about the coverage math?', 'That is the other tool. Once you know the territory can produce, <a href="/pipeline/">Kill My Pipeline</a> tells you how much pipeline it has to produce.'),
    ],
    config='''KillMy({
  slug: 'territory', name: 'Kill My Territory', url: 'https://killmydeal.com/territory/',
  questions: [
    { k: 'spend',    n: 'SPEND',    q: 'Is there enough addressable spend in the territory to make the number twice over?' },
    { k: 'accounts', n: 'ACCOUNTS', q: "Can you name ten accounts you'd expect to buy this year?" },
    { k: 'base',     n: 'BASE',     q: 'Is there existing business to grow, not just logos to win?' },
    { k: 'access',   n: 'ACCESS',   q: 'Do you have a way in: relationships, partners, contract vehicles?' },
    { k: 'history',  n: 'HISTORY',  q: 'Has anyone made this number in this territory before?' },
  ],
  weights: { spend: 24, accounts: 22, access: 20, base: 18, history: 16 },
  verdict(a, total) {
    if (total >= 75) return { label: 'Workable', cls: 'ready', attack: "The number is there. Now it's on you.", sub: 'Which is worse news than you were hoping for.' };
    if (total >= 55) return { label: 'Thin', cls: 'proof', attack: 'It can be done. Not by accident.', sub: 'The territory will not carry you. Every account needs a plan.' };
    if (total >= 35) return { label: 'A stretch', cls: 'prove', attack: "Something structural is wrong, and it isn't you.", sub: 'Take this to your manager in month one, with the sizing behind it.' };
    return { label: 'Nobody could', cls: 'dont', attack: "You're being asked to grow where nobody could.", sub: 'Say so now, with the math. Not in Q4.' };
  },
  askedBy: 'Your manager will ask',
  grill: {
    spend: 'Where is the money in this territory, specifically?',
    accounts: 'Which ten accounts?',
    base: "What's the renewal and expansion number before any new logo?",
    access: 'How are you getting in the door?',
    history: "Who's made this number here before, and how?",
  },
  moves: {
    spend: 'Size the patch: agency budgets, program lines, contract ceilings. One page.',
    accounts: "Write the ten. If you can't get to ten, tell your manager now.",
    base: 'Separate inherited from created. Put the inherited number on paper.',
    access: 'Map one route per account: a relationship, a partner, or a vehicle.',
    history: 'Find the last person who had the patch. Buy them coffee.',
  },
  noMove: 'Build the plan for the ten accounts. The territory is not the problem.',
  handoff: { overline: 'Now the coverage math', text: 'The territory can produce. Kill My Pipeline tells you how much it has to.', href: '/pipeline/', label: 'Kill my pipeline' },
  mark: { title: (s) => 'Stuck on ' + s.weak.n.toLowerCase() + '?', body: "I'm Mark. I have inherited the patch nobody could grow and handed one out by mistake. If the verdict is bad, I can help you make the case. If it's good, I can help you make the plan. One line. No account names." },
  dm: (s) => `Mark, ran my territory through Kill My Territory. ${s.label[0] + s.label.slice(1).toLowerCase()}, ${s.provenText}, weakest is ${s.weak.n.toLowerCase()}. Want to make the case to my manager and not sure how. Worth 20 minutes?`,
});''',
)

for t in (REP, PARTNER, TERRITORY):
    os.makedirs(t['slug'], exist_ok=True)
    html = page(t)
    assert '—' not in html and '–' not in html, t['slug']
    open(f"{t['slug']}/index.html", 'w').write(html)
    print(t['slug'], len(html))
