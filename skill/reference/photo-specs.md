# Photo and upload specs — the part generic agents miss

Verified 2026-10-27. There are **three different photo requirements** across surrender and OCI, and two of them contradict each other. Surface all of this before the user books a photo.

## 1. Surrender / renunciation — physical print
- 2 copies, 2 x 2 inch, colour, front pose, **white background only**, photographic paper, under 6 months old.
- Source: VFS adult with-passport checklist (2026-10-20).

## 2. Fresh OCI — physical print (affixed to the printed form)
- 2 copies, 2 x 2 inch (≥ 51 x 51 mm), colour, square, 80% face coverage, head and shoulders, full face centred, **plain light-coloured background, NOT white**, no border, no signature on it, not stapled.
- Source: Government of India instructions in the VFS "New OCI – Adult – Foreign National by Naturalization" checklist.
- The VFS one-pager says "white / plain light (pale) background with dark-coloured dress". Conflict. Recommend the stricter government version: **pale (light blue or light grey) background, dark clothing**. A CVS/Walgreens white-background passport photo risks rejection for OCI.
- The physical print and the uploaded digital photo must be **identical**.

## 3. Fresh OCI / OCI Misc — digital upload (ociservices.gov.in)
Two specs appear on VFS's own site in the same folder:

| | Spec A (Govt instructions, most checklists) | Spec B (one VFS checklist PDF) |
|---|---|---|
| Format | JPEG/JPG | JPEG/JPG |
| Max size | 500 KB | **30 KB** |
| Dimensions | square, 200–1500 px | square, **360–900 px** |

A file at **600 x 600 px, JPEG, under 30 KB** satisfies both. Target that. The portal's own validator is authoritative; if it rejects, re-export smaller.

### Signature upload
- JPEG/JPG, aspect ratio 3:1 (width:height). Spec A: 200x67 to 1500x500 px, ≤ 500 KB. Spec B: 360x120 to 900x300 px, ≤ 30 KB. Target **600 x 200 px, under 30 KB**.
- Must match the signature on the printed form and on the passport. Blue or black ink. Inside the box.

### Supporting documents upload
- PDF only, one file per category (7 categories), max 500 KB each (some pages say 1000 KB; assume 500).
- A4 colour scan at 100 DPI ≈ 200–250 KB per page.
- All documents must be uploaded or the application is returned unprocessed.

## 4. OCI passport upload (Misc Services, after a new passport)
- Recent photo (some consulates: not older than 30 days) + new passport bio page.
- Same JPEG specs as above; documents as PDF. Max document size cited as 500 KB.

## Practical order of operations
1. Decide which applications are in play. If both surrender and OCI: **two photo sessions or one session with two backgrounds**. Tell the user before they go anywhere.
2. Get the digital file first; derive the print from it (so print and upload are identical).
3. Run `scripts/check_photo.py` on the file. It emits `*_upload.jpg` (600px, ≤30 KB) and `*_print_2x2.jpg` (600px at 300 DPI = 2 inches).
4. Print the 2x2 on photographic paper (a pharmacy will print from a file).
