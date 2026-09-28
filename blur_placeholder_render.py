import subprocess, numpy as np, cv2, wave, math, sys, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
SRC = "/mnt/user-data/uploads/IMG_2839.MOV"
PINK, CORAL = (255, 107, 157), (255, 150, 90)
GF = "/usr/share/fonts/truetype/google-fonts/"
EMOJI_FONT = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)

def F(w, s): return ImageFont.truetype(GF + f"Poppins-{w}.ttf", s)

SCRIPT = json.load(open(sys.argv[1]))
OUT = sys.argv[2]

# ---------- text with emoji ----------
def is_emoji(c): return ord(c) >= 0x1F000 or 0x2600 <= ord(c) <= 0x27BF
_ecache = {}
def emoji_img(c, size):
    k = (c, size)
    if k not in _ecache:
        im = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((0, 0), c, font=EMOJI_FONT, embedded_color=True)
        im = im.crop(im.getbbox() or (0, 0, 1, 1))
        s = size / max(im.size)
        _ecache[k] = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)
    return _ecache[k]

def text_w(t, font):
    w = 0
    for c in t:
        w += int(font.size * 1.05) if is_emoji(c) else font.getlength(c)
    return w

def draw_text(img, xy, t, font, fill, stroke=0, stroke_fill=(0, 0, 0)):
    d = ImageDraw.Draw(img); x0, y = xy
    # split into runs
    runs, cur = [], ""
    for c in t:
        if is_emoji(c):
            if cur: runs.append(("t", cur)); cur = ""
            runs.append(("e", c))
        elif c in "\ufe0f\u200d": continue
        else: cur += c
    if cur: runs.append(("t", cur))
    passes = [0, 1] if stroke else [1]
    for p in passes:
        x = x0
        for kind, r in runs:
            if kind == "e":
                if p == 1:
                    e = emoji_img(r, int(font.size * 0.95))
                    img.alpha_composite(e, (int(x), int(y + font.size * 0.12)))
                x += int(font.size * 1.05)
            else:
                if p == 0:
                    d.text((x, y), r, font=font, fill=stroke_fill, stroke_width=stroke, stroke_fill=stroke_fill)
                else:
                    d.text((x, y), r, font=font, fill=fill)
                x += font.getlength(r)

def wrap(t, font, maxw):
    words, lines, cur = t.split(" "), [], ""
    for w_ in words:
        test = (cur + " " + w_).strip()
        if text_w(test, font) <= maxw: cur = test
        else: lines.append(cur); cur = w_
    lines.append(cur); return lines

# ---------- caption (TikTok style) ----------
def caption(img, t, y, size=62):
    f = F("Bold", size)
    lines = wrap(t, f, W - 160)
    for i, ln in enumerate(lines):
        x = (W - text_w(ln, f)) / 2
        draw_text(img, (x, y + i * size * 1.25), ln, f, (255, 255, 255), stroke=6)

# ---------- DM screen (Instagram dark mode look) ----------
LIB = "/usr/share/fonts/truetype/liberation/"
def L(w, s): return ImageFont.truetype(LIB + f"LiberationSans-{w}.ttf", s)
MF = L("Regular", 45)
PAD_X, PAD_Y, MAXW = 40, 26, 690
IN_GREY = (38, 38, 38, 255)
# IG sent-bubble gradient: purple at top of screen -> blue at bottom
IG_GRAD = Image.new("RGBA", (W, H))
_gd = ImageDraw.Draw(IG_GRAD)
_stops = [(0.0, (163, 57, 235)), (0.45, (110, 72, 245)), (1.0, (55, 151, 240))]
for yy in range(H):
    p = yy / (H - 1)
    for (p0, c0), (p1, c1) in zip(_stops, _stops[1:]):
        if p0 <= p <= p1:
            k = (p - p0) / (p1 - p0)
            _gd.line([(0, yy), (W, yy)], fill=tuple(int(c0[i] + (c1[i] - c0[i]) * k) for i in range(3)) + (255,))
            break

def bubble(msg):
    who, t = msg
    lines = wrap(t, MF, MAXW - 2 * PAD_X)
    bw = max(text_w(l, MF) for l in lines) + 2 * PAD_X
    bh = len(lines) * 58 + 2 * PAD_Y
    im = Image.new("RGBA", (int(bw), int(bh)), (0, 0, 0, 0))
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.width - 1, im.height - 1], min(46, im.height // 2), fill=255)
    if who != "me":
        im.paste(Image.new("RGBA", im.size, IN_GREY), (0, 0), mask)
    for i, l in enumerate(lines):
        draw_text(im, (PAD_X, PAD_Y + i * 58 - 2), l, MF, (255, 255, 255))
    im.info["mask"] = mask
    return im

def typing_bubble(frame_i):
    im = Image.new("RGBA", (140, 96), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 139, 95], 48, fill=IN_GREY)
    for k in range(3):
        on = (frame_i // 5) % 3 == k
        c = (190, 190, 190) if on else (110, 110, 110)
        d.ellipse([33 + k * 28, 39, 51 + k * 28, 57], fill=c)
    im.info["mask"] = None
    return im

def default_avatar(size):
    av = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(av)
    d.ellipse([0, 0, size - 1, size - 1], fill=(219, 219, 219))
    d.ellipse([size * .33, size * .2, size * .67, size * .54], fill=(255, 255, 255))
    d.pieslice([size * .15, size * .6, size * .85, size * 1.3], 180, 360, fill=(255, 255, 255))
    m = Image.new("L", (size, size), 0); ImageDraw.Draw(m).ellipse([0, 0, size - 1, size - 1], fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0)); out.paste(av, (0, 0), m)
    return out
SMALL_AV = default_avatar(56)

def dm_base(name):
    bg = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    d = ImageDraw.Draw(bg)
    # status bar
    d.text((95, 52), "9:41", font=L("Bold", 40), fill=(255, 255, 255), anchor="mm")
    for i in range(4):
        d.rounded_rectangle([860 + i * 16, 60 - i * 7, 870 + i * 16, 66], 2, fill=(255, 255, 255))
    d.rounded_rectangle([940, 38, 1010, 68], 8, outline=(255, 255, 255), width=3)
    d.rounded_rectangle([945, 43, 1000, 63], 5, fill=(255, 255, 255))
    d.rectangle([1012, 47, 1017, 59], fill=(255, 255, 255))
    # header
    cy = 170
    d.line([(58, cy - 24), (36, cy), (58, cy + 24)], fill=(255, 255, 255), width=6, joint="curve")
    bg.alpha_composite(default_avatar(92), (95, cy - 46))
    draw_text(bg, (210, cy - 44), name, L("Bold", 40), (255, 255, 255))
    d.text((210, cy + 8), "Active now", font=L("Regular", 31), fill=(168, 168, 168))
    # phone icon
    d.arc([832, cy - 30, 892, cy + 30], 110, 250, fill=(255, 255, 255), width=8)
    d.rounded_rectangle([846, cy - 36, 866, cy - 18], 6, fill=(255, 255, 255))
    d.rounded_rectangle([846, cy + 18, 866, cy + 36], 6, fill=(255, 255, 255))
    # video icon
    d.rounded_rectangle([925, cy - 22, 985, cy + 22], 10, outline=(255, 255, 255), width=5)
    d.polygon([(990, cy - 4), (1025, cy - 22), (1025, cy + 22), (990, cy + 4)], outline=(255, 255, 255), width=5)
    d.line([(0, 248), (W, 248)], fill=(38, 38, 38), width=2)
    # input bar
    d.rounded_rectangle([28, 1738, W - 28, 1850], 56, fill=(38, 38, 38))
    d.ellipse([44, 1752, 128, 1836], fill=(55, 151, 240))
    d.rounded_rectangle([66, 1778, 106, 1812], 7, outline=(255, 255, 255), width=4)
    d.ellipse([78, 1786, 94, 1802], outline=(255, 255, 255), width=3)
    d.text((152, 1794), "Message...", font=L("Regular", 40), fill=(168, 168, 168), anchor="lm")
    # mic, gallery, sticker icons
    d.rounded_rectangle([760, 1770, 784, 1806], 12, outline=(255, 255, 255), width=4)
    d.arc([750, 1790, 794, 1822], 0, 180, fill=(255, 255, 255), width=4)
    d.rounded_rectangle([840, 1772, 890, 1818], 8, outline=(255, 255, 255), width=4)
    d.ellipse([850, 1782, 862, 1794], fill=(255, 255, 255))
    d.ellipse([930, 1770, 980, 1820], outline=(255, 255, 255), width=4)
    d.arc([942, 1790, 968, 1810], 20, 160, fill=(255, 255, 255), width=4)
    return bg

def render_dm(section, base, prior, frames_out):
    msgs = section["messages"]
    dur = section["duration"]
    top, bottom, gap = 520, 1712, 10
    bubbles_prior = [bubble((m[0], m[1])) for m in prior]
    bubbles_new = [bubble((m[0], m[1])) for m in msgs]
    events = [(m[2], m[0]) for m in msgs]
    n = int(dur * FPS)
    scroll = 0.0
    for fi in range(n):
        t = fi / FPS
        vis = [(p[0], b, 99) for p, b in zip(prior, bubbles_prior)]
        typing = False
        for idx, (m, b) in enumerate(zip(msgs, bubbles_new)):
            if t >= m[2]: vis.append((m[0], b, (t - m[2]) if m[2] > 0 else 99))
            elif m[0] == "her" and m[2] - t < 0.55 and not typing and all(t >= mm[2] for mm in msgs[:idx]):
                typing = True
        items = list(vis)
        if typing: items.append(("her", typing_bubble(fi), 99))
        # extra spacing when sender changes
        spaces = []
        for i, it in enumerate(items):
            spaces.append(gap + (26 if i + 1 < len(items) and items[i + 1][0] != it[0] else 0))
        total = sum(b.height + sp for (_, b, _), sp in zip(items, spaces))
        target = max(0, top + total - bottom)
        scroll += (target - scroll) * 0.35
        img = base.copy()
        y = top - scroll
        for i, ((who, b, age), sp) in enumerate(zip(items, spaces)):
            a = min(1, age / 0.17)
            off = int((1 - a) * 30)
            if y + b.height > 440:
                x = W - 30 - b.width if who == "me" else 110
                yy = int(y + off)
                layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                mask = b.info.get("mask")
                if who == "me" and mask is not None:
                    layer.paste(IG_GRAD.crop((x, yy, x + b.width, yy + b.height)), (x, yy), mask)
                layer.alpha_composite(b, (x, yy))
                last_in_group = who == "her" and (i + 1 == len(items) or items[i + 1][0] != "her")
                if last_in_group:
                    layer.alpha_composite(SMALL_AV, (34, yy + b.height - 56))
                if a < 1:
                    layer.putalpha(layer.getchannel("A").point(lambda v: int(v * a)))
                img.alpha_composite(layer)
            y += b.height + sp
        cover = base.crop((0, 0, W, 520))
        m = Image.new("L", (W, 520), 255)
        md = ImageDraw.Draw(m)
        for yy2 in range(440, 520): md.line([(0, yy2), (W, yy2)], fill=int(255 * (520 - yy2) / 80))
        img.paste(cover, (0, 0), m)
        for cap in section.get("captions", []):
            if cap["from"] <= t < cap["to"]:
                caption(img, cap["text"], cap.get("y", 290), cap.get("size", 62))
        frames_out(img)
    return prior + [(m[0], m[1]) for m in msgs], events

# ---------- footage ----------
def render_footage(section, frames_out):
    ss, dur_src, speed = section["src_start"], section["src_dur"], section["speed"]
    cmd = ["ffmpeg", "-v", "error", "-ss", str(ss), "-t", str(dur_src), "-i", SRC,
           "-vf", f"setpts=PTS/{speed},fps={FPS},scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ref = cv2.cvtColor(cv2.imread("ref.png"), cv2.COLOR_BGR2GRAY)
    tpls = []
    for (cx, cy) in [(120, 465), (608, 380)]:
        tpls.append(ref[cy - 50:cy + 50, cx - 50:cx + 50])
    pos = [(120, 465), (608, 380)]
    fi = 0
    while True:
        raw = p.stdout.read(W * H * 3)
        if len(raw) < W * H * 3: break
        fr = np.frombuffer(raw, np.uint8).reshape(H, W, 3).copy()
        g = cv2.cvtColor(fr, cv2.COLOR_RGB2GRAY)
        scores = [0, 0]; found = [None, None]
        for k in range(2):
            cx, cy = pos[k]; R = 170
            x0, y0 = max(0, cx - 50 - R), max(0, cy - 50 - R)
            win = g[y0:min(H, cy + 50 + R), x0:min(W, cx + 50 + R)]
            best = (-1, None)
            for s in (0.85, 0.95, 1.05, 1.15):
                tp = cv2.resize(tpls[k], None, fx=s, fy=s)
                if win.shape[0] < tp.shape[0] or win.shape[1] < tp.shape[1]: continue
                r = cv2.matchTemplate(win, tp, cv2.TM_CCOEFF_NORMED)
                _, mv, _, ml = cv2.minMaxLoc(r)
                if mv > best[0]: best = (mv, (x0 + ml[0] + tp.shape[1] // 2, y0 + ml[1] + tp.shape[0] // 2))
            scores[k], found[k] = best
        OFF = (120 - 608, 465 - 380)
        for k in range(2):
            if scores[k] > 0.55: pos[k] = found[k]
        for k in range(2):
            o = 1 - k
            if scores[k] <= 0.55 and scores[o] > 0.55:
                sgn = 1 if k == 0 else -1
                pos[k] = (pos[o][0] + sgn * OFF[0], pos[o][1] + sgn * OFF[1])
        for k in range(2):
            # pixelate circle
            cx, cy = pos[k]; r_ = 64
            xa, ya, xb, yb = max(0, cx - r_), max(0, cy - r_), min(W, cx + r_), min(H, cy + r_)
            patch = fr[ya:yb, xa:xb]
            small = cv2.resize(patch, (8, 8), interpolation=cv2.INTER_LINEAR)
            pix = cv2.resize(small, (patch.shape[1], patch.shape[0]), interpolation=cv2.INTER_NEAREST)
            pix = cv2.GaussianBlur(pix, (0, 0), 6)
            mask = np.zeros(patch.shape[:2], np.uint8)
            cv2.circle(mask, (cx - xa, cy - ya), r_, 255, -1)
            patch[mask > 0] = pix[mask > 0]
        img = Image.fromarray(fr).convert("RGBA")
        t = fi / FPS
        z = section.get("zoom")
        if z and t < z["until"]:
            k_ = 1 - (t / z["until"]) ** 2
            s = 1 + (z["scale"] - 1) * k_
            cx, cy = z["cx"], z["cy"]
            cw, ch = W / s, H / s
            x0 = min(max(0, cx - cw / 2), W - cw); y0 = min(max(0, cy - ch / 2), H - ch)
            img = img.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.LANCZOS)
        for cap in section.get("captions", []):
            if cap["from"] <= t < cap["to"]:
                caption(img, cap["text"], cap.get("y", 250), cap.get("size", 62))
        frames_out(img); fi += 1
    p.wait()
    return fi

# ---------- end card ----------
def render_end(section, frames_out):
    n = int(section["duration"] * FPS)
    base = Image.new("RGBA", (W, H), (12, 12, 16, 255))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([140, 520, 940, 1320], fill=(255, 107, 157, 110))
    base.alpha_composite(glow.filter(ImageFilter.GaussianBlur(170)))
    d = ImageDraw.Draw(base)
    d.text((W / 2, 700), "CoupleIn", font=F("Bold", 120), fill=PINK, anchor="mm")
    y = 860
    for ln in wrap(section["line"], F("Bold", 64), W - 200):
        d.text((W / 2, y), ln, font=F("Bold", 64), fill=(255, 244, 236), anchor="mm"); y += 84
    d.text((W / 2, y + 60), "Free on iOS & Android", font=F("Medium", 40), fill=(190, 190, 200), anchor="mm")
    d.text((W / 2, y + 200), "7 days. Uninstall if nothing changes.", font=F("Medium", 42), fill=(255, 150, 120), anchor="mm")
    for fi in range(n):
        img = base.copy()
        a = min(1, fi / 8)
        if a < 1:
            black = Image.new("RGBA", (W, H), (12, 12, 16, int(255 * (1 - a))))
            img.alpha_composite(black)
        frames_out(img)

# ---------- main ----------
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                        "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                        "-pix_fmt", "yuv420p", "tmp_video.mp4"], stdin=subprocess.PIPE)
count = [0]
def out(img):
    enc.stdin.write(img.convert("RGB").tobytes()); count[0] += 1

sfx = []
prior = []
base = dm_base(SCRIPT["name"])
for sec in SCRIPT["sections"]:
    t0 = count[0] / FPS
    if sec["type"] == "dm":
        prior, ev = render_dm(sec, base, prior if sec.get("continue") else [], out)
        sfx += [(t0 + t, w) for t, w in ev]
    elif sec["type"] == "footage":
        render_footage(sec, out); sfx.append((t0, "whoosh"))
    elif sec["type"] == "end":
        render_end(sec, out); sfx.append((t0, "whoosh"))
enc.stdin.close(); enc.wait()
total = count[0] / FPS

# ---------- sfx track ----------
sr = 44100
audio = np.zeros(int(sr * (total + 0.5)))
def add(t, sig):
    i = int(t * sr); audio[i:i + len(sig)] += sig[:len(audio) - i]
tt = np.arange(int(sr * 0.09)) / sr
pop_in = np.sin(2 * np.pi * (900 + 600 * tt / tt[-1]) * tt) * np.exp(-tt * 45) * 0.35
pop_out = np.sin(2 * np.pi * (1400 - 500 * tt / tt[-1]) * tt) * np.exp(-tt * 55) * 0.3
tw = np.arange(int(sr * 0.35)) / sr
whoosh = np.random.randn(len(tw)) * np.sin(np.pi * tw / tw[-1]) ** 2 * 0.12
whoosh = np.convolve(whoosh, np.ones(30) / 30, mode="same")
for t, w in sfx:
    add(t, pop_out if w == "me" else whoosh if w == "whoosh" else pop_in)
audio = np.clip(audio, -1, 1)
with wave.open("tmp_sfx.wav", "w") as wf:
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
    wf.writeframes((audio * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "tmp_video.mp4", "-i", "tmp_sfx.wav", "-c:v", "copy",
                "-c:a", "aac", "-b:a", "160k", "-shortest", OUT], check=True)
print("done", OUT, round(total, 2), "s")
