$ErrorActionPreference = 'Stop'
$root = 'c:\Projects\CLIENTS\CHEEL4REEL'

# ---------- universal pool replacement (all 20 files) ----------
$U_OLD = 'Wagering applies to Sweet Bonanza, Gates of Olympus, Big Bass Splash, Sugar Rush 1000'
$U_NEW = 'Wagering applies to Gates of Olympus Super Scatter, 3 Super Hot Chillies, Joker Streak XL: Hold and Win, The Count'

# ---------- per-Welcome-N transforms ----------
# Each entry: file glob OR explicit list. We mutate via -replace with regex.

function Save-File($path, $content) {
    # Preserve original encoding (UTF8 no BOM) — assume Set-Content -Encoding UTF8 (BOM in PS5)
    # Stripo files are UTF8 no BOM; use [IO.File]::WriteAllText with UTF8NoBOM via .NET.
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($path, $content, $utf8NoBom)
}

function Apply-Common($content) {
    return $content.Replace($U_OLD, $U_NEW)
}

# ===== WELCOME 1 =====
function Apply-W1($content) {
    # Order matters to avoid double-Super-Scatter. Use negative lookahead via regex for GoO.
    # 1. Sweet Bonanza -> Gates of Olympus Super Scatter (W1 single-game mention in standard emails)
    $content = $content -replace "Pragmatic Play's Sweet Bonanza", "Pragmatic Play's Gates of Olympus Super Scatter"
    $content = $content -replace '100 Free Spins on Sweet Bonanza', '100 Free Spins on Gates of Olympus Super Scatter'
    # 2. Gates of Olympus (BOOST125 promo, NOT already Super Scatter) -> add Super Scatter
    $content = $content -replace "Pragmatic Play's Gates of Olympus(?! Super Scatter)", "Pragmatic Play's Gates of Olympus Super Scatter"
    $content = $content -replace '150 Free Spins on Gates of Olympus(?! Super Scatter)', '150 Free Spins on Gates of Olympus Super Scatter'
    $content = $content -replace '150 FS on Gates of Olympus(?! Super Scatter)', '150 FS on Gates of Olympus Super Scatter'
    $content = $content -replace '125% \+ 150 FS on Gates of Olympus(?! Super Scatter)', '125% + 150 FS on Gates of Olympus Super Scatter'
    $content = $content -replace '125% \+ 150 FS on Gates Of Olympus(?! Super Scatter)', '125% + 150 FS on Gates Of Olympus Super Scatter'
    # 3. Sugar Rush 1000 (FINAL150 promo) -> Gates of Olympus Super Scatter (W1 only)
    $content = $content -replace "Pragmatic Play's Sugar Rush 1000", "Pragmatic Play's Gates of Olympus Super Scatter"
    $content = $content -replace '200 Free Spins on Sugar Rush 1000', '200 Free Spins on Gates of Olympus Super Scatter'
    $content = $content -replace '200 FS on Sugar Rush 1000', '200 FS on Gates of Olympus Super Scatter'
    $content = $content -replace '150% \+ 200 FS on Sugar Rush 1000', '150% + 200 FS on Gates of Olympus Super Scatter'
    $content = $content -replace 'tematics? Sugar Rush 1000', 'tematics Gates of Olympus Super Scatter'
    # UA descriptions: "тематика Gates of Olympus", "(Sugar Rush 1000)"
    $content = $content -replace 'тематика Gates of Olympus(?! Super Scatter)', 'тематика Gates of Olympus Super Scatter'
    $content = $content -replace 'тематика Sugar Rush 1000', 'тематика Gates of Olympus Super Scatter'
    $content = $content -replace 'гра Gates of Olympus(?! Super Scatter)', 'гра Gates of Olympus Super Scatter'
    $content = $content -replace 'game: Gates of Olympus(?! Super Scatter)', 'game: Gates of Olympus Super Scatter'
    $content = $content -replace 'game: Sugar Rush 1000', 'game: Gates of Olympus Super Scatter'
    $content = $content -replace '\(Sugar Rush 1000\)', '(Gates of Olympus Super Scatter)'
    $content = $content -replace 'тільки Sugar Rush 1000', 'тільки Gates of Olympus Super Scatter'
    $content = $content -replace 'фінальний апгрейд \(Sugar Rush 1000\)', 'фінальний апгрейд (Gates of Olympus Super Scatter)'
    # Banners EN-CA: "Final Upgrade on Sugar Rush 1000", "Upgrade on Sugar Rush 1000"
    $content = $content -replace 'on Sugar Rush 1000', 'on Gates of Olympus Super Scatter'
    # 4. W1 narrative "Gates of Olympus and Big Bass Splash" -> updated canon games
    $content = $content -replace 'Gates of Olympus Super Scatter and Big Bass Splash', 'Gates of Olympus Super Scatter and Joker Streak XL: Hold and Win'
    # 5. W1 line "Pragmatic Play, NetEnt, Hacksaw Gaming, Play'n GO. Sweet Bonanza, Gates of Olympus, Big Bass Splash, Sugar Rush 1000."
    $content = $content -replace "Pragmatic Play, NetEnt, Hacksaw Gaming, Play'n GO\. Sweet Bonanza, Gates of Olympus Super Scatter, Big Bass Splash, Gates of Olympus Super Scatter\.", "Pragmatic Play, 3Oaks, Hacksaw Gaming, Croco. Gates of Olympus Super Scatter, 3 Super Hot Chillies, Joker Streak XL: Hold and Win, The Count."
    # (after prior cascading replaces; build a few permutations to be safe)
    $content = $content -replace "Pragmatic Play, NetEnt, Hacksaw Gaming, Play'n GO\. [^\.]+?\.", "Pragmatic Play, 3Oaks, Hacksaw Gaming, Croco. Gates of Olympus Super Scatter, 3 Super Hot Chillies, Joker Streak XL: Hold and Win, The Count."
    # 6. Banner description (Interac, Gates of Olympus, Sugar Rush)
    $content = $content -replace 'Interac, Gates of Olympus(?! Super Scatter), Sugar Rush', 'Interac, Gates of Olympus Super Scatter, 3 Super Hot Chillies'
    # 7. W1 batch split clarity (after Sweet Bonanza already replaced)
    $oldBatch = "🍁 Free Spins delivered in 2 batches: 50 on first deposit, 50 on Day 2`n🍁 Free Spins are given on Pragmatic Play's Gates of Olympus Super Scatter"
    $newBatch = "🍁 Free Spins delivered in 2 batches: 50 on first deposit (Day 1), 50 on Day 2`n🍁 Free Spins Day 1 are given on Pragmatic Play's Gates of Olympus Super Scatter`n🍁 Free Spins Day 2 are given on 3Oaks' 3 Super Hot Chillies"
    $content = $content.Replace($oldBatch, $newBatch)
    # HTML version with <br> instead of \n
    $oldBatchHtml = "🍁 Free Spins delivered in 2 batches: 50 on first deposit, 50 on Day 2<br>🍁 Free Spins are given on Pragmatic Play's Gates of Olympus Super Scatter"
    $newBatchHtml = "🍁 Free Spins delivered in 2 batches: 50 on first deposit (Day 1), 50 on Day 2<br>🍁 Free Spins Day 1 are given on Pragmatic Play's Gates of Olympus Super Scatter<br>🍁 Free Spins Day 2 are given on 3Oaks' 3 Super Hot Chillies"
    $content = $content.Replace($oldBatchHtml, $newBatchHtml)
    # Stripo Table data uses "<br> " (with space)
    $oldBatchTd  = "🍁 Free Spins delivered in 2 batches: 50 on first deposit, 50 on Day 2<br> 🍁 Free Spins are given on Pragmatic Play's Gates of Olympus Super Scatter"
    $newBatchTd  = "🍁 Free Spins delivered in 2 batches: 50 on first deposit (Day 1), 50 on Day 2<br> 🍁 Free Spins Day 1 are given on Pragmatic Play's Gates of Olympus Super Scatter<br> 🍁 Free Spins Day 2 are given on 3Oaks' 3 Super Hot Chillies"
    $content = $content.Replace($oldBatchTd, $newBatchTd)
    return $content
}

# ===== WELCOME 2 =====
function Apply-W2($content) {
    # 1. Day 2 batch (50 FS on Sweet Bonanza, $150 cap) -> 3Oaks' 3 Super Hot Chillies, $250 cap
    $content = $content -replace "50 Free Spins on Pragmatic Play's Sweet Bonanza, auto-credited", "50 Free Spins on 3Oaks' 3 Super Hot Chillies, auto-credited"
    # 2. Dep2 standard (Gates of Olympus) -> Croco's Joker Streak XL: Hold and Win
    $content = $content -replace "Pragmatic Play's Gates of Olympus(?! Super Scatter)", "Croco's Joker Streak XL: Hold and Win"
    $content = $content -replace '50 Free Spins on Gates of Olympus(?! Super Scatter)', '50 Free Spins on Joker Streak XL: Hold and Win'
    $content = $content -replace '50 FS on Gates of Olympus(?! Super Scatter)', '50 FS on Joker Streak XL: Hold and Win'
    # 3. FLASH100 (Big Bass Splash) -> Joker Streak XL: Hold and Win
    $content = $content -replace "Pragmatic Play's Big Bass Splash", "Croco's Joker Streak XL: Hold and Win"
    $content = $content -replace '50 Free Spins on Big Bass Splash', '50 Free Spins on Joker Streak XL: Hold and Win'
    $content = $content -replace '50 FS on Big Bass Splash', '50 FS on Joker Streak XL: Hold and Win'
    $content = $content -replace '100% \+ 50 FS on Big Bass Splash', '100% + 50 FS on Joker Streak XL: Hold and Win'
    # UA descriptions
    $content = $content -replace 'Big Bass Splash — лише натяк формою', 'Joker Streak XL — лише натяк формою'
    $content = $content -replace 'риболовна блискавка на Big Bass Splash', 'блискавка на Joker Streak XL'
    $content = $content -replace 'game: Big Bass Splash', 'game: Joker Streak XL: Hold and Win'
    # 4. Day 2 batch $150 cap -> $250 (per user instruction). Only in W2 Day 2 batch context.
    # We can't safely global-replace $150 (other lines legit use $150). Targeted block replace.
    $oldCap = "🍁 50 Free Spins on 3Oaks' 3 Super Hot Chillies, auto-credited`r`n🍁 Free Spins wager x35`r`n🍁 Max bet during wagering `$5 CAD`r`n🍁 Max win from Free Spins `$150 CAD"
    $newCap = "🍁 50 Free Spins on 3Oaks' 3 Super Hot Chillies, auto-credited`r`n🍁 Free Spins wager x35`r`n🍁 Max bet during wagering `$5 CAD`r`n🍁 Max win from Free Spins `$250 CAD"
    $content = $content.Replace($oldCap, $newCap)
    # also LF-only variant
    $oldCapLf = "🍁 50 Free Spins on 3Oaks' 3 Super Hot Chillies, auto-credited`n🍁 Free Spins wager x35`n🍁 Max bet during wagering `$5 CAD`n🍁 Max win from Free Spins `$150 CAD"
    $newCapLf = "🍁 50 Free Spins on 3Oaks' 3 Super Hot Chillies, auto-credited`n🍁 Free Spins wager x35`n🍁 Max bet during wagering `$5 CAD`n🍁 Max win from Free Spins `$250 CAD"
    $content = $content.Replace($oldCapLf, $newCapLf)
    # Inapp single-line T&C for Day 2 batch
    $content = $content -replace 'T&C: FS wager x35 \| Max bet \$5 CAD \| Max FS win \$150 CAD \| FS expire 7 days from credit', 'T&C: FS wager x35 | Max bet $5 CAD | Max FS win $250 CAD | FS expire 7 days from credit'
    return $content
}

# ===== WELCOME 3 =====
function Apply-W3($content) {
    # Dep3 (Big Bass Splash) -> Hacksaw Gaming's The Count
    $content = $content -replace "Pragmatic Play's Big Bass Splash", "Hacksaw Gaming's The Count"
    $content = $content -replace '75 Free Spins on Big Bass Splash', '75 Free Spins on The Count'
    $content = $content -replace '75 FS on Big Bass Splash', '75 FS on The Count'
    $content = $content -replace '100% \+ 75 FS on Big Bass Splash', '100% + 75 FS on The Count'
    return $content
}

# ===== WELCOME 4 =====
function Apply-W4($content) {
    # Dep4 (Sugar Rush 1000) -> Pragmatic Play's Gates of Olympus Super Scatter
    $content = $content -replace "Pragmatic Play's Sugar Rush 1000", "Pragmatic Play's Gates of Olympus Super Scatter"
    $content = $content -replace '75 Free Spins on Sugar Rush 1000', '75 Free Spins on Gates of Olympus Super Scatter'
    $content = $content -replace '75 FS on Sugar Rush 1000', '75 FS on Gates of Olympus Super Scatter'
    $content = $content -replace '125% \+ 75 FS on Sugar Rush 1000', '125% + 75 FS on Gates of Olympus Super Scatter'
    return $content
}

# Map: folder/file -> which welcome
$plan = @(
    @{ Path = "$root\тексти\WELCOME 1\chill4reel welcome 1 banner descriptions UA.txt"; W = 1 },
    @{ Path = "$root\тексти\WELCOME 1\chill4reel welcome 1 banners EN-CA.txt"; W = 1 },
    @{ Path = "$root\тексти\WELCOME 1\chill4reel welcome 1 texts EN-CA.txt"; W = 1 },
    @{ Path = "$root\тексти\WELCOME 1\WELCOME 1 - Table data.txt"; W = 1 },
    @{ Path = "$root\тексти\WELCOME 2\chill4reel welcome 2 banner descriptions UA.txt"; W = 2 },
    @{ Path = "$root\тексти\WELCOME 2\chill4reel welcome 2 banners EN-CA.txt"; W = 2 },
    @{ Path = "$root\тексти\WELCOME 2\chill4reel welcome 2 texts EN-CA.txt"; W = 2 },
    @{ Path = "$root\тексти\WELCOME 2\WELCOME 2 - Table data.txt"; W = 2 },
    @{ Path = "$root\тексти\WELCOME 3\chill4reel welcome 3 banner descriptions UA.txt"; W = 3 },
    @{ Path = "$root\тексти\WELCOME 3\chill4reel welcome 3 banners EN-CA.txt"; W = 3 },
    @{ Path = "$root\тексти\WELCOME 3\chill4reel welcome 3 texts EN-CA.txt"; W = 3 },
    @{ Path = "$root\тексти\WELCOME 3\WELCOME 3 - Table data.txt"; W = 3 },
    @{ Path = "$root\тексти\WELCOME 4\chill4reel welcome 4 banner descriptions UA.txt"; W = 4 },
    @{ Path = "$root\тексти\WELCOME 4\chill4reel welcome 4 banners EN-CA.txt"; W = 4 },
    @{ Path = "$root\тексти\WELCOME 4\chill4reel welcome 4 texts EN-CA.txt"; W = 4 },
    @{ Path = "$root\тексти\WELCOME 4\WELCOME 4 - Table data.txt"; W = 4 },
    @{ Path = "$root\html\Chill4Reel Welcome 1.html"; W = 1 },
    @{ Path = "$root\html\Chill4Reel Welcome 2.html"; W = 2 },
    @{ Path = "$root\html\Chill4Reel Welcome 3.html"; W = 3 },
    @{ Path = "$root\html\Chill4Reel Welcome 4.html"; W = 4 }
)

foreach ($item in $plan) {
    $p = $item.Path
    if (-not (Test-Path -LiteralPath $p)) { Write-Output "SKIP missing: $p"; continue }
    $original = [System.IO.File]::ReadAllText($p)
    $content = $original
    # universal first
    $content = Apply-Common $content
    switch ($item.W) {
        1 { $content = Apply-W1 $content }
        2 { $content = Apply-W2 $content }
        3 { $content = Apply-W3 $content }
        4 { $content = Apply-W4 $content }
    }
    if ($content -ne $original) {
        Save-File $p $content
        $diff = ($content.Length - $original.Length)
        Write-Output "MODIFIED ($diff chars): $p"
    } else {
        Write-Output "UNCHANGED: $p"
    }
}
Write-Output "DONE"
