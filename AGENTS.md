# Agent instructions — Tamia4Life

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

See also: `docs/azm-deliverables/K-TA-3.4/REPO-SURVEY.md` for the full repository baseline.
