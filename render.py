import subprocess, numpy as np, wave, math, sys, json, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
PINK, CORAL = (255, 107, 157), (255, 150, 90)
GF = "/usr/share/fonts/truetype/google-fonts/"
EMOJI_FONT = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)

def F(w, s): return ImageFont.truetype(GF + f"Poppins-{w}.ttf", s)

SCRIPT = json.load(open(sys.argv[1]))
OUT = sys.argv[2]
TMP = OUT + ".tmp"

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

SYSF = L("Regular", 30)
def bubble(msg):
    who, t = msg
    if t.startswith("[SYS]"):
        txt = t[5:]
        im = Image.new("RGBA", (W - 60, 56), (0, 0, 0, 0))
        tw_ = text_w(txt, SYSF)
        draw_text(im, ((W - 60 - tw_) / 2, 10), txt, SYSF, (150, 150, 150))
        im.info["mask"] = None; im.info["sys"] = True
        return im
    if t.startswith("[VOICE]"):
        dur = t[7:]
        im = Image.new("RGBA", (520, 110), (0, 0, 0, 0))
        mask = Image.new("L", im.size, 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, 519, 109], 55, fill=255)
        if who != "me": im.paste(Image.new("RGBA", im.size, IN_GREY), (0, 0), mask)
        d = ImageDraw.Draw(im)
        d.polygon([(40, 33), (40, 77), (78, 55)], fill=(255, 255, 255))
        import random; rnd = random.Random(dur)
        for k in range(26):
            hh = rnd.randint(8, 44); x = 105 + k * 12
            d.rounded_rectangle([x, 55 - hh // 2, x + 6, 55 + hh // 2], 3, fill=(255, 255, 255))
        d.text((430, 55), dur, font=L("Regular", 34), fill=(255, 255, 255), anchor="lm")
        im.info["mask"] = mask
        return im
    if t.startswith("[REEL]"):
        im = Image.new("RGBA", (380, 520), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([0, 0, 379, 519], 36, fill=(58, 58, 64))
        d.polygon([(160, 220), (160, 300), (230, 260)], fill=(255, 255, 255))
        d.text((24, 470), "Reel", font=L("Bold", 32), fill=(230, 230, 230))
        im.info["mask"] = None
        return im
    core = t.replace(" ", "").replace("\ufe0f", "")
    if core and len(core) <= 3 and all(is_emoji(c) for c in core):
        size = 130
        im = Image.new("RGBA", (int(size * 1.1 * len(core)) + 10, size + 20), (0, 0, 0, 0))
        x = 0
        for c in core:
            e = emoji_img(c, size); im.alpha_composite(e, (x, 10)); x += int(size * 1.1)
        im.info["mask"] = None
        return im
    if t.startswith("[PHOTO:"):
        ph = Image.open(t[7:-1]).convert("RGBA")
        pw = 560; ph = ph.resize((pw, int(ph.height * pw / ph.width)), Image.LANCZOS)
        if ph.height > 700: ph = ph.crop((0, (ph.height - 700) // 2, pw, (ph.height - 700) // 2 + 700))
        m = Image.new("L", ph.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, ph.width - 1, ph.height - 1], 40, fill=255)
        out = Image.new("RGBA", ph.size, (0, 0, 0, 0)); out.paste(ph, (0, 0), m); out.info["mask"] = None
        return out
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

KB_TOP, BAR_Y0, BAR_Y1, CHAT_BOTTOM = 1250, 1130, 1230, 1105
KEYS = {}
def _layout():
    kw, g, h = 94, 12, 118
    for i, c in enumerate("qwertyuiop"): KEYS[c] = (16 + i * (kw + g), 1270, kw, h)
    for i, c in enumerate("asdfghjkl"): KEYS[c] = (69 + i * (kw + g), 1405, kw, h)
    for i, c in enumerate("zxcvbnm"): KEYS[c] = (169 + i * (kw + g), 1540, kw, h)
    KEYS["shift"] = (16, 1540, 130, h); KEYS["back"] = (922, 1540, 142, h)
    KEYS["123"] = (16, 1675, 130, h); KEYS["emoji"] = (158, 1675, 110, h)
    KEYS[" "] = (280, 1675, 560, h); KEYS["return"] = (852, 1675, 212, h)
_layout()
KF = L("Regular", 50); KFS = L("Regular", 34)
def draw_keyboard(img, hl):
    d = ImageDraw.Draw(img)
    d.rectangle([0, KB_TOP, W, H], fill=(36, 36, 38))
    for k, (x, y, w, h) in KEYS.items():
        special = len(k) > 1
        col = (60, 60, 64) if special else (98, 98, 103)
        if hl is not None and k == hl: col = (160, 160, 166)
        d.rounded_rectangle([x, y, x + w, y + h], 14, fill=col)
        if not special: d.text((x + w / 2, y + h / 2), k, font=KF, fill=(255, 255, 255), anchor="mm")
        elif k == "123": d.text((x + w / 2, y + h / 2), "123", font=KFS, fill=(255, 255, 255), anchor="mm")
        elif k == "return": d.text((x + w / 2, y + h / 2), "return", font=KFS, fill=(255, 255, 255), anchor="mm")
        elif k == " ": d.text((x + w / 2, y + h / 2), "space", font=KFS, fill=(255, 255, 255), anchor="mm")
        elif k == "shift": d.polygon([(x + 65, y + 34), (x + 40, y + 64), (x + 55, y + 64), (x + 55, y + 84), (x + 75, y + 84), (x + 75, y + 64), (x + 90, y + 64)], outline=(255, 255, 255), width=3)
        elif k == "back": d.polygon([(x + 40, y + 59), (x + 60, y + 37), (x + 108, y + 37), (x + 108, y + 81), (x + 60, y + 81)], outline=(255, 255, 255), width=3)
        elif k == "emoji": d.ellipse([x + 33, y + 37, x + 77, y + 81], outline=(255, 255, 255), width=3)
    d.ellipse([60, 1830, 104, 1874], outline=(200, 200, 200), width=3); d.line([(82, 1830), (82, 1874)], fill=(200, 200, 200), width=2); d.line([(60, 1852), (104, 1852)], fill=(200, 200, 200), width=2)
    d.rounded_rectangle([990, 1826, 1012, 1860], 11, outline=(200, 200, 200), width=3); d.arc([980, 1840, 1022, 1872], 0, 180, fill=(200, 200, 200), width=3)

def draw_input(img, text, cursor_on):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([28, BAR_Y0, W - 28, BAR_Y1], 50, fill=(38, 38, 38))
    d.ellipse([42, BAR_Y0 + 10, 122, BAR_Y1 - 10], fill=(55, 151, 240))
    cy = (BAR_Y0 + BAR_Y1) // 2
    d.rounded_rectangle([64, cy - 17, 100, cy + 15], 7, outline=(255, 255, 255), width=4)
    d.ellipse([74, cy - 9, 90, cy + 7], outline=(255, 255, 255), width=3)
    f = L("Regular", 40)
    if text:
        shown = text
        while text_w(shown, f) > 690: shown = shown[1:]
        draw_text(img, (148, cy - 24), shown, f, (255, 255, 255))
        if cursor_on:
            cx = 148 + text_w(shown, f) + 4
            d.rectangle([cx, cy - 24, cx + 4, cy + 24], fill=(55, 151, 240))
        d.text((W - 60, cy), "Send", font=L("Bold", 40), fill=(55, 151, 240), anchor="rm")
    else:
        if cursor_on: d.rectangle([150, cy - 24, 154, cy + 24], fill=(55, 151, 240))
        d.text((160, cy), "Message...", font=f, fill=(168, 168, 168), anchor="lm")
        d.rounded_rectangle([760, cy - 18, 784, cy + 16], 12, outline=(255, 255, 255), width=4)
        d.arc([750, cy - 2, 794, cy + 30], 0, 180, fill=(255, 255, 255), width=4)
        d.rounded_rectangle([840, cy - 22, 890, cy + 22], 8, outline=(255, 255, 255), width=4)
        d.ellipse([850, cy - 12, 862, cy], fill=(255, 255, 255))
        d.ellipse([930, cy - 25, 980, cy + 25], outline=(255, 255, 255), width=4)
        d.arc([942, cy - 5, 968, cy + 15], 20, 160, fill=(255, 255, 255), width=4)

def type_dur(txt): return max(0.55, len(txt) / 14.0)

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
    draw_keyboard(bg, None)
    return bg

def render_dm(section, base, prior, frames_out):
    msgs = section["messages"]
    dur = section["duration"]
    top, bottom, gap = 520, CHAT_BOTTOM - 25, 10
    bubbles_prior = [bubble((m[0], m[1])) for m in prior]
    bubbles_new = [bubble((m[0], m[1])) for m in msgs]
    events = []
    for m in msgs:
        if m[0] == "me" and not m[1].startswith("["):
            st = m[2] - type_dur(m[1]) - 0.12
            for k, ch in enumerate(m[1]):
                events.append((st + (k + 1) / len(m[1]) * type_dur(m[1]), "key"))
        events.append((m[2], m[0]))
    n = int(dur * FPS)
    scroll = None
    for fi in range(n):
        t = fi / FPS
        vis = [(p[0], b, 99) for p, b in zip(prior, bubbles_prior)]
        typing = False; typed = ""; hl = None
        for idx, (m, b) in enumerate(zip(msgs, bubbles_new)):
            if t >= m[2]: vis.append((m[0], b, (t - m[2]) if m[2] > 0 else 99))
            else:
                prev_done = all(t >= mm[2] for mm in msgs[:idx])
                if not prev_done: continue
                if m[0] == "her" and m[2] - t < 0.55: typing = True
                if m[0] == "me" and not m[1].startswith("["):
                    td = type_dur(m[1]); st = m[2] - td - 0.12
                    if t >= st:
                        k = min(len(m[1]), int((t - st) / td * len(m[1])) + 1)
                        typed = m[1][:k]; ch = typed[-1].lower()
                        hl = ch if ch in KEYS else None
                break
        items = list(vis)
        if typing: items.append(("her", typing_bubble(fi), 99))
        spaces = []
        for i, it in enumerate(items):
            spaces.append(gap + (26 if i + 1 < len(items) and items[i + 1][0] != it[0] else 0))
        total = sum(b.height + sp for (_, b, _), sp in zip(items, spaces))
        target = max(0, top + total - bottom)
        scroll = target if scroll is None else scroll + (target - scroll) * 0.5
        img = base.copy()
        y = top - scroll
        for i, ((who, b, age), sp) in enumerate(zip(items, spaces)):
            a = min(1, age / 0.17)
            off = int((1 - a) * 30)
            if y + b.height > 440 and y < CHAT_BOTTOM + 20:
                if b.info.get("sys"): x = 30
                else: x = W - 30 - b.width if who == "me" else 110
                yy = int(y + off)
                layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                mask = b.info.get("mask")
                if who == "me" and mask is not None:
                    gy = max(0, min(yy + 700, H - b.height)); layer.paste(IG_GRAD.crop((x, gy, x + b.width, gy + b.height)), (x, yy), mask)
                layer.alpha_composite(b, (x, yy))
                last_in_group = who == "her" and not b.info.get("sys") and (i + 1 == len(items) or items[i + 1][0] != "her")
                if last_in_group:
                    layer.alpha_composite(SMALL_AV, (34, yy + b.height - 56))
                if a < 1:
                    layer.putalpha(layer.getchannel("A").point(lambda v: int(v * a)))
                img.alpha_composite(layer)
            y += b.height + sp
        # keep keyboard/input area clean
        img.paste(base.crop((0, CHAT_BOTTOM + 15, W, H)), (0, CHAT_BOTTOM + 15))
        if hl: draw_keyboard(img, hl)
        draw_input(img, typed, (fi // 15) % 2 == 0 or bool(typed))
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
    ss, dur_src, speed, src = section.get("src_start", 0), section["src_dur"], section.get("speed", 1.0), section["src"]
    cmd = ["ffmpeg", "-v", "error", "-ss", str(ss), "-t", str(dur_src), "-i", src,
           "-vf", f"setpts=PTS/{speed},fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    fi = 0
    while True:
        raw = p.stdout.read(W * H * 3)
        if len(raw) < W * H * 3: break
        fr = np.frombuffer(raw, np.uint8).reshape(H, W, 3)
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
                        "-pix_fmt", "yuv420p", TMP + "_v.mp4"], stdin=subprocess.PIPE)
count = [0]
def out(img):
    enc.stdin.write(img.convert("RGB").tobytes()); count[0] += 1

sfx = []
prior = []
base = dm_base(SCRIPT["name"])
for sec in SCRIPT["sections"]:
    t0 = count[0] / FPS
    if sec["type"] == "dm":
        start_prior = prior if sec.get("continue") else [tuple(h) for h in SCRIPT.get("history", [])]
        prior, ev = render_dm(sec, base, start_prior, out)
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
tk = np.arange(int(sr * 0.025)) / sr
click = np.random.RandomState(1).randn(len(tk)) * np.exp(-tk * 400) * 0.08
for t, w in sfx:
    add(t, click if w == "key" else pop_out if w == "me" else whoosh if w == "whoosh" else pop_in)
audio = np.clip(audio, -1, 1)
with wave.open(TMP + "_a.wav", "w") as wf:
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
    wf.writeframes((audio * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", TMP + "_v.mp4", "-i", TMP + "_a.wav", "-c:v", "copy",
                "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", OUT], check=True)
os.remove(TMP + "_v.mp4"); os.remove(TMP + "_a.wav")
print("done", OUT, round(total, 2), "s")
