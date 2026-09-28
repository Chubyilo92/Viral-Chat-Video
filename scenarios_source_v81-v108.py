import json
S = json.load(open('/home/claude/pipeline/scenarios.json'))
def add(feat, pov, hook, fight, clip, in_app, overlay, twist, bait, photo=None):
    S.append(dict(id=f"V{len(S)+1:02d}", feature=feat, pov=pov, hook=hook, fight=fight, clip=clip, in_app=in_app,
                  overlay=overlay, twist=twist, bait=bait, photo=photo, top=True))

add("C","him","my girlfriend's been secretly seeing my ex every 6 weeks",
 [["me","why is 'Megan ✂️ Sat 10am' in your calendar"],["me","MY Megan??"],["them","she's the only one who knows what I like"],["them","I'm not giving her up"]],
 "C-EVENT","Event 'Megan ✂️ Sat 10am', repeating every 6 weeks.",["every 6 weeks. for a YEAR."],
 [["them","she does my hair 😭"],["them","best balayage in Kent"],["them","she charges me less since you dumped her"],["me","she gives you a DISCOUNT??"]],
 "'Would you let your partner get their hair done by your ex?' is a huge split.")

add("C","her","'Babe 💕' is on his PlayStation every night till 2am",
 [["me","who is 'Babe 💕' on your PlayStation"],["me","every night. till 2am"],["them","she's the only one who gets me"],["me","SHE??"]],
 "C-ADD","He adds event 'Date night 🚫🎮 Fri 8pm'.",["2am. every night."],
 [["them","it's Dave 😭"],["them","we've called each other babe since Year 9"],["me","you said SHE"],["them","Dave's a she when he's healing"]],
 "Bromance names plus 'Dave's a she when he's healing'. Gamers will flood the comments.")

add("C","her","there's a ring in his drawer and it's too big for me",
 [["me","why is there a ring in your drawer"],["me","it's too big for me"],["me","so who is it for"],["them","someone very special"]],
 "C-EVENT","Event 'Collect ring 💍 Fri' in his calendar.",["too big. for me."],
 [["them","me 😭"],["them","it's a smart ring"],["them","it tracks my sleep"],["me","I've told my mum"]],
 "Proposal heartbreak played for laughs. 'She told her mum' gets quoted.")

add("C","her","his ex has been using our Netflix for 3 years",
 [["me","why is there a profile called 'Jess 🌸' on our Netflix"],["them","she's always been there"],["me","3 YEARS??"],["them","I didn't know how to kick her off"]],
 "C-ADD","She adds event 'Change Netflix password 🔒 TONIGHT'.",["she's on season 4 of OUR show"],
 [["them","update"],["them","I changed it"],["them","she messaged me asking for the new one"],["me","and??"],["them","I gave her yours"]],
 "'Kick your ex off Netflix' is a universal debate, and 'gave her yours' is chaos.")

add("C","him","her 'work husband' is taking her to lunch",
 [["them","can't talk, lunch with my work husband 🍝"],["me","your WHAT"],["them","he's been there for me through everything"],["me","I'm your actual husband"]],
 "C-EVENT","Event 'Lunch w/ work husband 🍝 Tue 1pm'.",["'work husband' 🙂"],
 [["them","it's Carol 😭"],["them","she's 63"],["them","she brings biscuits and hates everyone except me"],["me","Carol can have you"]],
 "'Work husband/wife' is a massive debate. Everyone has a Carol.")

add("B","her","he's slept with his phone face down every night since March",
 [["me","why is your phone always face down"],["me","every night since March"],["them","you know why"],["me","no I DON'T"]],
 "B-SCROLL","Her wishlist item 'Phone face down at night 📵 +10', Done 180×.",["since March."],
 [["them","the light wakes you up"],["them","you added it to your wishlist"],["them","I've done it 180 times"],["me","…I forgot I asked"]],
 "'Phone face down = cheating?' is one of the biggest debates on TikTok, and the reveal flips it.")

add("C","her","he's been going to a woman's house every Tuesday for 3 months",
 [["me","who is 'Linda 🚗 Tue 6pm'"],["them","she's patient with me"],["them","she said I'm the best she's ever had"],["me","EXCUSE ME??"]],
 "C-EVENT","Event 'Linda 🚗 Tue 6pm', repeating weekly.",["'the best she's ever had'"],
 [["them","driving lessons 😭"],["them","she said best student"],["them","I'm 31 and I wanted to drive you on dates"],["me","you told me you had a licence??"]],
 "'A man who can't drive at 31' roasts plus 'he lied about his licence'.")

add("B","her","he screenshotted another girl's Instagram story",
 [["them","Amara just messaged me"],["them","'why did your man screenshot my story'"],["me","WHY did you screenshot her story"],["them","I can explain"]],
 "B-ADD","He adds to her wishlist 'That dress from Amara's story 👗 +100', then Mark done.",["she got the NOTIFICATION"],
 [["them","the dress 😭"],["them","you said you loved it at dinner"],["them","it's arriving Friday"],["me","why didn't you just ASK"],["them","then it's not a surprise"]],
 "Screenshot-notification panic, then the 'just ask her' vs 'surprise' debate.")

add("B","him","my girlfriend's been married to another man for 2 years",
 [["them","I need to tell you something"],["them","I've been married for 2 years"],["them","we have 2 kids"],["me","WHAT"]],
 "B-ADD","He adds a gesture: 'Play Stardew WITH her 🎮 +25'.",["2 years. 2 kids."],
 [["them","in Stardew Valley 😭"],["them","his name's Sebastian"],["them","he's emo and he's always there"],["me","divorce him"],["them","never"]],
 "'Is a game marriage cheating' is a gamer-couple debate. Stardew fans will turn up in force.")

add("C","her","he's been lying about going to the gym",
 [["me","you said gym Tuesday and Thursday"],["me","your gym bag hasn't been opened in 2 months"],["them","…"],["me","WHERE ARE YOU GOING"]],
 "C-EVENT","Recurring event 'Gym 💪 Tue/Thu 7pm' with the note 'jollof class, don't tell her'.",["the gym bag hasn't moved"],
 [["them","cooking class 😭"],["them","I wanted to make your mum's jollof"],["them","so she stops looking at me like that"],["me","…is it Nigerian or Ghanaian"]],
 "Jollof wars are a guaranteed comment war, and 'learning her mum's recipe' is wholesome.")

add("R","him","she said I'm her 'second choice'",
 [["them","you know you were my second choice"],["me","what"],["them","it's fine, the first one said no"],["me","WHO WAS FIRST"]],
 "R-FLOW","Resolve: type 'she said I'm her second choice'. Reflect-back.",["took it to Resolve before I lost my mind"],
 [["them","your brother 😭"],["them","uni. 2019"],["them","he said no. then I met you"],["me","CHRISTMAS IS GOING TO BE AWKWARD"]],
 "Chaos. Comments split between 'she needs to go' and 'the brother knew'.")

add("C","him","she changed her passcode and won't tell me what it is",
 [["me","why did you change your passcode"],["them","because you'll never guess it"],["me","what are you hiding??"],["them","nothing you'd remember"]],
 "C-EVENT","Event 'Our anniversary 🥂' showing the date.",["3 days trying to get in"],
 [["them","it's our anniversary"],["them","you tried 14 times"],["them","every one wrong"],["me","…it's in the calendar isn't it"]],
 "'Test your partner: do they know your anniversary?' Comments will be full of confessions.")

add("C","her","someone's been in our flat while we're at work",
 [["me","someone's been in our flat"],["me","the bed's made and the towels are folded like a hotel"],["them","…"],["me","who has a KEY"]],
 "C-EVENT","Event 'Mum 🧽 Wed 11am', repeating weekly.",["folded. like. a. hotel."],
 [["them","my mum 😭"],["them","she's had a key since we moved in"],["them","she ironed my pants"],["me","SHE IRONED YOUR PANTS"]],
 "'Mother-in-law with a key' is one of the biggest UK couple debates.")

add("B","her","I found a receipt: dinner for two on the night he 'worked late'",
 [["me","receipt from Friday. table for 2"],["me","2 mains. 2 desserts. 2 cocktails"],["me","you said you were working late"],["them","I was hungry"]],
 "B-ADD","He adds a gesture: 'Take her for the 2-for-1 🍝 +25'.",["2 mains. 2 desserts."],
 [["them","it was just me 😭"],["them","it was 2-for-1"],["them","I wasn't wasting half a deal"],["me","you ATE BOTH"]],
 "'He ate both mains' gets men defending him and women losing it. Big split.")

add("R","him","she's not speaking to me because of what I did in her dream",
 [["them","I'm not talking to you today"],["me","why"],["them","you know what you did"],["me","I've been ASLEEP"],["them","exactly"]],
 "R-FLOW","Resolve: type 'she's angry about something I did in her dream'. Reflect-back.",["the app took HER side"],
 [["them","you kissed my cousin"],["them","in my dream"],["them","and you didn't even say sorry"],["me","it wasn't REAL"],["them","it felt real"]],
 "'Being mad at your partner for a dream' is a top-tier relatable debate.")

add("C","him","she changed her surname on Facebook and it's not mine",
 [["me","why is your surname different on Facebook"],["them","I changed it"],["me","to WHOSE"],["them","someone who'll actually commit"]],
 "C-EVENT","Her event in the shared calendar: 'Deadline 💍 31 Dec'.",["and then this appeared in our calendar"],
 [["them","YOURS 😭"],["them","I've changed it to yours"],["them","now hurry up"],["them","you've got till 31 December"]],
 "'Men taking too long to propose' is a huge debate. Wives and girlfriends will tag their partners.")

add("B","him","my girlfriend's been secretly talking to my ex",
 [["me","why are you messaging Jess"],["me","MY ex Jess"],["them","we've been talking for weeks"],["them","she's got something I want"]],
 "B-ADD","Her wishlist item 'Something he's NEVER bought his ex 🙄 +100'.",["'something I want' 😐"],
 [["them","she's selling everything you bought her on Vinted"],["them","I bought your Christmas jumper back"],["them","£4"],["me","why would you WEAR that"],["them","it's warm and she's losing"]],
 "'Wearing what your partner bought their ex' and Vinted petty energy.")

add("C","him","she leaves at 6am every morning in full makeup",
 [["me","where do you go at 6am in full glam"],["them","I have to be first"],["me","first for WHO"],["them","you wouldn't understand"]],
 "C-EVENT","Recurring event 'Tesco 🟡 6am'.",["full glam. 6am."],
 [["them","yellow stickers 😭"],["them","the reduced aisle"],["them","I got a whole salmon for 42p"],["me","why the MAKEUP"],["them","Janet's there"]],
 "UK yellow-sticker culture plus the Janet rivalry. The comments will be pure UK.")

add("C","him","a man called 'Uncle Ernie' sends my girlfriend money every month",
 [["me","who is Uncle Ernie"],["me","and why does he send you money every month"],["them","he's been generous since 2019"],["me","HOW generous"]],
 "C-EVENT","Recurring event 'Ernie day 💷 1st of the month'.",["'generous since 2019'"],
 [["them","£25"],["them","Premium Bonds 😭"],["them","ERNIE's the computer"],["me","you've won £25 in 5 years"],["them","and you've won me"]],
 "UK in-joke: Premium Bonds and ERNIE. Plus 'is it even worth it' money comments.")

add("R","her","he said my lasagne tastes exactly like his ex's",
 [["them","this tastes exactly like Jess's lasagne"],["me","EXCUSE ME"],["them","it's a compliment"],["me","how is that a COMPLIMENT"]],
 "R-FLOW","Resolve: type 'he compared my cooking to his ex's'. Reflect-back.",["took it to Resolve"],
 [["them","ok the app said explain"],["them","it tastes exactly like hers"],["them","because hers was Iceland too"],["me","…you KNEW??"],["them","I've always known"]],
 "Passing off a frozen lasagne as homemade is peak UK comment bait.")

add("R","him","she's been deleting her search history every night",
 [["me","why do you delete your search history every night"],["them","it's private"],["me","what are you googling at midnight"],["them","things I can't tell you"]],
 "R-FLOW","Resolve: type 'she hides her search history'. Reflect-back.",["'things I can't tell you'"],
 [["them","'how to tell my boyfriend I don't like football'"],["them","I've pretended for 3 years"],["me","YOU CRIED AT THE FINAL"],["them","I was bored"]],
 "'Faking hobbies for your partner' is a big debate, and 'you cried at the final' gets stitched.")

add("C","her","he sent me 'happy birthday Emma'. my name isn't Emma.",
 [["them","happy birthday Emma ❤️ still think about you"],["me","who is Emma"],["me","and why do you 'still think about' her"],["them","wait"]],
 "C-ADD","He adds event 'HER birthday 🎂 (not Emma's)', repeating yearly.",["'still think about you' 😐"],
 [["them","same birthday 😭"],["them","I wrote hers and yours at the same time"],["them","copy-paste"],["me","so EMMA got mine??"],["them","she said thank you"]],
 "'Texting your ex happy birthday' is a debate, and the copy-paste disaster makes it chaos.")

add("B","him","she said she's on Hinge 'just to check'",
 [["them","I've been on Hinge"],["me","WHAT"],["them","just to check something"],["me","check WHAT"]],
 "B-SCROLL","Her wishlist item 'Delete your Hinge 🗑️ +1000'.",["and then I saw her wishlist"],
 [["them","you're still on it"],["them","'looking for someone who laughs at my jokes'"],["them","since 2022"],["me","…I forgot it existed"],["them","1000 brownies. today."]],
 "The accusation flips onto him. 'Old dating profile still up = cheating?' is a massive debate.")

add("R","him","her best friend 'bestie 🫶' has a photo of them kissing",
 [["me","why has 'bestie' got a photo of you two kissing"],["them","we dated"],["me","YOU DATED YOUR BEST FRIEND??"],["them","briefly"]],
 "R-FLOW","Resolve: type 'her best friend is her ex'. Reflect-back.",["'briefly' 😐"],
 [["them","2 weeks"],["them","Year 7"],["them","he dumped me on MSN"],["me","does Year 7 even count"],["them","he says it does"]],
 "'Does Year 7 count as an ex?' plus the opposite-sex best friend debate. Very commentable.")

add("B","him","my girlfriend follows 12 of my exes on Instagram",
 [["me","why do you follow 12 of my exes"],["them","research"],["me","RESEARCH??"],["them","I needed to know what I'm dealing with"]],
 "B-SCROLL","Her wishlist with 'Remember my birthday (unlike with Jess) 🎂', 'Text back within the hour (unlike with Sophie)'.",["she built a WISHLIST from them"],
 [["them","every one of them said the same thing"],["them","'he forgets everything'"],["them","so now it's on my list"],["me","you interviewed my EXES?"],["them","3 of them are in a group chat now"]],
 "'Stalking your partner's exes' is a huge debate, and the exes' group chat is chaos.")

add("C","her","he moved our wedding date without telling me",
 [["me","why has our WEDDING moved in the calendar"],["them","I had to"],["me","HAD TO??"],["them","there was a clash"]],
 "C-EVENT","Event 'Wedding 💍' dragged from 1 June to 8 June.",["a 'clash' 🙂"],
 [["them","Champions League final 😭"],["them","1 June"],["me","you moved our WEDDING for FOOTBALL"],["them","the venue was £400 cheaper too"],["me","…fine"]],
 "Football vs the wedding is a guaranteed comment war. '£400 cheaper' flips it.")

add("C","him","a man came round at 8pm, stayed till midnight and left smiling",
 [["me","Ring doorbell says a man came at 8pm"],["me","left at midnight SMILING"],["them","he was amazing"],["them","4 hours and he didn't stop once"]],
 "C-EVENT","Event 'Electrician ⚡ 8pm' in the shared calendar.",["4 hours. smiling."],
 [["them","the electrician 😭"],["them","it's in the calendar"],["them","£240"],["me","that's why he was smiling"]],
 "Innuendo misdirect, then UK tradesman prices. 'It's in the calendar, you just don't read it' is the app point.")

add("B","him","my girlfriend's been spraying another man's aftershave on her pillow",
 [["me","why does your pillow smell of aftershave"],["me","it's not mine"],["them","it's the one I love"],["them","I can't sleep without it"]],
 "B-SCROLL","Her wishlist item 'Wear the old aftershave again 🧴 +25'.",["'the one I love' 😐"],
 [["them","it's YOUR old one 😭"],["them","before your mum bought you the new one"],["them","the new one smells like a car air freshener"],["me","…I've worn it for 2 years"],["them","I know"]],
 "'Tell him his aftershave is bad' and 'blame his mum'. Very relatable.")

json.dump(S, open('/home/claude/pipeline/scenarios.json','w'), ensure_ascii=False, indent=1)
print(len(S), sum(s['top'] for s in S))
