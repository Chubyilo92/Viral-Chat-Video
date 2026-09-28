import json
S={s['id']:s for s in json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'scenarios.json'))) if s['top']}
ANGRY=lambda v: "Jay" if S[v]['pov']=="him" else "Ella"
OTHER=lambda v: "Ella" if S[v]['pov']=="him" else "Jay"

# calendar events: id -> (creator, title, when, repeat, note)
NR="does not repeat"
CAL={
"V74":("Jay","Lads' night 🍻","Sat 19 Sep, 7:00pm",NR,None),
"V25":("Ella","Leave him","Mon 28 Sep, 5:30pm to 6:00pm",NR,"…alone for 30 mins when he gets in from work 🫡"),
"V76":("Jay","Lenny 🌙","Tue 29 Sep, all day",NR,None),
"V107":("Ella","Him ⚡","Wed 30 Sep, 8:00pm",NR,None),
"V14":("Jay","Sarah 🌸","Thu 1 Oct, 7:00pm",NR,"don't tell her"),
"V80":("Ella","Ali 🌙","Fri 2 Oct, 2:00am",NR,None),
"V19":("Jay","Ex's wedding 💍","Sat 3 Oct, all day",NR,"£900 🤝"),
"V64":("Jay","Sunday dinner 🍗 + Liam","Sun 4 Oct, 1:00pm",NR,"Added by Mum"),
"V98":("Ella","Janet 😤","Mon 5 Oct, 6:00am",NR,None),
"V85":("Ella","Lunch w/ work husband 🍝","Tue 6 Oct, 1:00pm",NR,None),
"V82":("Jay","Babe 💕🎮","Wed 7 Oct, 10:00pm",NR,None),
"V24":("Jay","Make her feel special 🙂","Thu 8 Oct, 6:00pm",NR,None),
"V83":("Jay","Collect ring 💍","Fri 9 Oct, all day",NR,None),
"V69":("Ella","Meeting him 😍","Sat 10 Oct, 11:00am",NR,None),
"V73":("Jay","Ask her dad ☕","Sun 11 Oct, 2:00pm",NR,None),
"V22":("Ella","Malaga ☀️","Mon 12 Oct to Thu 15 Oct, all day",NR,None),
"V75":("Ella","Exit plan 🚪","Sat 17 Oct, 2:00pm",NR,None),
"V79":("Ella","Josh's family 🏠","Sun 18 Oct, 1:00pm",NR,None),
"V67":("Jay","Jess 📞 / Priya 📞 / Chloe 📞 (three separate events)","Jess: Mon 19 Oct 7pm · Priya: Wed 21 Oct 7pm · Chloe: Fri 23 Oct 7pm",NR,None),
"V87":("Jay","Linda 🤍","Tue 20 Oct, 6:00pm",NR,None),
"V81":("Ella","Megan 🤍","Sat 24 Oct, 10:00am",NR,None),
"V90":("Jay","Gym 💪","Tue 27 Oct, 7:00pm",NR,None),
"V71":("Jay","Send £50 to my queen 👑","Sun 1 Nov, all day",NR,None),
"V99":("Ella","Ernie day 💷","Tue 1 Dec, all day",NR,None),
"V102":("Jay","Emma 🎂 AND Ella 🎂 (two separate events)","both on Sun 14 March 2027",NR,None),
"V106":("Jay","Wedding 💍","Tue 1 June 2027, all day",NR,None),
}
# resolve lines
RES={"V43":"he said I'm just like his mum","V44":"she's upset and I don't know how to say sorry","V63":"she sent our fight to her group chat",
"V68":"he's been sleeping at Sophie's","V72":"he said I love you to another woman","V78":"he checks my phone every night",
"V86":"he keeps his phone face down every night","V88":"she hired someone to follow me","V89":"she says she's been married for 2 years",
"V91":"she said I'm her second choice","V92":"she changed her passcode and won't tell me","V93":"someone has a key to our flat",
"V94":"he had dinner for two when he said he was working late","V95":"she's angry about something I did in her dream",
"V96":"she changed her surname and it's not mine","V100":"he compared my cooking to his ex's","V101":"she hides her search history",
"V103":"she's on Hinge just to check","V104":"her best friend is her ex","V108":"her pillow smells of another man's aftershave"}
MOOD={"V33":"In love 😍","V34":"Betrayed","V61":"Guilty","V65":"Annoyed"}

# recordings: code -> (phone, title, [ (vid, step text) ])
def cal_step(v):
    c,t,w,r,n=CAL[v]
    go = w.split(",")[0].replace(" to Thu 15 Oct","").replace("Jess: ","")
    base=f"Open Calendar. Go to {go}. Tap {c}'s event “{t}” to open it. Finger off the screen, count to 5, so the title"+(" and the note" if n else "")+" can be read. Go back to the calendar and count to 2 before the next one."
    if v=="V25": base="Open Calendar. Go to Mon 28 Sep. First hold 3 seconds on the day list showing “Leave him” at 5:30. Then tap it open so the note “…alone for 30 mins when he gets in from work 🫡” shows. Hold 5 seconds. Go back. Count to 2 before the next one."
    if v=="V67": base="Open Calendar in WEEK view for the week of Mon 19 Oct, so Monday “Jess 📞”, Wednesday “Priya 📞” and Friday “Chloe 📞” are all visible at once. Finger off, count to 5. Count to 2 before the next one."
    if v=="V102": base="Open Calendar. Go to Sun 14 March 2027. Finger off, count to 5 with both “Emma 🎂” and “Ella 🎂” showing on the same day. Go back. Count to 2 before the next one."
    if v=="V106": base="Open Calendar. Go to Tue 1 June 2027. Open “Wedding 💍”, change the date to Tue 8 June 2027 (drag it, or edit the date), and save. Show 8 June with “Wedding 💍” for 5 seconds. Count to 2 before the next one."
    if v=="V74": base="Open Calendar. Go to Sat 19 Sep. Tap your own event “Lads' night 🍻”. Finger off, count to 5. Go back. Count to 2 before the next one."
    return base
def res_step(v): return f"Open Resolve and start a new one. Type exactly: “{RES[v]}”. Continue until the screen that reflects it back with the TIME LEFT timer. Finger off, count to 5. Go back to the start of Resolve and count to 2 before the next one."
REC=[
("J1","Jay","Brownies – Ella's wishlist",[
 ("V03","Open Brownies → Ella's wishlist. Scroll slowly until “Flowers for no reason 💐 +25” is in the middle of the screen. Take your finger off the screen and count to 5. Don't tap anything."),
 ("V62","Keep scrolling until “Hall pass 🎫 +100” is in the middle of the screen. Finger off, count to 5."),
 ("V97","Keep scrolling until “Something he's NEVER bought his ex 🙄 +100” is in the middle of the screen. Finger off, count to 5."),
 ("V105","Keep scrolling until “Remember my birthday (unlike with Jess) 🎂” and “Text back within the hour (unlike with Leah)” are both on screen. Finger off, count to 5."),
 ("V01","Tap “I did this” on “Foot rub (10 mins)”, then on “Tea without me asking”, then on “Text me at lunch”, one after another. Then finger off, count to 3."),
 ("V09","Scroll until “Back rub, 10 mins 💆‍♀️ +25” is in the middle of the screen. Finger off, count to 2. Tap “I did this”. Finger off, count to 3."),
 ("V66","Tap “I did this” on “Bring the washing in”, then “Plan a date night”, then “Hug when I get home”. Then finger off, count to 3."),
 ("V77","Tap “I did this” on “Take the bins out”, then “Cook dinner Friday”, then “Fill my car up”. Then finger off, count to 3. Stop recording."),
]),
("J2","Jay","Calendar – Ella's events (+ your own Lads' night and the wedding)",[(v,cal_step(v)) for v in ["V22","V25","V69","V74","V75","V79","V80","V81","V85","V98","V99","V107","V106"]]),
("J3","Jay","Mood – Ella's mood (4 short recordings)",[(v,f"FIRST, on Ella's login, set her mood to “{MOOD[v]}”. THEN on Jay's login: open Mood, show Ella's mood “{MOOD[v]}” on screen and finger off, count to 5. Stop recording. (This is its own short recording.)") for v in ["V33","V34","V61","V65"]]),
("J4","Jay","Resolve – one full session on Jay's login",[("RJ","Open Resolve and start a session. Go through the whole thing, start to finish, following the app's steps. On EVERY new screen, take your finger off and count to 5 before tapping on. On the repeat-back step, let the TIME LEFT timer run for about 5 seconds so it visibly counts down. Stop recording at the end. (This one recording covers 12 videos: V44, V63, V88, V89, V91, V92, V95, V96, V101, V103, V104, V108.)")]),
("E1","Ella","Brownies – Ella's OWN wishlist",[("V70","Open Brownies → My wishlist (Ella's own). Scroll until “The ring 💍 +1000” is in the middle of the screen. Finger off, count to 5. Stop recording.")]),
("E2","Ella","Calendar – Jay's events (+ one you add live)",[(v,cal_step(v)) for v in ["V14","V19","V24","V64","V67","V71","V73","V76","V82","V83","V87","V90","V102"]]+[("V84","Tap + to add a new event. Type “Change Netflix password 🔒 TONIGHT”, set it for today (the day you record) at 9:00pm, and save. Finger off, count to 5 on the saved event. Stop recording.")]),
("E3","Ella","Resolve – one full session on Ella's login",[("RE","Same as J4, on Ella's login: start a session and go through every step, finger off and count to 5 on each new screen, let the timer run about 5 seconds on the repeat-back step. Stop at the end. (This one recording covers 8 videos: V43, V68, V72, V78, V86, V93, V94, V100.)")]),
]
where={}
for code,ph,title,items in REC:
    for i,(v,_) in enumerate(items,1): where[v]=(code,i,ph)
RJ=["V44","V63","V88","V89","V91","V92","V95","V96","V101","V103","V104","V108"]; RE=["V43","V68","V72","V78","V86","V93","V94","V100"]
for v in RJ: where[v]=("J4",1,"Jay")
for v in RE: where[v]=("E3",1,"Ella")
where.pop("RJ",None); where.pop("RE",None)
assert set(where)==set(S), set(S)-set(where)

WISH_ELLA=[("Foot rub (10 mins)","25"),("Tea without me asking","25"),("Text me at lunch","25"),("Back rub, 10 mins 💆‍♀️","25"),
 ("Flowers for no reason 💐","25"),("Hall pass 🎫","100"),("The ring 💍","1000"),("Something he's NEVER bought his ex 🙄","100"),
 ("Remember my birthday (unlike with Jess) 🎂","25"),("Text back within the hour (unlike with Leah)","25"),
 ("Bring the washing in","25"),("Plan a date night","25"),("Hug when I get home","25"),("Take the bins out","25"),("Cook dinner Friday","25"),("Fill my car up","25")]

why={}
for v,s in S.items():
    f=s['feature']
    if f=="C": why[v]="The calendar is the evidence the angry person finds. It proves something is going on but doesn't give away the twist."
    elif f=="R": why[v]="Instead of escalating, the angry person takes the fight to Resolve, which guides the argument and makes the listener repeat back what they heard. The twist only arrives afterwards in the DMs."
    elif f=="M": why[v]="Ella's mood is the evidence Jay sees on his phone. It makes the fight feel real, but the reason only comes out in the twist."
    else: why[v]="Jay is looking at Ella's wishlist. It either shows the evidence or shows him doing her wishlist to win her back."
why["V44"]="This is what Ella caught Jay doing: using Resolve to work out how to talk to her. So it comes from Jay's session."
why["V106"]="This shows what Jay did (moving the wedding). So it's filmed on Jay's phone, even though Ella is the angry one."
why["V70"]="Ella checks her own wishlist: the ring has been on it for 3 years and never done. It makes her angrier, and the £47.12 twist lands harder."
why["V74"]="Jay checks his own calendar: last Saturday he was out with the lads. That quietly plants the twist (the 14 calls were him)."
why["V01"]="Jay races through Ella's wishlist to beat 'the 6'2 man'."
why["V09"]="Ella pays a man £45 to hold her, so Jay does her back rub himself: 'I can hold you for free'."
why["V66"]="She's saved him as 'Mistake', so he's earning his name back one item at a time."
why["V77"]="She says his best mate is a better man, so he competes on her wishlist."

out=[]
for v in sorted(S, key=lambda x:int(x[1:])):
    s=S[v]; code,i,ph=where[v]
    out.append(dict(id=v, hook=s['hook'], angry=ANGRY(v), other=OTHER(v), dmname=("ella 🤍" if s['pov']=="him" else "jay 🤍"),
        fight=s['fight'], twist=s['twist'], overlay=s['overlay'], photo=s.get('photo'), rec=code, idx=i, phone=ph,
        step=(dict((x for c,p,t,items in REC if c==code for x in items)).get(v) or "Nothing extra to film. This clip comes from the full Resolve session in recording "+code+". I'll use a moment from it (the start, the speaking step, the repeat-back step with the timer, or the next step)."), why=why[v],
        setup=(CAL[v] if v in CAL else None)))
json.dump(dict(videos=out, recs=[dict(code=c,phone=p,title=t,items=[dict(id=v,step=st) for v,st in items]) for c,p,t,items in REC],
  cal=[dict(id=v,creator=c[0],title=c[1],when=c[2],repeat=c[3],note=c[4]) for v,c in sorted(CAL.items(),key=lambda x:(x[1][0],int(x[0][1:]))) if v!="V84"],
  wish=WISH_ELLA, mood=MOOD), open('plan.json','w'), ensure_ascii=False, indent=1)
print(len(out), "videos;", len(REC), "recordings")
