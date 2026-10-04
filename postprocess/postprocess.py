#!/usr/bin/env python3
"""Post-process rendered viral chat videos (output of build.py) into the final posting versions.

What it does to every video (see SPEC.md section 13 for the why):
  1. Replaces the old still home-screen + white splash (the first ~2s of the footage section)
     with the owner's real iPhone recording (assets/iphone_home_to_couplein.mp4):
     swipe across home pages -> tap CoupleIn -> iOS app-open zoom -> CoupleIn splash.
  2. Makes the HEADER and FOOTER match from the first frame to the last:
     - the same 9:41 status bar (assets/statusbar_template.png, cut from the chat render) on every
       section: chat, iPhone home screen, splash, app footage (black or white to suit the background);
     - the same iPhone home bar at the bottom of chat, splash and app footage
       (the home screen itself has none, like a real iPhone);
     - app footage is shifted down 100px so its own header sits under the status bar.
  3. Sets every still shot in the app footage to the time a viewer needs to read it
     (caption + on-screen evidence, minus time the caption was already on screen; never under 2s):
     too long -> trimmed, too short -> the frozen frame is held longer.
  4. Paints out the "Free Trial / N days left" card wherever it appears in the footage.
  5. Rebuilds the audio so every sound effect and the twist sting stay in sync.

Usage:
  python3 postprocess.py IN_DIR OUT_DIR V03 V80 ...      (IN_DIR holds V##.mp4 from build.py)
Needs: ffmpeg, Python 3 with numpy, Pillow, opencv-python-headless.
"""
import subprocess, numpy as np, json, wave, sys, os
from PIL import Image, ImageDraw, ImageFilter
import cv2

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, 'assets')
W, H, FPS = 1080, 1920, 30
SB_H = 100            # status bar band height
SHIFT = 100           # app footage shifted down by this much
MIN_HOLD = 2.0        # never trim a still shot below this (punchline needs a beat)
ORIENT, CAP_WPS, EV_WPS, BEAT = 0.4, 4.0, 4.0, 0.3   # reading model (seconds, words/sec)

# ---------------------------------------------------------------- video io
def readv(path):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', path, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    n = W * H * 3
    try:
        while True:
            b = p.stdout.read(n)
            if len(b) < n: break
            yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
    finally:
        p.stdout.close(); p.kill()

def small_frames(path, w=54, h=96, fmt='rgb24', ch=3):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'scale={w}:{h}', '-f', 'rawvideo',
                          '-pix_fmt', fmt, '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, ch).astype(int)

# ---------------------------------------------------------------- header / footer
_c = np.array(Image.open(os.path.join(ASSETS, 'statusbar_template.png')).convert('L')).astype(float)
SB_ALPHA = np.clip((_c[:SB_H] - 20) / 235, 0, 1)[..., None]
IND = (381, 1900, 699, 1911)          # home bar box, matches the real iPhone recording
_m = Image.new('L', (W * 2, H * 2), 0)
ImageDraw.Draw(_m).rounded_rectangle([IND[0] * 2, IND[1] * 2, IND[2] * 2, IND[3] * 2], 12, fill=255)
IND_A = np.array(_m.resize((W, H), Image.LANCZOS)).astype(float)[..., None] / 255

def draw_sb(f, color):
    f = f.astype(float); f[:SB_H] = f[:SB_H] * (1 - SB_ALPHA) + np.array(color, float) * SB_ALPHA; return f

def draw_ind(f, color):
    f = f.astype(float); y0, y1 = IND[1] - 4, IND[3] + 4
    a = IND_A[y0:y1]; f[y0:y1] = f[y0:y1] * (1 - a) + np.array(color, float) * a; return f

def u8(f): return np.clip(f, 0, 255).astype(np.uint8)

def chat_post(f):
    return u8(draw_ind(f, (255, 255, 255)))       # chat already has the status bar; add white home bar

def footage_post(f, sb_col, ind_col):
    g = np.empty_like(f); g[SHIFT:] = f[:H - SHIFT]; g[:SHIFT] = f[0:1]
    return u8(draw_ind(draw_sb(g, sb_col), ind_col))

# ---------------------------------------------------------------- iPhone transition (shared by all videos)
# source ranges (seconds) kept from the recording: home-page swipes, then the CoupleIn page -> tap -> app-open zoom.
# 0.78-1.65 is cut: a detour onto the Screen Time widget page and back, plus extra hold before the tap.
KEEP_RANGES = [(0.0, 0.78), (1.65, 2.50)]
LAUNCH_FROM = 2.0                       # from here the app card is opening: clean its mini status bar
SPLASH_FRAMES = 10

def iphone_frames():
    src_path = os.path.join(ASSETS, 'iphone_home_to_couplein.mp4')
    pts = [float(x.strip(',')) for x in subprocess.run(
        ['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'frame=pts_time', '-of', 'csv=p=0', src_path],
        capture_output=True, text=True).stdout.split()]
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', src_path, '-vsync', '0', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         capture_output=True).stdout
    sw, sh = 592, 1280
    src = np.frombuffer(raw, np.uint8).reshape(-1, sh, sw, 3)
    times = []
    for a, b in KEEP_RANGES:
        t = a
        while t < b - 1e-6: times.append(t); t += 1 / FPS
    fit_w = int(round(sw * H / sh)); padl = (W - fit_w) // 2
    out = []
    for t in times:
        i = int(np.argmin([abs(p - t) for p in pts]))
        f = np.array(Image.fromarray(src[i]).resize((fit_w, H), Image.LANCZOS)).astype(float)
        if t >= LAUNCH_FROM:            # remove the red recording pill + the card's own status icons
            top = f[:260]; R, G, B = top[..., 0], top[..., 1], top[..., 2]
            card = (f[262].min(1) > 225)[None, :]
            top[(R - (G + B) / 2 > 25) | ((top.max(2) < 215) & card)] = 255
            f[:260] = top
        f[:78] = f[78:79]               # erase native status bar (10:32 + red pill)
        canvas = np.zeros((H, W, 3))
        canvas[:, padl:padl + fit_w] = f
        canvas[:, :padl] = f[:, :6].mean(1, keepdims=True); canvas[:, padl + fit_w:] = f[:, -6:].mean(1, keepdims=True)
        bl = np.array(Image.fromarray(u8(canvas)).filter(ImageFilter.GaussianBlur(6))).astype(float)
        canvas[:, :padl] = bl[:, :padl]; canvas[:, padl + fit_w:] = bl[:, padl + fit_w:]
        out.append(u8(draw_sb(canvas, (0, 0, 0))))
    logo = Image.open(os.path.join(ASSETS, 'couplein_logo.png')).convert('RGB')
    lw = 300; lh = int(logo.height * lw / logo.width)
    sp = Image.new('RGB', (W, H), (255, 255, 255)); sp.paste(logo.resize((lw, lh), Image.LANCZOS), ((W - lw) // 2, (H - lh) // 2 - 20))
    out += [u8(draw_ind(draw_sb(np.array(sp), (0, 0, 0)), (0, 0, 0)))] * SPLASH_FRAMES
    return out

# ---------------------------------------------------------------- analysis
def segment(path):
    """Footage section = first long bright run. It starts with the old home screen (H),
    then a white splash (W), then the app footage (A). Returns Hs, A, E, N."""
    a = small_frames(path); m = a.mean((1, 2, 3)); N = len(m)
    bright = m > 90
    s = int(np.argmax(bright)); e = s
    while e < N and bright[e]: e += 1
    i = s
    while i < e and m[i] < 190: i += 1          # home screen
    while i < e and m[i] <= 245: i += 1
    while i < e and m[i] > 245: i += 1          # white splash
    return s, i, e, N

def still_runs(path, A, E, min_len=45):
    a = small_frames(path, 108, 192)[A:E]
    d = np.abs(np.diff(a, axis=0)).max(axis=(1, 2, 3)); still = d < 25
    runs = []; s = None
    for i, b in enumerate(still):
        if b and s is None: s = i
        if (not b or i == len(still) - 1) and s is not None:
            e = i if not b else i + 1
            if e - s >= min_len: runs.append((A + s, A + e + 1))
            s = None
    return runs

def caption_prior_seconds(path, A, s):
    """How long the caption box seen at frame s was already on screen before s."""
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf', f"select='between(n,{A},{s})'", '-vsync', '0',
                          '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W)
    band = fr[-1][1000:1600]; m = (band < 35).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    if n < 2: return 0.0
    k = 1 + np.argmax(st[1:, 4]); x, y, w, h = st[k, :4]
    tpl = band[y:y + h, x:x + w]; prior = 0
    for f in fr[-2::-1]:
        if cv2.matchTemplate(f[800:1800], tpl, cv2.TM_SQDIFF_NORMED).min() < 0.05: prior += 1
        else: break
    return prior / FPS

def reading_text(v, k=0):
    """caption + evidence for still shot k. reading.json wins (an entry may be a list, one per still shot); otherwise fall back to scenarios.json
    (overlay = caption, in_app = evidence). Check the on-screen text when adding new videos."""
    rj = os.path.join(HERE, 'reading.json')
    if os.path.exists(rj):
        d = json.load(open(rj))
        if v in d:
            e = d[v]
            if isinstance(e, list): e = e[min(k, len(e) - 1)]     # one entry per still shot, in order
            return e['caption'], e['evidence']
    sc = {s['id']: s for s in json.load(open(os.path.join(HERE, '..', 'scenarios.json')))}
    s = sc.get(v, {})
    print(f'  {v}: not in reading.json, using scenarios.json text (verify against the frame)')
    return ' '.join(s.get('overlay', [])), str(s.get('in_app', ''))

def paint_free_trial(f):
    g = f.astype(int); R, G, B = g[..., 0], g[..., 1], g[..., 2]
    org = ((R > 230) & (G > 120) & (G < 215) & (B < 100))[:, 100:520].sum(1)     # orange part of the trial bar
    ly = ((R > 238) & (G > 215) & (B > 90) & (B < 175))[:, 520:1030].sum(1)      # pale-yellow rest of the bar
    rows = np.where((org > 150) & (ly > 150))[0]
    if not len(rows): return f, False
    top = max(0, int(rows.min()) - 165)
    bg = np.median(f[top - 6:top - 2, 10:40].reshape(-1, 3), 0).astype(np.uint8)
    f = f.copy(); f[top:, :] = bg; return f, True

# ---------------------------------------------------------------- main
def process(v, in_dir, out_dir, TR):
    src = os.path.join(in_dir, f'{v}.mp4')
    Hs, A, E, N = segment(src); NT = len(TR)
    cuts, exts = [], {}      # trims (start, end) and extensions {last_frame: extra_frames}
    for k, (s, e) in enumerate(still_runs(src, A, E)):
        cap, ev = reading_text(v, k)
        prior = caption_prior_seconds(src, A, s)
        need = ORIENT + max(0, len(cap.split()) / CAP_WPS - prior) + len(ev.split()) / EV_WPS + BEAT
        kf = int(round(max(need, MIN_HOLD) * FPS))
        if e - s > kf: cuts.append((s + kf, e))
        elif kf - (e - s) >= 3: exts[e - 1] = kf - (e - s)   # still too short to read: hold it longer
    # output order as original intervals; piece index 1 is the iPhone transition
    pieces = [(0, Hs), (Hs, Hs + NT)]
    cur = A
    events = sorted([(cs, 'cut', ce) for cs, ce in cuts] + [(le + 1, 'ext', x) for le, x in exts.items()])
    for at, kind, val in events:
        pieces.append((cur, at))
        if kind == 'cut': cur = val
        else: pieces.append((at - val, at)); cur = at       # repeat the audio under the held frame
    pieces.append((cur, N))
    keep = np.zeros(N, bool)
    for s, e in [(0, Hs)] + [(A, N)]: keep[s:e] = True
    for cs, ce in cuts: keep[cs:ce] = False
    state = {'sb': None, 'ind': None}
    def pick(key, val):            # black/white status & home bar with hysteresis (no flicker)
        c = state[key]
        if c is None or (c == 'k' and val < 120) or (c == 'w' and val > 170): state[key] = 'k' if val >= 145 else 'w'
        return (0, 0, 0) if state[key] == 'k' else (255, 255, 255)
    painted = [0]
    def frames():
        for i, f in enumerate(readv(src)):
            if i == Hs:
                for t in TR: yield t
            if keep[i]:
                if A <= i < E:
                    f, p = paint_free_trial(f); painted[0] += p
                    g = footage_post(f, pick('sb', float(f[0:60].mean())), pick('ind', float(f[1790:1820, 380:700].mean())))
                    for _ in range(1 + exts.get(i, 0)): yield g
                else:
                    yield chat_post(f)
    # audio: each kept piece keeps its own original audio, joined with 40ms crossfades
    wav_in = os.path.join(out_dir, f'{v}_o.wav'); wav_out = os.path.join(out_dir, f'{v}_a.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vn', '-ac', '1', '-ar', '44100', wav_in])
    w = wave.open(wav_in); sr = w.getframerate(); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float)
    a = np.concatenate([a, np.zeros(sr)])
    total = sum(e - s for s, e in pieces); out = np.zeros(int(total / FPS * sr) + sr); fd = int(0.04 * sr); pos = 0
    for idx, (s, e) in enumerate(pieces):
        s0, e0, p0 = int(s / FPS * sr), int(e / FPS * sr), int(pos / FPS * sr)
        lo = fd if idx > 0 else 0; hi = fd if idx < len(pieces) - 1 else 0
        sa = a[max(0, s0 - lo):e0 + hi].copy()
        if lo: sa[:2 * lo] *= np.linspace(0, 1, 2 * lo)
        if hi: sa[-2 * hi:] *= np.linspace(1, 0, 2 * hi)
        out[p0 - lo:p0 - lo + len(sa)] += sa; pos += e - s
    out = out[:int(total / FPS * sr)]
    o = wave.open(wav_out, 'wb'); o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr)
    o.writeframes(np.clip(out, -32768, 32767).astype(np.int16).tobytes()); o.close()
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                          '-i', '-', '-i', wav_out, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '20', '-preset', 'slow',
                          '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart',
                          os.path.join(out_dir, f'{v}.mp4')], stdin=subprocess.PIPE)
    n = 0
    for f in frames(): p.stdin.write(f.tobytes()); n += 1
    p.stdin.close(); p.wait(); os.remove(wav_in); os.remove(wav_out)
    print(f'{v}: {N / FPS:.2f}s -> {n / FPS:.2f}s  trims={[(round(s / FPS, 2), round(e / FPS, 2)) for s, e in cuts]}  holds_extended={ {round((k+1)/FPS,2): round(x/FPS,2) for k, x in exts.items()} }  free-trial frames painted={painted[0]}', flush=True)

if __name__ == '__main__':
    in_dir, out_dir, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
    os.makedirs(out_dir, exist_ok=True)
    TR = iphone_frames()
    for v in ids: process(v, in_dir, out_dir, TR)
