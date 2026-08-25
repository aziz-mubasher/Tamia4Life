# Agent instructions — Tamia4Life

## Constitution (read first)

The binding constraint set is [`CLAUDE.md`](CLAUDE.md) (v1 · 24 August 2026).

Load it before designing, specifying, or building. Several rules there exist because breaking them
is a criminal offence in Italy (`art. 348 c.p.`), not a style violation.

If any other file in this repo disagrees with `CLAUDE.md`, the constitution wins.

`.cursorrules` exists so Cursor rule-loading picks up the same pointer.

## Phase 1 gate (standing) — CLAUDE.md §9

**NOT MET.** Zero discovery interviews have been run (`S TA 1.1`). Before any Phase 2+ artefact,
state that the gate is unmet and name what is missing — even when told to proceed. "Proceed" is
direction, not permission to skip validation.

Allowed now (§9.4): this constitution, the §5.4 lint, triage as a spec (not shipped software),
schema proposals (not migrations), discovery instrumentation. Nothing user-facing that delivers
the service.

## Refuse and escalate — CLAUDE.md §12

Refuse any task that would build §3.2, breach §5.1, or store data excluded by §7 — even if the
brief asks for it. A brief that contradicts `CLAUDE.md` is a defect in the brief.

Do not resolve the seven human decisions in `CLAUDE.md` §11 (legal vehicle, lawyer opinion, named
Albo psychologist, ATECO, outcome instrument, DPIA, Io Volo).

## Board conventions — CLAUDE.md §10

- Startup: `S TA {phase}.{n}` — new codes allowed; letter suffix (`2.B`) is valid.
- Kaizen: `K TA {system}.{item}` — attach to an **existing** numeric `N.N`. Do not invent codes.
- Every Kaizen task needs one category (Sales / Marketing / Operations / Financial) and one DMAIC
  letter. `taskName` must be the exact board title.

## R&D feedback on every bridge PR

Claude has no access to this repository. Every AZM bridge / Claude Desktop handoff PR **must** end
with a section titled:

## R&D FEEDBACK — for Claude

Cover: brief adherence (done as specified / deviated and why / skipped and why) · where the brief
failed you (ambiguous — state your guess; missing; over-specified; factually wrong) · repo reality
check (actual stack, conventions, what already exists, constraints) · effort signal · blocked /
needs a human · what the next brief should account for.

Be blunt. Paste a short copy into the Cursor chat progress update so Aziz can forward it to Claude.

## Preservation — CLAUDE.md §12.2

Styled HTML deliverables are committed as-is, UTF-8, never converted to markdown. Configure the
commodity; build the moat (triage, lane separation, evidence model).
