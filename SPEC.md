# Viral Chat Video: production spec (canonical)

This file is the single source of truth for CoupleIn's "viral chat video" format.
**Any new session (any Claude chat, any model) must read this whole file before doing any work on these videos.**
Chat is where decisions get made; this repo is where they live. When a decision changes, update this file in the same session.

Owner: Chuby (CoupleIn founder). Last consolidated: 28 Sep 2026.

---

## 1. What the format is

A 1080×1920 (9:16) video of about 25–30 seconds for TikTok and Instagram Reels, in four parts:

1. **DM fight (≈8–14s).** A fake Instagram dark-mode DM chat that reads as cheating or betrayal within the first two messages. A big caption (the hook) sits at the top the whole time.
2. **App footage (≈5–8s).** A real CoupleIn screen recording showing the evidence the angry person finds, or what they do in the app. It never shows the twist. A caption sits over it.
3. **Twist (≈6–9s).** Back to the same DM thread ("then she/he sent this…"). The reveal is harmless and absurd, and it breaks one detail planted in the fight (e.g. "he's 6'2" … it's the cat).
4. **End card (2.6s).** "CoupleIn" + a feature line + "Free on iOS & Android" + the fixed closer **"7 days. Uninstall if nothing changes."**

Inspiration: a Soultie app video that got 624K views on a 668-follower account with a DM rage-bait → app → twist structure (the twist was a puppy).

## 2. The quality bar (non-negotiable, set by the owner)

- Only "10 out of 10" ideas get made. **10/10 is judged on downloads, engagement, conversion and relatability**, not just compared with previous posts.
- Self-check every script and every rendered video **before** the owner sees it. Cut weak ideas; don't pad.
- **Do everything you're capable of yourself.** Only ask the owner to do something when you are certain you cannot do it.
- Every script must pass all four checks:
  1. **Betrayal in two messages:** the first two messages of the fight read as real cheating or betrayal.
  2. **Unguessable twist:** a viewer can't predict the reveal from the fight or the footage.
  3. **Comment bait:** a planted detail the twist breaks (the comments argue about it), or a known polarising couple debate (hall pass, work husband, checking phones, mum with a key, splitting the bill…).
  4. **The clip makes sense at that moment:** it shows what the angry person finds or does, filmed on their login, and **never gives the twist away**.
- Style rules: UK English and UK references (Greggs, Premium Bonds, Tesco yellow stickers, Premier Inn). Use "him"/"her", never "them" for one person. No real people's faces, names used as likeness, or brands implying endorsement in footage. Vary names across videos (don't reuse "Jess" as every ex).
- Gender mix: roughly 60/40 "he's raging" / "she's raging" (currently 34/26 across the 60).

## 3. The scripts

- `scenarios.json` is canonical (108 scripts, V01–V108). **Only the 60 with `"top": true` meet the bar**: that's one month at 2 a day. The other 48 are weaker drafts kept for reference. Never post them.
- The top 60: V01 V03 V09 V14 V19 V22 V24 V25 V33 V34 V43 V44 V61–V108.
- The fields are id, feature (B Brownies, C Calendar, M Mood, R Resolve, S Score), pov (`him` means Jay is angry, `her` means Ella is angry), hook, fight, clip, in_app, overlay (the captions over the footage), twist, bait, photo, top.
- In fight and twist, `me` is the angry person (right-hand, sent, purple→blue bubbles) and `them` is the partner (left, grey). `[PHOTO]` is a photo message, and `[screenshot] …` becomes a drawn image or plain text.
- `scenarios_source_*.py` are the original generators. They're historical only, because later fixes were made directly in the JSON.
- `index.html` is a filterable page of all scripts (opens on the top 60).

## 4. What the DM screen looks like (Instagram dark mode)

These are implemented in `render.py`:
- Black background. Incoming bubbles are #262626 with white text. Sent bubbles use the IG gradient, purple (163,57,235) → (110,72,245) → blue (55,151,240), coloured by screen position.
- Font: Liberation Sans (Helvetica/SF look), size 45 in bubbles. Rounded bubbles. The partner's small default avatar sits beside the last bubble of each incoming group.
- Header: 9:41 status bar, back chevron, default avatar, contact name (`ella 🤍` when Jay is angry, `jay 🤍` when Ella is angry), "Active now", phone and video icons.
- **The keyboard is always up** (iOS dark keyboard) with the IG message bar above it (blue camera circle, "Message...", mic/gallery/sticker icons).
- **Sent messages are typed live:** letters appear in the bar at about 14 characters per second, the pressed key lights up, "Send" shows in blue, then the bubble pops in. Key-click sounds play.
- The partner's messages show the "…" typing indicator first.
- **Emoji-only messages** (≤3 emoji) render large with no bubble, like real IG.
- Special message types: `[SYS]text` (small grey centred system line, e.g. "Seen", "You unsent a message", "Reacted 😂 to your message"), `[VOICE]0:03` (voice-note bubble), `[REEL]` (shared-reel card), `[PHOTO:path]`.
- **Awkward opener:** before the fight, the chat already shows yesterday's awkward ending: a `Yesterday 23:47` stamp, the opener lines, then a `Today 14:12` stamp, then the fight. There are 30 openers (in `build.py` `OPENERS`), chosen as comment bait on their own (milk before teabag, socks in bed, hot dog = sandwich, "love you" → 👍, 3-second voice note…). Each is used twice across the 60, about 30 videos apart. Check that an opener never clashes with or spoils its video's twist.
- Hook caption: Poppins Bold 62, white with a black stroke, centred at y≈290, present for the whole fight section. Frame 0 must show the hook and the opener (the scroll-stop).
- Pacing: reading time per message is 0.5s + 0.025s per character of the previous message, plus typing time for sent messages. The owner said the first version "moved too fast"; this pacing was approved.

## 5. Footage section

- Cover-cropped to 1080×1920 and played at 1.15× speed.
- **How long the app is shown is never a fixed time. It always matches how long the on-screen text takes to read (owner's rule, 4 Oct).** `build.py` gives each caption `0.4s + words/4 per s + 0.3s` (min 1.5s). The last caption also gets the on-screen evidence (`in_app` words/4 per s, min 2.0s). The footage is never cut shorter than that total: if the clip runs out, its last frame is held (`pad`). If the clip is longer, it plays up to 8.5s (or the reading total if that's longer) so the evidence isn't cut off.
- Captions (`overlay`) are timed by that reading need (not split evenly), Poppins Bold 62–80 with stroke, at y≈1250.
- `postprocess/postprocess.py` (section 13) then sets every still shot to exactly its reading time from the real on-screen text: too long gets trimmed, too short gets held longer.
- Sound effects: message pops (in/out), a whoosh at section changes and key clicks. **No music is baked in.** The owner adds a trending sound when posting, and Metricool can attach IG catalogue audio or TikTok auto-music.

## 6. End card lines (by feature)

- B: "Stop guessing. It's on her/his list."
- C: "Never forget. Ever."
- M: "Know how she/he feels before you ask."
- R: "Fight fair. Fix it faster."
- S: "Keep score of the love, not the fights."

Always followed by "Free on iOS & Android" and **"7 days. Uninstall if nothing changes."**

## 7. How the CoupleIn app actually works (facts learned; don't assume otherwise)

- **Brownies (wishlist/points):** each person adds what THEY want to their own wishlist ("My wishlist"). The partner sees it on the partner tab and taps **"I did this"**; the owner confirms with "Mark done". "Nudge" reminds. The header shows "You 67 ⭐ vs Partner 333 ⭐". **Nothing opens**: items are rows, so "hold" means stop scrolling with the row centred.
- **Resolve:** guides an argument step by step. The listener has to **repeat back** what they heard before responding, and a TIME LEFT timer and a Next step button are shown. **There is no text input.** Clips show moments from a session (start, speaking step, repeat-back with timer, next step).
- **Calendar:** shared. Events have a title and time, and possibly notes and repeats (unconfirmed; if missing, put the note at the end of the title).
- **Mood:** partner's mood is visible. The exact mood list is unconfirmed; the scripts need In love, Betrayed, Guilty and Annoyed. If any is missing, rewrite V33/V34/V61/V65 around the real options.
- Trial is 7 days. Brand pink is #FF6B9D.
- Mistakes made before, which must not be repeated: assuming Resolve had typing; assuming wishlist items "open"; putting many events on the same day (the day list then shows other videos' evidence); using daily/weekly repeats (they clutter every day). **Every calendar event gets its own date and does not repeat.**

## 8. Filming (what the owner records)

Full step-by-step guide: `CoupleIn_filming_guide.docx` (rebuild with `python3 plan.py && node make.js`).
- A demo couple, **Jay and Ella**, with plain avatars and no real photos. (The first test recording used celebrity avatars, Diddy and 50 Cent, and must never be used in posts.)
- **Film on the angry person's login.** Exceptions: V44 and V106 are filmed on Jay's login because they show what Jay did.
- Routine: "hold" means finger off the screen and count to 5. For Calendar and Resolve, go back and count to 2 between items. Tap actions: finger off and count to 3 after.
- 11 recordings plus 2 photos (cat for V01, sausage roll for V33):
  - J1 Brownies (Ella's wishlist) · J2 Calendar (Ella's events + Jay's Lads' night + the wedding move) · J3a–d Mood (Ella sets each mood, Jay films) · J4 one full Resolve session on Jay's login (covers 12 videos) · E1 Ella's own wishlist (the ring) · E2 Calendar (Jay's events + Netflix event added live) · E3 one full Resolve session on Ella's login (covers 8 videos).
- The owner sends them in the chat with the codes in the same order ("J1, J2, J3a…"). Chat limits: 500MB per file, 20 files per chat.
- Clip identification: sample frames, find the still "holds", read the on-screen text (event titles, item names) and cross-check against the guide order. If they disagree, flag the clip; don't guess.

## 9. Building

```
python3 build.py V03 V14 ... --footage FOOTAGE_DIR [--photos PHOTO_DIR] --out out
```
- FOOTAGE_DIR holds per-video clips named `V##.mp4` (cut from the long recordings), or clip-code files (`B-MARK.mp4`, `C-EVENT.mp4`, `M-VIEW.mp4`, `R-FLOW.mp4`…) as fallbacks. Photos go in `PHOTO_DIR/V##.jpg`.
- Output: `out/V##.mp4` (kept under 19MB) plus `out/captions.json` (post captions: hook, "whose side are you on? 👇", hashtags).
- Needs ffmpeg, Python with Pillow and numpy, and the fonts Poppins (`/usr/share/fonts/truetype/google-fonts/`), Liberation Sans and Noto Color Emoji.
- About 75s per video to render.
- **QC every video before showing it:** frame 0 shows the hook and the opener; there's no clipped or overlapping text; the footage matches the caption; the photo is present if needed; no real faces; the file is under 19MB.
- **Then always run the post-processing step (section 13)** on the build output before QC/preview/posting:
  `python3 postprocess/postprocess.py out final V03 V14 ...` → `final/V##.mp4` are the files that get posted.
- Preview to the owner on an artifact page with small (≈3MB) preview copies. Page limits are 15MB per file and 64MB per page. Downloads from chat file cards failed for the owner, so the page approach (long-press or right-click to save) is used.

## 10. Hosting and scheduling

- Finished videos are pushed to the public repo **github.com/Chubyilo92/Coupleinsocial**, folder `CoupleIn_videos/V##.mp4`. Metricool fetches them from `https://raw.githubusercontent.com/Chubyilo92/Coupleinsocial/main/CoupleIn_videos/V##.mp4`. Delete them after they've posted to keep the repo small.
- Claude pushes using a fine-grained GitHub token the owner provides (Contents: read & write, scoped to the repos, 90-day expiry). **Never store the token in memory or in any repo file.**
- Metricool (one brand holds Instagram @coupleinappp, TikTok @coupleinapp, Threads, Pinterest): `createScheduledPost` with providers instagram and tiktok, `instagramData.type = "REEL"`, the caption from captions.json, `videoCoverMilliseconds: 500`, 2 reels a day. The default times are 13:00 and 20:00 UK, which is on top of the 2 daily carousels (4 posts a day). The owner may choose to swap reels into carousel slots instead. Work out what's already done from the `CoupleIn_videos/V##` media URLs in Metricool posts.
- Order: top-60 in file order (V01, V03, V09, V14, … V108).
- Weekly batch: 14 videos (7 days × 2). Run each week in a fresh chat, because long chats burn usage.

## 11. Decisions log (most recent last)

- 24 Sep: chose the format (DM rage bait → app → twist); IG dark-mode look; slower pacing; the "tall → cat" contradiction-style twist became the house style.
- 24 Sep: 80 scripts → 32 met the bar → 28 more written to the bar = 60 (one month).
- 24 Sep: footage-logic audit. Clips must show evidence, never the answer; 23 clips were rewritten.
- 24 Sep: Resolve has no typing, so it's filmed as full sessions. Calendar events get unique dates and no repeats.
- 24 Sep: added live typing with keyboard, and awkward comment-bait openers.
- 28 Sep: all of this moved into this repo as the canonical home (flat layout).
- 4 Oct: post-processing step added (section 13): the owner's real iPhone recording as the chat→app transition (an Android version came first, then iPhone for relatability); the same 9:41 status bar and home bar across every section; still shots set to reading time (min 2s), not a fixed cap; Free Trial card painted out. Same day: footage length in build.py also made reading-time driven (caption timing by word count, last frame held if the clip is too short), and postprocess now also extends stills that are too short. Applied to the 14 Mike Gomorrah batch videos (github.com/Chubyilo92/Mikegomo).

## 13. Post-processing: iPhone transition, matching header/footer, reading-time pacing (4 Oct 2026)

Every video gets this step after `build.py`. Script: `postprocess/postprocess.py` (self-contained; run from anywhere).
`python3 postprocess/postprocess.py IN_DIR OUT_DIR V03 V80 ...` (IN_DIR holds the `V##.mp4` from build.py). About 60s per video. Needs `opencv-python-headless` as well as the build deps.

**Assets (`postprocess/assets/`):**
- `iphone_home_to_couplein.mp4`: the owner's real iPhone screen recording (592×1280, 2.9s): swipes across home pages, taps CoupleIn, iOS app-open zoom. Recorded on 4 Oct 2026. It replaced an Android recording because iPhone is more relatable to the audience. Real icons can only come from a real recording; never draw or copy brand app icons.
- `statusbar_template.png`: the 9:41 status bar cut from the chat render (white on black). It's used as an alpha mask and recoloured black or white.
- `couplein_logo.png`: the CoupleIn logo (hearts + wordmark) for the splash.

**1. Transition (replaces the old still home screen + white splash at the start of the footage):**
- Hard cut from the last chat frame into the iPhone recording at real speed (it's already quick, so no speed-up).
- Kept source ranges: 0.00–0.78s (page swipes, landing on the CoupleIn page) and 1.65–2.50s (short hold, tap, app-open zoom). 0.78–1.65s is cut: an accidental swipe onto the Screen Time widget page and back, plus extra hold before the tap. The owner said holding on the CoupleIn page too long kills the pace.
- The recording ends on a blank white app screen, so 10 frames of the CoupleIn splash (white + logo) are added after the zoom. Total ≈ 2.0s.
- The recording is scaled to fit the 1920 height (888 wide) with soft blurred side fill, because cover-cropping would cut off the CoupleIn icon and the dock. During the zoom, the red recording pill and the app card's mini status bar are painted out.
- If the owner sends a new recording: replace the asset, re-check `KEEP_RANGES` / `LAUNCH_FROM` by sampling frames (find the swipes, the still CoupleIn page, the tap and the zoom), and keep the hold on the CoupleIn page ≈0.5s.

**2. Header and footer always match, start to finish (owner's rule):**
- The same 9:41 status bar on every section: chat (already rendered), iPhone home screen (replaces the recording's own 10:32 + red pill), splash and app footage. It's black on light backgrounds and white on dark, with hysteresis so it never flickers.
- App footage is shifted down 100px (top band filled with the footage's own top colour), so the app's header sits under the status bar like a real app and nothing overlaps. The bottom 100px of footage is lost, which is fine.
- The same iPhone home bar (318×11px at y=1900, matching the real recording) is added to chat (white, under the keyboard), splash and app footage (black/white by background). The home screen has none, like a real iPhone.

**3. Still shots always match reading time, never a fixed cap (owner's rule):**
- Still runs (no pixel change for 1.5s+) in the footage are set to `0.4s orient + caption words/4 per s (minus the time the same caption was already on screen, found by template-matching the caption box) + evidence words/4 per s + 0.3s beat`, and never below 2.0s. Longer stills are trimmed. Shorter ones are held longer (the frozen frame is repeated and the audio under it is repeated with crossfades, so the sync holds).
- `postprocess/reading.json` holds the on-screen caption and the evidence the viewer must take in (event name, date, time, item) for each video. **For new videos, add their entry by reading the actual hold frame.** The on-screen captions often differ from `scenarios.json` (e.g. V80 shows "Friday. 2am. she's booked him in."). An entry can be a list (one per still shot, in order) when a clip has more than one still with different captions (see V25). If an entry is missing, the script falls back to scenarios.json overlay/in_app and warns.
- Results for batch 1 (old still → new): V03 5.3→3.2, V22 6.1→2.7, V62 4.4→2.0, V69 4.9→3.5, V74 2.8→2.0, V75 3.6→2.4, V79 5.2→2.6, V80 5.6→3.2, V81 6.3→2.0, V85 4.6→2.4; V25 2.6 kept (these 14 were approved before the hold-longer rule existed; from now on a still like V25's gets extended to its reading time).

**4. Free Trial card:** the "🎉 Free Trial · N days left" card must never be visible. The script detects its progress bar in every footage frame and paints the card (and everything below it) with the background colour. In batch 1 it only appeared in V03.

**5. Audio:** each kept piece keeps its own original audio, joined with 40ms crossfades, so key clicks, pops, the whoosh and the "faaaack" twist sting stay frame-synced. QC: no black frames, no audio drop-outs except quiet beats already in the music, file well under 19MB.

## Repo layout
`postprocess/` (section 13: `postprocess.py`, `reading.json`, `assets/`). Everything else is flat in the repo root: `SPEC.md`, `README.md`, `build.py`, `render.py`, `scenarios.json`, `index.html` (script browser), `CoupleIn_filming_guide.docx` + `plan.py` + `make.js` + `plan.json` (filming guide), `scenarios_source_*.py` and `blur_placeholder_render.py` (historical).

## 12. Open items

- Confirm the mood options in the app (V33/V34/V61/V65).
- Confirm whether calendar events have a notes field (V14, V19, V25, V64).
- Owner to record the 11 recordings and 2 photos, and provide a GitHub token.
- First batch: render, QC, preview, push, schedule.
