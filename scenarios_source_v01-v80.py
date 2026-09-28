# 60 CoupleIn rage-bait -> app -> twist scenarios
# me = the person raging (narrator, right-hand sent bubbles); them = partner (incoming)
# feature codes: B=Brownies, C=Calendar, M=Mood, R=Resolve, S=Streak/Score
import json

S = []
def add(feat, pov, hook, fight, clip, in_app, overlay, twist, bait, photo=None, top=False):
    S.append(dict(id=f"V{len(S)+1:02d}", feature=feat, pov=pov, hook=hook, fight=fight, clip=clip,
                  in_app=in_app, overlay=overlay, twist=twist, bait=bait, photo=photo, top=top))

# ---------------- BROWNIES ----------------
add("B", "him", "she said she met someone taller than me 😐",
    [["them","I met someone 😍"],["them","he's 6'2, never forgets anything and does whatever I ask"],["me","are you being serious rn"],["them","he's literally perfect"],["me","SEND ME HIS NAME"]],
    "B-MARK", "Tap Mark done on 3 items in a row: 'Foot rub (10 mins)', 'Tea without being asked', 'Text her at lunch'. Score visibly climbs.",
    ["so I did her whole wishlist in 4 minutes", "+75 🤎"],
    [["them","babe 😭"],["them","it's the cat"],["them","[PHOTO]"],["them","…but don't stop, you're on a roll"]],
    "'The cat is NOT 6'2' vs 'cats DO NOT do whatever you ask'. Two contradictions for the comments to fight over.", photo="cat", top=True)

add("B", "him", "apparently a man brings my girlfriend coffee every single morning",
    [["them","someone brings me a flat white every morning"],["them","oat milk. extra hot. he just KNOWS"],["me","who"],["them","you'd never"],["me","I'm coming to your work"]],
    "B-ADD", "Add a gesture: type 'Flat white, oat, extra hot ☕' and set it to +25.",
    ["adding it to my list before HE does it again"],
    [["them","it's Barry 😭"],["them","he's 71 and it's his coffee van"],["them","I pay him £3.40"],["them","but yours is free so you're winning"]],
    "'She PAYS him, that's not the same' vs 'Barry is the real one'.")

add("B", "him", "someone sent my girlfriend flowers at work. it wasn't me.",
    [["them","someone just sent me flowers at work 💐"],["them","the card says 'you deserve this x'"],["me","that wasn't me"],["them","I know it wasn't you 🙂"],["me","then WHO"]],
    "B-SCROLL", "Scroll her wishlist to 'Flowers for no reason 💐 +25' showing 'Done 0×'.",
    ["it's been on her list for 4 months. done 0 times."],
    [["them","me. I sent them to myself"],["them","signed from you. the girls think you're amazing now"],["them","you owe me £38 and I'm marking it done 🤎"]],
    "'She's a genius' vs 'that's manipulative'. Also 'he should be embarrassed'.", top=True)

add("B", "him", "why is 'a night with Marco' on my girlfriend's wishlist",
    [["me","why is 'a night with Marco 🌙' on your wishlist"],["me","for 25 brownies??"],["them","because I want a night with Marco"],["them","and you're going to make it happen"]],
    "B-SCROLL", "Her wishlist item 'A night with Marco 🌙 +25'. Zoom on it.",
    ["25 brownies for another man??"],
    [["them","Marco's is the pizza place 😭"],["them","Tuesday 2-for-1"],["me","that's not worth 25"],["them","it's worth 50 and you know it"]],
    "'2-for-1 pizza night IS a top-tier date' vs 'she deserves better than a deal'.")

add("B", "her", "found a £140 Pandora receipt in his jacket and it's not my birthday",
    [["me","who is the Pandora for"],["me","£140. yesterday. and it's not my birthday"],["them","don't open anything"],["me","DON'T OPEN ANYTHING??"]],
    "B-SCROLL", "His view of her wishlist: 'Pandora charm, the little house 🏠 +65'.",
    ["he sent me a screenshot of MY wishlist…"],
    [["them","item 3 babe"],["them","we get the keys on Friday"],["them","I was gonna mark it done then"],["me","I'm crying at my desk"]],
    "'£140 for a charm is mad' vs 'that's the bare minimum'. Plus 'house charm for the keys 😭'.")

add("B", "him", "she's making me earn points for a kiss now",
    [["them","new rule"],["them","kiss goodbye in the morning is worth 10 brownies"],["me","you're pricing KISSES"],["me","this is a relationship not Tesco Clubcard"]],
    "B-ADD", "Add a gesture: 'Kiss goodbye in the morning 😘 +10'.",
    ["fine. let's play."],
    [["them","it's 8:40am"],["them","you've kissed me goodbye 7 times"],["them","you're not even leaving"],["me","points are points"]],
    "'Gamifying love is dystopian' vs 'this is the cutest thing ever'. This is exactly the debate the app lives on.", top=True)

add("B", "him", "she put 'stop saying calm down' on her wishlist. for 100 brownies.",
    [["me","100 brownies to not say calm down??"],["me","the dishwasher is only 25"],["them","correct"],["me","that's insane"],["them","calm down"]],
    "B-SCROLL", "Her wishlist item 'Never say calm down 🤐 +100'.",
    ["100. for WORDS."],
    [["me","you just said it"],["them","I'm allowed, I'm not on the list"],["me","add it to MY list then"],["them","it's worth 5 on yours 🙂"]],
    "'Double standard' vs 'never say calm down to a woman, full stop'.")

add("B", "her", "his mate called me high maintenance and he LAUGHED",
    [["me","Dan called me high maintenance and you laughed"],["them","I didn't laugh laugh"],["me","you laughed with your whole chest"],["them","ok let me show him something"]],
    "B-SCROLL", "Scroll her wishlist: 'A hug when I get home +5', 'Text me when you land +5', 'Bring the washing in +10'.",
    ["he sent Dan my wishlist 👀"],
    [["them","Dan says sorry"],["them","he said 'she just wants a hug and the washing in??'"],["them","and now his girlfriend wants the app"]],
    "'Low maintenance is a trap' vs 'this is what men should be doing anyway'. Picks sides on Dan.")

add("B", "him", "she's been paying another man to hold her",
    [["them","I pay him £45 and he holds me for an hour"],["them","best hour of my week"],["me","WHO"],["them","he's got the strongest hands"]],
    "B-ADD", "Add a gesture: 'Back rub, 10 mins 💆‍♀️ +25', then Mark done.",
    ["I can hold you for FREE"],
    [["them","it's a massage 😭"],["them","it's a Groupon"],["them","but yours was better tbh"],["me","was it tho"]],
    "'Male massage therapist = cheating?' A huge, reliable comment war.", top=True)

add("B", "him", "found another man's hoodie in her drawer",
    [["me","whose hoodie is in your drawer"],["them","someone I love very much"],["me","it's grey. I don't own grey"],["them","you did once"]],
    "B-SCROLL", "Her wishlist item 'Let me keep your hoodie forever 🩶 +25'.",
    ["and then I saw her wishlist"],
    [["them","it's yours 😭"],["them","from our first date"],["them","you said you 'lost' it"],["them","25 brownies and it's legally mine"]],
    "'Hoodie theft is a love language' vs 'give it back'. Grey hoodie detail gets argued.")

add("B", "him", "my girlfriend added 'fix the shelf' 11 months ago",
    [["them","reminder the shelf is still on my list"],["me","I'll do it this weekend"],["them","you said that in November"],["me","it's only 25 brownies"]],
    "B-SCROLL", "Her wishlist 'Fix the shelf 🔨' with points edited to +250 and 'added 11 months ago' visible if possible.",
    ["it's 250 brownies now 💀"],
    [["them","inflation"],["me","that's not how points work"],["them","it is now"],["me","…where's the drill"]],
    "Men vs women on the 11-month shelf. Every couple has a shelf.")

add("B", "her", "he's been keeping a secret folder called 'Her 🔒'",
    [["me","why is there a note on your phone called 'Her 🔒'"],["them","don't open it"],["me","already opened it"],["them","then why are you asking"]],
    "B-ADD", "His gestures list with small peculiar items: 'No coriander. ever.', 'Blue M&Ms only', 'Sing in the car = don't laugh'.",
    ["it's a list of… me"],
    [["me","'blue M&Ms only'??"],["them","you pick them out and think I don't notice"],["me","I'm not crying you're crying"]],
    "'Checking his phone was toxic' vs 'she found GOLD'. Phone-checking debate is massive.")

add("B", "him", "she nudged me 14 times in one hour",
    [["me","why have I got 14 nudges"],["them","you know why"],["me","the bins?"],["them","not the bins"],["me","then WHAT"]],
    "B-NUDGE", "Show 'Put the bins out 🗑️' and the Nudge button being tapped (or nudge notifications stacking).",
    ["14. nudges."],
    [["them","ok it was the bins"],["them","it's always the bins"],["me","you said NOT the bins"],["them","I lied. bins."]],
    "'Just do the bins bro' vs 'then why say not the bins'. Simple and universal.", top=True)

# ---------------- CALENDAR ----------------
add("C", "her", "why is there a 'Sarah 🌸 7pm' in our shared calendar",
    [["me","who is Sarah"],["me","and why is she in OUR calendar"],["them","it's nothing"],["me","7pm Thursday with a flower emoji?"],["them","she's very important to me ok"]],
    "C-EVENT", "Open event 'Sarah 🌸 7pm' with note 'don't tell her'.",
    ["'don't tell her' 🙂"],
    [["them","Sarah is the dog 😭"],["them","it's her grooming appointment"],["them","'don't tell her' because she hates the groomer"],["me","who names a dog Sarah"]],
    "'Who names a dog Sarah' plus 'why write don't tell her'. Two threads.", top=True)

add("C", "him", "she's got a date on Friday. restaurant booked and everything.",
    [["them","can't do Friday, I've got a date"],["them","8pm. the Italian. he booked it weeks ago"],["me","who is HE"],["them","someone who plans things for once"]],
    "C-EVENT", "Friday event 'Date night 🍝 8pm', showing it was added by him.",
    ["so I checked the calendar…"],
    [["them","you 😭"],["them","you booked it in the app 3 weeks ago"],["me","…I knew that"],["them","you did not know that"]],
    "'How do you forget your own date' vs 'this is why men need reminders'.")

add("C", "him", "a man texts my girlfriend 'good morning beautiful' at 6am every day",
    [["me","who is 'D' and why does he text you good morning beautiful"],["them","he's done it for years"],["them","never missed a single day"],["me","YEARS??"]],
    "C-ADD", "Create a recurring event 'Good morning text ☀️ 7:00 daily'.",
    ["setting a reminder so I never lose to him again"],
    [["them","D is my dad 😭"],["them","and he's beaten you 3 years running"],["me","not anymore"]],
    "'Dad calling his daughter beautiful is the standard' vs 'men learn from this'.")

add("C", "her", "he put 'last day 💔' in our calendar for Friday",
    [["me","what does 'last day 💔' on Friday mean"],["me","last day of WHAT"],["them","you'll see"],["me","are you breaking up with me through the calendar"]],
    "C-EVENT", "Friday event 'Last day 💔' and Saturday event 'Nando's 🔥 7pm'.",
    ["then I scrolled to Saturday…"],
    [["them","last day of my diet 😭"],["them","Saturday is Nando's"],["them","I've booked it, it's in there too"]],
    "'Using 💔 for a diet is psychopath behaviour' plus lemon & herb vs extra hot.")

add("C", "him", "she put 'tell him tonight 😬 9pm' in the calendar",
    [["me","what are you telling me at 9pm"],["them","why are you reading my calendar"],["me","IT'S A SHARED CALENDAR"],["them","just be home by 9"]],
    "C-EVENT", "Event 'Tell him tonight 😬 9pm'.",
    ["longest 6 hours of my life"],
    [["them","I ate your leftover Chinese"],["them","on Tuesday"],["them","it's been eating me alive"],["me","I thought you were PREGNANT"]],
    "'Eating his leftovers IS a 9pm conversation' vs 'she's got to go'. Food crimes always get comments.")

add("C", "her", "he's going to his ex's wedding. it's in our calendar.",
    [["me","'Ex's wedding 💍 Sat'???"],["me","you're GOING?"],["them","I have to"],["me","you don't HAVE to do anything"]],
    "C-EVENT", "Saturday event 'Ex's wedding 💍' with note '£900 🤝'.",
    ["£900??"],
    [["them","I'm the photographer 😭"],["them","she's paying £900"],["them","that's Tenerife babe"],["me","…get her good angles"]],
    "'Would YOU go to your ex's wedding?' Everyone has an opinion.", top=True)

add("C", "her", "he put 'pick up baby 👶 3pm' in his calendar",
    [["me","WHOSE BABY"],["them","ours"],["me","WE DON'T HAVE A BABY"],["them","we do from 3pm"]],
    "C-EVENT", "Event 'Pick up baby 👶 3pm'.",
    ["I've never run home so fast"],
    [["them","[PHOTO]"],["them","the air fryer came in at Argos"],["them","she's 5.5 litres"],["me","you named the air fryer baby"]],
    "'Air fryer IS the baby' vs 'she should leave'. Air fryer content always does numbers.", photo="air fryer box")

add("C", "him", "she's been at 'Tom's' every Tuesday for 2 months",
    [["me","who is Tom"],["me","every Tuesday, 7pm, for 2 months"],["them","he's very hands on"],["me","HANDS ON??"]],
    "C-EVENT", "Recurring event 'Tom's 💪 Tue 7pm'.",
    ["every. single. Tuesday."],
    [["them","he's my PT 😭"],["them","he's 58 and 5'4"],["them","I'm training for your birthday hike"]],
    "'A PT is a red flag' vs 'insecure much'. Big debate every time.", top=True)

add("C", "her", "Ryan booked her flights to Malaga. again.",
    [["me","why did you get an email from Ryan at 1am"],["me","the SAME Ryan who took you to Malaga last year?"],["them","it's not what you think"],["me","it's exactly what I think"]],
    "C-EVENT", "Event 'Malaga ☀️ 12 to 15 Oct' in the shared calendar.",
    ["then this appeared in OUR calendar"],
    [["them","Ryanair babe 😭"],["them","it's for us"],["them","and yes, Malaga again. the hotel was that good"]],
    "'Taking your new partner to the place your ex took you' is a debate magnet.", top=True)

add("C", "him", "my girlfriend added 'Lawyer 📑 Mon 9am' to the calendar",
    [["me","why are we seeing a lawyer"],["them","it's time"],["me","time for WHAT"],["them","to make it official"]],
    "C-EVENT", "Event 'Lawyer 📑 Mon 9am' with note 'bring Biscuit'.",
    ["'bring Biscuit'??"],
    [["them","we're writing our wills 😭"],["them","Biscuit gets the sofa"],["me","the dog gets the sofa??"],["them","she earned it"]],
    "'Pets in wills' plus 'the dog gets the sofa'. Wholesome chaos.")

add("C", "her", "he set a REMINDER to make me feel special",
    [["me","'Make her feel special 🙂 Thu 6pm'??"],["me","you need a REMINDER??"],["them","yes"],["me","so none of it is real"]],
    "C-EVENT", "Recurring event 'Make her feel special 🙂 every Thursday'.",
    ["every Thursday for 6 months"],
    [["them","the Thursday flowers?"],["them","the Thursday takeaways?"],["them","all the reminder"],["me","…ok they were really good Thursdays"]],
    "'Needing a reminder is unromantic' vs 'at least he DOES it'. This is the app's core debate.", top=True)

add("C", "him", "she put 'Leave him 🏃‍♀️ 5:30' in her calendar",
    [["me","'leave him' at 5:30??"],["them","yes"],["me","today??"],["them","every day"]],
    "C-EVENT", "Recurring event 'Leave him alone 🫡 5:30 to 6:00' (the title gets cut off in the list view).",
    ["then I opened it"],
    [["them","leave him ALONE"],["them","your 30 mins after work"],["them","you said you need it"],["me","…I'd marry you but you'd put it in the calendar"]],
    "'Men need 30 minutes after work' is a massive debate.", top=True)

add("C", "him", "she put 'Bin him 🗑️' in the calendar for Thursday",
    [["me","'bin him' Thursday??"],["them","yep"],["me","after 4 years??"],["them","it's overdue tbh"]],
    "C-EVENT", "Event 'Bin him 🗑️ Thu 7am'.",
    ["overdue."],
    [["them","it's the big green one 😭"],["them","it's bin day"],["them","'him' is the bin"],["me","why is the bin a him"]],
    "'Why is the bin a him' plus bin-day wars.")

add("C", "her", "'Your ex's birthday 🎂' is in HIS calendar",
    [["me","why is my ex's birthday in your calendar"],["them","…"],["me","you added it 3 YEARS ago"],["them","I can explain"]],
    "C-EVENT", "Yearly event 'Her ex's birthday 🎂 👀'.",
    ["the 👀 though"],
    [["them","so I'd know when he posts"],["them","and when you'd see it"],["them","I've been checking your mood every year on that day"],["me","that's either the sweetest or scariest thing ever"]],
    "Sweet or scary? The comments will split 50/50.")

add("C", "her", "he texted 'I'm leaving' at 5pm and then nothing",
    [["them","I'm leaving"],["me","what"],["me","leaving WHAT"],["me","answer me"],["me","I'm calling your mum"]],
    "C-EVENT", "Event 'Leave work 5pm, cook her pasta 🍝'.",
    ["20 minutes of no reply"],
    [["them","the office 😭"],["them","I was driving"],["them","pasta's on"],["me","finish a sentence ONCE in your life"]],
    "'Men and incomplete texts' is a universal debate.")

add("C", "her", "he's been lying about where he goes on Saturday mornings",
    [["me","where do you go on Saturdays"],["them","gym"],["me","your gym bag hasn't moved in 3 weeks"],["them","…"]],
    "C-EVENT", "Recurring locked event 'Saturday 10am 🔒'.",
    ["🔒"],
    [["them","dance lessons"],["them","for the first dance"],["them","I didn't want you to see me being bad"],["me","SHOW ME RIGHT NOW"]],
    "'Men secretly learning the first dance' does huge shares. The lie debate keeps comments going.")

add("C", "her", "he booked a stag do to Prague on my birthday",
    [["me","'Stag do Prague 🍻' on MY birthday??"],["them","check again"],["me","I don't need to check"],["them","check the year"]],
    "C-EVENT", "Event 'Stag do Prague 🍻' dated 2027.",
    ["…2027"],
    [["them","it's next year"],["them","and I'm moving it"],["me","why are you planning a stag a YEAR ahead"],["them","that's what the app's for"]],
    "'Planning a year ahead: organised king or red flag?'")

add("C", "him", "she's meeting a woman called Alexa every night",
    [["them","me and Alexa every night before bed"],["me","who"],["them","she reminds me of everything you forget"],["me","that's aggressive"]],
    "C-ADD", "Add 3 events fast: 'Her mum's birthday 🎂', 'Our anniversary 🥂', 'Pick her up from work drinks 11pm 🚗'.",
    ["so I replaced Alexa"],
    [["them","ok why did I just get a notification to take ME to dinner"],["me","Alexa's fired"],["them","she's crying in the kitchen"]],
    "'Alexa is the real girlfriend' plus 'men with reminders are better men'.")

# ---------------- MOOD ----------------
add("M", "him", "her mood just changed to 'heartbroken' and I'm at work",
    [["me","why is your mood heartbroken 💔"],["me","what did I do"],["them","you know what you did"],["me","I LITERALLY DON'T"]],
    "M-VIEW", "Partner's mood showing 'Heartbroken 💔'.",
    ["spent 3 hours thinking about everything I've ever done"],
    [["them","nothing to do with you 😭"],["them","Bake Off sent Priya home"],["them","her Swiss roll was PERFECT"],["me","then why say you know what you did"]],
    "'Why say you know what you did' plus Bake Off loyalty.", top=True)

add("M", "him", "she set her mood to 'in love' while I'm at work",
    [["me","who are you in love with right now"],["me","I'm at work"],["them","don't worry about it"],["them","he's warm, he's flaky, he's always there for me"]],
    "M-VIEW", "Partner's mood showing 'In love 😍'.",
    ["warm. flaky. always there."],
    [["them","[PHOTO]"],["them","£1.35 and never lets me down"],["me","you set a MOOD for a sausage roll"]],
    "'Greggs sausage roll vs the vegan one' plus 'flaky 😭'. UK comments go crazy.", photo="sausage roll", top=True)

add("M", "him", "her mood says 'betrayed' and I know exactly why",
    [["them","I know what you did last night"],["me","what did I do"],["them","you were with HER"],["me","WITH WHO"]],
    "M-VIEW", "Partner's mood showing 'Betrayed 🗡️'.",
    ["betrayed??"],
    [["them","you finished Love Island without me"],["them","I saw 'continue watching: final'"],["me","…I was going to act surprised"]],
    "'Watching ahead IS cheating' is one of the biggest couple debates online.", top=True)

add("M", "her", "she's been 'hangry' for 3 hours and I did nothing",
    [["me","3 HOURS"],["me","my mood's been hangry for 3 hours"],["me","and you've done nothing"],["them","I didn't see"],["me","IT'S ON THE APP"]],
    "M-VIEW", "Partner's mood 'Hangry 😤' with timestamp.",
    ["the silence 🙂"],
    [["them","open the door"],["them","[PHOTO]"],["them","been outside 10 mins"],["them","wanted to see how long you'd last"]],
    "'He let her suffer on purpose' vs 'legend'.", photo="Nando's bag at the door")

add("M", "her", "he set his mood to sad and wouldn't tell me why",
    [["me","why is your mood sad 😔"],["me","talk to me"],["them","I can't talk about it"],["me","is it us??"],["them","it's bigger than us"]],
    "M-VIEW", "Partner's mood 'Sad 😔'.",
    ["'bigger than us' 😐"],
    [["them","Arsenal"],["me","I've been crying in the toilets at work"],["them","so have I"]],
    "Football fans vs everyone. The 'bigger than us' line gets quoted.")

add("M", "him", "she said 'I'm fine 😊' but her mood says 🔥",
    [["me","you ok?"],["them","I'm fine 😊"],["me","your mood says furious"],["them","I said I'm fine"]],
    "M-VIEW", "Partner's mood '🔥' (or 'Hot 🥵' if that's an option).",
    ["the smiley face is the scariest part"],
    [["them","I AM fine"],["them","I picked it because I'm HOT"],["them","it's 31 degrees and you've got the heating on"]],
    "'Women saying fine' plus UK heat vs the heating.")

add("M", "him", "she set her mood to 'butterflies' at 2am",
    [["me","who's giving you butterflies at 2am"],["them","someone I shouldn't have let in"],["me","LET IN??"],["them","it was a mistake"]],
    "M-VIEW", "Partner's mood 'Butterflies 🦋'.",
    ["2am. let in."],
    [["them","the prawn crackers"],["them","I let them in at 11pm"],["them","it's not butterflies it's regret"]],
    "'Prawn crackers after 11pm' plus 'why pick butterflies then'.")

add("M", "her", "he's been checking my mood every hour",
    [["me","why have you checked my mood 9 times today"],["me","are you monitoring me??"],["them","maybe"],["me","that's actually creepy"]],
    "M-VIEW", "Show opening partner's mood screen a few times (or 'viewed' state).",
    ["9 times."],
    [["them","you had your big presentation"],["them","I was waiting for 'happy' so I could send the cake"],["them","it's at reception"]],
    "'Monitoring vs caring' is exactly the objection people raise about couple apps.")

add("M", "him", "her mood says 'proud' and it's not about me",
    [["me","proud of who?"],["them","someone special got promoted today"],["me","I didn't get promoted"],["them","I know"]],
    "M-VIEW", "Partner's mood 'Proud 🥹'.",
    ["someone special 🙂"],
    [["them","I did"],["them","I'm proud of ME"],["them","you just forgot to ask how it went"],["me","…where do you want to eat"]],
    "'He forgot to ask' hits hard, with a big 'men don't ask questions' debate.")

add("M", "her", "his mood says 'jealous' and I'm just sitting here",
    [["me","why are you jealous"],["them","you know why"],["me","I'm on the sofa"],["them","exactly. with HIM"]],
    "M-VIEW", "Partner's mood 'Jealous 😒'.",
    ["with who??"],
    [["them","the heated blanket"],["them","you've been under it 4 hours"],["them","you said I was your heated blanket"]],
    "'The heated blanket IS better' plus 'men being jealous of objects'.")

# ---------------- RESOLVE ----------------
add("R", "him", "she won't speak to me because I 'breathe too loud'",
    [["them","can you breathe quieter"],["me","I'm breathing"],["them","you're breathing AT me"],["me","how do I breathe AT you"]],
    "R-FLOW", "In Resolve type: 'she says I breathe at her'. Show the reflect-back prompt and TIME LEFT timer.",
    ["took it to the app"],
    [["them","ok I read your side in the app"],["them","…fine I was hungry"],["them","breathe all you want. bring snacks"]],
    "'Breathing AT someone is real' gets surprisingly heated comments.", top=True)

add("R", "her", "he told me I'm 'just like his mum'",
    [["them","you're just like my mum"],["me","excuse me??"],["me","say that again"],["them","it was a compliment"],["me","it was NOT"]],
    "R-FLOW", "Resolve: type 'he said I'm like his mum', then the reflect-back.",
    ["the app made him explain himself"],
    [["them","she ran a business, raised 4 kids and never forgot a birthday"],["them","that's the highest thing I can say"],["me","…I'll allow it"]],
    "'Compliment or red flag?' is a guaranteed comment war.", top=True)

add("R", "her", "he asked an APP how to talk to me",
    [["me","you asked an APP how to deal with me?"],["them","it's not like that"],["me","I saw your screen"],["them","ok it's like that"]],
    "R-FLOW", "Resolve flow: typing, reflect-back, Next step.",
    ["this is what he was doing"],
    [["them","it told me to say sorry first"],["them","so… sorry"],["them","and that you were right about the thing"],["me","I'm framing that screen"]],
    "'Using an app for your relationship is sad' vs 'it's smart'. The core objection, argued out in public.", top=True)

add("R", "him", "she said 'we need to talk' and then went to sleep",
    [["them","we need to talk"],["me","about what"],["them","tomorrow"],["me","it's 11pm"],["them","goodnight x"]],
    "R-FLOW", "Resolve at 3am (phone clock visible): he types out everything he's ever done wrong.",
    ["3am. confessing everything to an app."],
    [["them","morning ☀️ ok so about tea tonight"],["them","pasta or curry"],["me","THAT WAS THE TALK??"]],
    "'Never say we need to talk before bed' goes viral every time.")

add("R", "him", "we've had the same thermostat argument 11 times",
    [["them","it's freezing"],["me","it's 20 degrees"],["them","it's Antarctica"],["me","we're not having this again"]],
    "R-FLOW", "Resolve: both type what they want. Show the Next step.",
    ["let the app decide"],
    [["them","you want 19"],["them","I want 23"],["me","so 21?"],["them","no. you buy me a heated blanket and it stays at 19"]],
    "UK thermostat wars, plus 'she won'.")

add("R", "her", "he told his friends I snore like a lawnmower",
    [["me","you told the WHOLE table I snore"],["them","I said it with love"],["me","you did the NOISE"],["them","it was an accurate noise"]],
    "R-FLOW", "Resolve: type 'he embarrassed me in front of friends', then the reflect-back.",
    ["dragged him into Resolve"],
    [["them","the app says I should say sorry privately AND publicly"],["them","so I've told the group chat"],["them","you snore like a leaf blower. I was wrong."]],
    "'Never embarrass your partner in front of friends' plus the fake apology.")

add("R", "her", "his mum knows I cried at Paddington 2",
    [["me","you told your MUM I cried at Paddington"],["them","she asked how the weekend was"],["me","that was PRIVATE"],["them","it was a U certificate"]],
    "R-FLOW", "Resolve: type 'he told his mum something private'.",
    ["we took it to Resolve"],
    [["them","update"],["them","mum cried too"],["them","she wants to come next time"],["me","…I'll allow it"]],
    "'Paddington 2 is a masterpiece' plus 'telling your mum private stuff is a red flag'.")

add("R", "him", "she wants to 'talk about us' at 9pm",
    [["them","can we talk about us tonight"],["me","is everything ok"],["them","9pm"],["me","that's not an answer"]],
    "R-FLOW", "Resolve: type 'she wants to talk about us and I'm scared'.",
    ["pre-writing my defence"],
    [["them","talk about us"],["them","getting a dog"],["them","I've named him already"],["me","what's his name"],["them","Sarah"]],
    "Callback to the Sarah video, and 'never say talk about us'.")

# ---------------- STREAK / SCORE ----------------
add("S", "him", "she's on 333 points and I'm on 67. apparently that's a problem.",
    [["them","we need to discuss the scoreboard"],["me","it's a game"],["them","333"],["them","67"],["me","it's not a competition"]],
    "S-SCORE", "Brownies header showing You 67 vs Her 333 (your existing footage works).",
    ["67 vs 333 💀"],
    [["them","it's not a competition"],["them","but if it was"],["them","you'd be losing to a woman who marked 'let him sleep in' 11 times"]],
    "'Keeping score is toxic' vs 'it's a game, relax'. The app's most important debate.", top=True)

add("S", "him", "she said if I break the streak tonight she's leaving",
    [["them","day 29"],["them","break it tonight and I'm done"],["me","I'm at the pub it's 11:52"],["them","tick tock"]],
    "S-STREAK", "Streak card; tap check-in with the phone clock at 11:59.",
    ["ran home. 11:59."],
    [["them","…babe that's MY streak"],["them","yours broke on Tuesday"],["me","so why did I run home"]],
    "'Whose fault' plus 'streaks are the best relationship hack'.")

add("S", "her", "he's on day 60 and wants a prize",
    [["them","day 60 🔥"],["them","what do I get"],["me","a girlfriend"],["them","I already had one of those"]],
    "S-STREAK", "Streak card on day 60 (or 30 if that's what you've got).",
    ["the audacity"],
    [["me","fine. check your wishlist"],["me","I added 'Your prize 🏆 +100'"],["them","what is it"],["me","sunday. no plans. no chores. PlayStation."]],
    "'Rewarding men for the bare minimum' vs 'reward what you want repeated'.")

add("S", "him", "she gave me 0 brownies for the date last night",
    [["me","0?"],["me","I booked the place, paid, walked you home"],["them","I know"],["me","so why ZERO"]],
    "B-MARK", "Show the gesture 'Date night 🍷' and 'I did this' being pressed.",
    ["0. brownies."],
    [["them","you never pressed 'I did this'"],["them","I've been waiting ALL day to give you 65"],["me","how was I meant to know"],["them","it's literally a button"]],
    "'It's literally a button' plus 'men don't read instructions'.")

# ---------------- MIXED / FAMILY / SOCIAL ----------------
add("C", "her", "he's been sending my brother money for weeks",
    [["me","why have you sent Jay £20 every Friday"],["them","he's helping me with something"],["me","WHAT something"],["them","can't say"]],
    "C-EVENT", "Event 'Operation 30 🎉' with a countdown.",
    ["'Operation 30' 👀"],
    [["them","your surprise 30th"],["them","Jay's been collecting from everyone"],["them","you've ruined it"],["me","I'm still coming"]],
    "'Secret money is a red flag even for surprises' debate.")

add("B", "her", "he nudged me to 'text his mum happy birthday'",
    [["me","why am I texting YOUR mum"],["them","because it's her birthday"],["me","you're her SON"],["them","she prefers you"]],
    "B-NUDGE", "Nudge on gesture 'Text my mum happy birthday 🎂'.",
    ["she prefers me??"],
    [["them","she literally said it at Christmas"],["them","'I'd keep her over you'"],["me","…ok I'm texting her"]],
    "Mother-in-law content always does numbers. 'Son's job not hers' debate.")

add("C", "him", "my girlfriend said yes to someone today 💍",
    [["them","I said yes today 💍"],["me","said yes to WHO"],["me","we're together??"],["them","he asked so nicely"]],
    "C-ADD", "He panics and adds event 'Buy the ring 💍' this Saturday.",
    ["panic-booked a jeweller"],
    [["them","the Aldi man asked if I wanted a bag"],["them","I said yes"],["them","…why is there a ring appointment in our calendar"]],
    "'Why the ring emoji' plus 'he was READY'. Then 'the calendar exposed him'.", top=True)

add("B", "him", "my girlfriend saved another man as 'Husband 💍'",
    [["me","who is 'Husband 💍' in your phone"],["them","someone I'm going to marry"],["me","we're not married"],["them","not yet 🙂"]],
    "B-SCROLL", "Her wishlist item 'You know what 💍 +1000'.",
    ["+1000 brownies 😐"],
    [["them","it's you 😭"],["them","I changed it this morning"],["them","the wishlist is a hint btw"]],
    "'Pressure vs hint' debate. Engaged and married couples pile in.")

add("B", "her", "he's been sleeping with someone else when I'm on nights",
    [["them","I don't sleep alone when you're on nights"],["me","EXCUSE ME"],["them","she's warm"],["them","she's got a beard"]],
    "B-ADD", "He adds gesture 'Warm your side of the bed before you get in 🔥 +10'.",
    ["a BEARD??"],
    [["them","[PHOTO]"],["them","hot water bottle"],["them","the cover's got a beard"],["them","her name's Kevin"]],
    "'Kevin is a HIM name' plus 'the beard'. Contradictions for the comments.", photo="knitted hot water bottle")

add("M", "her", "he said my mood is 'giving' today",
    [["them","your mood is giving"],["me","giving WHAT"],["them","you know"],["me","finish the sentence"]],
    "M-VIEW", "Her mood 'Sassy 💅' (or whichever emoji suits).",
    ["he never finishes the sentence"],
    [["them","giving wife"],["me","…"],["me","finish more sentences like that"]],
    "Men's half-texts plus the 'wife' pay-off. Very shareable.")

add("C", "him", "she put 'my other half' in the calendar for 7pm",
    [["me","'my other half 🥂 7pm'"],["me","I'm right here"],["them","not you"],["me","WHO THEN"]],
    "C-EVENT", "Event 'My other half 🥂 7pm'.",
    ["not me 🙂"],
    [["them","my twin 😭"],["them","it's our birthday"],["them","you forgot it's also MY birthday"],["me","…it's in the calendar now"]],
    "'Forgetting your partner's birthday is unforgivable' plus twin chaos.")

print(len(S))
json.dump(S, open("scenarios.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(s["feature"] for s in S), Counter(s["pov"] for s in S), sum(s["top"] for s in S))

# ======== +20 (built to the top-12 bar) ========
TOP12 = {"V01","V03","V09","V14","V19","V22","V24","V25","V33","V34","V43","V44"}
for s in S: s["top"] = s["id"] in TOP12

add("M", "him", "her mood says 'guilty' and then she told me she kissed someone",
    [["me","why is your mood guilty 😬"],["them","I kissed someone today"],["me","you WHAT"],["them","he was so small and cute"],["them","and he's got your nose"]],
    "M-VIEW", "Partner's mood 'Guilty 😬'.",
    ["'he's got your nose' ??"],
    [["them","my sister had the baby 😭"],["them","4 months old. he's called Leo"],["me","why has he got MY nose"],["them","that's what I'm asking you"]],
    "The last line flips the accusation onto him. The comments will be full of detectives.", top=True)

add("B", "him", "my girlfriend put a 'hall pass' on her wishlist",
    [["me","why is 'hall pass 🎫' on your wishlist"],["me","100 brownies??"],["them","one night. no questions asked"],["them","I've earned it"]],
    "B-SCROLL", "Her wishlist item 'Hall pass 🎫 +100'.",
    ["one night. no questions."],
    [["them","a pass on the HALL"],["them","you hoover the hallway for once"],["them","and I don't ask why it took 2 years"],["me","'no questions asked' 💀"]],
    "'Hall pass' is one of the biggest couple debates online. The misdirect lands, and 'no questions asked' gets quoted.", top=True)

add("R", "him", "she sent our argument to her group chat",
    [["me","why did Chloe just message me 'you're so wrong'"],["them","…"],["me","did you screenshot our argument"],["them","they needed context"],["me","ALL 9 OF THEM??"]],
    "R-FLOW", "Resolve: type 'she sent our fight to her group chat'. Show the reflect-back and TIME LEFT.",
    ["took it to Resolve instead of 9 women"],
    [["them","update"],["them","I showed them your side from the app"],["them","they said you're right"],["them","I've been removed from the group"]],
    "'Sending arguments to the group chat is betrayal' vs 'every woman does this'. Huge debate, funny payoff.", top=True)

add("C", "her", "my ex is coming to Sunday dinner. my MUM invited him.",
    [["me","why is 'Sunday dinner 🍗 + Liam' in the family calendar"],["them","your mum added it"],["me","LIAM?? my EX Liam??"],["them","she says he's been 'so lovely to her'"]],
    "C-EVENT", "Event 'Sunday dinner 🍗 + Liam', added by her mum (or by 'Mum' in the notes).",
    ["'so lovely to her' 😐"],
    [["them","babe"],["them","your mum's dating Liam"],["them","he's her plus one"],["me","I'm not going"],["them","I'm going. I need to see this"]],
    "Mum dating your ex will split the comments and get stitched and duetted.", top=True)

add("M", "him", "her mood's been 'annoyed' for 3 days so I confessed everything",
    [["me","ok you've been annoyed for 3 days"],["me","I'm sorry about the car"],["me","and the £60 on FIFA points"],["me","and I told your sister about the thing"],["them","…what thing"]],
    "M-VIEW", "Partner's mood 'Annoyed 😒'. Zoom on the date if it's visible.",
    ["3 days of 'annoyed'"],
    [["them","I forgot to change my mood 😭"],["them","I was annoyed at the Wi-Fi on Monday"],["them","but now tell me about the car"],["them","and the THING"]],
    "He confessed to nothing. The comments guess what 'the thing' is. Highest-engagement structure on the list.", top=True)

add("B", "her", "I saved him as 'Mistake' and he found it 😬",
    [["them","why am I saved as 'Mistake' in your phone"],["me","because you are one"],["them","after 2 years??"],["me","you're my biggest mistake"]],
    "B-ADD", "He adds a gesture: 'Earn my name back 📱 +500'.",
    ["adding it to her list. I want my name back."],
    [["me","open the contact"],["me","it says 'Mistake I'd make again ❤️'"],["me","it gets cut off"],["them","…I'm marking myself done"]],
    "Built-in comment prompt: 'what's your partner saved as?'. That drives thousands of comments.", top=True)

add("C", "her", "his calendar has a rotation. Monday Jess. Wednesday Priya. Friday Chloe.",
    [["me","what is this"],["me","Mon Jess 📞 Wed Priya 📞 Fri Chloe 📞"],["them","my rotation"],["me","YOUR ROTATION??"]],
    "C-EVENT", "Week view with recurring events 'Jess 📞', 'Priya 📞', 'Chloe 📞'.",
    ["he called it a rotation."],
    [["them","my sisters 😭"],["them","you said I never call my family"],["them","so I scheduled it"],["me","why did you call it a ROTATION"]],
    "Looks like a roster of women on screen, so the fight hits instantly. 'Scheduling family calls' then becomes the debate.", top=True)

add("R", "her", "he's been sleeping at 'Sophie's' twice a week",
    [["them","staying at Sophie's tonight x"],["me","who is Sophie"],["them","I told you, I stay there when you're like this"],["me","LIKE WHAT"]],
    "R-FLOW", "Resolve: type 'he's been sleeping at Sophie's'. Show the reflect-back.",
    ["'when you're like this'"],
    [["them","SOFA'S"],["them","autocorrect 😭"],["them","I sleep on the sofa when you snore"],["me","I don't snore"],["them","you're doing it right now"]],
    "'Sleep divorce' is a massive debate. 'I don't snore' / 'you're doing it now' is a guaranteed stitch.", top=True)

add("C", "him", "she's been swiping every night and she's 'found the one'",
    [["them","I've been swiping every night for weeks"],["them","and I think I've found the one"],["them","he's got a massive garden and a double garage"],["me","are you on TINDER??"]],
    "C-EVENT", "Calendar event 'Viewing 🏡 Sat 11am'.",
    ["and then she put THIS in our calendar"],
    [["them","Rightmove babe 😭"],["them","3 bed, Kent"],["them","massive garden"],["me","it's 20 foot"],["them","MASSIVE."]],
    "Rightmove swiping is a UK in-joke. 'Is 20ft massive' plus house-price comments.", top=True)

add("B", "her", "he's got a secret savings pot called 'Her 💍'",
    [["me","why have you got a savings pot called 'Her 💍'"],["them","don't look at that"],["me","WHO IS HER"],["them","you'll find out"]],
    "B-SCROLL", "His wishlist view of her item 'The ring 💍 +1000'.",
    ["'you'll find out' 😐"],
    [["them","it's you, obviously"],["them","I've been saving for 3 years"],["me","show me"],["them","[screenshot] £47.12"],["me","IN THREE YEARS??"]],
    "Wholesome setup, then roast. '£47.12' gets quoted in every comment.", top=True)


add("C", "her", "he's been sending 'my queen 👑' £50 every month",
    [["me","who is 'my queen 👑' and why do you pay her £50 a month"],["them","she needs it"],["me","she NEEDS it??"],["them","she's been there for me longer than you"]],
    "C-EVENT", "Recurring event 'Send £50 to my queen 👑 1st of the month'.",
    ["'longer than you' 😐"],
    [["them","my mum 😭"],["them","it's her bingo money"],["me","why is your mum saved as 'my queen'"],["them","why is yours saved as 'Sandra'"]],
    "'Grown man sending mum money' plus 'my queen' is a big mother vs girlfriend debate.", top=True)


add("R", "her", "he called me by another woman's name",
    [["me","who is Chloe"],["them","what"],["me","you just said 'I love you Chloe'"],["me","out LOUD"],["them","I can explain"]],
    "R-FLOW", "Resolve: type 'he said I love you to another woman'.",
    ["out. loud."],
    [["them","the sat nav"],["them","I named it Chloe"],["them","she got me home in 12 mins"],["me","why do you love the SAT NAV"],["them","she's never told me I'm going the wrong way"]],
    "Wrong-name rage is the highest-stakes fight. 'Never told me I'm wrong' is a dig that gets comments.", top=True)

add("C", "her", "he's meeting my DAD behind my back",
    [["me","why is 'Your dad ☕ Sun 2pm' in your calendar"],["them","it's a guy thing"],["me","what guy thing"],["them","just let me do this one thing"]],
    "C-EVENT", "Event 'Ask her dad ☕ Sun 2pm' (the title gets cut off in the list view, then opened).",
    ["'ask her dad' 👀"],
    [["me","wait"],["me","WAIT"],["them","act surprised on Friday"],["me","I'm literally shaking"]],
    "'Asking the dad's permission is outdated' vs 'that's respect'. One of the most reliable comment wars.", top=True)

add("B", "him", "she's got a man saved as 'DO NOT ANSWER'",
    [["me","who is 'DO NOT ANSWER'"],["me","he called you 14 times last Saturday"],["them","he's a nightmare"],["them","every weekend"]],
    "B-ADD", "He adds a gesture: 'Text her when I get home safe 🏠 +10'.",
    ["14 calls on a Saturday"],
    [["them","it's you 😭"],["them","your second number when you're out"],["them","you call me 14 times after 11pm to say you love me"],["me","…that's sweet though"]],
    "'Drunk calls are love' vs 'go home'. The comments start sharing their partner's drunk-contact name.", top=True)

add("C", "him", "she's in a group chat called 'Exit Plan 🚪' with my mates",
    [["me","why are you in a group chat called 'Exit Plan 🚪'"],["me","with MY mates"],["them","we've been planning for 3 months"],["them","how to get you out"]],
    "C-EVENT", "Event 'Escape room 🔐 Sat 2pm'.",
    ["3 months. with my boys."],
    [["them","it's an ESCAPE ROOM"],["them","for your birthday"],["them","the 'exit plan' is how to get you out"],["them","you have 60 mins and you're useless at puzzles"]],
    "The misdirect is double-meaning, and 'useless at puzzles' gets men defending themselves.", top=True)

add("C", "her", "he spent the night with Lenny and says the bed was better than ours",
    [["them","spent the night with Lenny 🌙"],["them","honestly the comfiest night I've had in months"],["them","better than our bed"],["me","WHO IS LENNY"]],
    "C-EVENT", "Event 'Work trip, Leeds 🧳' (the one she 'forgot').",
    ["'better than our bed' 😐"],
    [["them","Premier Inn 😭"],["them","Lenny's the moon"],["them","you forgot my work trip"],["them","it's in the calendar"]],
    "'Premier Inn beds ARE better' pulls UK comments by the thousand.", top=True)

add("B", "him", "she said my best mate is a better man than me",
    [["them","honestly Tom is a better man than you"],["me","say that again"],["them","he's attentive, he remembers everything"],["them","Sophie is so lucky"]],
    "B-MARK", "He taps Mark done on 3 of her wishlist items, then 'I did this'.",
    ["competing with my own best mate now"],
    [["them","Tom has the app"],["them","Sophie showed me his score"],["them","he's on 1,200"],["me","TOM'S BEEN CHEATING THE GAME"]],
    "Mate rivalry plus 'the app made him better' is the pitch, as a joke. Men tag their mates.", top=True)

add("R", "her", "he checks my phone every single night",
    [["me","why do you go through my phone every night"],["them","I'm not going through it"],["me","I watched you do it"],["them","I only check one thing"]],
    "R-FLOW", "Resolve: type 'he checks my phone every night'. Reflect-back.",
    ["'one thing' 😐"],
    [["them","screen time"],["them","6 hours of TikTok"],["them","11 minutes texting me"],["me","…"],["them","I'm not jealous of a man. I'm jealous of a For You page"]],
    "'Checking your partner's phone' is a top-3 couple debate. The last line gets stitched.", top=True)

add("C", "him", "she texted her ex 'I miss it so much 🥺'",
    [["me","why did you text Josh 'I miss it so much 🥺'"],["them","because I do"],["me","you text your EX??"],["them","nobody does it like his family"],["me","does WHAT like his family"]],
    "C-ADD", "He adds event 'Sunday roast at my mum's 🥔 12pm'.",
    ["booking my mum's roast. it's a war now."],
    [["them","the roast potatoes 😭"],["them","his mum's roasties"],["them","I still go round every other Sunday"],["me","you still see his MUM??"]],
    "'Staying close to your ex's family' is a huge debate, and so is whose mum makes the best roasties.", top=True)

add("B", "him", "she voice-noted another man at 2am: 'I need you'",
    [["me","why did you voice note Ali at 2am"],["me","'I need you. now.'"],["them","he's the only one who's there for me at 2am"],["them","and he knows exactly how I like it"]],
    "B-ADD", "He adds a gesture: '2am kebab run 🌯 +25', then Mark done.",
    ["'exactly how I like it' 😐"],
    [["them","Ali's Kebabs 😭"],["them","open till 4"],["them","extra garlic mayo, no onions"],["me","I'll learn the order"],["them","you'll never be Ali"]],
    "Misdirect innuendo turns into kebab-shop loyalty. UK comments will argue about their own Ali.", top=True)

print(len(S))
json.dump(S, open("scenarios.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(s["feature"] for s in S[60:]), sum(s["top"] for s in S))
