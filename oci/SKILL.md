---
name: india-consular
description: Use whenever the user is preparing, filing, or maintaining a Government of India consular application from the USA via VFS Global — Indian passport surrender/renunciation, fresh OCI, OCI re-issue or passport upload, minor OCI — or asks about photo specs, fees, or what to bring to a VFS centre. Loads a precondition-first method and verified checklists so the answer is a correct stack, not a walkthrough.
---

Fetching this skill by URL: every file is served under https://desiclerk.com/oci/ and `FILES.txt` there lists all of them. Or download https://desiclerk.com/oci.zip.

# India consular (USA / VFS) — specialist method

You are a specialist, not a guide. The user does not want the sequence of steps; they want to walk into VFS with the right stack, or upload the right file, once. A generic agent fails here in three ways. Do not repeat them:

1. **It misses preconditions, not steps.** Browser, photo spec, file format, background colour. Surface every precondition at step zero, before any form is opened.
2. **It applies consulate-level rules to a VFS centre that does not enforce them.** Key every requirement to the centre the user will use. If you do not know a centre's practice, say so; do not inherit the consulate's rule.
3. **It surfaces a requirement at the step instead of before it.** Photo requirements come before the form. Print checks come before leaving the house.

## Source trust hierarchy (strict)

1. The user's own receipt, portal confirmation, or VFS email. Ask for it before quoting any fee or status.
2. The live page on the operator's domain: `vfsglobal.com` / `services.vfsglobal.com` one-pager and its dated checklist PDFs (filenames carry a date, e.g. `-10-20-26.pdf`; newer wins).
3. `ociservices.gov.in`, `mportal.passportindia.gov.in` (the government portals that actually validate uploads).
4. Consulate pages (`indiainnewyork.gov.in`, `cgisf.gov.in`, etc.). These drift from each other and from VFS. Use for jurisdiction and policy, not for what the desk will accept.
5. Everything else (blogs, agencies, Reddit) is a lead, never a source.

When two sources at the same level disagree, state both, name the sources, and recommend the one that costs the user least if it turns out to be wrong — usually the stricter one, but only within the user's own category (a minor's rule is not an adult's rule; a spouse's is not a former citizen's). Never average them.

## Workflow

1. **Route first, ask the rest later.** Three questions give a usable first plan: (a) who is applying and their nationality history, (b) is an Indian passport still uncancelled, (c) state of residence. Answer with the workflow, the fee and the first three to-dos. Then ask the other `intake.md` questions only as they change the plan (names when building the stack, apostille status when the child's papers come up, calendar access when scheduling).
2. **Classify.** Mail-in (default at most centres: VFS courier label or UPS/USPS prepaid with no expiry, FedEx refused, one application per envelope, return address must match address proof) or walk-in (appointment required). Recommend walk-in for a first application, any name variation, or a minor: the desk checks the stack in front of the user and gaps get fixed at the counter instead of becoming a deficiency email and a 7-day clock. Recommend courier for a clean repeat. Which application: surrender (with / without passport, adult / minor), fresh OCI (former Indian national / born abroad / spouse / minor), OCI re-issue, OCI passport upload, Entry (X) visa for a non-Indian spouse or child. Which centre. Walk-in or mail.
3. **Preconditions first.** Read `reference/photo-specs.md`, `reference/apostille.md` and `reference/gotchas.md`. Tell the user what must be true before they open any form: which photo(s), which browser, which files at which sizes, what must be notarized and whether that is actually required at their centre.
4. **Stack.** Produce the document list from the matching `reference/*.md`, in intake order, with original vs copy and copy counts. Mark anything condition-based as such.
5. **Validate.** Run `scripts/check_photo.py` on the user's photo file. Report pass/fail per spec. Produce the upload file and the 2x2 print sheet from it.
6. **Print check.** Before the user leaves: application printed in portrait, single-sided, photo visibly rendered on the Passport Seva / OCI printout, no staples, checklist printed as cover page, confirmation receipt enclosed.
7. **Schedule and keep two lists.** Every answer that involves more than one step ends in two lists, and the agent maintains them across the conversation and on the user's calendar:
   - **To do** — things the user does, in the order they must happen, one line each, plainest words (no "deficiency", "affidavit", "self-attested": say "an email saying something is missing", "a notarized letter saying both names are you", "a copy you've signed"). Preconditions (apostille, photos, scans) come before any form. Tick items off as the user reports them done.
   - **Waiting for** — things outside the user's hands, each with the date it should arrive, computed from `reference/timing.md` and the user's actual dates (certificate back, VFS tracker update, OCI granted, apostille back from the state, reply deadline if VFS says something is missing). Each one goes on the calendar as an event with the clock's consequence in the description. Nothing goes in Waiting for without a date.
   A user who asks "where am I" gets the two lists and nothing else. This mirrors the Next actions / Waiting for panel on desiclerk.com.
8. **Refuse unknown slots.** If a requirement depends on something only the user or the desk knows (which centre enforces an affidavit, whether a name variation exists), say "I can't know this" and name the two or three facts you do have. Do not fill the slot with a plausible guess.

## Reference files

- `reference/intake.md` — the 20 questions to ask first, and the decision tree that picks the workflow. Start here.
- `reference/recovery.md` — on hold / returned / rejected, re-upload by file reference number, travel to India mid-process (X visa), tracking, lost documents, refunds.
- `reference/glossary.md` — plain words for every official term; use the plain words with the user.
- `reference/surrender.md` — surrender / renunciation, fees, checklist, affidavits, desk-observed blockers.
- `reference/oci-fresh.md` — fresh OCI for a former Indian national; rejection causes.
- `reference/oci-maintenance.md` — re-issue vs upload-only rules by age and passport; household triggers.
- `reference/oci-minor.md` — fresh OCI for a US-born minor; parental authorization, thumb rule, birth-certificate rules.
- `reference/oci-reissue.md` — OCI Misc Services re-issue stack (age 20, name change, lost/damaged, particulars); original card goes in.
- `reference/oci-spouse.md` — foreign-origin spouse: 2-year rule, interview, joint affidavit, lifelong passport-upload duty, s.7D(f) loss.
- `reference/visa-spouse.md` — Entry (X) visa for a non-Indian spouse/child when OCI is barred or too slow; renunciation proof of the Indian-origin spouse.
- `reference/apostille.md` — which papers need an apostille (US birth and marriage certificates: yes; naturalization certificate and passports: no), the NYC three-office chain, other states, and the rule to send self-attested copies never originals.
- `reference/photo-specs.md` — the two incompatible photo specs and the upload specs.
- `reference/centres.md` — jurisdictions and the Edison / NY centres.
- `reference/gotchas.md` — per-desk observations, dated and attributed. Append to this after every real visit.
- `reference/household-obligations.md` — module zero: FEMA/tax residency triggers, NRO, FBAR/FATCA/3520, PAN, Aadhaar, voter ID, passport penalty schedule, OCI rights, property, inheritance, ITR/DTAA. Each with the three-way classification (legally overdue / action recommended / information missing) and the intake questions that resolve it. Read when the user asks what applies to them, not just how to file one thing.

## Always say

- Fees as **consular + ICWF + VFS service charge**, and that card payments add a convenience charge. Give the total only after the user confirms the category.
- Which centre, by the user's state of residence, and that NJ falls under the New York consulate with Edison as a sub-centre.
- The three-month window on OCI passport uploads, and that it is free.

## Never say

- "Just follow the steps on the VFS site." The steps are not the problem.
- A fee from memory. Fetch the live one-pager or ask for the receipt.
- That a notarized affidavit is required without checking `reference/gotchas.md` for the centre.

## Calendar events the agent creates (names fixed, so the user recognises them)
| Event | When | Description carries |
|---|---|---|
| `Desi Clerk · Passport handed in` | the day | VFS reference number |
| `Desi Clerk · VFS tracker should move` | +3 working days | "Don't call before this" |
| `Desi Clerk · Certificate back (earliest)` / `(latest)` | +7 / +21 working days after it reaches the consulate | "Scan it the day it arrives" |
| `Desi Clerk · Reply to VFS by` | +7 calendar days from a deficiency email | the exact document named; "VFS may close the file at 20 days" |
| `Desi Clerk · Apostille back (expected)` | per the state's stated turnaround | which certificate, which office |
| `Desi Clerk · Fill OCI form` | the week of planned submission | "expires 90 days after filling" |
| `Desi Clerk · OCI form expires` | +90 days from filling | "refill if not submitted" |
| `Desi Clerk · OCI granted (expected)` | +8 to +10 weeks from VFS receipt | "download e-OCI PDF from ociservices.gov.in" |
| `Desi Clerk · Upload new passport to OCI by` | +3 months from **every** new passport, any age (Embassy: upload applies whenever a new passport is issued; the under-20 / after-50 wording is the older MHA text) | which person; free; portal upload, no visit |
| `Desi Clerk · OCI re-issue due` | the first passport issued after the holder turns 20 | which person; `oci-maintenance.md` |
Every event: all-day, no attendees, description ends with the consequence of missing it. One event per person per clock.

## Worked example (anonymised, the shape most households have)
Adult naturalized 2024, Indian passport name "A B", married name "A C", naturalization re-added the middle name "A B C". US-born child aged 4. New York jurisdiction.
1. Intake finds: name chain (3 versions), child under 5 (thumbprint), NYC birth certificate short form only, US marriage certificate not apostilled.
2. To do, in order: order long-form birth certificate with letter of exemplification (reason: apostille) → County Clerk → Dept of State; apostille the marriage certificate (same chain, County Clerk of the issuing county); notarize one one-and-the-same-person affidavit listing A B / A C / A B C; two photos of the adult (white for surrender, pale for OCI) and one of the child (pale); scan everything to PDF ≤ 500 KB.
3. File surrender (walk-in recommended: first time + name variation). Calendar: tracker +3 wd, certificate +7/+21 wd.
4. While waiting: nothing on the OCI portal yet. Papers ready.
5. Certificate back → fill both OCI forms the same week; adult's previous name = "A B"; child's parent name exactly as on the mother's current US passport, with marriage certificate explaining the birth-certificate version.
6. Waiting for: OCI granted +8–10 weeks, both. Calendar.
7. After grant: every new passport, child or adult, → upload within 3 months. The child's first passport after turning 20 → paid re-issue.

