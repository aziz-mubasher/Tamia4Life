# K TA 7.1 — copy audit (public site v1)

**Date:** 25 August 2026  
**Surface:** `tamia4life-site.html`  
**Lane:** C / public communication  
**Phase 1 gate:** NOT MET. This page is §9.4 discovery instrumentation, not a live offer.

R&D decision: **CLAUDE.md §5 wins over the Business Plan Summary register.**

The page UI is English by default, with Italian and Spanish packs applied in-browser (`data-i18n` / `t4l-lang`). The language wall (fourteen welcome lines) is unchanged and is not a UI locale.

| Term | Occurrences | Verdict |
|---|---|---|
| `psychologist` / `psychologists` | EN pack + Lane A / safety | Permitted — §5.3 Lane A usage, Albo named each time |
| `psychological` | EN safety / referral-out | Referral-out only ("medical or psychological care… not the place to look for it") |
| `stress` | EN + IT/ES statutory citations | Citations of the employer's obligation (`stress lavoro-correlato`), never something the service treats |
| `diagnosis` / `treatment` | EN Cassazione sentence | Inside the explanation of what the law reserves |
| `mental health`, `therapy`, `anxiety`, `depression`, `trauma`, `patient`, `cure`, `counselling`, `emotional support` | 0 | Banned on this surface |

Those permitted hits are listed in `compliance/banned-words.json` → `audited_surfaces`. Any *new* banned term on this file fails CI.

## Italian (IT)

§5.2 voice: orientamento, mediazione, accompagnamento, formazione, integrazione.  
Avoided: `cura` (care homes → RSA / assistenza), `supporto psicologico`, `benessere psicologico`, `percorso di cura`.

Italian reserved-act names (`sostegno psicologico`, `diagnosi`, `colloquio clinico`) appear only inside the Cassazione / L. 56/1989 explanation. `psicologo iscritto all'Albo` is Lane A only.

## Spanish (ES)

Same legal citations kept in Italian (`diagnosi`, `colloquio clinico`, `sostegno psicologico`, `stress lavoro-correlato`, Legge 56/1989).  
Avoided: `apoyo psicológico`, `soporte psicológico`. Lane A names the Albo professional. Safety note refers out to *medico di base* / ASST / 112 without inviting a reserved act on this page.

## Do not add

- A form, booking flow, or free-text "how are you feeling" field (§3.2 refuse-task)
- Cookie/privacy pages until a form exists
- Live-service positioning (that is Phase 2+ and the gate blocks it)
