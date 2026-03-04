# apply-fixes.ps1 — Apply all campaign data file fixes from fixes.txt
$ErrorActionPreference = 'Stop'
$enc = New-Object System.Text.UTF8Encoding($false)
$ok = 0; $fail = 0

function Do-Replace([string]$file, [string]$old, [string]$new, [string]$label) {
    $c = [System.IO.File]::ReadAllText($file, $script:enc)
    if ($c.Contains($old)) {
        $c = $c.Replace($old, $new)
        [System.IO.File]::WriteAllText($file, $c, $script:enc)
        Write-Host "[OK]   $label"
        $script:ok++
    } else {
        Write-Host "[FAIL] $label"
        $script:fail++
    }
}

$dep = 'c:\Projects\REPORTS\тексти\DEP Retention - Table data.txt'
$ftd = 'c:\Projects\REPORTS\тексти\FTD Retention Flow - Table data.txt'
$su  = 'c:\Projects\REPORTS\тексти\SU Retention - Table data.txt'
$wf  = 'c:\Projects\REPORTS\тексти\Welcome Flow - Table data.txt'

# ===================================================
# DEP RETENTION — Remove orphan header promo codes
# ===================================================
Write-Host "`n=== DEP RETENTION ==="

# DEP C3: Remove data-promocode="POWER140" from header
Do-Replace $dep `
    'preheader: Leave the world behind and step into the winner''s circle
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="POWER140"' `
    'preheader: Leave the world behind and step into the winner''s circle
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'DEP C3: Remove POWER140 from header'

# DEP S3: Remove data-promocode="WIN20NRF" from header
Do-Replace $dep `
    'preheader: See who dominated the lines this week at Celsius Sport
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WIN20NRF"' `
    'preheader: See who dominated the lines this week at Celsius Sport
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'DEP S3: Remove WIN20NRF from header'

# DEP S8: Remove data-promocode="WIN20NRF" from header
Do-Replace $dep `
    'preheader: See the top payouts of the week and pick your winning match
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WIN20NRF"' `
    'preheader: See the top payouts of the week and pick your winning match
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'DEP S8: Remove WIN20NRF from header'

# ===================================================
# FTD RETENTION — Add promo codes to headers + bodies
# ===================================================
Write-Host "`n=== FTD RETENTION — HEADERS ==="

# FTD C1: Add ANUBIS10050 to header
Do-Replace $ftd `
    'preheader: Second deposit bonus for Hand of Anubis is ready
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Second deposit bonus for Hand of Anubis is ready
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="ANUBIS10050"' `
    'FTD C1: Add ANUBIS10050 to header'

# FTD C3: Add PARTY140 to header
Do-Replace $ftd `
    'preheader: Sweeten your second deposit with this juicy bonus
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Sweeten your second deposit with this juicy bonus
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="PARTY140"' `
    'FTD C3: Add PARTY140 to header'

# FTD C4: Add DORK50110 to header
Do-Replace $ftd `
    'preheader: Dork Unit is waiting with a bonus that''s anything but silly
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Dork Unit is waiting with a bonus that''s anything but silly
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="DORK50110"' `
    'FTD C4: Add DORK50110 to header'

# FTD C5: Add BONANZA10080 to header
Do-Replace $ftd `
    'preheader: Second deposit bonus just got a whole lot sweeter
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Second deposit bonus just got a whole lot sweeter
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="BONANZA10080"' `
    'FTD C5: Add BONANZA10080 to header'

# FTD C6: Add RICH100150 to header
Do-Replace $ftd `
    'preheader: Boost your deposit and spin through the secrets
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Boost your deposit and spin through the secrets
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="RICH100150"' `
    'FTD C6: Add RICH100150 to header'

# FTD C8: Add FORGED150 to header
Do-Replace $ftd `
    'preheader: Strike hard with your second deposit bonus
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Strike hard with your second deposit bonus
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="FORGED150"' `
    'FTD C8: Add FORGED150 to header'

# FTD S1: Add WINBACKNRF20 to header
Do-Replace $ftd `
    'preheader: Get 20% of your bet back if things don''t go your way' + " `u{2014}" + ' only after your first deposit
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Get 20% of your bet back if things don''t go your way' + " `u{2014}" + ' only after your first deposit
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WINBACKNRF20"' `
    'FTD S1: Add WINBACKNRF20 to header'

# FTD S2: Add WINBACKNRF20 to header
Do-Replace $ftd `
    'preheader: Your 20% NoRisk FreeBet is live' + " `u{2014}" + ' keep playing with confidence
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Your 20% NoRisk FreeBet is live' + " `u{2014}" + ' keep playing with confidence
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WINBACKNRF20"' `
    'FTD S2: Add WINBACKNRF20 to header'

# FTD S3: Add WINBACKNRF20 to header
Do-Replace $ftd `
    'preheader: Win or not, your next bet comes with 20% back' + " `u{2014}" + ' no promo code needed
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Win or not, your next bet comes with 20% back' + " `u{2014}" + ' no promo code needed
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WINBACKNRF20"' `
    'FTD S3: Add WINBACKNRF20 to header'

# FTD S4: Add SAFETYNRF25 to header
Do-Replace $ftd `
    'preheader: Place your next bet and get 25% back if it doesn''t go your way
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Place your next bet and get 25% back if it doesn''t go your way
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="SAFETYNRF25"' `
    'FTD S4: Add SAFETYNRF25 to header'

# FTD S6: Add WINBACKNRF20 to header
Do-Replace $ftd `
    'preheader: Miss the mark? We''ll return 20% on your next bet' + " `u{2014}" + ' no code needed
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Miss the mark? We''ll return 20% on your next bet' + " `u{2014}" + ' no code needed
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WINBACKNRF20"' `
    'FTD S6: Add WINBACKNRF20 to header'

# FTD S7: Add WINBACKNRF20 to header
Do-Replace $ftd `
    'preheader: Play your next bet with confidence' + " `u{2014}" + ' 20% comes back if it misses
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Play your next bet with confidence' + " `u{2014}" + ' 20% comes back if it misses
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WINBACKNRF20"' `
    'FTD S7: Add WINBACKNRF20 to header'

# ===================================================
# FTD RETENTION — Add promo codes to bodies
# ===================================================
Write-Host "`n=== FTD RETENTION `u{2014} BODIES ==="

# FTD C1 body: Add ANUBIS10050
Do-Replace $ftd `
    'Make your second deposit and unlock a <strong>100% bonus + 50 Free Spins</strong> in <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong>.' `
    'Use code <strong class="promocode">ANUBIS10050</strong> on your second deposit and unlock a <strong>100% bonus + 50 Free Spins</strong> in <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong>.' `
    'FTD C1: Add ANUBIS10050 to body'

# FTD C3 body: Add PARTY140
Do-Replace $ftd `
    'Your second deposit gets a <strong>140% bonus + 50 Free Spins</strong> in <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong>.' `
    'Use code <strong class="promocode">PARTY140</strong> on your second deposit and get a <strong>140% bonus + 50 Free Spins</strong> in <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong>.' `
    'FTD C3: Add PARTY140 to body'

# FTD C4 body: Add DORK50110
Do-Replace $ftd `
    'Make your second deposit and get a <strong>110% bonus + 50 Free Spins</strong> in <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong>.' `
    'Use code <strong class="promocode">DORK50110</strong> on your second deposit and get a <strong>110% bonus + 50 Free Spins</strong> in <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong>.' `
    'FTD C4: Add DORK50110 to body'

# FTD C5 body: Add BONANZA10080
Do-Replace $ftd `
    'Your second deposit brings a <strong>100% bonus + 80 Free Spins</strong> on <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong>.' `
    'Use code <strong class="promocode">BONANZA10080</strong> on your second deposit and get a <strong>100% bonus + 80 Free Spins</strong> on <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong>.' `
    'FTD C5: Add BONANZA10080 to body'

# FTD C6 body: Add RICH100150 + fix game name
Do-Replace $ftd `
    'Make your second deposit and receive a <strong>100% bonus + 150 Free Spins</strong> in <strong>Rich Wilde and the Tome of Madness</strong> <strong>by Play''n GO</strong>.' `
    'Use code <strong class="promocode">RICH100150</strong> on your second deposit and receive a <strong>100% bonus + 150 Free Spins</strong> in <strong>Rich Wilde and the Tome of Madness by Play''n Go</strong>.' `
    'FTD C6: Add RICH100150 to body + fix game name'

# FTD C8 body: Add FORGED150
Do-Replace $ftd `
    'Your second deposit unlocks a <strong>150% bonus + 30 Free Spins</strong> on <strong>Stormforged by Hacksaw Gaming</strong> electrifying slot.' `
    'Use code <strong class="promocode">FORGED150</strong> on your second deposit to unlock a <strong>150% bonus + 30 Free Spins</strong> on <strong>Stormforged by Hacksaw Gaming</strong> electrifying slot.' `
    'FTD C8: Add FORGED150 to body'

# FTD S1 body: Add WINBACKNRF20
Do-Replace $ftd `
    'Enjoy a <strong>20% NoRisk FreeBet</strong> on your next wager.' `
    'Use code <strong class="promocode">WINBACKNRF20</strong> and enjoy a <strong>20% NoRisk FreeBet</strong> on your next wager.' `
    'FTD S1: Add WINBACKNRF20 to body'

# FTD S2 body: Add WINBACKNRF20
Do-Replace $ftd `
    'Place your next wager and get a <strong>20% NoRisk FreeBet</strong>.' `
    'Use code <strong class="promocode">WINBACKNRF20</strong> on your next wager and get a <strong>20% NoRisk FreeBet</strong>.' `
    'FTD S2: Add WINBACKNRF20 to body'

# FTD S3 body: Add WINBACKNRF20 (was "No code. No hassle.")
Do-Replace $ftd `
    'No code. No hassle. Just smarter betting.' `
    'Use code <strong class="promocode">WINBACKNRF20</strong> to activate. Just smarter betting.' `
    'FTD S3: Add WINBACKNRF20 to body (replace no-code text)'

# FTD S4 body: Add SAFETYNRF25
Do-Replace $ftd `
    'With a <strong>25% NoRisk FreeBet</strong>, your next wager comes with a safety net.' `
    'With code <strong class="promocode">SAFETYNRF25</strong>, activate a <strong>25% NoRisk FreeBet</strong> `u{2014} your next wager comes with a safety net.' `
    'FTD S4: Add SAFETYNRF25 to body'

# FTD S6 body: Add WINBACKNRF20 (was "no code needed")
Do-Replace $ftd `
    'With a <strong>20% NoRisk FreeBet</strong>, your next wager comes with built-in protection.' `
    'With code <strong class="promocode">WINBACKNRF20</strong>, activate a <strong>20% NoRisk FreeBet</strong> `u{2014} your next wager comes with built-in protection.' `
    'FTD S6: Add WINBACKNRF20 to body (replace no-code text)'

# FTD S7 body: Add WINBACKNRF20
Do-Replace $ftd `
    'Good news `u{2014} your <strong>20% NoRisk FreeBet</strong> is active and ready.' `
    'Good news `u{2014} use code <strong class="promocode">WINBACKNRF20</strong> to activate your <strong>20% NoRisk FreeBet</strong>.' `
    'FTD S7: Add WINBACKNRF20 to body'

# ===================================================
# SU RETENTION — Add promo codes
# ===================================================
Write-Host "`n=== SU RETENTION ==="

# SU 2CFS: Add FINTASTIC150 to header
Do-Replace $su `
    'preheader: Make your first deposit and start spinning with a bonus built for casino players
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Make your first deposit and start spinning with a bonus built for casino players
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="FINTASTIC150"' `
    'SU 2CFS: Add FINTASTIC150 to header'

# SU 2CFS: Add FINTASTIC150 to body (was "no code needed")
Do-Replace $su `
    'Get a <strong>100% Bonus and 150 Free Spins on Razor Shark</strong> `u{2014} no code needed.' `
    'Use code <strong class="promocode">FINTASTIC150</strong> and get a <strong>100% Bonus and 150 Free Spins on Razor Shark</strong>.' `
    'SU 2CFS: Add FINTASTIC150 to body'

# SU 1S: Add EARNNRF15X to header
Do-Replace $su `
    'subject: `u{1F3C6} 15% NoRisk FreeBets: Your Safety Net is Ready
preheader: You''ve joined `u{2014} now make your move with 15% FreeBets on your first deposit
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"
text_1' `
    'subject: `u{1F3C6} 15% NoRisk FreeBets: Your Safety Net is Ready
preheader: You''ve joined `u{2014} now make your move with 15% FreeBets on your first deposit
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="EARNNRF15X"
text_1' `
    'SU 1S: Add EARNNRF15X to header'

# SU 1S: Add EARNNRF15X to body
Do-Replace $su `
    'Make your first deposit and we''ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn''t go your way, we''ve got your back.' `
    'Make your first deposit with code <strong class="promocode">EARNNRF15X</strong> and we''ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn''t go your way, we''ve got your back.' `
    'SU 1S: Add EARNNRF15X to body'

# SU 10S: Add EARNNRF15X to header
Do-Replace $su `
    'subject: `u{1F3C6} Still Waiting: 15% NoRisk FreeBets
preheader: You''ve joined `u{2014} now make your move with 15% FreeBets on your first deposit
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'subject: `u{1F3C6} Still Waiting: 15% NoRisk FreeBets
preheader: You''ve joined `u{2014} now make your move with 15% FreeBets on your first deposit
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="EARNNRF15X"' `
    'SU 10S: Add EARNNRF15X to header'

# SU 10S: Add EARNNRF15X to body
Do-Replace $su `
    'Make your first deposit and we''ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn''t go your way, we''ve still got you covered.' `
    'Make your first deposit with code <strong class="promocode">EARNNRF15X</strong> and we''ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn''t go your way, we''ve still got you covered.' `
    'SU 10S: Add EARNNRF15X to body'

# SU 1M: Add FINTASTIC150 + EARNNRF15X to header
Do-Replace $su `
    'preheader: Make your first deposit and get both casino spins and NoRisk FreeBet bonus
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: Make your first deposit and get both casino spins and NoRisk FreeBet bonus
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="FINTASTIC150, EARNNRF15X"' `
    'SU 1M: Add FINTASTIC150+EARNNRF15X to header'

# SU 1M: Add codes to body
Do-Replace $su `
    'Your first deposit unlocks a <strong>100% Bonus + 150 Free Spins on Razor Shark</strong> by Push Gaming for casino, AND a <strong>15% NoRisk FreeBet</strong> for sports betting.' `
    'Use code <strong class="promocode">FINTASTIC150</strong> on your first deposit to unlock a <strong>100% Bonus + 150 Free Spins on Razor Shark by Push Gaming</strong> for casino. Use code <strong class="promocode">EARNNRF15X</strong> for a <strong>15% NoRisk FreeBet</strong> for sports betting.' `
    'SU 1M: Add FINTASTIC150+EARNNRF15X to body'

# SU 7M: Add WIN20NRF to header (body already has it)
Do-Replace $su `
    'preheader: Two ways to start on your first deposit `u{2014} unleash chaos or bet safely
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="CHAOSCTRL80"
text_1' `
    'preheader: Two ways to start on your first deposit `u{2014} unleash chaos or bet safely
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="CHAOSCTRL80, WIN20NRF"
text_1' `
    'SU 7M: Add WIN20NRF to header (body OK)'

# ===================================================
# WELCOME FLOW — Add promo code to 2S
# ===================================================
Write-Host "`n=== WELCOME FLOW ==="

# WF 2S: Add BOOST50 to header
Do-Replace $wf `
    'preheader: The action''s heating up. Make your move and back your pick today.
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"' `
    'preheader: The action''s heating up. Make your move and back your pick today.
header_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="BOOST50"' `
    'WF 2S: Add BOOST50 to header'

# WF 2S: Add BOOST50 to body
Do-Replace $wf `
    'To make it even better, enjoy a <strong>50% bonus on your next deposit</strong>' `
    'To make it even better, use code <strong class="promocode">BOOST50</strong> and enjoy a <strong>50% bonus on your next deposit</strong>' `
    'WF 2S: Add BOOST50 to body'

# ===================================================
# SUMMARY
# ===================================================
Write-Host "`n=========================================="
Write-Host "DONE: $ok OK, $fail FAILED out of $($ok + $fail) total"
Write-Host "=========================================="
