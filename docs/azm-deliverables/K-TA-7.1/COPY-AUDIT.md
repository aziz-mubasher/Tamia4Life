# K TA 7.1 — English copy audit (public site v1)

**Date:** 25 August 2026  
**Surface:** `tamia4life-site.html`  
**Lane:** C / public communication  
**Phase 1 gate:** NOT MET. This page is §9.4 discovery instrumentation, not a live offer.

R&D decision: **CLAUDE.md §5 wins over the Business Plan Summary register.**

| Term | Occurrences | Verdict |
|---|---|---|
| `psychologist` / `psychologists` | 4 | Permitted — §5.3 Lane A usage, Albo named each time |
| `psychological` | 1 | Referral-out only ("medical or psychological care… not the place to look for it") |
| `stress` | 2 | Both are citations of the employer's statutory obligation, never something the service treats |
| `diagnosis` / `treatment` | 2 | Inside the explanation of what the law reserves |
| `mental health`, `therapy`, `anxiety`, `depression`, `trauma`, `patient`, `cure`, `counselling`, `emotional support` | 0 | Banned on this surface |

Those permitted hits are listed in `compliance/banned-words.json` → `audited_surfaces`. Any *new* banned term on this file fails CI.

Italian reserved-act names (`sostegno psicologico`, `diagnosi`, `colloquio clinico`) appear only inside the Cassazione / L. 56/1989 explanation.

## Do not add

- A form, booking flow, or free-text "how are you feeling" field (§3.2 refuse-task)
- Cookie/privacy pages until a form exists
- Live-service positioning (that is Phase 2+ and the gate blocks it)
