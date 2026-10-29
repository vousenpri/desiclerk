# Gotchas — observed, dated, attributed

This file is the ground truth no page has. Append after every real visit or portal session. Format: date, centre, application, what happened, fix.

## 2026-10-27 · Edison VFS · Passport surrender (walk-in)
1. **Passport Seva printout had no photo.** The mportal.passportindia.gov.in PDF loads the photo lazily and does not render it in Chrome; printing before it renders gives a blank photo box. Applicant had to log into a public VFS computer with the full application to reprint. **Fix:** open the PDF in Safari or Firefox, wait until the photo is visibly rendered, then print. Better: download the PDF and open it in Preview/Acrobat before printing. Agent must say this before the user prints, not after.
2. **Notarized personal-appearance / signature-change affidavit was not required at Edison.** A generic agent told the applicant to get one, citing the New York consulate's practice. Edison did not ask for it. It is not on the national VFS checklist either. **Fix:** key condition-based affidavits to the centre; if unknown for a centre, say so and list it as "possibly asked at NY centre, not on VFS checklist" rather than as required.
3. **Photo requirement surfaced only at the last minute**, causing a rush to CVS. **Fix:** photo specs are step zero.
4. **CVS 2x2 print is not the upload file**, and its white background is wrong for OCI (which wants light, non-white). **Fix:** get the digital file first, derive the print from it, two backgrounds if both applications are in play. See `photo-specs.md`.

## Standing (from VFS/consulate pages, not yet desk-verified)
- Fee is $40 + $3 + $19 = $62 regardless of naturalization date; secondary sites still quote a pre/post-2010 split. Trust the live one-pager or the receipt.
- The "Declaration of Renunciation" (no-passport route) is only issued if 10 years have passed since naturalization.
- The two VFS OCI checklists in the same folder give different upload limits (500 KB/200–1500 px vs 30 KB/360–900 px). Make a file that satisfies both.
- Government OCI photo text says background "not white"; the VFS one-pager says "white / pale". Go pale.

## Standing (from pages, not desk-verified) — added 2026-10-27, minor / re-issue / spouse / X-visa
- **No physical OCI card since 8 July 2026.** New grants are e-OCI only, downloaded from ociservices.gov.in at "Granted" (CGI Chicago notice 2026-07-09; VFS checklists say "effective 1 July"). Existing booklets stay valid. Anyone planning around a card in the mail is planning around nothing.
- **Re-issue means surrendering the original OCI card** with the application (VFS Adult re-issue checklist, item 4). No travel to India on it until the e-OCI appears. Whether VFS returns the cancelled booklet is UNVERIFIED.
- **Foreign-spouse OCI: 2-year registered marriage** is a hard bar (one-pager + the VFS Sworn Affidavit text "married 2 years prior to the date of submission"). Under two years → Entry (X) visa.
- **Foreign-spouse OCI: in-person interview of both spouses.** CGI Chicago states it; NY has done it by email summons (lead). Not on any VFS checklist. Quote as "confirmed Chicago, likely elsewhere", not as a VFS requirement. Scheduling emails have gone to spam.
- **Spouse's name must appear on the Indian/OCI spouse's passport or OCI card** before the foreign spouse applies; otherwise that document is re-issued first (VFS spouse checklist). Commonest multi-month hold.
- **VFS joint marriage affidavit adds "return the card on death of either spouse"**; the statute (s.7D(f)) only covers divorce and remarriage. Advise the stricter affidavit reading.
- **Passport-validity minimums differ by checklist:** fresh adult 6 months, re-issue 6, minor fresh 9, spouse fresh 9 (Sep 2026; the older spouse PDF said 6). Photo age: 6 months everywhere except the Sep 2026 spouse PDF (9). Use 9-month passport validity and ≤ 6-month photo to satisfy all.
- **Apostille is required on US-issued birth and marriage certificates for OCI.** Sep 2026 VFS minor checklist, verbatim: born outside India → birth certificate "must either be apostilled by the relevant foreign government or attested by the appropriate foreign mission"; marriage certificate "issued outside India… must be apostilled or attested." Submit self-attested copies; originals of apostilled documents are refused. Registrar-issued only; religious certificates refused. The X-visa checklist does not ask for the apostille. (Re-verified 2026-10-28; an earlier page draft wrongly said the apostille was not needed.)
- **Minor birth certificate:** state/county long form naming both parents with DOB and nationality; hospital certificates refused. Mother's maiden vs married name is the classic "parents' names not matching" rejection (#5).
- **Minor signature rule:** under 5 → left thumb impression uploaded; 5+ → own ink signature. Parents sign Part B and the notarized Parental Authorization (both, unless sole custody order / death certificate / single-parent adoption), never the applicant's box.
- **Voter-ID / ration-card surrender undertaking** is a separate VFS form. Required on re-issue and for the Indian-origin spouse per the checklists; **also held for on fresh adult OCI** (immihelp report, 2025-06: hold reason "Undertaking for Surrender of Indian Voter Card and Ration Card: IS REQUIRED"). Sign it on every former-Indian-citizen application.
- **Embassy pages still print the VFS charge as $15.90** (OCI reissue page, NY visa fee chart). One-pager says $19. Go with the one-pager / receipt.
- **Entry (X) visa fee for US nationals** is on the Washington embassy chart only ($100 / $140 / $220 by validity); the VFS one-pager carries no amounts for this category and the $19 VFS charge is stated only in the Emergency-visa table. Confirm from the VFS payment confirmation.
- **X visa: Additional Particulars form (Annexure A) is mandatory even for minors**; the application is held without it. Original passport is submitted; white-background photo (opposite of OCI).
- **Upload size drift:** 2025–26 VFS checklists say 1000 KB per document; older Govt text 500 KB. Target ≤ 500.
- **Incomplete-application clocks (one-pager):** 20 calendar days to complete or returned (consular + ICWF refunded, less postage); 7 calendar days to answer a consulate request or processing may stop, no refund.

## From forum reports (immihelp / VisaJourney / Blind), collected 2026-10-28 — leads promoted to gotchas
- **Houston, surrender, 2026-04:** rejected for "present address is not correct"; VFS wants the US address as present address even though Passport Seva prompts for an Indian one. Reported as common.
- **Surrender fillable PDF truncates fields** (multiple reports). VFS phone line: retype in Word, sign in blue ink, one form per applicant, leave minors section blank on an adult's.
- **Name variation at naturalization (dropped middle name)** is the most repeated surrender blocker (Houston, SF, NY). A notarized one-and-the-same-person affidavit cleared it each time.
- **Minor OCI parental authorization: e-notary / e-signature refused** (Atlanta 2025-01, Chicago 2024-09, 2026-01). Wet-ink notary only.
- **Infant thumbprint held for clarity** (NY, 2025-12, 3-month-old, twice; returned by consulate). No resolution path reported. Advise ink pad, 300 dpi scan, check legibility before upload.
- **VFS paid scanning service uploaded only page 1 of each passport** (2025-02). Do your own scans.
- **e-OCI in practice (2026-07, SF):** portal shows Granted a day before the PDF is downloadable; approval visible on the portal before any email. One second-hand report (2026-10) of an Air India kiosk not reading the e-OCI; carry a printout.
- **Observed timings, 2026:** adult OCI roughly 4 (SF), 6 (NY), 8 (Chicago), 7–12 (Houston) weeks; Seattle 59 days; surrender ~3 weeks door to door.
- **No 2025–26 report of a NY appearance / signature-change affidavit being demanded.** Edison non-requirement stands unchallenged.
Full attributed list: `leads-reddit.md`. Reddit itself was unreachable from the research session; these are from other forums.
- **NYC long-form birth certificate:** VitalChek is the only authorized vendor; the long form with letter of exemplification is issued only when the request reason is "Apostille/Authentication" (online, mail form page 4, or in person at 45 Lafayette St, Room 133, by appointment). The apostille IS needed for OCI (see above). $15 + vendor fee; County Clerk $3; Dept of State $10. (nyc.gov DOH birth records page, read 2026-10-28.)
