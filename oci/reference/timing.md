# Timing — the clocks that disagree

Verified 2026-10-27. Compute dates from the user's actual dates; never say "soon".

## Sequential dependency
surrender → certificate in hand → fresh OCI. OCI cannot be filed in parallel. Plan OCI photos and scans during the surrender wait, but **do not fill the OCI form early** (see expiry).

## Clocks
| Clock | Length | Starts | Consequence |
|---|---|---|---|
| Surrender processing | 7–21 working days | application reaches consulate (add courier/VFS intake ~2–5 days) | certificate + cancelled passport returned |
| Surrender form age | ≤ 320 days, same calendar year | Passport Seva submission | older form = returned |
| OCI form expiry | 90 days (VFS: refill if > 70 at submission) | portal submission | expired form = returned, refill from scratch |
| OCI processing | ~8–10 weeks | VFS intake | e-OCI granted (no physical card since 8 Jul 2026); download from portal |
| On-hold deficiency | 7 days to supply; abandoned at 20–21 days | VFS deficiency email | abandoned = full restart, VFS fee lost |
| VFS status update | 48–72 business hours | delivery to VFS | don't chase before this |
| OCI passport upload | 3 months | receipt of new passport | lapse = non-compliance; travel still allowed on old number + new passport |
| OCI re-issue trigger | once, after first passport issued after age 20 | new passport | mandatory re-issue |
| US adult passport | 10 years | issue | triggers OCI upload / re-issue |
| US child passport | 5 years | issue | triggers OCI upload every time until 20 |
| Photo freshness | ≤ 6 months (some consulates ≤ 30 days for uploads) | photo taken | old photo = rejection risk |
| Utility bill as address proof | ≤ 3 months | bill date | expired = not accepted |

## Scheduling rule for the agent
Given today's date T and the surrender submission date S:
- Earliest OCI filing ≈ S + 3 to 5 weeks (certificate back).
- Fill the OCI portal form no earlier than ~5 days before the planned VFS submission; it is a 15-minute task once photos and PDFs exist.
- Everything that is not the form (photos, scans, affidavits, notarization, address proof date) is done during the surrender wait.
- For a household: list every member's passport expiry; each one is an OCI upload or re-issue event with a 3-month window after renewal.
