#!/usr/bin/env python3
"""Split text_2 into text_2 + promo_code_button_1 + text_3 for single-promo emails."""

T2_OPEN = '<td align="center" class="es-text-1167" style="padding:20px;Margin:0"><p class="es-text-mobile-size-12 es-override-size" style="Margin:0;mso-line-height-rule:exactly;font-family:Montserrat, helvetica, arial, sans-serif;line-height:21px;letter-spacing:0;color:#cccccc;font-size:14px">'
T2_CLOSE = '</p></td>'

# (code, text_2_body, text_3_body) for emails #1-9
splits = [
    # Email #1 - FRUITS50
    ("FRUITS50",
     'The sun is out, the music is up, and slots are bursting with flavor!<br>We\'re inviting you to the ultimate cluster-winning fiesta.<br>We\'ve got <strong style="color:#f9b758">50 Free Spins</strong> on <strong style="color:#f9b758">Fruit Party</strong> waiting for you!',
     'Enter your promo code when you deposit and let the good times roll!<br>Don\'t let these rewards get overripe - spin now!'),

    # Email #2 - STAR110
    ("STAR110",
     'Ready for an intergalactic adventure?<br>The cosmic gems are aligning, and a supernova of wins is about to erupt! We\'re giving you a stellar head start with <strong style="color:#f9b758">100 Free Spins</strong> on the iconic <strong style="color:#f9b758">Starburst</strong>.<br>It\'s time to light up the night and watch those expanding wilds lead you to big wins!',
     'Apply your promo code at the cashier to unlock your spins.<br>This offer won\'t orbit forever - launch your session now!'),

    # Email #3 - FRU7080
    ("FRU7080",
     'The sun is out and the clusters are ready to pop!<br>It\'s time for a sweet session on <strong style="color:#f9b758">Fruit Party</strong>, and we\'ve got the perfect combo to get you started!<br><br>Your Juicy Reward:<br>\U0001f4b0 <strong style="color:#f9b758">70% Bonus up to R4 500</strong><br>\U0001f352 <strong style="color:#f9b758">80 Free Spins on Fruit Party</strong>',
     'Drop your promo code with your next top-up to activate the deal.<br>These fruits won\'t stay fresh for long - pick your wins today!'),

    # Email #4 - AVI100
    ("AVI100",
     'It\'s time to take your seat in the cockpit and chase those high multipliers.<br>We\'ve fueled your account with <strong style="color:#f9b758">100 Free Spins</strong> on <strong style="color:#f9b758">Aviator</strong>.',
     'Use the promo code above with your deposit to get your boarding pass and start your ascent.<br>Keep your finger on the button - it\'s time to fly!'),

    # Email #5 - AVI100
    ("AVI100",
     'This is the final call at the gate! Your <strong style="color:#f9b758">100 Free Spins</strong> on <strong style="color:#f9b758">Aviator</strong> are taxiing to the runway and will be gone shortly.',
     'Use the promo code above with your deposit right now to claim your spins and reach new heights.<br>The plane is leaving - are you on board?'),

    # Email #6 - STAG120
    ("STAG120",
     'Why settle for less when you can have more?<br>Get a <strong style="color:#f9b758">120% Deposit Bonus</strong> right now!',
     'Use the promo code above when you top up to claim your extra funds.<br>The move is yours - make it a big one!'),

    # Email #7 - STAG120
    ("STAG120",
     'Time is running out to supercharge your deposit.<br>Your <strong style="color:#f9b758">120% Bonus</strong> is waiting, but not for long!',
     'Enter the promo code above with your deposit before the offer vanishes.<br>Grab it while it\'s still on the table!'),

    # Email #8 - SR180
    ("SR180",
     'Ready for a sugar rush? We\'re serving up a delicious treat that\'s too sweet to resist!<br>Get a <strong style="color:#f9b758">100% Bonus PLUS 80 Free Spins</strong> on the colorful <strong style="color:#f9b758">Sugar Rush</strong> slot.',
     'Use the promo code above with your next deposit to unlock this candy-filled reward.<br>Start spinning and watch those multipliers explode!'),

    # Email #9 - SR180
    ("SR180",
     'The candy store is closing soon!<br>Your <strong style="color:#f9b758">100% Bonus</strong> and <strong style="color:#f9b758">80 Free Spins</strong> on <strong style="color:#f9b758">Sugar Rush</strong> are about to disappear.',
     'Use the promo code above with your deposit right now to claim your treats before they\'re gone for good!<br>Don\'t let your sugary rewards melt away.'),
]

T1 = '<td align="center" class="es-text-1118" style="padding:0;Margin:0;padding-right:20px;padding-left:20px;padding-top:20px"><p class="es-text-mobile-size-12 es-override-size" style="Margin:0;mso-line-height-rule:exactly;font-family:Montserrat, helvetica, arial, sans-serif;line-height:27px;letter-spacing:0;color:#ffffff;font-size:18px"><strong style="font-weight:700 !important">Hey {{customer.first_name | default:&quot;friend&quot;}},</strong></p></td>'

headers = [
    ("Email #1", "\U0001f352 50 Free Spins inside", "Get juicy wins!"),
    ("Email #2", "\u2728 Reach for the stars with 100 Free Spins!", "Your dazzling reward is ready"),
    ("Email #3", "\U0001f353 Get juicy: 70% Bonus + 80 Free Spins are here!", "Turn up the flavor"),
    ("Email #4", "\u2708\ufe0f Your cockpit is ready: 100 Free Spins inside!", "Take control and fly high"),
    ("Email #5", "\u23f3 Your 100 FS are taking off...", "Final boarding call!"),
    ("Email #6", "\U0001f680 Boost your balance by 120%!", "More funds, more chances to win"),
    ("Email #7", "\U0001f525 Your 120% boost is expiring", "Last chance to claim your extra bonus funds"),
    ("Email #8", "\U0001f36c A sugar-coated reward: 100% + 80 Free Spins!", "Get a sweet deal on Sugar Rush"),
    ("Email #9", "\U0001f370 Your 80 bonus spins are almost gone...", "Don't let this sweet deal melt away!"),
]

emails = []
for i, (code, t2_body, t3_body) in enumerate(splits):
    name, subj, preh = headers[i]
    emails.append(f"""name: {name}
Subject: {subj}
Preheader: {preh}
text_1: {T1}
text_2: {T2_OPEN}{t2_body}{T2_CLOSE}
promo_code_button_1: {code}
text_3: {T2_OPEN}{t3_body}{T2_CLOSE}
button_text_1: CLAIM BONUS""")

# Emails #10-11 unchanged
emails.append(f"""name: Email #10
Subject: \U0001f420 130% Bonus or 120 Free Spins? Pick your tackle
Preheader: Which one will you hook?
text_1: {T1}
text_2: {T2_OPEN}The fish are jumping and the weather is perfect for a big win!<br>But every fisherman has their own style - so we're letting you choose your own bait.<br><br>Which reward are you reeling in today?<br>Get a huge <strong style="color:#f9b758">130% Bonus</strong> to use on any game - use promo code <strong style="color:#f9b758">STAG130</strong>!<br>Get <strong style="color:#f9b758">120 Free Spins</strong> on <strong style="color:#f9b758">Big Bass Splash</strong> - use promo code <strong style="color:#f9b758">BBSPL120</strong>!<br><br>Cast your line and claim your favorite reward before the tide turns!{T2_CLOSE}
button_text_1: CLAIM BONUS""")

emails.append(f"""name: Email #11
Subject: \U0001fabc Don't let the big one get away!
Preheader: Last chance to choose your bonus
text_1: {T1}
text_2: {T2_OPEN}This is your final chance to pick between a <strong style="color:#f9b758">130% Bonus</strong> or <strong style="color:#f9b758">120 Free Spins</strong> on <strong style="color:#f9b758">Big Bass Splash</strong>.<br><br>Get a huge <strong style="color:#f9b758">130% Bonus</strong> to use on any game - use promo code <strong style="color:#f9b758">STAG130</strong>!<br>Get <strong style="color:#f9b758">120 Free Spins</strong> on <strong style="color:#f9b758">Big Bass Splash</strong> - use promo code <strong style="color:#f9b758">BBSPL120</strong>!<br><br>The offer is expiring soon - don't get left on the shore.{T2_CLOSE}
button_text_1: CLAIM BONUS""")

output = "\n\n".join(emails) + "\n"

with open(r"C:\Projects\REPORTS\тексти\пантери нова праця\dep reten.txt", "w", encoding="utf-8") as f:
    f.write(output)

print(f"Done - {len(emails)} emails. #1-9 split into text_2 + promo_code_button_1 + text_3. #10-11 unchanged.")
