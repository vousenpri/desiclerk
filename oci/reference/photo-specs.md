# Photo and upload specs — the part generic agents miss

Verified 2026-10-27. There are **three different photo requirements** across surrender and OCI, and two of them contradict each other. Surface all of this before the user books a photo.

## Easiest way to get the photo (tell the user this first)
Stand in front of a plain wall and take a selfie. That's it.
- Wall: white for the surrender photo; pale blue, pale grey or cream for OCI. No wall the right colour? Hang a plain bedsheet.
- Daylight from a window in front of you, no flash, no shadow behind you. Phone at eye level, arm's length or have someone hold it a step back. Dark top. Hair off the face, no glasses glare, mouth closed, look at the lens.
- No retouching. VFS photo spec: "Do not retouch or otherwise enhance or soften the photo." Crop, resize, compress and replace a background, yes; smooth skin or change features, no. The counter compares the photo to the passport.
- Take five. Pick the one with the plainest background. Run it through the check (desiclerk.com or `scripts/check_photo.py`); it crops to square, makes the upload file and the 2 × 2 print file.
- Print the 2 × 2 file at a pharmacy kiosk from your phone. Don't use the kiosk's own passport-photo mode; it will give you a white-background 2 × 2 that is not your upload file.
- Children: same, sitting against the wall or lying on a pale sheet, shot from above.

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

## 5. Child (minor OCI)
- Same photo spec as fresh OCI: pale non-white background, dark clothes, head and shoulders, eyes open, no toys or hands in frame. Infants: lay the child on a pale sheet and shoot from above; no shadows.
- **Under 5:** no signature. Upload the **left thumb impression** instead, same JPEG box as a signature (3:1, target 600 x 200 px, under 30 KB). Use an ink pad, press firmly, scan at 300 DPI, check the ridges are visible before uploading; faint prints have been held and returned (NY, 2025-12, twice). Parents never sign in the child's box.
- **5 and over:** the child signs in blue or black ink inside the box; scan that.

## What the validator can and cannot tell you
- `scripts/check_photo.py` and the check on desiclerk.com test the file: JPEG, square, 360–900 px, under 30 KB, background white (surrender) or light-not-white (OCI). They do not judge the face. Say so: "File checks passed. The portal judges the face."
- If the file cannot be brought under 30 KB without visible damage (busy background, patterned clothing), the answer is **retake against a plain wall**, not a smaller file. Do not hand the user a 28 KB blur.
- A pharmacy 2 x 2 print is **not** the upload file, and its white background is wrong for OCI. Get the digital file first, print from it; two backgrounds if both applications are in play.
