# Tamia4Life — repo constitution

**v1 · 24 Aug 2026**  
**Venture:** Tamia4Life (TA) · `aziz-mubasher/Tamia4Life`  
**Status:** binding on every agent (Claude, Cursor, CI) and every human brief  
**Supersedes:** any earlier product framing that treats Tamia as undifferentiated “preventive wellness”, a single facilitator marketplace, or a wellbeing-score app.

If this file and another artifact disagree, **this file wins** until a human amends it.

---

## How to load this file

This is the venture constitution. Read it before designing, specifying, or building.

| Loader | What to do |
|---|---|
| Claude Code / Claude Desktop | This file is `CLAUDE.md` at repo root — it loads automatically. |
| Cursor Cloud / Cursor Desktop | `AGENTS.md` and `.cursorrules` point here. Follow this file as if it were inlined. |
| CI | The banned-words list in §10 is enforced by `scripts/lint-banned-words.py` (see `.github/workflows/banned-words.yml`). |
| Other ventures | This is the pattern to copy. Next: **SV LMS**, then **SV Patente**. Do not clone Tamia’s lanes into those repos — clone the *method* (name the Italian legal frame first). |

**Rule for every design decision:** name the Italian legal frame before specifying the feature. **No frame = not ready to build.**

---

## Standing status (read this first)

**Phase 1 gate: NOT MET.**

Customer discovery (S TA 1.1) has not produced validated demand. The assumption scorecard is still `pending` / 0 interviews. Agents must **state this gate status** at the start of any Phase 2+ work, even when a brief says “proceed anyway”. Proceeding does not make the gate met. Only a human may declare the gate met (§11.7).

What may still be built before the gate is listed in §9.

---

## Doctrine

Italy’s regulatory density is the **distribution channel**, not the obstacle. Every constraint has an opportunity attached that is only reachable by satisfying the constraint first.

- The reserved-act boundary (art. 348 c.p.; L. 56/1989; the Albo) is why Lane A can sell to ASST/ATS and employer benefit.
- The *Documento di Valutazione dei Rischi* (art. 28 D.lgs 81/08), including *stress lavoro-correlato*, is why Lane C can sell to employers — and why the honest line with OT23 must be drawn (§4.2).
- Accoglienza / integrazione (art. 2, letter r, D.lgs 112/2017) is why Lane B can sell to Comuni and FAMI/ISMU projects.
- Formazione (letter d) is why Lane C can sell into fondi interprofessionali, FSE+, Erasmus+, OT23 D-2.
- GDPR art. 9 and the DPIA duty are why Lane A is expensive to operate and therefore defensible.
- The >70% general-interest revenue test is why every euro in the product has a category field (§8).

Do not “simplify away” a constraint to ship faster. The constraint *is* the go-to-market.

---

## §1 Three hard-separated lanes

The law does not reserve “helping people feel better”. It reserves **specific acts**. The product is therefore three lanes with different personnel, branding, consent flows, and data handling.

**A user is in exactly one lane at a time. The system records which.**

Cross-lane presence (same person, same day) is a **handover**, not a blend. Handover creates a new lane occupancy; it does not merge the records.

### Lane A — Percorso clinico

| | |
|---|---|
| **Legal frame** | Reserved psychological act. Delivered only by a *psicologo iscritto all'Albo* (L. 56/1989). Where distress lives. |
| **art. 2 D.lgs 112/2017** | Letter **c)** — *prestazioni socio-sanitarie* (and, when the act is sanitaria, letter **b)** — never pretend otherwise). |
| **Data** | GDPR art. 9 special-category data. Separate store. DPIA signed before any real record (§7). |
| **Sells to** | Individuals; ASST/ATS; employer benefit (as access to a reserved professional — not as “wellness”). |
| **Personnel** | Albo-verified *psicologo* / *psicoterapeuta* only. Verification is a production invariant, not a profile badge. |
| **Consent** | Clinical informed consent, distinct from B/C. |
| **Branding** | May use reserved professional titles **only** for the named, verified professional. Never for the product, the company, or an AI. |

### Lane B — Mediazione

| | |
|---|---|
| **Legal frame** | Not reserved. Cultural mediation, orientation, navigation, accompaniment. |
| **art. 2 D.lgs 112/2017** | Letter **r)** — *accoglienza umanitaria ed integrazione sociale dei migranti*. |
| **Data** | Not art. 9 by default. Do not import Lane A data. Do **not** store immigration status (§7). |
| **Sells to** | Comuni; FAMI / ISMU and equivalent integration projects. |
| **Personnel** | Cultural mediators. Never presented as psychologists. No continuing individual emotional responsibility. |
| **Consent** | Service / accompaniment consent. No clinical consent theatre. |
| **Branding** | Navigation, orientation, accompaniment, *mediazione culturale*. Banned-words list applies in full (§10). |

### Lane C — Formazione

| | |
|---|---|
| **Legal frame** | Not reserved. Group, non-individual, psychoeducation and employer training. |
| **art. 2 D.lgs 112/2017** | Letter **d)** — *educazione, istruzione e formazione professionale* (and cultural-educational activity of social interest). |
| **Data** | Attendance, learning evidence, employer aggregates. Not art. 9. No individual distress record. |
| **Sells to** | Employers; fondi interprofessionali; FSE+ catalogue; Erasmus+; OT23 D-2 dossier (as the *incremental* intervention — §4.2). |
| **Personnel** | Trainers / facilitators. Group setting. No 1:1 emotional case-holding. |
| **Consent** | Training / catalogue consent. Employer sees aggregates of *this lane only*. |
| **Branding** | Formation, psychoeducation, organisational training. Not therapy, not “supporto psicologico”. |

### The triage rule

**The moment a person presents distress, the journey routes to Lane A.**

The triage outcome is an **immutable, timestamped record** that names:

1. UTC timestamp  
2. **Rule version** that fired (e.g. `triage.v1`)  
3. Lane occupancy after the fire (`A`)  
4. Actor (`system` / named human)  
5. The presentation class that fired the rule (not a diagnosis; not a free-text clinical note)

That record is the venture’s defence if the boundary is ever questioned. It is append-only. A later “correction” is a new record, not an edit.

Agents must not invent a softer on-ramp that keeps a distressed person in B or C “until they are ready”. Distress is the route, not a preference.

### Occupancy invariant (engineering)

When a data model exists, these are not optional:

- `lane_occupancy ∈ {A, B, C}` — exactly one, on every session, booking, message thread, and note.
- A person may have a history of occupancies. They do not have a blended current lane.
- Facilitator / professional records carry `eligible_lanes` constrained by credential. A Lane B mediator has `eligible_lanes = {B}` or `{B, C}` — never `A` without Albo verification.
- Matching inside a lane never reads another lane’s clinical or distress data.

---

## §2 The venture restated in art. 2 D.lgs 112/2017 language

Tamia4Life is an activity of general interest under **D.lgs 3 luglio 2017, n. 112, art. 2**, exercised in a combination of three letters — and only those three, until a human adds a letter:

| Letter | Statutory object (short) | Tamia lane | Typical buyer |
|---|---|---|---|
| **r)** | Accoglienza umanitaria ed integrazione sociale dei migranti | **B** Mediazione | Comuni, FAMI/ISMU |
| **c)** | Prestazioni socio-sanitarie | **A** Percorso clinico | Individual, ASST/ATS, employer benefit |
| **d)** | Educazione, istruzione e formazione professionale | **C** Formazione | Employers, fondi, FSE+, Erasmus+, OT23 D-2 |

Do not describe the venture as “mental health for immigrants”, “wellbeing marketplace”, or “preventive emotional wellness”. Those phrases collapse the letters and collapse the lanes.

Country of operation is Italy first, EU by design (language assets travel; licensing and Albo do not). **Nothing in the product may hard-code Italy as the only possible country** — country is a first-class dimension — but **every Italian feature still names its Italian frame before it is specified**. Foreign expansion does not relax the Italian boundary for Italian users.

---

## §3 Why the boundary is drawn where it is

**Cass. pen., sez. VI, n. 16562/2016.**

Conviction under **art. 348 c.p.** (*esercizio abusivo della professione*) — not for diagnosing or treating, but because **complexity, continuity, remuneration and professional self-presentation** together created an *«apparenza oggettiva di competenza specialistica»*.

Self-presentation is part of the offence. That is why:

- this repo carries a **banned-words list** (§10) enforced as a **CI lint** over copy and CMS content, **in every language**, not just Italian;
- Lane B/C must not hold continuing individual emotional responsibility;
- an automated system that produces *sostegno psicologico* is the reserved act **at scale** — and is on the do-not-build list (§5);
- branding, job titles, in-app chrome, and facilitator cards are compliance surfaces, not marketing surfaces.

The four Cassazione factors are a design checklist. A feature that adds complexity + continuity + pay + specialist tone, even with a disclaimer, is not safe because of the disclaimer.

---

## §4 Go-to-market frames

### §4.1 Lane A buyers

- **Individual** — pays for a *percorso clinico* with a named Albo professional.
- **ASST / ATS** — public purchaser of socio-sanitary / clinical capacity, in language, under public-contract rules. Not a “wellness vendor”.
- **Employer benefit** — the employer buys **access to Lane A**, never visibility into Lane A content. Aggregates, if any, come from Lane C or from separately consented, non-identifying operational stats — never from clinical notes.

### §4.2 art. 28 D.lgs 81/08 — the B2B door opener

**Frame:** the employer’s duty to assess **all** risks, including *rischio stress lavoro-correlato*, in the DVR.

That duty is why HR and RSPP will take the meeting. It is not, by itself, a Tamia product.

**Honest boundary:** the mandatory assessment is **compliance**, not an OT23-creditable intervention. Doing what art. 28 already requires does not earn INAIL OT23 credit.

Tamia’s B2B offer on this door is:

1. Help the organisation **see** the duty (conversation, not a Tamia-branded “risk score” of individuals).
2. Sell **Lane C** as the incremental organisational / formative intervention that *can* sit in an **OT23 D-2** dossier — because it goes beyond the mandatory assessment.
3. Sell **Lane A access** as the reserved path when a worker presents distress — never as a scored population of “at-risk employees”.

Agents must not write sales copy that claims “we fulfil your DVR” or “this module is OT23-eligible” without a human (§11). Catalogue language may *prepare* a dossier; it may not certify INAIL acceptance.

### §4.3 Bonus psicologo — deliberate, costly, defensible foreclosure

Tamia **does not** integrate, broker, invoice, or market through the *Bonus psicologo* (or successor CNOP / MEF session-reimbursement schemes).

This is a foreclosure, not an oversight.

| Why costly | Why defensible |
|---|---|
| Leaves a public subsidy on the table. | The bonus is a reserved-act reimbursement channel Tamia does not control. |
| Competitors can advertise “bonus accepted”. | Caps, stop-start funding, and political redesign would make Lane A a billing front-end. |
| | It would train the market to see Tamia as the bonus product, not a durable three-lane enterprise. |
| | It would pressure copy, UX, and data toward a single clinical reimbursement shape. |

Reversing this foreclosure is a **human-only** decision (§11.3). Agents must not “just add Stripe metadata for the bonus” or accept a brief that treats the bonus as a Phase-3 convenience.

---

## §5 Explicit do-not-build list

Do not build, prototype as-if-real, or leave in a merged spec as a future epic:

1. **Any wellbeing score, index, RAG, or interpretive assessment outside Lane A.** No “resilience check-in” that interprets the person. No employer-facing individual heatmap. No burnout / anxiety / depression scorer in B or C.
2. **Any AI agent that gives emotional support.** An automated system producing *sostegno psicologico* is the reserved act at scale — including chatbots, “companions”, “listening” agents, and LLM wrappers that reflect feelings back as care. AI may translate, schedule, navigate (Lane B), or teach a **group** curriculum (Lane C) without addressing the person as a case.
3. **Symptom-based facilitator matching.** Matching on language, culture, logistics, and (inside Lane A only) declared clinical specialty of an Albo professional is in scope. Matching on symptoms, PHQ-like answers, or inferred distress **to a Lane B/C facilitator** is not.
4. **Continuing individual emotional responsibility** held by a Lane B or Lane C facilitator. No caseload of “my people” in B/C. No weekly 1:1 “how are you holding up?” as a product loop in those lanes.
5. **Blended branding** — one product surface that looks like a clinic for everyone.
6. **Immigration-status fields** — *permesso*, visa class, asylum, irregularity (§7).
7. **Bonus psicologo** rails (§4.3).
8. **OT23 / DVR certification** claimed by software (§4.2, §11).

Earlier artifacts on unmerged PR branches (Roadmap v2 “preventive wellness”, Matching Engine “baseline self-assessment”, employer “wellbeing insights”, Prototype check-in index, Kaizen service line “Wellness & Lifestyle Coaching”) are **pre-constitution**. They are historical. They are not a licence to build those things.

---

## §6 Evidence model

Reporting is an **export**, never a retrofit.

If a funder, employer, or *bilancio sociale* needs a number, that number was designed as a field at capture time — or it does not exist. Do not mine chat logs, clinical notes, or free text after the fact to invent indicators.

Exports are designed for, and labelled as, one of:

| Export | Typical lane | What it may contain |
|---|---|---|
| **FSE+** | C | Enrolment, attendance, hours, completion, anagraphic fields the call requires — not distress. |
| **FAMI** | B | Project outputs (orientation sessions, accompaniment events, language of delivery). No immigration status. No art. 9. |
| **Erasmus+ KA210** | C | Partnership learning / small-scale partnership evidence. Group, educational. |
| **OT23 dossier** | C (incremental) | Organisational / formative intervention description. Not the DVR itself. Not individual names. |
| **Bilancio sociale** | A+B+C as categories | Revenue by art. 2 letter, users/participants by lane, no clinical content. |

Lane A clinical content is **not an export** to funders or employers. Lane A operational counts (sessions delivered by Albo professionals) may be exported only in form the DPIA and the contract allow.

Every new capture field must name: **which export it feeds**, **which lane it belongs to**, and **which legal frame requires it**. Fields with no export and no frame are not added “for later”.

---

## §7 GDPR

- **DPIA is mandatory before Lane A touches a real record.** A draft DPIA is not a DPIA. Sign-off is human (§11.4). Until then: no production Lane A, no imported clinical lists, no “just a pilot spreadsheet”.
- **Lane separation extends to storage.** Separate schemas / buckets / encryption contexts. A shared Postgres with a `lane` column is not separation if a Lane B role can `SELECT` Lane A rows. Least privilege by lane.
- **Art. 9 data lives only in Lane A.** Distress presentation that fired triage is a routing fact (the immutable record), not a clinical file. Do not copy it into B/C CRM.
- **Never store immigration status.** Not as a column, tag, note type, or “hidden admin field”. This is **schema-enforced**, not discipline-enforced: the migration that adds `permesso_di_soggiorno`, `status_giuridico`, `asylum`, `regularisation`, or equivalents **fails CI / review**. Language, nationality of cultural identification, and self-described context (“new to Italy”, “raising a family”) are not permesso class — and must not be used as a proxy for legal status.
- Consent is **per lane**. Employer legal basis for Lane C aggregates does not unlock Lane A.
- Retention schedules differ by lane. Do not apply a single “user deleted” that forgets the triage defence record without a human legal decision.
- Hosting: EU. No “the model is in the US but we anonymise” for Lane A.

---

## §8 Legal vehicle and the >70% ratio

Two live options; **agents must not choose** (§11.1):

| Vehicle | What it buys | What it costs |
|---|---|---|
| **Cooperativa sociale** (L. 381/91), typically tipo A | Familiar to Comuni and socio-sanitary purchasers; mutualistic governance | Capital and governance less flexible; 3% *fondo mutualistico*; cooperative constraints |
| **S.r.l. impresa sociale** (D.lgs 112/2017) | Capital flexibility; statutory *impresa sociale* brand | Asset lock; *bilancio sociale*; **general-interest activities in via principale** |

**Engineering consequence (either vehicle, especially impresa sociale):**

> **Revenue categorisation is a product data field** because of the **>70% general-interest ratio**.

Every chargeable object (session, seat, catalogue course, project invoice line) carries:

```
revenue_category ∈ {
  general_interest_c,   // art. 2 c) — Lane A socio-sanitary
  general_interest_d,   // art. 2 d) — Lane C formazione
  general_interest_r,   // art. 2 r) — Lane B mediazione / integrazione
  other                 // must remain the minority
}
```

The ratio is computed from product data, not reconstructed in March by an accountant guessing from Stripe descriptions. `other` includes merch, pure software licences with no general-interest activity, and anything a lawyer has not mapped to a letter.

Agents must not add a paid feature without proposing a `revenue_category`. If the category would be `other`, say so explicitly — that is a ratio risk, not a nicety.

---

## §9 Phase 1 gate

**The gate is NOT MET.** Restate this before Phase 2+ work.

Canonical gate (Startup board Phase 1 · Discovery & Problem Validation; S TA 1.1):

- Demand validated across the intended buyers, not a pitch-deck consensus.
- At least a few employers with a **costed** pain and a letter of intent.
- A plausible facilitator / professional **supply** signal (including, for Lane A, Albo-eligible professionals — not only mediators).
- The space the lanes occupy is real to interviewees — including that distress routes to A.

Surprises still emerging ⇒ do not close the gate.

### What may be built before the gate

Allowed, because they do not pretend the gate is met and they do not touch real Lane A records:

- This constitution, `AGENTS.md`, `.cursorrules`, banned-words lint and CI.
- Discovery interviews, notes, assumption scorecards (S TA 1.1).
- Community / language strategy, design system, **non-production** prototypes and brand work.
- Roadmaps, ADRs, board alignment — if they **name the legal frame** and do not smuggle do-not-build items back in.
- Paper schemas: occupancy, consent, triage record, `revenue_category`, no-immigration-status.
- **Unsigned** DPIA and legal memos.
- Facilitator **sourcing research** (conversations, not production credentialling of *psicologi*).

### What may not be built before the gate

- Production app with real users.
- Real Lane A records or any art. 9 data.
- Employer contracts that promise reserved acts the venture cannot yet deliver.
- Anything on the §5 do-not-build list.
- Shipping a matching engine, check-in index, or AI companion “to learn”.
- Declaring the gate met in a README, PR, or board because a brief was impatient.

A brief that says “build the MVP anyway” is still bound by this section. Build only from the allowed list, and say the gate is unmet at the top of the PR.

---

## §10 Copy, branding, banned words

Copy is a Cassazione surface. The lint runs on **every language** in the repo: UI strings, HTML prototypes, Markdown, CMS fixtures, emails, store listings.

Canonical machine list: [`compliance/banned-words.json`](compliance/banned-words.json).  
Runner: [`scripts/lint-banned-words.py`](scripts/lint-banned-words.py).

### What the list is for

Terms that create *apparenza oggettiva di competenza specialistica* when used for the **product**, **Lane B/C**, **AI**, or **unverified personnel**. Lane A may name a **specific Albo professional’s reserved title** in a context the allowlist and a human have approved. The default is deny.

### Starter categories (not exhaustive — the JSON is)

**Italian — reserved act / specialist appearance**

- *sostegno psicologico*, *supporto psicologico*, *aiuto psicologico*, *consulenza psicologica*
- *psicoterapia*, *psicoterapeuta*, *terapia* / *terapeuta* as product or B/C title
- *diagnosi*, *diagnosticare*, *trattamento clinico*, *paziente* (use *utente* / *partecipante* / *persona*)
- *il tuo psicologo* / *la tua psicologa* as product chrome
- *benessere mentale* + score / test / indice / interpretazione

**English — same function**

- psychological support, emotional support (as a product promise), AI therapist / AI companion
- therapist, psychotherapy, diagnosis, treatment, patient (as product nouns)
- wellbeing score, wellness index, burnout score, symptom checker
- mental health professional (for B/C or the company)

**Other languages:** Arabic, Romanian, Ukrainian, Albanian, Bengali, Urdu, Punjabi, Hindi, Tagalog — and every future locale — get **equivalent** phrases in the JSON **before** that locale ships. A locale without a banned-phrase set **does not ship**. Machine translation of the Italian list is a draft; a human signs the locale pack (§11.6).

### Required voice (safe defaults)

| Instead of | Use |
|---|---|
| Supporto psicologico | Percorso clinico (A) / mediazione (B) / formazione (C) |
| Therapist / coach del benessere | *Psicologo iscritto all'Albo* (A, named) / mediatore (B) / formatore (C) |
| Patient | Utente, partecipante, persona, membro |
| Wellbeing score | Nothing — or, in A only, a tool the *psicologo* chose, not a product index |
| AI that listens | AI that translates, schedules, or navigates |

Disclaimers do not rehab a banned phrase. “Not a substitute for therapy” next to a chatbot that does *sostegno* is still *apparenza*.

---

## §11 Seven decisions that require a human

Agents **must not** resolve these. Surface them and stop.

| # | Decision | Why it is not an agent’s |
|---|---|---|
| **1** | **Legal vehicle** — cooperativa sociale vs S.r.l. impresa sociale (or a holding structure). | Governance, asset lock, and purchaser perception. Engineering follows; it does not choose. |
| **2** | **Lane A go-live** — first Albo psychologist engaged, insurance, clinical governance, production DPIA-bound records. | Reserved-act exposure. |
| **3** | **Bonus psicologo foreclosure** — any reversal or “temporary” integration. | Already decided in §4.3. |
| **4** | **DPIA sign-off** (and any later material change to Lane A processing). | A draft is not a signature. |
| **5** | **Triage rule version** — publishing a new `triage.vN` that the immutable record will name. | The defence record is only as good as the rule a human owned. |
| **6** | **Banned-words / locale-pack amendments** — adding or removing phrases, or declaring a locale pack complete. | Self-presentation is part of art. 348 c.p. |
| **7** | **Phase 1 gate declaration** — stating the gate is met. | Agents only report evidence and the standing “NOT MET” until a human flips it. |

Related calls that inherit the same stop rule: certifying OT23 eligibility; storing anything adjacent to immigration status “because the Comune asked”; granting a mediator `eligible_lanes` including `A`; putting clinical export fields on a FAMI/FSE+ file.

---

## §12 Agent operating protocol

1. **State Phase 1 gate status** before Phase 2+ work.
2. **Name the legal frame** (lane + art. 2 letter + any special law) in the PR or spec. No frame → do not implement the feature.
3. **Refuse §5 items** even if a prototype, roadmap, or older brief asks for them. Say which clause blocked it.
4. **Escalate §11** instead of picking a default.
5. **Every paid surface** proposes `revenue_category`.
6. **Every copy change** must pass banned-words CI in the language of the copy.
7. **R&D feedback** — every AZM bridge / Claude Desktop handoff PR ends with `## R&D FEEDBACK — for Claude` (see `AGENTS.md`). Claude cannot see this repo; the feedback is how the next constitution-quality brief gets written.
8. **Do not merge pre-constitution artifacts onto `main` unchanged** if they violate §5 or §10. Rewrite or quarantine.

---

## §13 Repo reality (so briefs stop inventing a stack)

As of v1 of this constitution:

- **`main` is a docs/planning repo.** Application code, `package.json`, CI (beyond this lint), and i18n libraries **do not exist** until someone lands them.
- Substantive historical work lives on **unmerged PRs**: discovery (`discovery/`), Phase-2 HTML pack, language strategy, design system v0.1, roadmap v2, quality survey. Treat them as inputs, not as canon, where they conflict with this file.
- Deliverable convention: `docs/azm-deliverables/<TASK-CODE>/`.
- Tokens, when they exist, are `--t4l-*`. Typography branches on `lang`, never on `dir`. Urdu is Nastaliq, not Arabic Naskh. Chinese is out (S TA 2.B).
- Wave 1 languages: **Arabic + Romanian**. Language ≠ nationality.

---

## §14 Replication note (other eight ventures)

Copy the **method**, not the lanes:

1. Doctrine in one paragraph: the constraint *is* the channel.
2. Hard-separated product lanes that the law actually distinguishes.
3. The venture restated in the statute that will appear on the *bilancio* / accreditamento / licence.
4. Explicit do-not-build list.
5. Evidence as export, not retrofit.
6. Data rules that are schema-enforced.
7. Entity / revenue consequences as product fields.
8. Phase-gate honesty.
9. Banned presentation terms + CI.
10. A short human-only list.

**Next constitutions:** SV LMS (Accordo Stato-Regioni + accreditamento + white-label decision), then SV Patente (art. 123 c.11-bis boundary), then the rest.

---

*End of Tamia4Life constitution v1. Amendments are human (§11.6 for words; otherwise a dated v2 signed in this file’s header).*
