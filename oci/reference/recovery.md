# When it goes wrong — holds, returns, rejections, travel in between, tracking

## The four states after submission
| VFS wording | What it means | Clock | What the agent does |
|---|---|---|---|
| **On hold / deficiency / additional documents required** | Consulate wants something; application is parked | **7 calendar days** from the VFS email to supply it; VFS may close at 20 days | Read the email verbatim to the user. Put the 7-day date on the calendar the same hour. Prepare the exact document named; nothing extra. Reply through the channel the email names (VFS email with reference number, or re-upload on the portal). |
| **Returned unprocessed** | Missing precondition (no VFS registration, missing uploads, wrong courier label, expired form) | None; start over | Diagnose from the return note. The VFS fee is usually lost; consular fee refunded less postage. Re-file from scratch; the online form must be refilled if > 90 days old. |
| **Rejected by the consulate** | Substantive: DOB mismatch, lineage not proven, ineligible | None | Tell the user plainly which cause. DOB mismatch cannot be fixed by affidavit; the passport must be corrected first. Lineage: get the parent's cancelled passport or OCI. |
| **Granted** | Done | — | e-OCI PDF downloadable from ociservices.gov.in a day or so after status flips. Print two copies. No card is mailed. |

## Re-uploading photo or signature after a portal rejection
- The portal lets you replace photo/signature/documents using the **file reference number** printed vertically on the left of page 1 of the submitted form, below the barcode. No new application, no new fee.
- Supporting documents can be re-uploaded the same way. Each category must be present; a missing category returns the whole thing.

## Travel to India while this is in progress
- **After surrender, before OCI:** the Indian passport is gone and there is no OCI. The user needs an **Entry (X) visa** or a regular visa to travel. Apply through VFS with the surrender certificate (or the cancelled passport) as proof of former citizenship. `visa-spouse.md` has the X-visa stack; the same checklist applies to a former citizen. Budget 1–3 weeks.
- **OCI pending, old OCI still valid (re-issue):** the original card was sent in with the re-issue; the user cannot travel on it. Plan re-issue around travel, not the other way.
- **e-OCI granted:** carry a printout; one kiosk report (2026-10) of a machine not reading the PDF.

## Tracking
- **VFS tracker:** reference number on the receipt. First update 2–3 working days after the envelope arrives. Don't call before.
- **ociservices.gov.in → Status Enquiry:** application number + passport number. Shows "Under process", "Granted". Flips before any email arrives.
- **Passport Seva (surrender):** status on mportal.passportindia.gov.in under the ARN.
- Agent rule: check every 3 working days; report only changes.

## Lost things
- Lost Indian passport, naturalized ≥ 10 years: Declaration of Renunciation route, police report + affidavit (`surrender.md`).
- Lost surrender certificate: consulate can reissue against its records if post-2020 (VFS era); CKGS-era (pre-Nov 2020) records were not kept; the cancelled passport stamp is the fallback.
- Lost naturalization certificate: USCIS N-565 replacement, months; OCI cannot be filed without it.
- Lost OCI card: OCI Misc "lost/damaged" re-issue, $100 + 3 + 19, police report required (`oci-reissue.md`).

## Refunds
- Returned before consular processing: consular fee + ICWF refunded, VFS charge and postage not.
- Rejected after processing: no refund.
- Card surcharge 3.75% is never refunded.
