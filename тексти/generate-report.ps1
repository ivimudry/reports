<# Generate Celsius Text Audit Report - Dynamic Content Builder #>
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$dir      = Join-Path "C:\Projects\REPORTS" ([char]0x0442 + [char]0x0435 + [char]0x043A + [char]0x0441 + [char]0x0442 + [char]0x0438)
$shell    = Join-Path $dir 'report-shell.html'
$outPath  = Join-Path "C:\Projects\REPORTS\pages\promptgrid" 'REPORT_text_audit_celsius.html'

# ── HELPERS ──
function Strip-Html($text) {
    $t = $text -replace '<br\s*/?>',' '
    $t = $t -replace '<[^>]+>',' '
    $t = $t -replace '&nbsp;',' '
    $t = $t -replace '&amp;','&'
    $t = $t -replace '\s+',' '
    return $t.Trim()
}

function Esc($text) { return [System.Net.WebUtility]::HtmlEncode($text) }

function Extract-Bonuses($rawHtml) {
    $bonuses = [System.Collections.Generic.List[string]]::new()
    $strongMatches = [regex]::Matches($rawHtml, '<strong[^>]*>([^<]+)</strong>', 'IgnoreCase')
    $strongTexts = @()
    foreach($m in $strongMatches) {
        $val = $m.Groups[1].Value.Trim()
        if($val -and $val.Length -gt 1) { $strongTexts += $val }
    }
    $allStrong = $strongTexts -join ' '
    $clean = Strip-Html $rawHtml

    # compound: X% + Y FS
    $ms = [regex]::Matches($clean, '(\d{2,3})%\s*(?:bonus)?\s*\+\s*(\d+)\s*(?:Free Spins?|FS)', 'IgnoreCase')
    foreach($m in $ms) {
        $b = "$($m.Groups[1].Value)% + $($m.Groups[2].Value) FS"
        if(-not $bonuses.Contains($b)){$bonuses.Add($b)}
    }
    # standalone FS
    $ms = [regex]::Matches($clean, '(?<!\+\s{0,3})(\d{2,4})\s*(?:Free Spins?|FS\b)', 'IgnoreCase')
    foreach($m in $ms) {
        $num = $m.Groups[1].Value
        $val = "$num FS"
        $skip = $false
        foreach($b in $bonuses){if($b -match "\+ $num FS"){$skip=$true;break}}
        if(-not $skip -and -not $bonuses.Contains($val) -and [int]$num -ge 10){$bonuses.Add($val)}
    }
    # NRF / NoRisk FreeBet
    $ms = [regex]::Matches($clean, '(\d{1,3})%\s*(?:NoRisk\s*(?:Free\s*Bets?|FreeBets?)|NRF|No\s*Risk\s*(?:Free\s*Bets?|FreeBets?|Only\s*Win))', 'IgnoreCase')
    foreach($m in $ms) {
        $val = "$($m.Groups[1].Value)% NRF"
        if(-not $bonuses.Contains($val)){$bonuses.Add($val)}
    }
    # Cashback
    $ms = [regex]::Matches($clean, '(\d{1,2})%\s*(?:Cashback|CB)', 'IgnoreCase')
    foreach($m in $ms) {
        $val = "$($m.Groups[1].Value)% CB"
        if(-not $bonuses.Contains($val)){$bonuses.Add($val)}
    }
    # FreeBets (sport)
    $ms = [regex]::Matches($clean, '(\d{2,3})%\s*Free\s*Bets?\b', 'IgnoreCase')
    foreach($m in $ms) {
        $pct = $m.Groups[1].Value
        $val = "$pct% FreeBets"
        $hasNrf = $false
        foreach($b in $bonuses){if($b -eq "$pct% NRF"){$hasNrf=$true;break}}
        if(-not $hasNrf -and -not $bonuses.Contains($val)){$bonuses.Add($val)}
    }
    # standalone %
    $ms = [regex]::Matches($allStrong, '\b(\d{2,3})%\b', 'IgnoreCase')
    foreach($m in $ms) {
        $pct = [int]$m.Groups[1].Value
        if($pct -lt 50 -or $pct -gt 300){continue}
        $partOf = $false
        foreach($b in $bonuses){if($b -match "^$pct%"){$partOf=$true;break}}
        if(-not $partOf) {
            if($clean -match "$pct%\s*(?:bonus|on|deposit|Bonus)" -or $clean -match "code.*$pct%" -or $allStrong -match "^$pct%$") {
                $bonuses.Add("$pct%")
            }
        }
    }
    return $bonuses.ToArray()
}

function Extract-Games($rawHtml) {
    $games = [System.Collections.Generic.List[string]]::new()
    $ms = [regex]::Matches($rawHtml, '(?:in|on)\s+<strong>([^<]+?)</strong>\s*<strong>by\s+([^<]+)</strong>', 'IgnoreCase')
    foreach($m in $ms) {
        $g = "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())"
        if(-not $games.Contains($g)){$games.Add($g)}
    }
    if($games.Count -eq 0) {
        $ms = [regex]::Matches($rawHtml, '(?:in|on)\s+<strong>([^<]+?)\s+by\s+([^<]+?)</strong>', 'IgnoreCase')
        foreach($m in $ms) {
            $g = "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())"
            if(-not $games.Contains($g)){$games.Add($g)}
        }
    }
    if($games.Count -eq 0) {
        $clean = Strip-Html $rawHtml
        $ms = [regex]::Matches($clean, "(?:in|on)\s+([\w\s']+?)\s+by\s+((?:Hacksaw|Pragmatic|Push|Nolimit|Play.n|Relax)\s*\w*)", 'IgnoreCase')
        foreach($m in $ms) {
            $g = "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())"
            if($g -notmatch '^(?:your|the game|favor)' -and -not $games.Contains($g)){$games.Add($g)}
        }
    }
    return $games.ToArray()
}

function Parse-Campaign($filePath) {
    $content = Get-Content $filePath -Encoding UTF8 -Raw
    $blocks = $content -split '(?=\nname: Email )' | Where-Object { $_ -match 'name: Email' }
    $emails = @()
    foreach($block in $blocks) {
        $e = @{}
        if($block -match 'name: Email\s+(.+)') { $e.name = $Matches[1].Trim() } else { continue }
        $e.headerCodes = @()
        if($block -match 'data-promocode\s*=\s*"([^"]+)"') {
            $e.headerCodes = @(($Matches[1] -split ',\s*') | ForEach-Object { $_.Trim() } | Where-Object { $_ })
        }
        $bodyHtml = ""
        $textMatches = [regex]::Matches($block, 'text_\d+:\s*(.+?)(?=\n(?:text_\d+|button_text|name):|$)', 'Singleline')
        foreach($m in $textMatches) { $bodyHtml += " " + $m.Groups[1].Value }
        $e.bodyCodes = @()
        $wcm = [regex]::Matches($bodyHtml, '<strong class="promocode">([A-Z0-9]+)\s*</strong>')
        foreach($m in $wcm) { $e.bodyCodes += $m.Groups[1].Value.Trim() }
        $e.bodyCodes = @($e.bodyCodes | Select-Object -Unique)
        $e.bonuses = @(Extract-Bonuses $bodyHtml)
        $e.games = @(Extract-Games $bodyHtml)
        $e.hasHeader = ($e.headerCodes.Count -gt 0)
        $e.hasWrapper = ($e.bodyCodes.Count -gt 0)
        # header/body match
        $e.headerMatchesBody = $true
        if($e.headerCodes.Count -gt 0 -or $e.bodyCodes.Count -gt 0) {
            $hSet = @($e.headerCodes | Sort-Object)
            $bSet = @($e.bodyCodes | Sort-Object)
            if($hSet.Count -ne $bSet.Count) { $e.headerMatchesBody = $false }
            else { for($i=0;$i -lt $hSet.Count;$i++){if($hSet[$i] -ne $bSet[$i]){$e.headerMatchesBody=$false;break}} }
        }
        # status
        $e.status = "ok"; $e.statusNote = ""
        $cleanBody = Strip-Html $bodyHtml
        $hasBonusContent = ($cleanBody -match '\d+%\s*(?:\+|bonus|deposit|on|NRF|NoRisk|Cashback|CB|Free)' -or $cleanBody -match '\d+\s*(?:FS|Free Spin)')
        if($e.bodyCodes.Count -eq 0 -and $e.headerCodes.Count -eq 0 -and $hasBonusContent -and $e.bonuses.Count -gt 0) {
            $e.status = "warn"; $e.statusNote = "Bonus without promo code"
        } elseif(-not $e.headerMatchesBody) {
            if($e.headerCodes.Count -eq 0 -and $e.bodyCodes.Count -gt 0) {
                $e.status = "warn"; $e.statusNote = "No header code"
            } elseif($e.headerCodes.Count -gt 0 -and $e.bodyCodes.Count -eq 0) {
                $e.status = "warn"; $e.statusNote = "Header only, no body wrapper"
            } elseif($e.headerCodes.Count -ne $e.bodyCodes.Count) {
                $e.status = "warn"; $e.statusNote = "Header/body count mismatch"
            } else {
                $e.status = "warn"; $e.statusNote = "Header/body mismatch"
            }
        }
        $emails += $e
    }
    return $emails
}

# ── PARSE ALL CAMPAIGNS ──
$campaigns = @(
    @{id="dep-retention";name="DEP Retention";file="DEP Retention - Table data.txt";skipWrapper=$true}
    @{id="ftd-retention";name="FTD Retention";file="FTD Retention Flow - Table data.txt";skipWrapper=$false}
    @{id="nutrition-2";name="Nutrition #2";file="Nutrition #2 - Table data.txt";skipWrapper=$false}
    @{id="nutrition-3";name="Nutrition #3";file="Nutrition #3 - Table data.txt";skipWrapper=$false}
    @{id="su-retention";name="SU Retention";file="SU Retention - Table data.txt";skipWrapper=$false}
    @{id="welcome-flow";name="Welcome Flow";file="Welcome Flow - Table data.txt";skipWrapper=$false}
)

$allCampaigns = @()
$totalEmails = 0; $totalWithCode = 0; $totalIssues = 0
foreach($c in $campaigns) {
    $fp = Join-Path $dir $c.file
    $emails = Parse-Campaign $fp
    $withCode = @($emails | Where-Object { $_.bodyCodes.Count -gt 0 -or $_.headerCodes.Count -gt 0 }).Count
    $issues  = @($emails | Where-Object { $_.status -ne "ok" }).Count
    $noBonus = @($emails | Where-Object { $_.bodyCodes.Count -eq 0 -and $_.headerCodes.Count -eq 0 -and $_.bonuses.Count -eq 0 }).Count
    $allCampaigns += @{id=$c.id;name=$c.name;skipWrapper=$c.skipWrapper;emails=$emails;count=$emails.Count;withCode=$withCode;issues=$issues;noBonus=$noBonus}
    $totalEmails += $emails.Count; $totalWithCode += $withCode; $totalIssues += $issues
}
Write-Host "Parsed: $totalEmails emails, $totalWithCode with code, $totalIssues issues"

# ── BUILD DYNAMIC HTML ──
$sb = [System.Text.StringBuilder]::new(200000)

# ── SUMMARY SECTION ──
$warnClass = if($totalIssues -gt 0){' warn'}else{''}
[void]$sb.Append(@"
<div class="section section-anchor" id="summary">
  <h2>
    <span data-lang="en" class="active">Summary</span>
    <span data-lang="ua">&#1055;&#1110;&#1076;&#1089;&#1091;&#1084;&#1086;&#1082;</span>
    <span data-lang="ru">&#1048;&#1090;&#1086;&#1075;&#1080;</span>
  </h2>
  <div class="cards">
    <div class="card"><div class="card-value">$totalEmails</div><div class="card-label">
      <span data-lang="en" class="active">Total Emails</span><span data-lang="ua">&#1042;&#1089;&#1100;&#1086;&#1075;&#1086; &#1083;&#1080;&#1089;&#1090;&#1110;&#1074;</span><span data-lang="ru">&#1042;&#1089;&#1077;&#1075;&#1086; &#1087;&#1080;&#1089;&#1077;&#1084;</span>
    </div></div>
    <div class="card"><div class="card-value">$totalWithCode</div><div class="card-label">
      <span data-lang="en" class="active">With Promo Code</span><span data-lang="ua">&#1047; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1086;&#1084;</span><span data-lang="ru">&#1057; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1086;&#1084;</span>
    </div></div>
    <div class="card"><div class="card-value$warnClass">$totalIssues</div><div class="card-label">
      <span data-lang="en" class="active">Issues Found</span><span data-lang="ua">&#1047;&#1085;&#1072;&#1081;&#1076;&#1077;&#1085;&#1086; &#1087;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084;</span><span data-lang="ru">&#1053;&#1072;&#1081;&#1076;&#1077;&#1085;&#1086; &#1087;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084;</span>
    </div></div>
  </div>
  <table class="at">
    <thead><tr>
      <th><span data-lang="en" class="active">Campaign</span><span data-lang="ua">&#1050;&#1072;&#1084;&#1087;&#1072;&#1085;&#1110;&#1103;</span><span data-lang="ru">&#1050;&#1072;&#1084;&#1087;&#1072;&#1085;&#1080;&#1103;</span></th>
      <th><span data-lang="en" class="active">Emails</span><span data-lang="ua">&#1051;&#1080;&#1089;&#1090;&#1110;&#1074;</span><span data-lang="ru">&#1055;&#1080;&#1089;&#1077;&#1084;</span></th>
      <th><span data-lang="en" class="active">With Code</span><span data-lang="ua">&#1047; &#1082;&#1086;&#1076;&#1086;&#1084;</span><span data-lang="ru">&#1057; &#1082;&#1086;&#1076;&#1086;&#1084;</span></th>
      <th><span data-lang="en" class="active">No Bonus</span><span data-lang="ua">&#1041;&#1077;&#1079; &#1073;&#1086;&#1085;&#1091;&#1089;&#1091;</span><span data-lang="ru">&#1041;&#1077;&#1079; &#1073;&#1086;&#1085;&#1091;&#1089;&#1072;</span></th>
      <th><span data-lang="en" class="active">Issues</span><span data-lang="ua">&#1055;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084;</span><span data-lang="ru">&#1055;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084;</span></th>
    </tr></thead>
    <tbody>
"@)

$tCnt=0;$tCode=0;$tNoB=0;$tIss=0
foreach($c in $allCampaigns){
    $ic = if($c.issues -gt 0){'s-w'}else{'s-ok'}
    [void]$sb.AppendLine("      <tr><td class=`"eid`">$($c.name)</td><td>$($c.count)</td><td>$($c.withCode)</td><td>$($c.noBonus)</td><td class=`"$ic`">$($c.issues)</td></tr>")
    $tCnt+=$c.count;$tCode+=$c.withCode;$tNoB+=$c.noBonus;$tIss+=$c.issues
}
$tIc = if($tIss -gt 0){'s-w'}else{'s-ok'}
[void]$sb.Append(@"
      <tr style="font-weight:700;border-top:2px solid #4ec9b0"><td class="eid">TOTAL</td><td>$tCnt</td><td>$tCode</td><td>$tNoB</td><td class="$tIc">$tIss</td></tr>
    </tbody>
  </table>
</div>
"@)

# ── RULES SECTION ──
[void]$sb.Append(@'

<div class="section section-anchor" id="rules">
  <h2>
    <span data-lang="en" class="active">1. Promo Code Rules</span>
    <span data-lang="ua">1. &#1055;&#1088;&#1072;&#1074;&#1080;&#1083;&#1072; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1110;&#1074;</span>
    <span data-lang="ru">1. &#1055;&#1088;&#1072;&#1074;&#1080;&#1083;&#1072; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1086;&#1074;</span>
  </h2>
  <p class="desc">
    <span data-lang="en" class="active">How promo codes are placed in each email.</span>
    <span data-lang="ua">&#1071;&#1082; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1080; &#1088;&#1086;&#1079;&#1084;&#1110;&#1097;&#1077;&#1085;&#1110; &#1091; &#1082;&#1086;&#1078;&#1085;&#1086;&#1084;&#1091; &#1083;&#1080;&#1089;&#1090;&#1110;.</span>
    <span data-lang="ru">&#1050;&#1072;&#1082; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1099; &#1088;&#1072;&#1079;&#1084;&#1077;&#1097;&#1077;&#1085;&#1099; &#1074; &#1082;&#1072;&#1078;&#1076;&#1086;&#1084; &#1087;&#1080;&#1089;&#1100;&#1084;&#1077;.</span>
  </p>
  <div class="rule-grid">
    <div class="rule-card">
      <h4><span data-lang="en" class="active">Body &#8212; Wrapper</span><span data-lang="ua">&#1058;&#1110;&#1083;&#1086; &#8212; &#1054;&#1073;&#1075;&#1086;&#1088;&#1090;&#1082;&#1072;</span><span data-lang="ru">&#1058;&#1077;&#1083;&#1086; &#8212; &#1054;&#1073;&#1105;&#1088;&#1090;&#1082;&#1072;</span></h4>
      <p><span data-lang="en" class="active">In the email body, each promo code is wrapped in:</span><span data-lang="ua">&#1059; &#1090;&#1110;&#1083;&#1110; &#1083;&#1080;&#1089;&#1090;&#1072; &#1082;&#1086;&#1078;&#1077;&#1085; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076; &#1086;&#1073;&#1075;&#1086;&#1088;&#1085;&#1091;&#1090;&#1080;&#1081; &#1091;:</span><span data-lang="ru">&#1042; &#1090;&#1077;&#1083;&#1077; &#1087;&#1080;&#1089;&#1100;&#1084;&#1072; &#1082;&#1072;&#1078;&#1076;&#1099;&#1081; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076; &#1086;&#1073;&#1105;&#1088;&#1085;&#1091;&#1090; &#1074;:</span></p>
      <p style="margin-top:8px"><code>&lt;strong class="promocode"&gt;CODE&lt;/strong&gt;</code></p>
      <p style="margin-top:6px"><span data-lang="en" class="active">This ensures the code is visually highlighted and can be automatically copied.</span><span data-lang="ua">&#1062;&#1077; &#1079;&#1072;&#1073;&#1077;&#1079;&#1087;&#1077;&#1095;&#1091;&#1108; &#1074;&#1110;&#1079;&#1091;&#1072;&#1083;&#1100;&#1085;&#1077; &#1074;&#1080;&#1076;&#1110;&#1083;&#1077;&#1085;&#1085;&#1103; &#1082;&#1086;&#1076;&#1091; &#1090;&#1072; &#1084;&#1086;&#1078;&#1083;&#1080;&#1074;&#1110;&#1089;&#1090;&#1100; &#1072;&#1074;&#1090;&#1086;&#1084;&#1072;&#1090;&#1080;&#1095;&#1085;&#1086;&#1075;&#1086; &#1082;&#1086;&#1087;&#1110;&#1102;&#1074;&#1072;&#1085;&#1085;&#1103;.</span><span data-lang="ru">&#1069;&#1090;&#1086; &#1086;&#1073;&#1077;&#1089;&#1087;&#1077;&#1095;&#1080;&#1074;&#1072;&#1077;&#1090; &#1074;&#1080;&#1079;&#1091;&#1072;&#1083;&#1100;&#1085;&#1086;&#1077; &#1074;&#1099;&#1076;&#1077;&#1083;&#1077;&#1085;&#1080;&#1077; &#1082;&#1086;&#1076;&#1072; &#1080; &#1074;&#1086;&#1079;&#1084;&#1086;&#1078;&#1085;&#1086;&#1089;&#1090;&#1100; &#1072;&#1074;&#1090;&#1086;&#1084;&#1072;&#1090;&#1080;&#1095;&#1077;&#1089;&#1082;&#1086;&#1075;&#1086; &#1082;&#1086;&#1087;&#1080;&#1088;&#1086;&#1074;&#1072;&#1085;&#1080;&#1103;.</span></p>
    </div>
    <div class="rule-card">
      <h4><span data-lang="en" class="active">Header &#8212; data-promocode</span><span data-lang="ua">&#1064;&#1072;&#1087;&#1082;&#1072; &#8212; data-promocode</span><span data-lang="ru">&#1064;&#1072;&#1087;&#1082;&#1072; &#8212; data-promocode</span></h4>
      <p><span data-lang="en" class="active">The same promo code(s) must be present in the HTML tag attribute:</span><span data-lang="ua">&#1058;&#1110; &#1089;&#1072;&#1084;&#1110; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1080; &#1084;&#1072;&#1102;&#1090;&#1100; &#1073;&#1091;&#1090;&#1080; &#1074; &#1072;&#1090;&#1088;&#1080;&#1073;&#1091;&#1090;&#1110; HTML-&#1090;&#1077;&#1075;&#1091;:</span><span data-lang="ru">&#1058;&#1077; &#1078;&#1077; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1099; &#1076;&#1086;&#1083;&#1078;&#1085;&#1099; &#1073;&#1099;&#1090;&#1100; &#1074; &#1072;&#1090;&#1088;&#1080;&#1073;&#1091;&#1090;&#1077; HTML-&#1090;&#1077;&#1075;&#1072;:</span></p>
      <p style="margin-top:8px"><code>data-promocode="CODE1, CODE2"</code></p>
      <p style="margin-top:6px"><span data-lang="en" class="active">Header codes should match body codes exactly.</span><span data-lang="ua">&#1050;&#1086;&#1076;&#1080; &#1091; &#1096;&#1072;&#1087;&#1094;&#1110; &#1084;&#1072;&#1102;&#1090;&#1100; &#1090;&#1086;&#1095;&#1085;&#1086; &#1074;&#1110;&#1076;&#1087;&#1086;&#1074;&#1110;&#1076;&#1072;&#1090;&#1080; &#1082;&#1086;&#1076;&#1072;&#1084; &#1091; &#1090;&#1110;&#1083;&#1110;.</span><span data-lang="ru">&#1050;&#1086;&#1076;&#1099; &#1074; &#1096;&#1072;&#1087;&#1082;&#1077; &#1076;&#1086;&#1083;&#1078;&#1085;&#1099; &#1090;&#1086;&#1095;&#1085;&#1086; &#1089;&#1086;&#1086;&#1090;&#1074;&#1077;&#1090;&#1089;&#1090;&#1074;&#1086;&#1074;&#1072;&#1090;&#1100; &#1082;&#1086;&#1076;&#1072;&#1084; &#1074; &#1090;&#1077;&#1083;&#1077;.</span></p>
    </div>
  </div>
  <div class="note">
    <span data-lang="en" class="active"><strong>Status legend:</strong> <span class="s-ok">&#10004; OK</span> &#8212; all codes match &amp; wrapped correctly. <span class="s-w">&#9888; Warning</span> &#8212; mismatch or missing code (e.g., bonus described but no promo code, or header/body code count differs). <span class="s-na">&#8212; N/A</span> &#8212; email has no bonus/promo content.</span>
    <span data-lang="ua"><strong>&#1051;&#1077;&#1075;&#1077;&#1085;&#1076;&#1072; &#1089;&#1090;&#1072;&#1090;&#1091;&#1089;&#1110;&#1074;:</strong> <span class="s-ok">&#10004; OK</span> &#8212; &#1074;&#1089;&#1110; &#1082;&#1086;&#1076;&#1080; &#1079;&#1073;&#1110;&#1075;&#1072;&#1102;&#1090;&#1100;&#1089;&#1103; &#1090;&#1072; &#1086;&#1073;&#1075;&#1086;&#1088;&#1085;&#1091;&#1090;&#1110; &#1087;&#1088;&#1072;&#1074;&#1080;&#1083;&#1100;&#1085;&#1086;. <span class="s-w">&#9888; &#1055;&#1086;&#1087;&#1077;&#1088;&#1077;&#1076;&#1078;&#1077;&#1085;&#1085;&#1103;</span> &#8212; &#1085;&#1077;&#1074;&#1110;&#1076;&#1087;&#1086;&#1074;&#1110;&#1076;&#1085;&#1110;&#1089;&#1090;&#1100; &#1095;&#1080; &#1074;&#1110;&#1076;&#1089;&#1091;&#1090;&#1085;&#1110;&#1089;&#1090;&#1100; &#1082;&#1086;&#1076;&#1091;. <span class="s-na">&#8212; &#1053;/&#1044;</span> &#8212; &#1083;&#1080;&#1089;&#1090; &#1073;&#1077;&#1079; &#1073;&#1086;&#1085;&#1091;&#1089;&#1091;.</span>
    <span data-lang="ru"><strong>&#1051;&#1077;&#1075;&#1077;&#1085;&#1076;&#1072; &#1089;&#1090;&#1072;&#1090;&#1091;&#1089;&#1086;&#1074;:</strong> <span class="s-ok">&#10004; OK</span> &#8212; &#1074;&#1089;&#1077; &#1082;&#1086;&#1076;&#1099; &#1089;&#1086;&#1074;&#1087;&#1072;&#1076;&#1072;&#1102;&#1090; &#1080; &#1086;&#1073;&#1105;&#1088;&#1085;&#1091;&#1090;&#1099; &#1087;&#1088;&#1072;&#1074;&#1080;&#1083;&#1100;&#1085;&#1086;. <span class="s-w">&#9888; &#1055;&#1088;&#1077;&#1076;&#1091;&#1087;&#1088;&#1077;&#1078;&#1076;&#1077;&#1085;&#1080;&#1077;</span> &#8212; &#1085;&#1077;&#1089;&#1086;&#1086;&#1090;&#1074;&#1077;&#1090;&#1089;&#1090;&#1074;&#1080;&#1077; &#1080;&#1083;&#1080; &#1086;&#1090;&#1089;&#1091;&#1090;&#1089;&#1090;&#1074;&#1080;&#1077; &#1082;&#1086;&#1076;&#1072;. <span class="s-na">&#8212; &#1053;/&#1044;</span> &#8212; &#1087;&#1080;&#1089;&#1100;&#1084;&#1086; &#1073;&#1077;&#1079; &#1073;&#1086;&#1085;&#1091;&#1089;&#1072;.</span>
  </div>
</div>
'@)

# ── CAMPAIGN SECTIONS ──
$secNum = 2
foreach($camp in $allCampaigns) {
    $anchor = $camp.id
    $cname  = $camp.name
    $cnt    = $camp.count
    $wc     = $camp.withCode
    $iss    = $camp.issues
    $nwc    = $cnt - $wc
    $skipW  = $camp.skipWrapper

    $issEN = if($iss -gt 0){"$iss issue(s) found."}else{"All clean &#8212; no issues."}
    $issUA = if($iss -gt 0){"$iss &#1087;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084;(&#1080;)."}else{"&#1042;&#1089;&#1077; &#1095;&#1080;&#1089;&#1090;&#1086; &#8212; &#1087;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084; &#1085;&#1077;&#1084;&#1072;&#1108;."}
    $issRU = if($iss -gt 0){"$iss &#1087;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084;(&#1099;)."}else{"&#1042;&#1089;&#1105; &#1095;&#1080;&#1089;&#1090;&#1086; &#8212; &#1087;&#1088;&#1086;&#1073;&#1083;&#1077;&#1084; &#1085;&#1077;&#1090;."}

    [void]$sb.Append(@"

<div class="section section-anchor" id="$anchor">
  <h2>
    <span data-lang="en" class="active">$secNum. $cname &#8212; $cnt emails</span>
    <span data-lang="ua">$secNum. $cname &#8212; $cnt &#1083;&#1080;&#1089;&#1090;&#1110;&#1074;</span>
    <span data-lang="ru">$secNum. $cname &#8212; $cnt &#1087;&#1080;&#1089;&#1077;&#1084;</span>
  </h2>
  <p class="desc">
    <span data-lang="en" class="active">$wc with promo code, $nwc without. $issEN</span>
    <span data-lang="ua">$wc &#1079; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1086;&#1084;, $nwc &#1073;&#1077;&#1079;. $issUA</span>
    <span data-lang="ru">$wc &#1089; &#1087;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;&#1086;&#1084;, $nwc &#1073;&#1077;&#1079;. $issRU</span>
  </p>
"@)

    # Table header
    if($skipW) {
        [void]$sb.Append(@'
  <table class="at">
    <thead><tr>
      <th>#</th>
      <th>Email</th>
      <th><span data-lang="en" class="active">Bonus</span><span data-lang="ua">&#1041;&#1086;&#1085;&#1091;&#1089;</span><span data-lang="ru">&#1041;&#1086;&#1085;&#1091;&#1089;</span></th>
      <th><span data-lang="en" class="active">Game</span><span data-lang="ua">&#1043;&#1088;&#1072;</span><span data-lang="ru">&#1048;&#1075;&#1088;&#1072;</span></th>
      <th><span data-lang="en" class="active">Promo Code</span><span data-lang="ua">&#1055;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;</span><span data-lang="ru">&#1055;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;</span></th>
      <th><span data-lang="en" class="active">Header</span><span data-lang="ua">&#1064;&#1072;&#1087;&#1082;&#1072;</span><span data-lang="ru">&#1064;&#1072;&#1087;&#1082;&#1072;</span></th>
      <th><span data-lang="en" class="active">Status</span><span data-lang="ua">&#1057;&#1090;&#1072;&#1090;&#1091;&#1089;</span><span data-lang="ru">&#1057;&#1090;&#1072;&#1090;&#1091;&#1089;</span></th>
    </tr></thead>
    <tbody>
'@)
    } else {
        [void]$sb.Append(@'
  <table class="at">
    <thead><tr>
      <th>#</th>
      <th>Email</th>
      <th><span data-lang="en" class="active">Bonus</span><span data-lang="ua">&#1041;&#1086;&#1085;&#1091;&#1089;</span><span data-lang="ru">&#1041;&#1086;&#1085;&#1091;&#1089;</span></th>
      <th><span data-lang="en" class="active">Game</span><span data-lang="ua">&#1043;&#1088;&#1072;</span><span data-lang="ru">&#1048;&#1075;&#1088;&#1072;</span></th>
      <th><span data-lang="en" class="active">Promo Code</span><span data-lang="ua">&#1055;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;</span><span data-lang="ru">&#1055;&#1088;&#1086;&#1084;&#1086;&#1082;&#1086;&#1076;</span></th>
      <th><span data-lang="en" class="active">Header</span><span data-lang="ua">&#1064;&#1072;&#1087;&#1082;&#1072;</span><span data-lang="ru">&#1064;&#1072;&#1087;&#1082;&#1072;</span></th>
      <th><span data-lang="en" class="active">Wrapper</span><span data-lang="ua">&#1054;&#1073;&#1075;&#1086;&#1088;&#1090;&#1082;&#1072;</span><span data-lang="ru">&#1054;&#1073;&#1105;&#1088;&#1090;&#1082;&#1072;</span></th>
      <th><span data-lang="en" class="active">Status</span><span data-lang="ua">&#1057;&#1090;&#1072;&#1090;&#1091;&#1089;</span><span data-lang="ru">&#1057;&#1090;&#1072;&#1090;&#1091;&#1089;</span></th>
    </tr></thead>
    <tbody>
'@)
    }

    # Table rows
    $n = 0
    foreach($e in $camp.emails) {
        $n++

        # Bonus
        $bonusHtml = if($e.bonuses.Count -gt 0){ Esc ($e.bonuses -join ", ") }else{'<span class="s-na">&#8212;</span>'}

        # Game
        $gameHtml = if($e.games.Count -gt 0){ '<span class="game">' + (Esc ($e.games -join ", ")) + '</span>' }else{'<span class="s-na">&#8212;</span>'}

        # Promo code
        $allCodes = @()
        if($e.bodyCodes.Count -gt 0){$allCodes = $e.bodyCodes}
        elseif($e.headerCodes.Count -gt 0){$allCodes = $e.headerCodes}
        $codeHtml = if($allCodes.Count -gt 0){
            ($allCodes | ForEach-Object { '<span class="code">' + (Esc $_) + '</span>' }) -join " "
        }else{'<span class="s-na">&#8212;</span>'}

        # Header check
        $hdrHtml = if($e.hasHeader){'<span class="s-ok">&#10004;</span>'}
                   elseif($allCodes.Count -gt 0){'<span class="s-e">&#10008;</span>'}
                   else{'<span class="s-na">&#8212;</span>'}

        # Wrapper check
        $wrpHtml = if($e.hasWrapper){'<span class="s-ok">&#10004;</span>'}
                   elseif($allCodes.Count -gt 0){'<span class="s-e">&#10008;</span>'}
                   else{'<span class="s-na">&#8212;</span>'}

        # Status
        if($e.status -eq "ok") {
            $stHtml = if($allCodes.Count -eq 0 -and $e.bonuses.Count -eq 0){'<span class="s-na">&#8212;</span>'}else{'<span class="s-ok">OK</span>'}
        } elseif($e.status -eq "warn") {
            $noteEsc = Esc $e.statusNote
            $stHtml = "<span class=`"s-w`" title=`"$noteEsc`">&#9888; $noteEsc</span>"
        } else {
            $stHtml = '<span class="s-e">&#10008; ERROR</span>'
        }

        $eName = Esc $e.name
        if($skipW) {
            [void]$sb.AppendLine("      <tr><td>$n</td><td class=`"eid`">$eName</td><td>$bonusHtml</td><td>$gameHtml</td><td>$codeHtml</td><td class=`"chk`">$hdrHtml</td><td>$stHtml</td></tr>")
        } else {
            [void]$sb.AppendLine("      <tr><td>$n</td><td class=`"eid`">$eName</td><td>$bonusHtml</td><td>$gameHtml</td><td>$codeHtml</td><td class=`"chk`">$hdrHtml</td><td class=`"chk`">$wrpHtml</td><td>$stHtml</td></tr>")
        }
    }

    [void]$sb.Append(@'
    </tbody>
  </table>
</div>
'@)
    $secNum++
}

# ── ASSEMBLE FINAL REPORT ──
$shellHtml = Get-Content $shell -Encoding UTF8 -Raw
$finalHtml = $shellHtml -replace '<!-- %%DYNAMIC_CONTENT%% -->', $sb.ToString()
[System.IO.File]::WriteAllText($outPath, $finalHtml, [System.Text.Encoding]::UTF8)

Write-Host "`nReport generated successfully: $outPath" -ForegroundColor Green
Write-Host "Total: $totalEmails emails, $totalWithCode with code, $totalIssues issues"
foreach($c in $allCampaigns) {
    $bar = if($c.issues -gt 0){"  [!$($c.issues)]"}else{""}
    Write-Host "  $($c.name): $($c.count) emails, $($c.withCode) with code$bar"
}
