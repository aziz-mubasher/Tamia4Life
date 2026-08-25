# Agent instructions — Tamia4Life

## Constitution (read first)

The binding venture constitution is [`CLAUDE.md`](CLAUDE.md) (v1 · 24 Aug 2026).

Cursor agents must treat `CLAUDE.md` as loaded context: lanes A/B/C, the Italian legal-frame-first rule, the Phase 1 gate (**not met**), the do-not-build list, GDPR/storage separation, revenue categorisation, and the seven human-only decisions. If any other file in this repo disagrees with `CLAUDE.md`, the constitution wins.

`.cursorrules` exists so this pointer is also picked up by Cursor rule loading.

## Phase 1 gate (standing)

**NOT MET.** State this before Phase 2+ work, even when a brief says to proceed. See `CLAUDE.md` §9.

## R&D feedback on every bridge PR

Every pull request opened from an AZM bridge / Claude Desktop handoff **must** end its description with a section titled:

## R&D FEEDBACK — for Claude

That section must cover:

1. **Brief adherence** — What was implemented exactly as specified; what was deviated from and why; anything skipped and why.
2. **Where the brief failed you** — Ambiguous (what you guessed); missing (what you decided alone); over-specified (what conflicted with repo conventions); wrong (factually incorrect about this codebase).
3. **Repo reality check** — Stack, conventions, what already exists that the brief seemed unaware of, constraints (CI, tooling, hosting, legacy).
4. **Effort signal** — Larger or smaller than implied; correctly scoped or should have been split.
5. **Blocked / needs a human** — Secrets, DNS, provisioning, credentials, product decisions.
6. **Next task should account for** — Concrete instructions for the next brief author.

Paste a short copy of this summary into the Cursor chat progress update when the PR is ready, so Aziz can forward it to Claude.

Claude cannot see this repository. Without that section, the next brief is written blind.
