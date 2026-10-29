# Desi Clerk

Your agent knows the rules. Desi Clerk knows the counter.

Indian passport surrender and first OCI, for yourself and your US-born child, from the USA via VFS Global. Free. No accounts, no document uploads.

- **index.html** — the page: what to bring, in order, with a browser-side photo check and the clocks. Live at desiclerk.com.
- **oci/** — the loop-engineered skill for your agent (Claude, Duet, Dot, Muse). `SKILL.md` is the method; `reference/` holds checklists verified against VFS and consulate pages, with dates; `scripts/check_photo.py` validates a photo against both VFS upload specs.

## Hand it to your agent

> Load the India consular skill from the oci folder at github.com/vousenpri/desiclerk and prepare my VFS applications: surrender, OCI for me, OCI for my child. Tell me the preconditions before any form, then tell me whether to mail it or walk in at my centre, check VFS appointment availability if walk-in, pick a slot that fits my calendar, and put the deadlines on it.

Your passport scans stay with your agent. Desi Clerk never receives them.

## Send a desk note

Something a VFS desk asked for that isn't on the checklist? Open an issue with the centre, the date, the application, and what happened. Dated, attributed observations go in `oci/reference/gotchas.md`; single reports stay leads until repeated.

## Sources

Every fact carries the page it came from and the date it was read. Rules change. The receipt in your hand beats this repo.

Seek less. Do more.
