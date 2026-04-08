# How to Create a Website Proposal

Create a commercial proposal that deploys directly to `ddvb.tech/ru/proposals/{slug}`.

## When to Use

A prospective client needs a proposal. You have call transcripts, meeting notes, or a brief.

## What You Need

- Client name
- At least one of: call transcript, meeting notes, sales brief, client's website URL
- Materials placed in the `Presales/{ClientName}/` folder (or any accessible directory)

## Steps

### 1. Run the command

```
/ddvb-product-scoping:create-proposal ClientName
```

Or describe the task conversationally: *"Create a КП for Adapter based on the call transcript in Presales/Adapter/"*

### 2. Answer context questions

Claude will ask for anything missing:
- Company name and industry
- Key contacts
- Website URL (for research)
- Budget range and timeline (if known)

### 3. Review the research

Claude researches the client's website and extracts pain points from transcripts. It will show you:
- Identified pain points (with verbatim quotes)
- Mapped DDVB capabilities
- Proposed solutions

Confirm or adjust before Claude generates the proposal.

### 4. Get the output

Two files are created:

**HTML body** — `Dev/ddvb-tech-website/src/data/proposals/{slug}-body.html`
- Dark cinematic theme with `proposal.css` classes
- Sections: Cover → Business → Approach → Deliverables → Pricing → Timeline → Why Us
- No `<html>`, `<style>`, or `<script>` tags — the page component handles those

**TypeScript data** — Entry added to `Dev/ddvb-tech-website/src/data/proposals.ts`
- Structured metadata: hero, stats, painPoints, solutions, pricing, timeline, cta
- The CTA is rendered by a React component, not in the HTML body

### 5. Deploy

Run the website build to verify:

```bash
cd Dev/ddvb-tech-website && npm run build
```

The proposal is now at `ddvb.tech/ru/proposals/{slug}`.

## Tips

- **Verbatim quotes win.** The most powerful content in a proposal is the client's own words from call transcripts. Claude prioritizes these.
- **Pain → Solution mapping.** Every solution section must connect to a stated pain point. If a solution doesn't map, Claude will flag it.
- **The CTA is automatic.** Don't try to include a call-to-action in the HTML body — the `ProposalCtaSection` React component handles it from the TypeScript data.
- **Check existing proposals** (`adapter-body.html`, `resinstudiocz-body.html`) for style reference.
