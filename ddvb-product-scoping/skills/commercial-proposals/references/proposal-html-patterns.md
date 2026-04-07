# Proposal HTML Body Patterns

Copy-paste patterns for every component used in proposal HTML bodies. The body is raw HTML rendered inside `<div class="proposal-page">` — no wrapping `<html>`, `<head>`, `<body>`, `<style>`, or `<script>` tags.

## Cover

```html
<header class="cover" id="top">
  <img class="cv-logo" src="/logo.png" alt="DDVB TECH">
  <div class="cv-kicker">Commercial Proposal</div>
  <h1>AI-автоматизация<br>для <strong>Client Name</strong></h1>
  <p class="cv-lead">One-sentence description of what we're proposing and why it matters to the client.</p>
  <div class="cv-meta">
    <dl class="cv-meta-item"><dt>Подготовлено для</dt><dd>Client Name</dd></dl>
    <dl class="cv-meta-item"><dt>Контакт</dt><dd>Contact Person</dd></dl>
    <dl class="cv-meta-item"><dt>Дата</dt><dd>Месяц 2026</dd></dl>
    <dl class="cv-meta-item"><dt>Формат</dt><dd>Discovery Phase</dd></dl>
  </div>
  <div class="cv-scroll"><span></span></div>
</header>
```

**Rules:**
- Always `id="top"` on the cover
- Logo always points to `/logo.png`
- Use `<br>` for line breaks in `<h1>` — the title should breathe
- Wrap the client name or key phrase in `<strong>` for gold highlight
- 3-4 meta items: always include "Подготовлено для", "Контакт", "Дата" — fourth varies

## Section Header

```html
<section id="business">
  <div class="sec-n reveal">01 &mdash; О вашем бизнесе</div>
  <div class="sec-t reveal reveal-d1">Мы понимаем ваши задачи</div>
  <p class="sec-s reveal reveal-d2">Brief context paragraph about the client's business and situation.</p>
  <!-- section content follows -->
</section>
```

**Rules:**
- Section IDs: `business`, `approach`, `deliverables`, `content`, `analytics`, `pricing`, `plan`, `why`, `stack`, `visuals` (choose what fits)
- Number format: `01 &mdash; Section Name`
- Always add `reveal` to sec-n, `reveal reveal-d1` to sec-t, `reveal reveal-d2` to sec-s
- Subtitle (sec-s) is optional — omit if the title is self-explanatory

## Stats Bar

```html
<div class="stats reveal reveal-d3">
  <div class="stat"><div class="stat-v">8</div><div class="stat-l">Интервью</div></div>
  <div class="stat"><div class="stat-v">3</div><div class="stat-l">Недели</div></div>
  <div class="stat"><div class="stat-v">4</div><div class="stat-l">Отдела</div></div>
  <div class="stat"><div class="stat-v">5</div><div class="stat-l">Deliverables</div></div>
</div>
```

**Rules:** Always exactly 4 stats. Values can be numbers or short text ("CZ", "B2C").

## Cards — Light (for pain points / business context)

```html
<div class="cards cards-2 reveal">
  <div class="card card-light"><h3>Pain Point Title</h3><p>Description of the problem in client's context.</p></div>
  <div class="card card-light"><h3>Pain Point Title</h3><p>Description of the problem in client's context.</p></div>
</div>
```

## Cards — Dark with Numbers (for solutions / deliverables)

```html
<div class="cards cards-2 reveal">
  <div class="card card-dark"><div class="card-num">01</div><h3>Solution Name</h3><p>What this solution does and why it matters.</p></div>
  <div class="card card-dark"><div class="card-num">02</div><h3>Solution Name</h3><p>What this solution does and why it matters.</p></div>
  <div class="card card-dark"><div class="card-num">03</div><h3>Solution Name</h3><p>What this solution does and why it matters.</p></div>
  <div class="card card-dark"><div class="card-num">04</div><h3>Solution Name</h3><p>What this solution does and why it matters.</p></div>
</div>
```

## Card Spanning Full Width

```html
<div class="cards cards-2 reveal">
  <div class="card card-dark" style="grid-column: span 2"><div class="card-num">05</div><h3>Full-Width Item</h3><p>Description that needs more horizontal space.</p></div>
</div>
```

## Callout — Standard

```html
<div class="callout reveal">
  <p><strong>Label:</strong> Explanatory text about an important point, caveat, or summary.</p>
</div>
```

## Callout — Verbatim Quote

```html
<div class="callout reveal">
  <p><strong>&laquo;Verbatim quote from the client, word for word.&raquo;</strong> &mdash; Person Name, Role</p>
</div>
```

## Callout — Emphasized (highlighted)

```html
<div class="callout reveal" style="background:var(--gold-20);border-left-color:var(--gold)">
  <p style="text-align:center;font-family:var(--display);font-size:28px;font-weight:300;color:var(--chalk);margin-bottom:4px">Итого: <strong style="color:var(--gold)">180 000 &#8381;</strong></p>
  <p style="text-align:center;font-size:12px;color:var(--stone)">Description of the total</p>
</div>
```

## Divider

```html
<div class="divider">
  <h2 class="reveal">Two-Line<br>Headline</h2>
  <p class="reveal reveal-d1">Subtitle with key themes separated by &middot;</p>
</div>
```

**Rules:** Use between major sections as a visual break. Title should be short and impactful. Use `<br>` for line breaks. Subtitle uses `&middot;` to separate concepts.

## Flow Diagram

```html
<div class="flow reveal" style="flex-wrap:wrap;gap:0;padding:0">
  <div style="display:flex;align-items:center;justify-content:center;gap:0;padding:28px 24px;width:100%;background:var(--surface)">
    <div class="flow-step"><div style="font-family:var(--display);font-size:32px;font-weight:300;color:var(--gold);line-height:1;margin-bottom:8px">1</div><div class="flow-label">Step One</div></div>
    <div class="flow-arr">&rarr;</div>
    <div class="flow-step"><div style="font-family:var(--display);font-size:32px;font-weight:300;color:var(--gold);line-height:1;margin-bottom:8px">2</div><div class="flow-label">Step Two</div></div>
    <div class="flow-arr">&rarr;</div>
    <div class="flow-step"><div style="font-family:var(--display);font-size:32px;font-weight:300;color:var(--gold);line-height:1;margin-bottom:8px">3</div><div class="flow-label">Step Three</div></div>
  </div>
  <div style="width:100%;padding:12px 24px;background:rgba(253,183,28,0.08);text-align:center;font-family:var(--text);font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:var(--gold)">Summary of the flow in one line</div>
</div>
```

## Table

```html
<table class="tbl reveal">
  <thead>
    <tr><th>Column A</th><th>Column B</th><th>Column C</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Row Title</strong></td>
      <td>Description text here</td>
      <td><strong>Value</strong></td>
    </tr>
    <tr>
      <td><strong>Row Title</strong><br><em>Optional subtitle in stone</em></td>
      <td>Description with more detail</td>
      <td><strong>$3,000</strong><br><em>240,600 ₽</em></td>
    </tr>
  </tbody>
</table>
```

**Rules:** Use `<strong>` for emphasis in cells. Use `<em>` for subtle subtitles (renders 10px stone). Use `<br>` to separate primary/secondary values. Use `&#8381;` for ₽.

## Pricing Cards

```html
<div class="cards cards-2 reveal">
  <div class="card card-dark" style="text-align:center">
    <div class="card-num">$7,500</div>
    <h3>Package Name</h3>
    <p>What's included.<br>Timeline: ~5 weeks.</p>
  </div>
  <div class="card card-light" style="text-align:center">
    <div class="card-num" style="color:var(--ink)">$9,500</div>
    <h3>Package Name</h3>
    <p>What's included.<br>Timeline: ~7 weeks.</p>
  </div>
</div>
```

## Timeline

```html
<div class="timeline reveal">
  <div class="tl-item"><div class="tl-step">Неделя 01</div><div class="tl-title">Phase Name</div><div class="tl-desc">What happens in this phase. One paragraph of detail.</div></div>
  <div class="tl-item"><div class="tl-step">Неделя 02</div><div class="tl-title">Phase Name</div><div class="tl-desc">What happens in this phase. One paragraph of detail.</div></div>
  <div class="tl-item"><div class="tl-step">Неделя 03</div><div class="tl-title">Phase Name</div><div class="tl-desc">What happens in this phase. One paragraph of detail.</div></div>
</div>
```

**Rules:** Use "Неделя 01" for weekly phases, "Шаг 01" for non-time-bound steps. Keep descriptions concise — 1-2 sentences.

## Checklist

```html
<ul class="checks reveal">
  <li>First capability or credential</li>
  <li>Second capability or credential</li>
  <li>Third capability or credential</li>
  <li>Fourth capability or credential</li>
</ul>
```

## Schematics / Images

```html
<div class="reveal">
  <p class="sch-t">Diagram Title</p>
  <p class="sch-d">Brief description of what the diagram shows.</p>
  <div class="sch"><img src="/proposals/path/to/image.png" alt="Alt text"></div>
</div>
```

**Rules:** Images reference paths served by Next.js (public directory). Place images in `public/proposals/`.

## Why Us Section (standard pattern)

```html
<section id="why">
  <div class="sec-n reveal">0N &mdash; Почему мы</div>
  <div class="sec-t reveal reveal-d1">DDVB TECH</div>
  <p class="sec-s reveal reveal-d2">Мы создаём AI-продукты для компаний, которым нужна автоматизация.</p>

  <div class="cards cards-2 reveal">
    <div class="card card-dark"><h3>Competency 1</h3><p>Evidence and proof.</p></div>
    <div class="card card-dark"><h3>Competency 2</h3><p>Evidence and proof.</p></div>
    <div class="card card-dark"><h3>Competency 3</h3><p>Evidence and proof.</p></div>
    <div class="card card-dark"><h3>Competency 4</h3><p>Evidence and proof.</p></div>
  </div>

  <ul class="checks reveal">
    <li>Key fact about DDVB TECH</li>
    <li>Client references or social proof</li>
    <li>Tech stack summary</li>
    <li>Relevant methodology or experience</li>
  </ul>
</section>
```

## HTML Entity Reference

| Entity | Renders | Use for |
|--------|---------|---------|
| `&mdash;` | — | Section numbers, em dashes |
| `&laquo;` | « | Opening Russian quote |
| `&raquo;` | » | Closing Russian quote |
| `&times;` | × | Multiplication (4 × 10,000) |
| `&middot;` | · | Divider subtitle separators |
| `&rarr;` | → | Flow arrows |
| `&#8381;` | ₽ | Russian ruble |
| `&nbsp;` | (space) | Non-breaking space in prices |

## Complete Section Ordering Example

```
<header class="cover" id="top"> ... </header>
<section id="business"> ... </section>
<div class="divider"> ... </div>
<section id="approach"> ... </section>
<section id="deliverables"> ... </section>
<section id="pricing"> ... </section>
<section id="plan"> ... </section>
<section id="why"> ... </section>
```

Do NOT include a CTA section — the React `ProposalCtaSection` component handles that from the TypeScript data.
