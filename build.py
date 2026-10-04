"""CoupleIn twist-reel batch builder.

Usage:
  python3 build.py V03 V14 V22 --footage FOOTAGE_DIR [--photos PHOTO_DIR] [--out OUT_DIR] [--placeholder FILE]

FOOTAGE_DIR holds screen recordings named by clip code, e.g. B-SCROLL.mp4, C-EVENT.mov,
M-VIEW.mp4, R-FLOW.mp4 (a file named after a video ID, e.g. V14.mov, overrides the clip code
for that one video). PHOTO_DIR holds twist photos named by video ID, e.g. V01.jpg.
Writes OUT_DIR/<ID>.mp4 (kept under 19MB) and OUT_DIR/captions.json (post captions).
"""
import json, os, sys, glob, subprocess, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
S = {s["id"]: s for s in json.load(open(os.path.join(HERE, "scenarios.json")))}

END_LINES = {
    "B": "Stop guessing. It's on {p} list.",
    "C": "Never forget. Ever.",
    "M": "Know how {q} feels before you ask.",
    "R": "Fight fair. Fix it faster.",
    "S": "Keep score of the love, not the fights.",
}
HASHTAGS = "#couples #relationships #boyfriend #girlfriend #couplegoals #relationshiptips"

def find(d, names):
    if not d: return None
    for n in names:
        hits = [f for f in glob.glob(os.path.join(d, n + ".*")) if f.lower().endswith((".mp4", ".mov", ".m4v", ".jpg", ".jpeg", ".png", ".heic", ".webp"))]
        if hits: return hits[0]
    return None

def duration(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                       capture_output=True, text=True)
    return float(r.stdout.strip())

def type_dur(txt): return max(0.55, len(txt) / 14.0)

def retime(msgs, start):
    """Times are when each message lands. 'me' messages are typed first, so they need typing time."""
    t, prev, out = start, None, []
    for w, txt in msgs:
        typed = (w == "me" and not txt.startswith("["))
        if prev is None:
            t = start + (type_dur(txt) + 0.12 if typed else 0.5)
        else:
            plen = 10 if prev[1].startswith("[") else len(prev[1])
            read = 0.5 + 0.025 * plen
            gap = read + (type_dur(txt) + 0.12 if typed else 0.35 if w == "her" else 0.3)
            t += gap
        out.append([w, txt, round(t, 2)]); prev = (w, txt)
    return out, t

# Awkward last messages already in the chat before the fight starts (me = angry person).
OPENERS = [
 [["me","love you"],["them","👍"]],
 [["me","if I was a worm would you still love me"],["them","no"]],
 [["them","you put the milk in before the teabag again"],["me","and I'll do it again"]],
 [["me","[SYS]You unsent a message"],["them","I saw it"]],
 [["them","[VOICE]2:47"],["me","I'm not listening to all that"]],
 [["me","is a hot dog a sandwich"],["them","I'm not doing this again"]],
 [["them","why do you sleep with socks on"],["me","why DON'T you"]],
 [["me","hey"],["me","hey"],["me","hey"]],
 [["me","I paid for dinner so you're getting the Uber"],["them","that's not how love works"]],
 [["me","I've been thinking about us"],["them","[VOICE]0:03"]],
 [["them","do you shower morning or night"],["me","neither 🙂"]],
 [["me","toilet roll goes OVER not under"],["them","[SYS]Seen"]],
 [["them","why did you like my photo from 2016 at 3am"],["me","thumb slipped"]],
 [["me","pineapple on pizza tonight?"],["them","I will leave you"]],
 [["me","on a scale of 1 to 10 how mad are you"],["them","11"]],
 [["me","rate my mum's cooking out of 10"],["them","[SYS]Seen"]],
 [["them","do you still have your ex's hoodie"],["me","which one"]],
 [["me","what's for tea"],["me","[SYS]Seen"]],
 [["them","who's your celebrity crush"],["me","[VOICE]0:41"]],
 [["me","I think I'm getting really good at cooking"],["them","[SYS]Reacted 😂 to your message"]],
 [["them","did you eat my yoghurt"],["me","what yoghurt"],["them","exactly"]],
 [["me","do you think pigeons know they're pigeons"],["them","why are you like this"]],
 [["them","why is there a whole lasagne in the bath"]],
 [["me","we need to talk"],["me","about the Wi-Fi password"]],
 [["them","why is your nan following me on TikTok"],["me","she likes your content"]],
 [["me","be honest. do I snore"],["them","[VOICE]1:12"]],
 [["them","stop sending me reels at 2am"],["me","[REEL]"]],
 [["me","I just realised I don't know your middle name"],["them","it's been 3 years"]],
 [["me","can we get a snake"],["them","absolutely not"],["me","a small one"]],
 [["them","did you just burp on the phone"],["me","no"],["them","you did"]],
]
YDAY = ["Yesterday 23:47","Yesterday 21:12","Yesterday 00:58","Yesterday 18:30","Sun 22:04","Sat 01:17"]
TODAY = ["Today 14:12","Today 09:41","Today 17:26","Today 12:03","Today 19:48","Today 08:15"]
TOPS = None
def opener_for(vid):
    global TOPS
    if TOPS is None: TOPS = [x["id"] for x in json.load(open(os.path.join(HERE, "scenarios.json"))) if x.get("top")]
    i = TOPS.index(vid) if vid in TOPS else int(vid[1:])
    lines = [["me" if w == "me" else "her", t] for w, t in OPENERS[i % len(OPENERS)]]
    return [["her", "[SYS]" + YDAY[i % len(YDAY)]]] + lines + [["her", "[SYS]" + TODAY[i % len(TODAY)]]]

def build_script(s, clip_file, photo):
    partner_is_her = s["pov"] == "him"
    def conv(arr):
        res = []
        for w, t in arr:
            if t == "[PHOTO]" or t.startswith("[screenshot]"):
                if photo: t = f"[PHOTO:{photo}]"
                elif t == "[PHOTO]": continue
                else: t = t.replace("[screenshot]", "").strip()
            res.append(["me" if w == "me" else "her", t])
        return res
    fight, e1 = retime(conv(s["fight"]), 0.0)
    twist, e2 = retime(conv(s["twist"]), 0.8)
    clip_len = duration(clip_file)
    speed = 1.15
    # Footage time follows reading time (SPEC 5 + 13): each caption gets what it takes to read,
    # the last one also covers the on-screen evidence (in_app). Never cut the clip short of that:
    # if the clip is shorter than the reading time, its last frame is held (pad).
    ov = s["overlay"]
    needs = [max(1.5, 0.4 + len(t.split()) / 4.0 + 0.3) for t in ov]
    needs[-1] = max(2.0, needs[-1] + len(str(s.get("in_app", "")).split()) / 4.0)
    read_total = sum(needs)
    src_dur = min(clip_len, max(8.5, read_total) * speed)
    fdur = max(src_dur / speed, read_total)
    pad = max(0.0, read_total - src_dur / speed)
    scale = fdur / read_total
    caps, t0 = [], 0.0
    for i, (t, n) in enumerate(zip(ov, needs)):
        t1 = t0 + n * scale
        caps.append({"from": round(t0, 2), "to": 99 if i == len(ov) - 1 else round(t1, 2),
                     "text": t, "y": 1250, "size": 80 if len(t) <= 14 else 62})
        t0 = t1
    line = END_LINES[s["feature"]].format(p="her" if partner_is_her else "his", q="she" if partner_is_her else "he")
    return {"name": "ella 🤍" if partner_is_her else "jay 🤍", "history": opener_for(s["id"]), "sections": [
        {"type": "dm", "duration": round(e1 + 1.6, 2), "captions": [{"from": 0, "to": 99, "text": s["hook"], "y": 290}], "messages": fight},
        {"type": "footage", "src": clip_file, "src_start": 0, "src_dur": round(src_dur, 2), "speed": speed, "pad": round(pad, 2), "captions": caps},
        {"type": "dm", "duration": round(e2 + 2.0, 2), "continue": True,
         "captions": [{"from": 0, "to": 2.4, "text": f"then {'she' if partner_is_her else 'he'} sent this…", "y": 290}], "messages": twist},
        {"type": "end", "duration": 2.6, "line": line}]}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--footage", required=True)
    ap.add_argument("--photos")
    ap.add_argument("--out", default="out")
    ap.add_argument("--placeholder", help="use this clip when a clip code is missing (testing only)")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    capfile = os.path.join(a.out, "captions.json")
    captions = json.load(open(capfile)) if os.path.exists(capfile) else {}
    problems = []
    for vid in a.ids:
        s = S[vid]
        clip = find(a.footage, [vid, s["clip"]]) or a.placeholder
        if not clip:
            problems.append(f"{vid}: no footage for {s['clip']} (add {s['clip']}.mp4 to {a.footage})"); continue
        photo = find(a.photos, [vid])
        if ("[PHOTO]" in json.dumps(s["twist"]) or "[screenshot]" in json.dumps(s["twist"])) and not photo:
            problems.append(f"{vid}: twist expects a photo ({s.get('photo') or 'screenshot'}) - rendered without it")
        script = build_script(s, clip, photo)
        jf = os.path.join(a.out, f"{vid}.json"); json.dump(script, open(jf, "w"), ensure_ascii=False, indent=1)
        mp4 = os.path.join(a.out, f"{vid}.mp4")
        subprocess.run([sys.executable, os.path.join(HERE, "render.py"), jf, mp4], check=True)
        if os.path.getsize(mp4) > 19_000_000:
            tmp = mp4 + ".c.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp4, "-c:v", "libx264", "-crf", "25", "-preset", "slow",
                            "-c:a", "copy", "-movflags", "+faststart", tmp], check=True)
            os.replace(tmp, mp4)
        os.remove(jf)
        captions[vid] = f"{s['hook']}\n\nwhose side are you on? 👇\n\n{HASHTAGS}"
        print(f"OK {vid} {os.path.getsize(mp4)/1e6:.1f}MB")
    json.dump(captions, open(capfile, "w"), ensure_ascii=False, indent=1)
    for p in problems: print("WARN", p)

if __name__ == "__main__":
    main()
