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

- `pipeline/scenarios.json` is canonical (108 scripts, V01–V108). **Only the 60 with `"top": true` meet the bar**: that's one month at 2 a day. The other 48 are weaker drafts kept for reference. Never post them.
- The top 60: V01 V03 V09 V14 V19 V22 V24 V25 V33 V34 V43 V44 V61–V108.
- The fields are id, feature (B Brownies, C Calendar, M Mood, R Resolve, S Score), pov (`him` means Jay is angry, `her` means Ella is angry), hook, fight, clip, in_app, overlay (the captions over the footage), twist, bait, photo, top.
- In fight and twist, `me` is the angry person (right-hand, sent, purple→blue bubbles) and `them` is the partner (left, grey). `[PHOTO]` is a photo message, and `[screenshot] …` becomes a drawn image or plain text.
- `tools/scenarios_source_*.py` are the original generators. They're historical only, because later fixes were made directly in the JSON.
- `scripts-browser/index.html` is a filterable page of all scripts (opens on the top 60).

## 4. What the DM screen looks like (Instagram dark mode)

These are implemented in `pipeline/render.py`:
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

- Cover-cropped to 1080×1920, played at 1.15× speed, trimmed to ≤8.5s.
- Captions (`overlay`) are split evenly across the clip, Poppins Bold 62–80 with stroke, at y≈1250.
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

Full step-by-step guide: `filming/CoupleIn_filming_guide.docx` (rebuild with `cd filming && python3 plan.py && node make.js`).
- A demo couple, **Jay and Ella**, with plain avatars and no real photos. (The first test recording used celebrity avatars, Diddy and 50 Cent, and must never be used in posts.)
- **Film on the angry person's login.** Exceptions: V44 and V106 are filmed on Jay's login because they show what Jay did.
- Routine: "hold" means finger off the screen and count to 5. For Calendar and Resolve, go back and count to 2 between items. Tap actions: finger off and count to 3 after.
- 11 recordings plus 2 photos (cat for V01, sausage roll for V33):
  - J1 Brownies (Ella's wishlist) · J2 Calendar (Ella's events + Jay's Lads' night + the wedding move) · J3a–d Mood (Ella sets each mood, Jay films) · J4 one full Resolve session on Jay's login (covers 12 videos) · E1 Ella's own wishlist (the ring) · E2 Calendar (Jay's events + Netflix event added live) · E3 one full Resolve session on Ella's login (covers 8 videos).
- The owner sends them in the chat with the codes in the same order ("J1, J2, J3a…"). Chat limits: 500MB per file, 20 files per chat.
- Clip identification: sample frames, find the still "holds", read the on-screen text (event titles, item names) and cross-check against the guide order. If they disagree, flag the clip; don't guess.

## 9. Building

```
cd pipeline
python3 build.py V03 V14 ... --footage FOOTAGE_DIR [--photos PHOTO_DIR] --out out
```
- FOOTAGE_DIR holds per-video clips named `V##.mp4` (cut from the long recordings), or clip-code files (`B-MARK.mp4`, `C-EVENT.mp4`, `M-VIEW.mp4`, `R-FLOW.mp4`…) as fallbacks. Photos go in `PHOTO_DIR/V##.jpg`.
- Output: `out/V##.mp4` (kept under 19MB) plus `out/captions.json` (post captions: hook, "whose side are you on? 👇", hashtags).
- Needs ffmpeg, Python with Pillow and numpy, and the fonts Poppins (`/usr/share/fonts/truetype/google-fonts/`), Liberation Sans and Noto Color Emoji.
- About 75s per video to render.
- **QC every video before showing it:** frame 0 shows the hook and the opener; there's no clipped or overlapping text; the footage matches the caption; the photo is present if needed; no real faces; the file is under 19MB.
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
- 28 Sep: all of this moved into this repo as the canonical home.

## 12. Open items

- Confirm the mood options in the app (V33/V34/V61/V65).
- Confirm whether calendar events have a notes field (V14, V19, V25, V64).
- Owner to record the 11 recordings and 2 photos, and provide a GitHub token.
- First batch: render, QC, preview, push, schedule.
