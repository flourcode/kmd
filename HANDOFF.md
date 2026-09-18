# KillMyDeal.com — handoff

Everything needed to maintain, extend or rebuild this. One HTML file, one page,
no build step, no server, no dependencies.

**Current build: 2026-09-18.1400**

---

## 1. What it is

A federal seller answers five questions about a deal and gets a verdict, the
question their manager is most likely to ask, and the one thing to go do before
the review. About a minute on a phone.

It is not a CRM, a forecast model, or a system of record. It is a **rehearsal**:
the sixty seconds before somebody senior says *"okay, tell me about this deal."*

**Hero:** *Before you put it in commit, try to kill it.*
**Promise:** *Five questions to separate proof from hopium before your manager does.*
**Philosophy (not on the page):** *Hope is not evidence.*

### The vocabulary

One system, four words. Everything on the site should fit inside it:

| Word | Role |
| --- | --- |
| **Kill** | the action — try to disprove your own forecast first |
| **Hopium** | the problem — what you believe but haven't proved |
| **Proof** | the cure — the artifact or the person that settles it |
| **Commit** | the moment that matters — the decision the seller and manager make, not the tool |

**The intellectual claim, and its limit.** The site does not claim a new
methodology. It claims a narrower job: *MEDDIC helps you work the deal; Kill My
Deal helps you decide whether you've earned the right to call it one.* The "Why
these five" section makes that argument — each question disproves a different
failure mode (inventing the requirement, no real money, access without
influence, no way to transact, no reason to act) and PATH is the one BANT and
MEDDIC underweight, which is the federal-specific reason this exists. Keep that
framing: a gate before those frameworks matter, never a replacement for them.

Three phrases carry it: **TRY TO KILL IT** (product), **HOPE IS NOT EVIDENCE**
(philosophy), **BRING THE PROOF** (standard). The middle one belongs in talks,
posts and the way the offer is described — it was tried as a line under the five
questions on the homepage and read as preaching. The site should demonstrate the
idea, not announce it. The four verdicts are written in
that language — *it survived, bring the proof / you believe it, you haven't
proved it / something important is still an assumption / this is a conversation,
not a deal* — as is the managers section ("get the hopium out of the pipeline
before the review") and the free call ("bring me a deal and we'll try to kill it
together").

Hopium is the recurring joke **inside** the system, never the brand itself.
Do not make "get off the hopium" the tagline: it tips into sales-guru bit, which
the voice rules below rule out. It works as occasional copy and would work as a
content series.

The dead bluebird is the **mascot, not the message**. The user never has to
understand the metaphor: the bird carries the brand in the logo and the share
card while the words carry the instruction. Copy explaining what a bluebird is
was removed from the hero and the lede. It lives in exactly one place: the FAQ
entry "What is a bluebird in sales?", which is a real search and the only spot
a curious reader can learn what the logo is.

A bluebird, in sales, is the deal nobody worked for — an inbound call, a warm
introduction, a requirement that appears out of nowhere. They feel like luck,
which is why they get forecast on feelings instead of facts. The whole brand
sits on that joke: the logo is a dead bluebird, and the tool tells you which
kind you are holding.

---

## 2. Who uses it

**The seller.** Ten minutes before a pipeline review, on a phone, often carrying
a deal they already suspect is soft. Ages run Gen X to Gen Z, so the design can
skew neither corporate-beige nor startup-toy — it has to be something nobody is
embarrassed to be caught using at work.

**The manager.** Asks the five questions out loud during a review and taps the
answers as the rep gives them. Gets a neutral instrument, so the disagreement is
with the rubric rather than with them.

**The skeptic.** A federal seller who has been pitched a lot of sales software
and assumes anything free is harvesting something. This person is why the
privacy design is absolute and why the scoring math is printed on the page.

---

## 3. The end goal

1. **Be genuinely useful in one minute.** Nothing else works if that fails. The
   measure is whether a seller walks into a review already knowing where they
   will get hit.
2. **Earn a conversation with Mark.** The result writes the DM for them — a
   sanitized one-liner naming their weakest pillar — and one tap copies it and
   opens LinkedIn. Calendly is the secondary path for people who already know
   they need help.

Not goals: accounts, retention, a SaaS product, traffic for its own sake. If a
change requires a database or a login, it is the wrong change.

**Sharing is not the growth mechanic.** A bad verdict is self-incriminating and
a good one is boring, so almost nobody pastes it in a team channel. The share
block exists, but the DM is the conversion path; do not re-prioritise them.

---

## 4. How the scoring works

Five pillars, chosen to be memorable without opening the site:
**CUSTOMER · MONEY · POWER · PATH · NOW.**

Each is answered YES / SORT OF / NO, worth **92 / 50 / 8**, weighted:

| Pillar | Weight | Question |
| --- | --- | --- |
| MONEY | 26 | Do you know where the money comes from? |
| POWER | 22 | Are you talking to someone who can make this happen? |
| CUSTOMER | 20 | Has the customer actually said they want to solve this? |
| PATH | 16 | Do you know how they will buy it? |
| NOW | 16 | Is there a real reason this happens now? |

Three caps, each printing its reason on screen:

| Condition | Cap | Reason shown |
| --- | --- | --- |
| MONEY = NO | 55 | you can't say where the money comes from |
| POWER = NO | 60 | you haven't reached anyone who can act |
| CUSTOMER = NO | 45 | the customer hasn't confirmed they intend to act |
| **any pillar = NO** | **74** | **you answered no on {pillar}** |

That last row is an invariant, not a tuning choice: **no deal with a flat NO can
be HEALTHY.** Before it existed, YES on everything but PATH scored 79 and printed
HEALTHY with "nothing obvious to attack" while the same screen showed PATH = NO.
The prose elsewhere says a missing acquisition path makes the timeline guesswork
and that the weakest link sets the forecast; the score has to agree.

Verdicts:

| Score | Verdict |
| --- | --- |
| 75+ | **HEALTHY** |
| 55–74 | **HOPIUM** |
| 35–54 | **ON LIFE SUPPORT** |
| under 35 | **DEAD ON ARRIVAL** |

The ladder is medical and the mascot is a bird; they meet at "dead," which is
the only place they need to agree. An earlier draft used GRILL IT for the second
tier, which collided with the GRILL ME button two inches below it. Do not
reintroduce that.

Everything else is a lookup keyed to the **weakest pillar**, ties broken toward
MONEY because money is what gets attacked: the attack line (`ATTACK`, with
`POWER_ATTACKS` randomising the power variant), the BE READY FOR question, the
three Boss Mode questions (`GRILL`), and the ordered actions (`FIX`) — every
pillar not answered YES, weakest first, capped at three.

**Honest limits, stated in the FAQ and worth keeping:** the weights are not
calibrated against thousands of closed deals and the tool has never seen the
pipeline. What it offers is consistency. *Use it to find the hole, not to set
the number.*

**The tool never makes the commit decision.** HEALTHY reads "no obvious fatal
hole — bring the proof and defend the deal," not "commit it." The other three
tiers may warn against committing, which is a different thing from authorising
it. The promise is: the tool pressure-tests, the seller and the manager decide
the forecast. Copy that crosses that line undermines the rigor FAQ two sections
below it.

---

## 5. There is no AI, on purpose

An earlier build sent the five answers to a language model for coaching. It
produced confident, specific, wrong advice — task orders, recompetes and bridge
contracts nobody had mentioned — because five words is not enough context to
reason from. Confident wrong advice is worse than none when the whole promise is
that every line is defensible.

That is the bar for anyone revisiting it: the model must not be able to invent
procurement context. The deterministic list cannot.

---

## 6. Privacy is a feature, not a footnote

Nothing the user enters is stored or transmitted. No localStorage, no cookies,
no analytics on answers, no server, no account. The tool never asks for the
customer, agency, contract number, partner or dollar value.

**If you add analytics, a save feature, a CRM integration or an AI call, the
copy on the page stops being true.** Update it in the same commit or don't make
the change. The claims live in three places: the line under the home-screen
button, the FAQ entry "Does anything I enter leave my device?", and the footer.

---

## 7. The ask, and how it spreads

**The DM (primary).** The result block names the weakest pillar in its heading
("Stuck on money?") and shows the message already written in a dashed preview:

> Mark — just ran a deal through Kill My Deal. Scored 47, on life support.
> Weakest pillar is money: who exactly has told you the money is available?
> I don't have a good answer yet. Worth 20 minutes?

**COPY THIS & DM ME** copies it and opens LinkedIn. A second, hotter version
appears at the end of Boss Mode when the seller fails questions — that is the
peak-discomfort moment and converts better than the calm one. See `dmText()`,
`dmGrillText()`, `copyDM()`.

**The squares (secondary).** Copy/share emit a block that reads in any channel:

```
Kill My Deal 47 · ON LIFE SUPPORT
● ○ ◐ ● ○
CUSTOMER · MONEY · POWER · PATH · NOW

Your boss is going to come after the money.
killmydeal.com/#ynsyn
```

Filled / half / empty circles rather than coloured squares: emoji colours belong
to whatever platform renders them so they never match the palette, and red vs
green is invisible to a colourblind reader. These inherit the message's own text
colour anywhere they land.

**The link.** A result is five letters — y/s/n in pillar order — in the URL hash.
`killmydeal.com/#ynsyn` restores that verdict, shows a "someone sent you this"
banner, and offers to run the reader's own. No storage, no server: the deal *is*
the five answers, so the five answers *are* the URL.

**The hash is written only when the user asks for it.** Finishing a deal does not
touch the address bar; Copy link does. Hash fragments never reach a server, but
they do land in browser history, and "nothing is saved" is easier to defend when
the tool doesn't quietly write someone's answers into a URL they never chose to
share. Incoming shared hashes still restore normally.

**The three actions are deliberately distinct:** *Copy for review* gives the
formatted block, *Copy link* gives the bare URL, the DM button copies the
message. `copyDM()` calls `window.open` synchronously inside the click — a
deferred open after an await or a timeout gets eaten by popup blockers.

**Every copy path goes through `copyText()`**, which returns the promise so
failures are caught. `writeText` is async: a synchronous `try/catch` around it
misses permission denials and the button then lies about having copied. On
failure the labels say what to do instead ("Copy failed — use the address bar",
"Press and hold the text above to copy"). Verified with clipboard access
denied.

---

## 8. Style guide

### The principle

**Bold where it judges, sober where it claims.**

The verdict, the questions and the share block can be as loud as you like. The
privacy promise, the rigor FAQ, the credentials and the consulting CTA cannot —
those have to survive a skeptic, and a toy cannot make a claim about data
handling that anyone believes. It is also why this stops short of full
neo-brutalism: the tool has to be usable in front of a manager.

### Foundation

Material 3 with the **M3 Expressive** additions (May 2025 — an expansion of M3,
not a replacement): spring motion instead of duration+easing, shape morphing on
press, emphasized typography, and grouping by containment.

**Inter (variable, latin subset), embedded as base64 inside the CSS** — not
fetched from Google Fonts. Same typeface, no third-party request, and it renders
on a network that blocks `fonts.googleapis.com`, which is the entire premise of
this tool. It adds ~63 KB, which is the right trade.

**On privacy wording:** do not write "makes no network requests at all." That was
used once and it is too absolute — the page still loads its own images, and Copy
link deliberately puts the five answers in the URL. The defensible line, used on
the page and in the FAQ: *your answers stay in your browser; no account,
analytics, CRM connection or API call; nothing is sent anywhere unless you choose
to share a result.*

To update it: `npm pack @fontsource-variable/inter`, take
`files/inter-latin-wght-normal.woff2`, base64 it into the `@font-face` block.
Icons are **inline SVG only** —
the Material Symbols font was tried and removed, because when that request fails
on a locked-down government network every icon renders as the literal word
`check_circle`.

### Colour — seeded from the bird

The logo's body is `#9DD2FF`, hue 207°. The scheme is that hue at M3 tones.

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `--primary` | `#9DD2FF` | `#9DD2FF` | filled buttons, the bird itself |
| `--on-primary` | `#0C2448` | `#0C2448` | text on those fills (9.6:1) |
| `--primary-ink` | `#045595` | `#9DD2FF` | primary **as text**: links, labels |
| `--primary-container` | `#CDE8FE` | `#045595` | BE READY FOR card, tonal surfaces |
| `--surface` | `#F7FAFF` | `#0E1216` | page |
| `--on-surface` | `#181C20` | `#E1E3E7` | body text |
| success / warn / error | `#146C2E` / `#7A5900` / `#B3261E` | lightened | YES / SORT OF / NO |

**Why the split.** `#9DD2FF` is a tone-80 value: superb as a fill, unusable as
text (1.5:1 on the surface). M3's tonal ramp exists exactly for this — the fill
keeps the bird's colour, `--primary-ink` carries anything that has to be read.
Never set text to `var(--primary)` on a light surface.

**Colour carries meaning.** Green, amber and red mean YES, SORT OF and NO; the
four verdict blocks are tonal containers. Never add decorative colour that
competes with them. Every pair passes WCAG AA in both schemes — re-measure if
you change a value.

### Emphasis

The verdict block is the loud moment: a full-bleed tonal surface keyed to the
tier, with the score at display size. The answers are a grouped, shape-morphing
set. The questions carry weight. Everything else — the five signals, the SEO
sections, the bio, the FAQ — stays quiet.

*Exact borders, shadows and radii live in the CSS and change freely. Do not treat
any pixel value in this document as a contract; the invariant is the hierarchy,
not the implementation.*

### Voice

Plain, specific, unsparing. *"You are selling to a building, not a person."*

**One verb runs through the product: commit.** The hero is the instruction
(*before you put it in commit, try to kill it*), the four verdict subtitles all
answer it — commit it, do not commit it yet, nothing goes in commit until
something is confirmed, take it out — and the managers section closes on the
habit. Keep new copy inside that frame; it is what makes the tool a behaviour
rather than a quiz.

**No stat bar.** A row of numbers — $54M committed contract, $20M pipeline built
from zero — was tried and cut. On a site whose entire premise is that an
assertion is not proof, unverifiable dollar claims undercut the argument before
they add anything, and the bio prose already carries the same credentials in a
form that doesn't ask to be taken on faith.

**Mark's section is a guide, not a résumé.** It opens on the question the whole
tool is about ("Okay, but is this deal actually real?"), lists the roles as
experience rather than credentials, ends on "This isn't a big consulting firm.
It's just me," and the first offer is *Kill one with me* with the CTA **BRING ME
A DEAL** — so the consulting reads as more of the product rather than the point
where the site turns into a brochure.

**The third offer is for teams.** The rep is the user; the manager is the buyer.
Reps rarely hold budget for a consultant, so the paid tiers point at the person
who does: *Run the review with me* is a manager buying a better pipeline review,
not a rep buying coaching. Keep the ladder shaped that way.

Never label the tone. The copy is already unsparing; writing "grumpy" into the
page turns authority into a bit.

**No faces.** An earlier mark was a round face with X eyes; a filled dark head
with high-contrast eyes and mouth reads as a minstrel caricature. The bird
replaced it. Mark's photo appears only in the bio section — a face in persistent
chrome competes with the face in the content and reads as vanity.

---

## 9. Where to change things

| Change | Where |
| --- | --- |
| Question wording or options | `const P = [...]` at the top of the script |
| Weights, caps, thresholds | `function score()` |
| Attack lines | `ATTACK`, `POWER_ATTACKS` |
| Boss Mode questions, BE READY FOR | `const GRILL` |
| DO THIS actions | `const FIX` |
| The DM copy | `dmText()`, `dmGrillText()` |
| Share block format | `shareBlock()`, `DIAL` |
| Mark's block after a result | `mountMark()` |
| SEO copy, FAQ, bio, offer | the `<section class="band">` blocks |
| Structured data | the `application/ld+json` block in `<head>` |
| Colour, type, spacing, springs | `:root` tokens at the top of `<style>` |

---

## 10. SEO and social

- One `<h1>`, rendered as **static HTML**, not by JavaScript. The script captures
  it into `INTRO_HTML` at load and restores it on return home, so crawlers and
  no-JS visitors get real content and there is never a second `<h1>`.
- Canonical URL, description, OpenGraph and Twitter tags, `card.jpg` at 1200×630
  with width, height and alt declared.
- The `<title>` carries the search terms ("Federal Sales Pipeline Review Tool |
  Kill My Deal"); the bluebird line stays the `<h1>` and the OpenGraph title,
  where it actually does its work.
- JSON-LD: `WebApplication`, `Person`, `FAQPage`. Treat it as semantic
  housekeeping rather than an SEO lever — Google no longer shows standalone FAQ
  rich results in normal search, and `HowTo` was dropped because Google retired
  it in 2023 and it was the five pillars stated a fourth time. **The JSON-LD FAQ
  text must match the on-page FAQ word for word**; it drifted once and carried a
  privacy claim the page had already retired.
- ~1,300 words across five sections: the five questions and what each disproves,
  why not BANT/MEDDIC, the pipeline review (sellers first, then managers), the
  bio, and the FAQ. Each pillar is explained **once**. An earlier build explained
  them three times — as signals, as bullets, and as failure-pattern cards — and
  the repetition read as filler. Written for sellers, not for a keyword. Thin SEO
  filler would undercut the only thing the tool is selling, which is credibility.
- The dek names the audience: *Built for federal sellers.* Everything above the
  fold was otherwise generic sales-speak, and federal is the reason PATH exists.

To regenerate `card.jpg`: run `python3 make-card.py` from a folder containing
`bluebird.png` (it extracts Inter from `index.html` itself, so the card cannot
drift from the page's typeface or palette). Change the copy in the script, not
the JPEG. The card must carry the current hero and dek; it fell out of sync once.

---

## 11. Traps that have already bitten

- **Leftover grid columns.** `.markblk` kept `grid-template-columns:64px 1fr`
  after its avatar was removed, squeezing the DM preview into a 64px lane, one
  word per line. It is `display:block` now.
- **Class-name collisions.** `.mark` was the pillar checkmark style before the
  bio block reused it and got forced to 40px wide. The bio block is `.markblk`.
- **Logo with a white background.** The first bird PNG was not transparent and
  showed as a white box on the tinted surface. The shipped `bluebird.png` has
  the field knocked out and is trimmed to the art.
- **Long button labels.** Two CTAs have overflowed on a phone. Buttons are
  `white-space:nowrap` with ellipsis; short labels are the real fix.
- **Duplicate script tags.** Assembling this page from the tool-only version
  once included the script twice and every `const` collided. There should be
  exactly two `<script>` elements: JSON-LD and the app.
- **Share text duplicating the URL.** `shareBlock()` already ends with the link.
- **Regex that eats the rest of a tag.** A `<link rel="icon">` replacement
  stopped at the first `>` inside a data URI and left `😵">` visible on the page.
- **Passing a handler the event.** `back2.onclick = result` handed the click
  event to `result(shared)`, so *Back to the verdict* showed "Someone sent you
  this verdict" on the user's own deal. Wrap it: `() => result(false)`.
- **Focus ring changing the shape.** `:focus-visible { border-radius:8px }`
  reset every pill button to 8px corners on keyboard focus. The ring is
  `outline` only now, in `--primary-ink` so it clears AA on the light surface.
- **Favicon inlined as base64.** A 256px PNG as a data URI put 69 KB in `<head>`,
  more than the font. It is `favicon.png` (64px) and `apple-touch-icon.png` now.
- **`theme-color` from a template.** It was M3's default lavender `#FEF7FF`,
  not the surface. Light and dark values are declared with media queries.

---

## 12. Deploying

Copy to the web root: `index.html`, `bluebird.png`, `favicon.png`,
`apple-touch-icon.png`, `card.jpg`, `mark.jpg`, `robots.txt`, `sitemap.xml`.
Any static host works. `make-card.py` stays in the repo, not the web root.

**`mark.jpg` needs replacing.** The current headshot has visible processing
artifacts — white blotches across the hair, beard and glasses from a bad
background cut. On a site whose premise is credibility, a clean 640×640 photo
on a plain background is worth the afternoon.

The footer and `window.KMD_BUILD` carry a build stamp. Bump it on every change;
it is how you confirm what is actually deployed, which has already saved a
debugging session.

---

## 13. Testing before you ship

1. Answer all five questions; the verdict block appears in the right colour.
2. GRILL ME asks three questions and reaches a closing verdict; failing any
   shows the DM block underneath.
3. COPY THIS & DM ME copies the written message and opens LinkedIn.
4. *Copy for review* emits the circles block, *Copy link* emits only the URL,
   and the address bar stays clean until one of them is pressed.
5. Opening that link in a fresh tab restores the verdict with the "someone sent
   you this" banner.
6. The logo returns home with answers cleared and exactly one `<h1>`.
7. DevTools → Network shows only the page's own files (`index.html`, the
   images, `favicon.png`) and nothing to any other host.
8. At 390px nothing overflows horizontally and no button clips its label.
9. Dark mode: the button is bird-blue with navy text; links stay legible.
10. No combination of answers containing a NO returns HEALTHY.
11. GRILL ME → *Back to the verdict* does **not** show the "someone sent you
    this" banner.
12. Tab through the answer buttons: they stay pills while focused.

---

## 14. Related properties

- **fedhoo.com** — Mark's federal market research tool, built on USASpending and
  SAM data. Cross-linked from the bio note and the footer.
- **Calendly** — `calendly.com/markflournoy/chat-with-mark`, free 30 minutes,
  UTM-tagged `utm_source=killmydeal`.
- **LinkedIn** — `linkedin.com/in/markflournoy`. The DM is the primary ask;
  a stressed rep sends one line long before booking a meeting.

---

## 15. Changelog

**2026-09-18.1400** — review pass.
- `card.jpg` regenerated to match the current hero and dek (it still carried
  the retired bluebird line); `make-card.py` added so it cannot drift again.
- Content: the five pillars explained once instead of three times; the review
  section and the managers section merged; FAQ entries that restated sections
  above cut; the bluebird FAQ entry added; the third consulting tier reshaped
  for teams; "Built for federal sellers" added to the dek.
- Bugs: *Back to the verdict* showing the shared-link banner; focus ring
  reshaping buttons; `theme-color` mismatch; stale privacy claim in JSON-LD;
  shared hash surviving *Kill another deal* from the Boss Mode screen.
- Housekeeping: dead CSS and JS state removed (`mode`, `nick`, `step`,
  `setHome`, `MARK`, `strongOnes`, input/ghost/avatar rules); `HowTo` schema
  dropped; favicon moved out of the head; `color-scheme` and dark
  `theme-color` declared; answer buttons are plain buttons in a `group` rather
  than radios that never get checked. Page 192 KB → 118 KB.
