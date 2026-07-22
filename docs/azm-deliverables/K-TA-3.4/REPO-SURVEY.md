# Tamia4Life — Repository Survey (Technical Baseline)

**Task:** K TA 3.4 · Quality  
**Venture:** Tamia4Life (TA)  
**Kaizen category:** Operations  
**DMAIC phase:** Measure  
**Survey date:** 2026-07-22  
**Surveyed by:** Cursor Cloud Agent (branch inventory + open PR review)

---

> **Headline finding:** This repository contains **no application code**. It is a planning and deliverables repo. Every R&D brief that assumes a Next.js app, npm packages, CI pipelines, or an existing i18n library is designing for something that does not exist yet. The most useful thing Claude can do before the next brief is internalise that fact and stop inventing stack details.

---

## 1. REPOSITORY STATE

### Application code vs docs/planning repo

**Docs/planning only.** There is no runnable application, no `package.json`, no source tree, no tests, no build config, and no deployment manifests. The entire repo is markdown, self-contained HTML reference documents, SVG/PNG brand assets, and a Git bundle archive.

The only file on **`main`** today is `README.md` (13 bytes: `# Tamia4Life`).

All substantive content lives on **five open PR branches** that have not been merged to `main`:

| PR | Branch | What it adds |
|----|--------|--------------|
| [#1](https://github.com/aziz-mubasher/Tamia4Life/pull/1) | `cursor/customer-discovery-interviews-6b6c` | `discovery/` workspace (S TA 1.1) |
| [#3](https://github.com/aziz-mubasher/Tamia4Life/pull/3) | `docs/startup-phase2-assets-mrvll3df` | `docs/startup/phase-2/` Phase-2 design pack (7 HTML specs + brand assets) |
| [#4](https://github.com/aziz-mubasher/Tamia4Life/pull/4) | `cursor/s-ta-2b-community-language-strategy-c887` | Community & Language Strategy HTML |
| [#5](https://github.com/aziz-mubasher/Tamia4Life/pull/5) | `cursor/design-system-v0-1-font-stack-4391` | Design System v0.1 HTML (typography correction) |
| [#6](https://github.com/aziz-mubasher/Tamia4Life/pull/6) | `cursor/roadmap-v2-board-aligned-72ad` | Roadmap v2 HTML (board-aligned phases) |

**Implication:** Anyone cloning `main` sees an empty repo. Anyone writing a brief must specify whether deliverables target `main` post-merge or a feature branch, and must not assume prior PR content is already canonical on the default branch.

### Top-level directory structure (as of open PRs combined)

```
Tamia4Life/
├── README.md                          # main only — title stub
├── AGENTS.md                          # (this PR) standing R&D feedback rule
├── discovery/                         # PR #1 — S TA 1.1
│   ├── README.md                      # full interview guide (~280 lines)
│   ├── assumption-scorecard.md        # A1–A7 tracker (all pending, 0 interviews)
│   ├── templates/
│   │   └── interview-notes-template.md
│   └── notes/
│       └── .gitkeep                   # no completed interview notes committed
├── docs/
│   ├── azm-deliverables/              # PRs #4, #5, #6 — canonical handoff path
│   │   ├── K-TA-2.1/
│   │   │   └── Tamia4Life_Roadmap_v2_Board_Aligned.html
│   │   ├── K-TA-3.4/
│   │   │   └── REPO-SURVEY.md         # this file
│   │   ├── K-TA-7.2/
│   │   │   └── Tamia4Life_Design_System_v0-1.html
│   │   └── S-TA-2.B/
│   │       └── Tamia4Life_Community_Language_Strategy.html
│   └── startup/
│       └── phase-2/                   # PR #3 — earlier upload path
│           ├── README.md
│           ├── Tamia4Life.bundle      # Git bundle (archive of related commits)
│           ├── Tamia4Life_Design_System_v0.html
│           ├── Tamia4Life_Matching_Engine_v1_Spec.html
│           ├── Tamia4Life_Portals_Build_Plan.html
│           ├── Tamia4Life_Prototype_Phase1_Screens.html
│           ├── Tamia4Life_Prototype_v0.html
│           └── brand-guidelines/
│               ├── tamia4life-logo-and-favicon.html
│               └── tamia_assets/      # SVG logos, favicons, PNG sizes
```

There is **no** `src/`, `app/`, `components/`, `public/locales/`, `.github/workflows/`, or any language-runtime project root.

### Approximate size

| Scope | Files (excl. `.git`) | Approx. lines |
|-------|----------------------|---------------|
| `main` | 1 | 1 |
| PR #1 (`discovery/`) | 4 | ~550 |
| PR #3 (`docs/startup/phase-2/`) | 19 | ~2,650 (HTML + assets) |
| PR #4 | 1 HTML | ~324 lines |
| PR #5 | 1 HTML | ~349 lines |
| PR #6 | 1 HTML | ~325 lines |
| **Combined across all open PRs** | **~27** | **~4,200** (mostly HTML/CSS/JS embedded in single files) |

Zero TypeScript, JavaScript modules, Python, or other compiled source files exist outside inline `<script>` blocks inside HTML prototypes.

### Git history summary

| Metric | Value |
|--------|-------|
| Total commits (all branches) | 9 |
| Commits on `main` | 1 |
| Period | 2026-07-21 → 2026-07-22 (2 days) |
| Authors | Mubasher Aziz (1), Cursor Agent (7), AZM Bridge (1) |
| Repo created | 2026-07-21 |

Commit timeline:

1. `28f9eac` — Initial commit (`README.md`) — Mubasher Aziz
2. `4e7c8df` / `dcc53bc` — Discovery workspace — Cursor Agent
3. `b821a75` — Phase-2 design pack upload — AZM Bridge
4. `6ecc35a` — Community Language Strategy — Cursor Agent
5. `2eb28ec` / `93f5770` — Design System v0.1 (+ path correction) — Cursor Agent
6. `3ac177f` — Roadmap v2 — Cursor Agent

### Dead, abandoned, or half-finished areas

1. **`main` is effectively empty.** Five PRs worth of work are stranded unmerged. Until merge policy is decided, `main` is not a reliable baseline.

2. **Duplicate deliverable paths.** Design System exists in two places:
   - `docs/startup/phase-2/Tamia4Life_Design_System_v0.html` (PR #3, **superseded for typography**)
   - `docs/azm-deliverables/K-TA-7.2/Tamia4Life_Design_System_v0-1.html` (PR #5, **current typography**)
   
   Briefs must name which path is canonical. Right now typography canonical = K-TA-7.2 v0.1; colour/spacing/radius still only in v0.

3. **Prototype v0 is stale relative to language strategy.** Still shows Chinese (`Noto Sans SC`) and branches fonts on `dir="rtl"` — both explicitly corrected in v0.1 and S TA 2.B.

4. **Phase labelling is inconsistent.** Portals Build Plan, Prototype, Matching Engine, and Design System v0 all use retired **Phase 0–4** labels. Roadmap v2 (PR #6) realigns to board **Phase 1–6** but downstream artifacts are not yet re-labelled.

5. **Discovery (S TA 1.1) is scaffolded, not executed.** Scorecard shows 0 interviews, all assumptions `pending`. The workspace is ready; fieldwork has not started.

6. **`Tamia4Life.bundle`** on PR #3 is a Git bundle archive — useful as backup, not referenced by any workflow.

7. **Orphan branch** `cursor/customer-discovery-interviews-de16` (3 commits) appears superseded by PR #1 branch `6b6c`.

---

## 2. STACK

### Languages and versions

**None declared.** No runtime, no compiler, no `engines` field. Content is UTF-8 HTML and Markdown.

### Frameworks

**None.** No Next.js, React, Vue, Svelte, or static-site generator. Interactive prototypes are single-file HTML with embedded CSS and vanilla JavaScript.

### Package manager

**None.** No `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb`, or `packageManager` field.

### Notable dependencies (as referenced in HTML deliverables, not installed)

These appear only as Google Fonts CDN `<link>` tags inside HTML files:

| Category | What the design docs specify |
|----------|------------------------------|
| **Display font** | Fraunces |
| **UI font** | Inter |
| **Script coverage** | Noto Sans, Noto Kufi Arabic, Noto Sans Bengali, Noto Sans Devanagari, Noto Sans Gurmukhi, Noto Nastaliq Urdu |
| **Removed** | Noto Sans SC (Chinese — excluded per S TA 2.B) |
| **Brand/marketing font** | Figtree (brand-guidelines pack only) |
| **Monospace** | JetBrains Mono (brand asset index) |

| Category | Status in repo |
|----------|----------------|
| **i18n library** | None — prototype uses a hand-rolled JS object with 3 locales (`en`, `ar`, `it`) |
| **UI/component library** | None — HTML/CSS mockups only |
| **Styling** | Embedded CSS custom properties in each HTML file; no Tailwind, CSS Modules, or styled-components |
| **State management** | None |
| **Date/time** | None |
| **Auth** | Mentioned in Portals Build Plan as future work; not implemented |
| **Payments** | Stripe mentioned in Portals Build Plan; not implemented |
| **Video** | Not referenced |

### Backend / API / database

**None.** Matching Engine v1 Spec describes pseudocode logic only. Portals Build Plan mentions Stripe, CMS, and back-office concepts — all aspirational. No ORM, no schema files, no API routes.

---

## 3. CONVENTIONS ALREADY IN PLACE

### File and folder naming

- **New Cursor/AZM handoff deliverables:** `docs/azm-deliverables/<TASK-CODE>/` where task code uses hyphens (e.g. `K-TA-7.2`, `S-TA-2.B`).
- **Earlier Phase-2 upload:** `docs/startup/phase-2/` (predates the azm-deliverables convention).
- **Discovery research:** top-level `discovery/` (not under `docs/`).
- **HTML deliverables:** `Tamia4Life_<Topic>_<version>.html` or descriptive kebab-case for brand assets.
- **Branch naming (Cursor agents):** `cursor/<descriptive-name>-<suffix>`.

### Component structure

Not applicable — no component codebase. HTML prototypes use BEM-ish class names (`.langopt`, `.lopt`, `.mcell`) scoped per file.

### Styling and design tokens

Tokens live **inside HTML files** as CSS custom properties prefixed `--t4l-`:

| Token file location | Contents |
|---------------------|----------|
| `docs/startup/phase-2/Tamia4Life_Design_System_v0.html` | Full token set: colour, spacing, radius, elevation, typography (includes Chinese) |
| `docs/azm-deliverables/K-TA-7.2/Tamia4Life_Design_System_v0-1.html` | Typography-only update; colour/spacing unchanged from v0 |
| `docs/startup/phase-2/Tamia4Life_Prototype_v0.html` | Subset of tokens inlined (`--font-ui`, colour vars) — **not synced with v0.1** |

There is **no** standalone `tokens.css`, `tokens.json`, or Tailwind config. The v0.1 doc includes a copy-paste developer token block for future extraction.

**Canonical typography rule (v0.1):** branch on `lang`, never on `dir`. Urdu uses separate `--t4l-font-urdu`, `--t4l-lineheight-urdu` (2.4), applied via `[lang="ur"]`.

### Tests

**None.** No test framework, no test files, no coverage config.

### Linting / formatting

**None.** No ESLint, Prettier, Stylelint, EditorConfig, or `.github` CODEOWNERS.

### Conventions a new brief should respect

1. Deliverables as **self-contained UTF-8 HTML** viewable in a browser without a build step.
2. Place new handoffs under `docs/azm-deliverables/<TASK-CODE>/`.
3. Do not assume anything on `main` beyond `README.md` until PRs merge.
4. Reference **Design System v0.1** (`K-TA-7.2`) for typography; v0 for colour/spacing until a consolidated v1 exists.
5. Use **Startup board Phase 1–6** labels (Roadmap v2), not retired Phase 0–4.
6. PR descriptions for bridge tasks should end with **"## R&D FEEDBACK — for Claude"** (see `AGENTS.md`).

---

## 4. WHAT ALREADY EXISTS THAT R&D SEEMED UNAWARE OF

### Design tokens / theme / CSS variables

**Already exists** in Design System v0 (PR #3) and v0.1 (PR #5). Briefs that say "create the design system from scratch" are wrong — extend or consolidate what exists. Colour palette uses teal/amber/warm neutrals with `--t4l-teal`, `--t4l-amber`, etc.

### i18n setup, locale files, RTL handling

**Partially exists as prototype patterns, not as architecture:**

| Artifact | What it actually has |
|----------|---------------------|
| `Tamia4Life_Prototype_v0.html` | Inline JS locale object for `en`, `ar`, `it` only; toggles `dir` on `.app`; **branches fonts on `dir="rtl"`** (anti-pattern per v0.1) |
| Language grid | Shows Chinese — **contradicts** S TA 2.B and v0.1 |
| Design System v0/v0.1 | Specimens and language-selector mockups for 10-community scripts |
| Community Language Strategy | Strategic decisions on scripts, waves, EU scale — **no code** |

There are **no** JSON/YAML locale files, no `next-intl`, no `react-i18next`, no ICU message format, no RTL plugin.

### Auth, payments, scheduling, video

**Not implemented.** Mentioned only in Portals Build Plan (Stripe for B2C freemium, back-office for facilitator vetting). Zero code or config.

### `/discovery` workspace (S TA 1.1)

**State: ready for fieldwork, zero data.**

- Complete interview guide with Mom Test scripts for 3 segments + optional institutions
- Screeners, ethical guardrails, assumption scorecard template
- Interview notes template
- `discovery/notes/` empty except `.gitkeep`
- All assumptions A1–A7 = `pending`, 0 interviews completed

This is **research infrastructure**, not product code. PR #1 is open, unmerged.

### Component library / design system

**Reference HTML only.** v0 includes button, field, card, language-selector, and typography specimens as static CSS. Not extracted into reusable components. v0.1 adds corrected language-selector and Urdu Nastaliq proof. Brand assets (logos, favicons) exist under `docs/startup/phase-2/brand-guidelines/tamia_assets/`.

### Other artifacts R&D may not know are already committed (on PR branches)

| Artifact | Location | Notes |
|----------|----------|-------|
| Matching Engine v1 Spec | `docs/startup/phase-2/` | Rules-based matcher pseudocode; language as hard filter |
| Portals Build Plan | `docs/startup/phase-2/` | Three portals, Phase 0–4 labels (stale) |
| Prototype Phase 1 Screens | `docs/startup/phase-2/` | Static screen flow HTML |
| Roadmap v2 | `docs/azm-deliverables/K-TA-2.1/` | Board-aligned Phase 1–6 mapping |
| Community Language Strategy | `docs/azm-deliverables/S-TA-2.B/` | 10 communities, script decisions, launch waves |

---

## 5. CONSTRAINTS R&D MUST DESIGN AROUND

### CI/CD

**None.** No `.github/workflows/`, no GitHub Actions, no status checks. CI state: **N/A (nothing to run).**

When an app is scaffolded, CI will need to be created from zero. Do not assume existing green/red pipelines.

### Build tooling

**None.** HTML deliverables require only a browser. Google Fonts load from CDN — offline viewing breaks typography specimens.

### Hosting / deployment

**Not configured.** No Vercel, Netlify, Docker, or `fly.toml. The repo gives no signal of target host. Portals Build Plan references architecture inspired by OpenUp and Transiti — product research, not repo config.

### Fragile or easy-to-break areas

1. **Duplicate canonical paths** — editing v0 instead of v0.1 (or vice versa) silently desynchronises typography vs colour.
2. **Unmerged PRs** — briefs referencing "the repo" may mean different branch snapshots.
3. **Prototype anti-patterns** — `dir="rtl"` font branching will clip Urdu if copied into real CSS.
4. **Phase label drift** — mixing Phase 0–4 (old pack) with Phase 1–6 (Roadmap v2) will confuse sequencing.
5. **HTML-as-source-of-truth** — tokens are embedded in large HTML files; manual extraction is error-prone until an app exists.

### Requires a human

| Item | Why |
|------|-----|
| PR merge decisions | 5 open PRs; `main` is empty |
| Kaizen/Startup board sync | No board MCP in agent environment |
| Google Fonts / CDN policy | Production font loading strategy undecided |
| Stripe, auth, hosting credentials | Not in repo; cannot be scaffolded without Aziz |
| Customer discovery fieldwork | S TA 1.1 requires real interviews |
| DNS, domain, email | Not referenced in repo |

---

## 6. FEEDBACK ON THE BRIEFS SO FAR (PRs #4, #5, #6)

Reviewed against actual repo state on 2026-07-22.

### PR #4 — Community & Language Strategy (S TA 2.B)

| Dimension | Assessment |
|-----------|------------|
| **Ambiguous** | Whether downstream tasks should update files on PR #3 branch path vs new `docs/azm-deliverables/` path. Brief lists corrections but not target file paths for Prototype v0 (still only on PR #3). |
| **Missing** | Explicit statement that **no app exists** — downstream "Epic 1 i18n" sizing implies a codebase. Should say "architecture document only until scaffold task lands." |
| **Over-specified** | Launch wave assignments and font names are appropriately specific for strategy doc. Fine for this deliverable type. |
| **Factually wrong** | Brief implied Chinese was in "the product" — it's only in Prototype v0 HTML on an unmerged PR branch, not in any deployed app (because there is no app). |
| **Effort** | Correctly scoped. Single HTML commit. |

### PR #5 — Design System v0.1 (K TA 7.2)

| Dimension | Assessment |
|-----------|------------|
| **Ambiguous** | Task code was initially K TA 1.A — corrected in follow-up commit. Brief vs Cursor PR title conflict (used Cursor requirement). |
| **Missing** | Should have stated upfront: "extract tokens to CSS file" is **future work** blocked on app scaffold. Agent correctly skipped but brief could mislead next author. |
| **Over-specified** | Byte-for-byte HTML commit instruction was correct and necessary. |
| **Factually wrong** | Brief dedupe check was accurate — no conflicting token files exist. However, **v0 at `docs/startup/phase-2/` does exist** with old typography; brief should name both paths. |
| **Effort** | Correctly scoped. Relocation commit was small overhead from wrong task code. |

### PR #6 — Roadmap v2 (K TA 2.1)

| Dimension | Assessment |
|-----------|------------|
| **Ambiguous** | PR title: brief said long descriptive title; requirements said `[K TA 2.1] Scope`. |
| **Missing** | Merge order guidance — roadmap references artifacts that exist only on other open PRs. |
| **Over-specified** | N/A |
| **Factually wrong** | Brief said "repo may reference Phase 0–4" — on `main` it does not reference anything. The Phase 0–4 references exist **only inside PR #3 HTML files**. PR #6's own R&D feedback noted this correctly. |
| **Effort** | Correctly scoped. |

### Cross-cutting brief failures

1. **Invented stack.** Portals Build Plan (PR #3) discusses i18n architecture, Stripe, and three portals as if build is imminent — but no framework choice exists in repo. **Claude must not assume Next.js, React, or any specific i18n library until a scaffold brief explicitly chooses one.**

2. **Treated HTML prototypes as product code.** Prototype v0's JS i18n hack is a usability-testing shim, not an architecture to extend.

3. **Ignored branch/merge reality.** Multiple briefs write as if prior deliverables are on `main`. They are not.

4. **Duplicate path confusion.** `docs/startup/phase-2/` vs `docs/azm-deliverables/` — no brief has standardised migration or deprecation of the old path.

---

## 7. WHAT THE NEXT BRIEF SHOULD ACCOUNT FOR

**Context:** Claude is about to write an **i18n architecture brief** covering Bengali, Devanagari, Gurmukhi, and Nastaliq Urdu, plus two distinct RTL systems (Arabic Naskh vs Urdu Nastaliq).

### Hard facts the brief must open with

1. **There is no application.** The deliverable should be an **architecture decision record (HTML or Markdown)** under `docs/azm-deliverables/<TASK-CODE>/`, not implementation tasks inside a codebase.

2. **No framework has been chosen.** The brief must either:
   - (a) recommend a stack as part of the architecture doc and flag it for a separate scaffold task, OR
   - (b) write framework-agnostic requirements only.
   
   Do **not** write `next-intl` config paths or `app/[locale]/layout.tsx` unless a scaffold brief has landed.

3. **Typography decisions are already made** — reference `docs/azm-deliverables/K-TA-7.2/Tamia4Life_Design_System_v0-1.html`:
   - Font stack per script (Noto family)
   - Urdu is **not** in main UI stack; use `[lang="ur"]` with `--t4l-font-urdu`, line-height 2.4
   - **Never branch on `dir="rtl"` for font selection** — branch on `lang`
   - Chinese (Noto Sans SC) is **removed** from target set

4. **Community/Language Strategy (S TA 2.B)** defines launch waves and script-community mapping. i18n architecture should align with Wave 1 (Arabic + Romanian) first, Wave 2 (Bengali, Urdu, Punjabi) second — not attempt all scripts day one.

5. **Prototype v0 patterns are wrong** — do not copy its `dir="rtl"` font rules or Chinese language option. Flag Prototype v0 for a separate correction task on PR #3 path.

### What the i18n brief should specify (because nothing exists yet)

| Topic | Repo reality | Brief should decide |
|-------|--------------|---------------------|
| Locale file format | None | JSON vs YAML vs ICU; nested vs flat keys |
| Translation workflow | None | Who translates; CL tools; fallback chain |
| RTL layout | Prototype toggles `dir` on container | Logical properties (`margin-inline`) vs mirrored CSS; component-level vs page-level `dir` |
| Script detection | None | `lang` attribute strategy on HTML root vs per-component |
| Font loading | Google Fonts CDN in HTML | Self-hosted vs CDN; subsetting; FOUT/FOIT policy |
| Romanian | Latin script, LTR | No special rendering — do not over-engineer |
| Multi-language members | Matching Engine spec allows multiple languages per member | Data model for user language preferences (not yet in code) |
| Country dimension | S TA 2.B requires country as first-class filter for EU | i18n doc must separate **locale** (language) from **country** (compliance/matching) |

### What the i18n brief should NOT do

- Assume existing `public/locales/` or `messages/` directories
- Reference npm packages as "already installed"
- Size work as "modify existing i18n middleware" — there is no middleware
- Treat Prototype v0's 3-locale JS object as the starting architecture
- Re-debate script/font choices already locked in v0.1 and S TA 2.B

### Recommended brief structure

1. **Decision record** (HTML, matching existing deliverable style) covering locale model, RTL strategy, font loading, and content workflow
2. **Explicit dependency:** "App scaffold task must run before implementation"
3. **Explicit correction task:** Update Prototype v0 language grid (PR #3 path) — separate from architecture
4. **Consolidation task (future):** Merge Design System v0 colour/spacing + v0.1 typography into single `tamia4life.tokens.css` when scaffold exists

### Merge-order recommendation for Aziz

Before i18n architecture is implemented, consider merging in this order:

1. PR #6 (Roadmap v2) — establishes phase vocabulary
2. PR #4 (Language Strategy) — establishes script/community decisions
3. PR #5 (Design System v0.1) — establishes typography tokens
4. PR #3 (Phase-2 pack) — bulk historical artifacts (note stale labels)
5. PR #1 (Discovery) — independent research track

This survey (K TA 3.4) should merge early so Claude reads it before the i18n brief.

---

## Appendix: Quick reference for Claude

```
REPO TYPE:        docs/planning only — zero application code
MAIN BRANCH:      README.md only (1 line)
PACKAGE MANAGER:  none
FRAMEWORK:        none
CI:               none
TESTS:            none
DESIGN TOKENS:    embedded in HTML (--t4l-* vars); v0.1 typography canonical
I18N:             prototype shim only (en/ar/it); no library
RTL RULE:         branch on lang, not dir; Urdu is separate from Arabic
OPEN PRs:         #1 discovery, #3 phase-2 pack, #4 language strategy, #5 DS v0.1, #6 roadmap v2
STALE ARTIFACTS:  Prototype v0 (Chinese, dir-based fonts), Phase 0–4 labels in PR #3 pack
DISCOVERY:        scaffolded, 0 interviews done
```

---

*End of survey. This document is the technical baseline for all future Tamia4Life R&D briefs until the repo gains application code.*
