# OCI maintenance — re-issue vs upload-only

## Rule change — read this first (CGI Chicago, page updated 27 Oct 2026)
https://www.cgichicago.gov.in/page/oci-card-updation-reissuance-of-oci-cards-discontinued/ (read 2026-10-30):
- "The provision for reissuance of Physical OCI Cards has been discontinued."
- "The earlier requirement of mandatory OCI Card reissuance upon issuance of a new passport is no longer applicable."
- After every new passport, any age: **update passport particulars on the OCI portal within 3 months**. Online, free, no documents to VFS, no visit.
- **Late (after 3 months): $25 consular + $3 ICWF + $19 VFS**, paid through VFS. (CGI San Francisco advisory 2026-06-16 says the same.)
- The update needs a photo **taken within the last 30 days**.
**Sources disagree:** the VFS one-pager and the Embassy page (indianembassyusa.gov.in/pages/NjI) still carry the old "re-issue after the first passport after 20 / upload under 20 and once after 50" text. Follow Chicago: it is newer, cheaper, and the portal is the same for every mission. Tell the user both exist. Re-check quarterly.

Verified 2026-10-27 against Indian Embassy USA, CGI San Francisco, CGI Milan, HCI Kuala Lumpur pages (all citing the 2021 MHA revision).

## Re-issue of the card is required (OCI Misc Services via VFS)
- **Once**, when a new passport is issued after completing age 20 (to capture adult facial features).
- Change of name, father's name, or nationality (not to Pakistan/Bangladesh).
- Lost or damaged card.
- Errors on the card.

Fee: $25 + $3 ICWF + $19 VFS (lost/damaged: $100 + 3 + 19). Card +3.75%.

## Upload only, no new card, free (ociservices.gov.in → OCI Miscellaneous Services)
- Each time a new passport is issued **before age 20**.
- **Once** after completing age 50 on the next new passport.
- Foreign spouse of an Indian citizen or of an OCI holder: **every** new passport, plus a declaration that the marriage subsists and copies of the Indian spouse's passport / the OCI spouse's passport and card.
- Upload: new passport bio page + recent photo (some consulates: ≤ 30 days old). Within **3 months** of receiving the new passport. Auto-acknowledgement email; details updated in records in ~5 weeks; no new card.
- Between 20 and 50 with no name change: **upload the new passport and a photo within 3 months** (free, portal only, no visit). CGI Chicago (27 Oct 2026) and CGI San Francisco say uploads apply each time a new passport is issued, irrespective of age; the Embassy page NjI and the older MHA wording (under 20 / once after 50) are superseded. Late upload costs $47. Travel on the existing OCI + new passport meanwhile.

## Drift to watch
- CGI San Francisco and the Embassy both now read the upload rule as "each time a new passport is issued", no age limits. Older MHA text said under 20 / once after 50. Rule for the agent: **upload every time**, within 3 months.
- Travel: allowed on the existing OCI card bearing the old passport number as long as the new passport is carried, including during the upload window.
- An OCI holder who joins foreign military or police must renounce the OCI.

## Household triggers
For each family member record: date of birth, current passport issue/expiry, OCI card number and the passport number printed on it, last upload/re-issue date. The event list is then derivable:
- Child's passport renewed (every 5 years) → upload, 3-month window.
- Child turns 20 → next passport → mandatory re-issue.
- Adult passport renewed, age 20–49 → upload within 3 months (re-issue only if the name changed).
- Adult passport renewed, age 50+ → upload once.
- Foreign spouse passport renewed → upload every time, with marriage declaration.
