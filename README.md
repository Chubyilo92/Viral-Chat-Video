# Viral Chat Video

CoupleIn's DM rage-bait → app → twist short videos for TikTok and Instagram Reels.

**Start here: read [`SPEC.md`](SPEC.md) in full before doing anything.** It's the canonical production spec.

| File | What it is |
|---|---|
| `SPEC.md` | The canonical production spec. Read first. |
| `build.py`, `render.py`, `scenarios.json` | The batch builder, the renderer, and all scripts (`top: true` = the 60 to post) |
| `postprocess/` | **Run after build.py on every video**: the iPhone transition, matching header/footer, reading-time pacing, Free Trial removal (SPEC.md section 13) |
| `CoupleIn_filming_guide.docx` | The owner's filming guide (rebuilt by `plan.py` and `make.js` from `plan.json`) |
| `index.html` | A filterable view of every script |
| `scenarios_source_*.py`, `blur_placeholder_render.py` | Historical, reference only |

To start a new weekly batch in a fresh chat: "Read SPEC.md in github.com/Chubyilo92/Viral-Chat-Video and run this week's batch."
