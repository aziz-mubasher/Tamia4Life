# CLAUDE.md — Tamia4Life

> **Load this before designing, specifying or building anything in this repository.**
> It is not background reading. It is the constraint set. Several rules here exist because
> breaking them is a criminal offence in Italy, not a style violation.
>
> Cursor: reference this file from `AGENTS.md` / `.cursorrules` so the venture agent loads it too.

| | |
|---|---|
| **Venture** | Tamia4Life |
| **Venture id (bridge)** | `tamia` |
| **Venture code** | `TA` |
| **Repo** | `aziz-mubasher/Tamia4Life` |
| **Startup board** | `tamia` · https://www.azizmubasher.net/startup/tamia |
| **Kaizen board** | `kaizen-tamia` · https://www.azizmubasher.net/kaizen/tamia |
| **Current phase** | **Phase 1 — Discovery & Problem Validation. GATE NOT MET.** See §9. |
| **Jurisdiction** | Italy · Regione Lombardia · provincia di Brescia |
| **Doc version** | v1 · 24 August 2026 |

---

## 0. Read this first — the five things that govern everything

1. **Tamia4Life is a regulated-adjacent service, not a wellness app.** Italian law reserves
   psychological acts to the Albo. Get this wrong and it is `art. 348 c.p.`, not a takedown notice.
2. **The compliance boundary is the product architecture.** Three service lanes, hard-separated.
   Every user journey routes into exactly one. See §3.
3. **Words are legally operative.** A page that implies clinical competence is evidence against you
   even if the service behind it is lawful. See §5.
4. **The evidence model is not reporting — it is the product.** Funders and the venture want the
   same data. Build it in from the first schema. See §6.
5. **Phase 1's gate is not met.** No discovery interviews have been run. Nothing in Phase 2+ ships
   until §9 clears — and that is not a delay, because the earliest funding deadline is March 2027.

---

## 1. Doctrine — adopt the system, do not fight it

Italy has a dense, specific, and mostly coherent body of law about who may do what to whom, and a
large amount of public money attached to it. The instinct of most founders is to treat that as
friction and route around it. **That instinct is wrong here, and expensively so.**

The system is not an obstacle to Tamia4Life. It is the distribution channel. Every constraint below
has a corresponding opportunity attached to it, and the opportunity is only reachable by satisfying
the constraint first:

| The constraint | What it unlocks once satisfied |
|---|---|
| Psychological acts are reserved to the Albo | A psychologist on staff makes the clinical lane sellable to ASST, ATS and employers who will not buy from an unlicensed provider |
| An impresa sociale must draw >70% of revenue from *attività di interesse generale* | RUNTS registration → FSE+ Terzo Settore (€7M open now), FAMI partner status, Fondazione Bresciana, AMIF |
| `art. 28 D.lgs 81/2008` obliges every employer to assess work-related stress | Turns the first B2B conversation from a wellbeing pitch into a compliance gap the buyer already owns |
| INAIL OT23 D-2 specifies a psychologist-delivered, in-person, all-staff intervention | A recurring, legally anchored B2B product worth up to 28% off the client's insurance premium |
| GDPR art. 9 makes health data special-category | A documented lawful basis and a real DPIA are exactly what a public commissioner audits before contracting |

**The rule for every design decision in this repo:** name the Italian legal frame the feature sits
inside *before* specifying the feature. If no frame can be named, the feature is not ready to build.

---

## 2. What Tamia4Life is, in the vocabulary the system recognises

**Plain description.** A mother-tongue, culturally-matched, explicitly **non-clinical** emotional
wellness and adaptation service for multicultural communities in Italy. Two-sided: foreign-origin
residents who carry the strain, and employers with multicultural workforces who pay to relieve it.
Delivered by bilingual facilitators. Positioned in the space between *"I'm fine"* and
*"I need a psychiatrist"*.

**The same thing, in statutory language.** Under `art. 2 D.lgs 112/2017` (*attività di interesse
generale*), the venture sits across three letters and the statute should name all three:

- **r)** *accoglienza umanitaria ed integrazione sociale dei migranti* — the anchor
- **c)** *prestazioni socio-sanitarie*, expressly including *promozione della salute e prevenzione*
- **d)** *educazione, istruzione e formazione professionale*

**Why this matters and is not cosmetic.** There is public money in Italy and Europe for migrant
integration at every level of government. There is almost none for "wellness". The service is
identical either way. Lead with **integrazione**, always.

**Candidate ATECO:** `88.99` (altre attività di assistenza sociale non residenziale) or `85.59.20`
(formazione professionale) depending on which lane dominates revenue. ⚠️ Not yet decided — this
choice drives the INPS gestione, the IVA treatment and the >70% ratio. See §11.

---

## 3. Service architecture — three lanes, hard-separated

**This is the single most important section for anyone writing code.**

The law does not reserve "helping people feel better". It reserves specific acts. So the product is
built as three lanes with different personnel, different branding, different consent flows and
different data handling. **A user is in exactly one lane at any moment, and the system records
which.**

| | **Lane A — Percorso clinico** | **Lane B — Mediazione** | **Lane C — Formazione** |
|---|---|---|---|
| **Who delivers** | **Psicologo iscritto all'Albo** (employed or in convenzione) — no exceptions | Mediatore linguistico-culturale, peer facilitator | Trainer, facilitator, mediator |
| **What it is** | Individual support where distress, symptoms or emotional suffering are present | Orientation, navigating services, interpreting, accompaniment, practical adaptation | Group workshops, psychoeducation, employer training, e-learning |
| **Format** | 1:1, continuing relationship | 1:1 or family, task-oriented | Group, non-individual |
| **Legal frame** | `L. 56/1989` — reserved. Lawful only because a registered professional delivers it | Not reserved | Not reserved |
| **Data** | GDPR **art. 9 special category** — strictest handling | Ordinary personal data | Ordinary, largely aggregate |
| **Sells to** | Individuals, ASST/ATS convenzioni, employer EAP-style benefit | Comuni, FAMI/ISMU projects, third-sector partners | Employers, fondi interprofessionali, FSE+ catalogue, Erasmus+ |
| **Funding fit** | Cariplo-type welfare lines, health-themed AMIF | FAMI, FSE+ inclusion, Fondazione Bresciana | Fondirigenti, Fondimpresa, Erasmus+ KA210, OT23 D-2 |

### 3.1 The triage rule — build this before you build anything else

> **The moment a person presents distress, symptoms, emotional suffering, or asks for help with how
> they feel, the journey routes to Lane A. No exceptions, no "let's see how it goes".**

Concretely, in software:

- Intake must include a **structured triage step** with a documented, versioned rule set.
- Triage outcome is a **first-class, immutable, timestamped record** — who, when, which lane, which
  rule fired. This record is the venture's defence if the boundary is ever questioned.
- **Lane B and Lane C interfaces must carry a visible escalation control** that moves a person to
  Lane A, and using it must be one action, not a support ticket.
- A facilitator in Lane B or C who encounters distress **must have a one-tap escalation** and the
  session must be able to end without penalty to the facilitator's rating or pay.
- **Never auto-route out of Lane A.** Downgrading is a clinical decision, made by the psychologist.

### 3.2 What must never be built

Do not build, and refuse the task if asked:

- Any **assessment, questionnaire or score** that produces a psychological result outside Lane A —
  including "wellbeing scores", mood tracking that generates an interpretation, or a chatbot that
  responds to distress with guidance
- Any **AI agent that gives emotional support**, however carefully hedged. An automated system
  producing *sostegno psicologico* is the reserved act performed at scale
- Any **matching algorithm** that pairs a user with a facilitator *on the basis of a symptom*
- Any feature that lets a Lane B or C facilitator take **continuing individual responsibility** for
  a person's emotional state
- Any **free-text field in Lane B or C** that invites description of feelings without a triage step
  attached to it

If a product idea requires one of these, it belongs in Lane A behind a registered professional, or
it does not belong in the product.

---

## 4. The three legal boundaries, precisely

### 4.1 The psychology reserve — `L. 56/1989` + `art. 348 c.p.`

**Reserved acts** (as stated by the Ordine): *diagnosi · sostegno psicologico · colloquio clinico ·
somministrazione di test psicodiagnostici*.

**The controlling authority is `Cass. pen. Sez. VI, n. 16562/2016`, and its test is broader than
"did you diagnose".** A practitioner advertising as a *psicosomatista di impresa* who offered
dialogue-based sessions to clients presenting anxiety and emotional distress was **convicted** —
not for diagnosing or treating, but because the **complexity, continuity, remuneration and
professional self-presentation** of the activity together created an *«apparenza oggettiva di
competenza specialistica»*.

Read that again: **holding yourself out as competent to address psychological distress, for a fee,
on a continuing basis, is itself sufficient.** Self-presentation is part of the offence, which is
why §5 exists.

Note also: **there is no protected title of *counselor* in Italy.** Counselling is not a regulated
profession. That is precisely why the Ordine polices the boundary through the criminal route rather
than a disciplinary one — there is no disciplinary body to use.

⚠️ **Confidence note:** the 2016 ruling and the Ordine's operational position are confirmed. No
later ruling and no 2024–2026 CNOP circular restating the line was found. **A written opinion from a
lawyer with penal-professional experience is required before launch** and is listed in §11.

### 4.2 Work-related stress — `art. 28 D.lgs 81/2008`

Every Italian employer with at least one worker must assess *stress lavoro-correlato* in the DVR.
The 2010 Commissione Consultiva circular confirmed it applies **regardless of size or sector** —
only the method scales. Omitted or incomplete assessment is prosecuted as a DVR defect.

INAIL's methodology is two-phase, run by a *gruppo di gestione* (datore di lavoro, RSPP, medico
competente, RLS) with an occupational psychologist recommended: a preliminary objective phase on
verifiable indicators, then a **deeper phase — questionnaire, semi-structured interviews, focus
groups — triggered at medium or high risk.** The 2025 update added an integrated checklist for
remote work and *tecnostress*.

**Why this is in an engineering document.** Most prospects have discharged this obligation with a
tick-box checklist. The deeper phase is a service someone has to deliver, and it is Lane A + Lane C
work. It reframes the first employer meeting entirely.

**The boundary to state honestly to every buyer:** performing the mandatory assessment is compliance,
**not** an OT23-creditable intervention. You sell the qualified delivery of the deeper phase and the
above-minimum interventions that follow — never the legal minimum dressed up as a funded product.

### 4.3 The reimbursement wall — Bonus psicologo

The national *Bonus psicologo* requires the professional to be enrolled in the **elenco degli
psicoterapeuti** and to have notified adherence to CNOP, and the sessions must be **psicoterapia**.

**A non-clinical, preventive, mediator- or coach-delivered service is categorically outside it.**
Tamia4Life cannot accept it as payment, cannot advertise against it, and must not position adjacent
to it in a way that implies eligibility.

This is a deliberate strategic choice with a real cost: the non-clinical positioning forecloses
Italy's only national reimbursement mechanism for psychological support. Made with open eyes, it is
defensible. Discovered late, it is a hole in the revenue model.

Where individual Lane A professionals *are* registered psicoterapeuti, they may serve bonus clients
— **under their own Albo identity, delivering psicoterapia**. That is a different product from the
one described in this repo, and the platform must not blur the two.

---

## 5. Naming, copy and interface rules

Under `Cass. 16562/2016`, **self-presentation is evidence**. These rules are not brand guidelines.

### 5.1 Banned on Lane B and Lane C surfaces

Never use, in any service name, page title, meta description, button, ad, or facilitator bio outside
Lane A:

`sostegno psicologico` · `supporto psicologico` · `benessere psicologico` · `psicologico` (as a
descriptor of what the service provides) · `terapia` · `terapeutico` · `ansia` · `depressione` ·
`stress` (as something the service treats) · `trauma` · `disagio psichico` · `cura` · `paziente` ·
`diagnosi` · `percorso di cura`

### 5.2 Use instead

`orientamento` · `mediazione linguistico-culturale` · `accompagnamento` · `percorso di adattamento` ·
`inserimento` · `formazione` · `laboratorio` · `gruppo di confronto` · `partecipante` · `beneficiario`

### 5.3 Lane A copy rules

Lane A may and **should** use clinical language — but every such page must state, visibly and near
the offer, that the service is delivered by *psicologi iscritti all'Albo*, with the professional's
registration details available. Vagueness here is worse than silence.

### 5.4 Implementation requirements

- The banned list lives in the repo as a **lint rule over copy files and CMS content**, running in
  CI. Add it to the pipeline before the first public page ships.
- Multilingual copy must be checked **in every language**, not just Italian. A translation that
  reintroduces "psychological support" in Urdu or Spanish carries the same exposure.
- Marketing assets (ads, social, video scripts) go through the same check. The Veo/Kling prompt
  packages used elsewhere in the portfolio are in scope.

---

## 6. Evidence and data model — build it once, report forever

Every funder in the map asks for the same things: quantified need, a defined cohort, baseline,
outcome, attendance, cost per beneficiary. **The venture wants exactly the same data to know whether
the service works.** They are one requirement, not two.

**Design principle: reporting is an export, never a retrofit.**

### 6.1 Minimum first-class entities

Capture from the first schema, not "later":

- **Beneficiary** — pseudonymous id; language of delivery; broad cohort markers only (age band,
  years in Italy band, employment status band, comune). **Never** immigration or legal status.
  **Never** free-text identity description.
- **Lane assignment** — immutable, timestamped, with the triage rule version that produced it.
- **Session** — lane, delivery mode (in person / synchronous remote), duration, language,
  facilitator role class, attendance state, funding stream attribution.
- **Facilitator** — role class (`psicologo_albo` / `mediatore` / `formatore`), languages,
  credential verification state and expiry, Albo registration number where applicable.
- **Outcome instrument** — a validated pre/post measure with instrument name and version.
  ⚠️ **Instrument choice is a Lane A clinical decision, not an engineering one.** Do not pick one.
- **Employer engagement** — organisation, sector ATECO, workforce size band, intervention type,
  and — where relevant — the **OT23 intervention code** the activity is intended to evidence.
- **Consent** — versioned consent artefact per lane, with withdrawal timestamp and effect.

### 6.2 Reporting exports to design against

Build these as first-class outputs, not ad-hoc queries:

- **FSE+ / Regione Lombardia** — participants, hours, attendance, cohort composition, costi standard
- **FAMI / ISMU-type projects** — beneficiaries by nationality band and language, service type, hours
- **Erasmus+ KA210** — lump-sum activity evidence: what happened, when, with whom, produced what
- **OT23 dossier** — per employer per calendar year, the intervention record the client files with
  INAIL by 28 February
- **Bilancio sociale** — mandatory for an impresa sociale regardless of size; it needs impact
  numbers, not prose

### 6.3 The rule that keeps this honest

> No funding claim may be made from data the platform did not record at the time the service was
> delivered. If a report needs a number, the number must have an entity behind it.

---

## 7. GDPR and data protection — non-negotiable

Lane A processes **art. 9 special-category health data**. This is the highest-risk data in the
portfolio and the audience is a population with reason to distrust data collection.

- **A DPIA is mandatory** before Lane A processes a single real record. Not optional, not later.
- **EU-hosted infrastructure only.** No transfer outside the EEA without a documented mechanism.
- **Lane separation extends to storage.** Lane A data must be logically separated with its own
  access-control boundary. A Lane C trainer must be technically incapable of reading Lane A records.
- **Never store**: immigration or legal status, religion, ethnicity, or any free-text field that
  invites them. The discovery guide already commits to this with participants — the schema must
  enforce it, not rely on discipline.
- **Data minimisation on cohort markers**: bands, never exact values. Exact date of birth, exact
  address and exact income are not needed for any report listed in §6.2.
- **Retention policy per lane**, published, with automated deletion.
- **Right to erasure must actually work**, including in backups and exports, and must not break
  aggregate reporting — design the aggregates to survive individual deletion.
- Interpreters and mediators handling personal data need **written appointments as authorised
  persons** under `art. 29 GDPR`, not just an NDA.

---

## 8. Legal form — and why it is an engineering constraint

The vehicle is not yet constituted. Two candidates, and the choice changes the product:

| | **Cooperativa sociale tipo A** | **S.r.l. impresa sociale** |
|---|---|---|
| Minimum people | **3 soci** | 2 soci (a single natural-person member is **barred**) |
| Formation | €1.500–2.500 | €3.000–4.500 |
| **Organo di controllo** | Only above ordinary thresholds | **ALWAYS mandatory, any size — €2.000–3.500/yr** |
| Tassa CC.GG. €309,87/yr | **Exempt** | Due |
| External audit | Revisione ministeriale ~€429/biennium | Revisione legale only above thresholds |
| Annual cost delta | — | **+€2.400–3.800/yr** |
| Governance | One head one vote, open door, ministerial inspection | Ordinary S.r.l. control, transferable quote |
| Impresa sociale status | **Di diritto** — automatic | By qualification |

**Both are ETS. Both reach FSE+ Terzo Settore, FAMI partner status, Fondazione Bresciana.** The coop
is materially cheaper and, given a named team of five and a genuinely collective mission, deserves
the serious look. The S.r.l. wins only if control or an investor cap table matters.

**The engineering consequences either way:**

- **>70% of revenue must come from *attività di interesse generale*.** The B2B employer work must be
  drafted and *invoiced* under letters d) and r) — not as generic consulting. **Revenue
  categorisation is a product data field**, not an accounting afterthought. Build it now.
- **Bilancio sociale is mandatory regardless of size** and must be published on the venture's own
  website. That is a build item, not a PDF upload.
- **Worker and user involvement mechanisms** must be in the statute and, above thresholds, in
  governance. If the platform is where facilitators and beneficiaries are heard, that mechanism is
  partly a software feature.

---

## 9. Phase gate — current status and what is blocked

**Phase 1 — Discovery & Problem Validation. GATE NOT MET.**

The Customer Discovery Interview Guide exists (`S TA 1.1`). **Zero interviews have been run.**

This venture has already failed this gate once: a design system, two prototypes, a matching-engine
spec and an MVP backlog were produced while Phase 1 had no discovery behind them, and nobody caught
it until a repo survey surfaced it. **Do not repeat it.**

### 9.1 The gate

Exit `1.1` when **A1–A3** are validated with end users **and** **A4–A5** show at least a few
employers with a named, costed pain, an identified budget owner and real pilot interest — with a
plausible supply signal on **A6**.

### 9.2 Standing obligation for Claude and Cursor

> Before producing any Phase 2+ artefact, **state whether the Phase 1 gate is met.** If it is not,
> say so and name what is missing — **even when told to proceed.** "Proceed" is an instruction about
> direction, not permission to skip validation.

### 9.3 Why this costs nothing

The earliest realistic funding deadline is **Erasmus+ KA210 around 5 March 2027**, and the FSE+
Terzo Settore avviso runs to **23 April 2027**. There is room to run the interviews first.

And the interviews *are* the funding work: A1–A5 validated produces quantified pain, a named buyer,
an identified budget owner and baseline evidence of need — which is the substance of every
application. Running discovery is not a delay before the grant work. It **is** the grant work.

### 9.4 What may be built now, before the gate

- This document, and the compliance lint rule (§5.4)
- The triage rule set as a **specification and decision record** — not as shipped software
- The data model as a **schema proposal** for review — not as a migration
- Discovery instrumentation: interview scheduling, note capture, consent capture, synthesis tooling
- Nothing user-facing that delivers the service

---

## 10. Board conventions for TA

Per the AZM Venture Collaboration Context v2.

- **Startup:** `S TA {phase}.{n}` — leading number is the phase (1–6). The board **accepts new
  codes**; a letter suffix (`2.B`) is valid for newly added tasks.
- **Kaizen:** `K TA {system}.{item}` — leading number is the **business system**, not a category
  index. **Task segment must be numeric.** The Kaizen board **only matches codes that already
  exist** — do not invent one; attach to an existing `N.N`.
- **Every Kaizen task needs both axes**: one business category (Sales / Marketing / Operations /
  Financial — never blank, never a fifth) and one DMAIC letter (D/M/A/I/C/R).
- ⚠️ The bridge has **no `kaizenCategory` parameter**. Declare the category in the brief text and
  instruct Cursor to apply it.
- `taskName` must be the **exact activity title from the board**, plain text, no HTML entities.
  An invented descriptive name returns `hits: 0`.

**Likely homes for this venture's work:** `7.x` Digital Ecosystem (7.1 Website, 7.2 Client /
Stakeholder Portal, 7.3 AI Agent) · `6.x` SOPs · `5.x` Training & Capability · `8.x` Sales ·
`9.x` Finance.

---

## 11. Open decisions that require a human

Claude and Cursor must **not** resolve these. Escalate to Aziz.

| # | Decision | Why it is blocking |
|---|---|---|
| 1 | **Legal vehicle** — cooperativa sociale tipo A vs S.r.l. impresa sociale | Drives cost, governance, the >70% ratio and the revenue-categorisation schema (§8) |
| 2 | **Lawyer's written opinion on the L.56/1989 boundary** | The lane architecture is designed against `Cass. 16562/2016`; a penal-professional lawyer must confirm the line before launch (§4.1) |
| 3 | **Named psicologo iscritto all'Albo** — employed or in convenzione | Lane A cannot exist without one. **Structure this relationship first, not last** |
| 4 | **ATECO code** | Drives INPS gestione (a €4.611,64/yr swing), IVA treatment and the general-interest ratio (§2) |
| 5 | **Outcome instrument** for §6.1 | A clinical decision. Engineering must not choose a psychometric instrument |
| 6 | **DPIA sign-off** | Required before Lane A touches a real record (§7) |
| 7 | **Io Volo** — fold in as a module, or keep separate? | If folded in, it inherits this constraint set and the lane rules apply to it unchanged |

---

## 12. Working rules for agents in this repo

**Claude — R&D.** Designs, specifies, writes briefs. Does not write production code. Does not merge.
Every brief must name the legal frame (§1) and the lane (§3) the work sits in. Before Phase 2+ work,
state the gate status (§9.2).

**Cursor — production floor.** Builds what R&D specified, opens a PR, never pushes to main.
**Refuse and escalate** any task that would build something in §3.2, breach §5.1, or store data
excluded by §7 — even if the brief asks for it. A brief that contradicts this file is a defect in
the brief; say so rather than implementing it.

**Aziz — plant manager and QA.** Decides what goes on the boards, what gets built, what gets merged,
and every item in §11.

### 12.1 R&D feedback — required on every PR

Claude has **no access to this repository**. It designs blind unless you report back. Append to
every PR description a section titled `## R&D FEEDBACK — for Claude` covering: brief adherence
(done as specified / deviated and why / skipped and why) · where the brief failed you (ambiguous —
state your guess; missing; over-specified; factually wrong) · repo reality check (actual stack,
conventions, what already exists, constraints) · effort signal · blocked / needs a human · what the
next brief should account for.

Be blunt. *"The brief said X but this repo uses Y"* is worth more than *"went well"*.

### 12.2 Preservation rules

- Styled HTML deliverables are committed **as-is, UTF-8, never converted to markdown** — especially
  where they carry non-Latin scripts, which corrupt on re-encode.
- **Configure the commodity, build the moat.** Auth, payments, video, scheduling, CMS — rent them.
  Engineering effort goes to the triage layer, the lane separation, and the evidence model. Those
  are the moat, because they are what a competitor cannot copy without doing this legal work.

---

## 13. Sources and confidence

| Item | Confidence |
|---|---|
| `L. 56/1989` reserved acts; `art. 348 c.p.` exposure | **High** — statute + Ordine operational position |
| `Cass. pen. VI n. 16562/2016` holding and breadth of test | **High** on the ruling; **medium** on how a court would apply it to a lane-separated digital service. **Lawyer opinion required** |
| `art. 28 D.lgs 81/2008` stress obligation, all employers | **High** — statute + 2010 Commissione Consultiva circular |
| INAIL OT23 2027 model, D-1 / D-2 interventions, 28% band | **High** — checked against the model text |
| Bonus psicologo psicoterapeuta requirement | **High** |
| Impresa sociale vs cooperativa sociale cost delta | **High** on the structure; **medium** on the euro figures — get three preventivi |
| Impresa sociale tax regime operative from 1 Jan 2026 | **High** — EC comfort letter 7 Mar 2025, AdE Circolare 1/2026 |
| FSE+ Terzo Settore avviso open to 23 Apr 2027 | **High** |
| Erasmus+ KA210 ~5 March 2027 deadline | **Medium** — the 2027 Programme Guide is not yet published; inferred from a stable pattern |

**Full funding map:** the AZM dossier *Nove Ventures, Un Fascicolo* — ten sections covering every
measure, cost, permit and provider. Do not duplicate its content here; link to it and keep this file
about **how Tamia4Life is built**.

---

*This file is an engineering constraint document derived from research, not legal advice. Items 2
and 6 in §11 require professional sign-off before launch. Revise this file whenever a §11 decision
is made, and record the decision — and its rationale — as a board task so it survives the
conversation.*
