# Generate the rebuilt Celsius Text Audit report
# Reads all 6 data files, extracts per-email data, generates complete HTML report

$ErrorActionPreference = 'Stop'
$outPath = "C:\Projects\REPORTS\pages\promptgrid\REPORT_text_audit_celsius.html"

# ── PARSING FUNCTIONS ──
function Strip-Html($text) {
    $t = $text -replace '<br\s*/?>', ' '
    $t = $t -replace '<[^>]+>', ' '
    $t = $t -replace '&nbsp;', ' '
    $t = $t -replace '&amp;', '&'
    $t = $t -replace '&lt;', '<'
    $t = $t -replace '&gt;', '>'
    $t = $t -replace '\s+', ' '
    return $t.Trim()
}

function Extract-Bonuses($rawHtml) {
    $bonuses = [System.Collections.Generic.List[string]]::new()
    
    # Extract from <strong> tags the meaningful bonus parts
    $strongMatches = [regex]::Matches($rawHtml, '<strong[^>]*>([^<]+)</strong>', 'IgnoreCase')
    $strongTexts = @()
    foreach($m in $strongMatches) { 
        $val = $m.Groups[1].Value.Trim()
        if($val -and $val -ne '' -and $val.Length -gt 1) { $strongTexts += $val }
    }
    $allStrong = $strongTexts -join ' '
    
    $clean = Strip-Html $rawHtml
    
    # Pattern: X% + Y FS / Free Spins (compound bonus)
    $ms = [regex]::Matches($clean, '(\d{2,3})%\s*(?:bonus)?\s*\+\s*(\d+)\s*(?:Free Spins?|FS)', 'IgnoreCase')
    foreach($m in $ms) { 
        $b = "$($m.Groups[1].Value)% + $($m.Groups[2].Value) FS"
        if(-not $bonuses.Contains($b)) { $bonuses.Add($b) }
    }
    
    # Pattern: standalone Y FS / Free Spins (not part of compound)
    $ms = [regex]::Matches($clean, '(?<!\+\s{0,3})(\d{2,4})\s*(?:Free Spins?|FS\b)', 'IgnoreCase')
    foreach($m in $ms) {
        $num = $m.Groups[1].Value
        $val = "$num FS"
        $isPartOfCompound = $false
        foreach($b in $bonuses) { if($b -match "\+ $num FS") { $isPartOfCompound = $true; break } }
        if(-not $isPartOfCompound -and -not $bonuses.Contains($val) -and [int]$num -ge 10) { $bonuses.Add($val) }
    }
    
    # Pattern: X% NoRisk FreeBet / NRF
    $ms = [regex]::Matches($clean, '(\d{1,3})%\s*(?:NoRisk\s*(?:Free\s*Bets?|FreeBets?)|NRF|No\s*Risk\s*(?:Free\s*Bets?|FreeBets?|Only\s*Win))', 'IgnoreCase')
    foreach($m in $ms) { 
        $val = "$($m.Groups[1].Value)% NRF"
        if(-not $bonuses.Contains($val)) { $bonuses.Add($val) }
    }
    
    # Pattern: X% NoRisk Only Win
    $ms = [regex]::Matches($clean, '(\d{1,3})%\s*(?:No\s*Risk\s*Only\s*Win)', 'IgnoreCase')
    foreach($m in $ms) { 
        $val = "$($m.Groups[1].Value)% NRF"
        if(-not $bonuses.Contains($val)) { $bonuses.Add($val) }
    }
    
    # Pattern: X% Cashback / CB
    $ms = [regex]::Matches($clean, '(\d{1,2})%\s*(?:Cashback|CB)', 'IgnoreCase')
    foreach($m in $ms) { 
        $val = "$($m.Groups[1].Value)% CB"
        if(-not $bonuses.Contains($val)) { $bonuses.Add($val) }
    }
    
    # Pattern: X% FreeBets (sport, standalone)
    $ms = [regex]::Matches($clean, '(\d{2,3})%\s*Free\s*Bets?\b', 'IgnoreCase')
    foreach($m in $ms) {
        $pct = $m.Groups[1].Value
        $val = "$pct% FreeBets"
        # Don't add if already have NRF with same %
        $hasNrf = $false
        foreach($b in $bonuses) { if($b -eq "$pct% NRF") { $hasNrf = $true; break } }
        if(-not $hasNrf -and -not $bonuses.Contains($val)) { $bonuses.Add($val) }
    }
    
    # Pattern: standalone X% (deposit bonus, high %)
    $ms = [regex]::Matches($allStrong, '\b(\d{2,3})%\b', 'IgnoreCase')
    foreach($m in $ms) {
        $pct = [int]$m.Groups[1].Value
        $pctStr = "$pct%"
        if($pct -lt 50 -or $pct -gt 300) { continue }
        # Skip if already part of another bonus
        $partOf = $false
        foreach($b in $bonuses) { if($b -match "^$pct%") { $partOf = $true; break } }
        if(-not $partOf -and -not $bonuses.Contains($pctStr)) {
            # Check context: should be a deposit bonus, not a random percentage
            if($clean -match "$pct%\s*(?:bonus|on|deposit|Bonus)" -or 
               $clean -match "code.*$pct%" -or
               $clean -match "$pct%.*on your" -or
               $allStrong -match "^$pct%$") {
                $bonuses.Add($pctStr)
            }
        }
    }
    
    return $bonuses.ToArray()
}

function Extract-Games($rawHtml) {
    $games = [System.Collections.Generic.List[string]]::new()
    
    # Pattern: in <strong>GameName</strong> <strong>by Provider</strong>
    $ms = [regex]::Matches($rawHtml, '(?:in|on)\s+<strong>([^<]+?)</strong>\s*<strong>by\s+([^<]+)</strong>', 'IgnoreCase')
    foreach($m in $ms) { 
        $g = "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())"
        if(-not $games.Contains($g)) { $games.Add($g) }
    }
    
    # Pattern: in <strong>GameName by Provider</strong>
    if($games.Count -eq 0) {
        $ms = [regex]::Matches($rawHtml, '(?:in|on)\s+<strong>([^<]+?)\s+by\s+([^<]+?)</strong>', 'IgnoreCase')
        foreach($m in $ms) { 
            $g = "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())"
            if(-not $games.Contains($g)) { $games.Add($g) }
        }
    }
    
    # Pattern in clean text: in GameName by Provider (Hacksaw|Pragmatic|Push|Nolimit|Play'n|Relax)
    if($games.Count -eq 0) {
        $clean = Strip-Html $rawHtml
        $ms = [regex]::Matches($clean, '(?:in|on)\s+([\w\s'']+?)\s+by\s+((?:Hacksaw|Pragmatic|Push|Nolimit|Play.n|Relax)\s*\w*)', 'IgnoreCase')
        foreach($m in $ms) { 
            $g = "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())"
            if($g -notmatch '^(?:your|the game|favor)' -and -not $games.Contains($g)) { $games.Add($g) }
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
        
        # Header promo codes
        $e.headerCodes = @()
        if($block -match 'data-promocode\s*=\s*"([^"]+)"') {
            $e.headerCodes = @(($Matches[1] -split ',\s*') | ForEach-Object { $_.Trim() } | Where-Object { $_ })
        }
        
        # Collect all body text_X fields
        $bodyHtml = ""
        $textMatches = [regex]::Matches($block, 'text_\d+:\s*(.+?)(?=\n(?:text_\d+|button_text|name):|$)', 'Singleline')
        foreach($m in $textMatches) { $bodyHtml += " " + $m.Groups[1].Value }
        
        # Body wrapped codes <strong class="promocode">CODE</strong>
        $e.bodyCodes = @()
        $wcm = [regex]::Matches($bodyHtml, '<strong class="promocode">([A-Z0-9]+)\s*</strong>')
        foreach($m in $wcm) { $e.bodyCodes += $m.Groups[1].Value.Trim() }
        $e.bodyCodes = @($e.bodyCodes | Select-Object -Unique)
        
        # Bonuses & Games
        $e.bonuses = @(Extract-Bonuses $bodyHtml)
        $e.games = @(Extract-Games $bodyHtml)
        
        # Flags
        $e.hasHeader = ($e.headerCodes.Count -gt 0)
        $e.hasWrapper = ($e.bodyCodes.Count -gt 0)
        
        # Header/body match check
        $e.headerMatchesBody = $true
        if($e.headerCodes.Count -gt 0 -or $e.bodyCodes.Count -gt 0) {
            $hSet = @($e.headerCodes | Sort-Object)
            $bSet = @($e.bodyCodes | Sort-Object)
            if($hSet.Count -ne $bSet.Count) { $e.headerMatchesBody = $false }
            else {
                for($i=0; $i -lt $hSet.Count; $i++) {
                    if($hSet[$i] -ne $bSet[$i]) { $e.headerMatchesBody = $false; break }
                }
            }
        }
        
        # Determine status
        $e.status = "ok"
        $e.statusNote = ""
        $cleanBody = Strip-Html $bodyHtml
        $hasBonusContent = ($cleanBody -match '\d+%\s*(?:\+|bonus|deposit|on|NRF|NoRisk|Cashback|CB|Free)' -or $cleanBody -match '\d+\s*(?:FS|Free Spin)')
        
        if($e.bodyCodes.Count -eq 0 -and $e.headerCodes.Count -eq 0 -and $hasBonusContent -and $e.bonuses.Count -gt 0) {
            $e.status = "warn"
            $e.statusNote = "Bonus without promo code"
        } elseif(-not $e.headerMatchesBody) {
            if($e.headerCodes.Count -eq 0 -and $e.bodyCodes.Count -gt 0) {
                $e.status = "warn"
                $e.statusNote = "No header code"
            } elseif($e.headerCodes.Count -gt 0 -and $e.bodyCodes.Count -eq 0) {
                $e.status = "warn"
                $e.statusNote = "Header only, no body wrapper"
            } elseif($e.headerCodes.Count -ne $e.bodyCodes.Count) {
                $e.status = "warn"
                $e.statusNote = "Header/body count mismatch"
            } else {
                $e.status = "warn"
                $e.statusNote = "Header/body mismatch"
            }
        }
        
        $emails += $e
    }
    return $emails
}

# ── PARSE ALL CAMPAIGNS ──
$dir = "C:\Projects\REPORTS\тексти"
$campaigns = @(
    @{id="dep-retention"; name="DEP Retention"; file="DEP Retention - Table data.txt"; skipWrapper=$true},
    @{id="ftd-retention"; name="FTD Retention"; file="FTD Retention Flow - Table data.txt"; skipWrapper=$false},
    @{id="nutrition-2"; name="Nutrition #2"; file="Nutrition #2 - Table data.txt"; skipWrapper=$false},
    @{id="nutrition-3"; name="Nutrition #3"; file="Nutrition #3 - Table data.txt"; skipWrapper=$false},
    @{id="su-retention"; name="SU Retention"; file="SU Retention - Table data.txt"; skipWrapper=$false},
    @{id="welcome-flow"; name="Welcome Flow"; file="Welcome Flow - Table data.txt"; skipWrapper=$false}
)

$allCampaigns = @()
$totalEmails = 0; $totalWithCode = 0; $totalIssues = 0
foreach($c in $campaigns) {
    $emails = Parse-Campaign (Join-Path $dir $c.file)
    $withCode = @($emails | Where-Object { $_.bodyCodes.Count -gt 0 -or $_.headerCodes.Count -gt 0 }).Count
    $issues = @($emails | Where-Object { $_.status -ne "ok" }).Count
    $noBonus = @($emails | Where-Object { $_.bodyCodes.Count -eq 0 -and $_.headerCodes.Count -eq 0 -and $_.bonuses.Count -eq 0 }).Count
    $allCampaigns += @{
        id = $c.id; name = $c.name; skipWrapper = $c.skipWrapper
        emails = $emails; count = $emails.Count
        withCode = $withCode; issues = $issues; noBonus = $noBonus
    }
    $totalEmails += $emails.Count
    $totalWithCode += $withCode
    $totalIssues += $issues
}

# ── HTML HELPER ──
function Esc($text) { return [System.Net.WebUtility]::HtmlEncode($text) }

# ── BUILD HTML ──
$html = [System.Text.StringBuilder]::new()

# HEAD
[void]$html.AppendLine('<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Celsius — Text Audit Report</title>
<link rel="icon" type="image/svg+xml" href="../../assets/pg-logo.svg">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#181818;color:#d4d4d4;font-family:''Montserrat'',sans-serif;font-size:14px;line-height:1.6;max-width:1060px;margin:0 auto;padding:0}
a{color:#4ec9b0;text-decoration:none}
div[data-lang],p[data-lang],h1[data-lang]{display:none}
div[data-lang].active,p[data-lang].active,h1[data-lang].active{display:block}
span[data-lang]{display:none}
span[data-lang].active{display:inline}
.report-header{background:linear-gradient(135deg,#181818 0%,#212121 100%);padding:48px 40px 40px;border-bottom:3px solid #4ec9b0;position:relative}
.report-header .logo{height:28px;margin-bottom:0}
.report-header h1{font-size:26px;font-weight:700;color:#fff;margin:0 0 8px 0;letter-spacing:-.5px}
.report-header .meta{color:#888;font-size:13px;margin:0}
.report-header .meta span{color:#4ec9b0;font-weight:600}
.gnb-line{font-size:11px;color:#666;display:flex;align-items:center;gap:5px}
.gnb-line img{height:14px}
.report-footer .gnb-line{justify-content:center}
.lang-switcher{position:absolute;top:20px;right:40px;display:flex;gap:6px}
.lang-btn{background:#212121;border:1px solid #3a3a3a;border-radius:8px;padding:6px 14px;cursor:pointer;font-size:13px;color:#888;font-family:inherit;font-weight:500;transition:all .2s;display:flex;align-items:center;gap:6px}
.lang-btn:hover{border-color:#4ec9b0;color:#ccc}
.lang-btn.active{background:#4ec9b0;color:#181818;border-color:#4ec9b0;font-weight:700}
.report-nav{position:sticky;top:0;z-index:100;background:rgba(24,24,24,.92);border-bottom:1px solid #2d2d2d;padding:10px 40px;display:flex;gap:6px;backdrop-filter:blur(14px);overflow-x:auto;overflow-y:hidden;scrollbar-width:thin;scrollbar-color:#4ec9b0 #1e1e1e;-webkit-overflow-scrolling:touch}
.report-nav::before,.report-nav::after{content:'''';flex:1 0 0px}
.report-nav::-webkit-scrollbar{height:5px}
.report-nav::-webkit-scrollbar-track{background:#1e1e1e;border-radius:3px}
.report-nav::-webkit-scrollbar-thumb{background:#4ec9b0;border-radius:3px}
.nav-link{background:transparent;border:1px solid #3a3a3a;border-radius:20px;padding:5px 14px;font-size:12px;font-weight:500;color:#888;text-decoration:none;cursor:pointer;transition:all .25s;font-family:inherit;white-space:nowrap;flex-shrink:0}
.nav-link:hover{border-color:#4ec9b0;color:#ccc}
.nav-link.active{background:#4ec9b0;color:#181818;border-color:#4ec9b0;font-weight:700}
.nav-num{font-weight:700;margin-right:4px;font-size:11px;opacity:.7}
.section-anchor{scroll-margin-top:56px}
.content{padding:0 40px 60px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:30px 0 40px}
.card{background:#1c1c1c;border:1px solid #2d2d2d;border-radius:12px;padding:24px;text-align:center}
.card-value{font-size:36px;font-weight:800;color:#4ec9b0}
.card-value.warn{color:#cca700}
.card-label{font-size:12px;color:#888;margin-top:6px;text-transform:uppercase;letter-spacing:.5px}
.section{margin-bottom:50px}
.section h2{font-size:20px;font-weight:700;color:#fff;margin-bottom:6px;padding-bottom:12px;border-bottom:2px solid #4ec9b0}
.section .desc{font-size:13px;color:#888;margin-bottom:16px}
.at{width:100%;border-collapse:collapse;font-size:12px;margin-bottom:24px}
.at thead{background:#1a1a1a;position:sticky;top:48px;z-index:10}
.at th{padding:8px 10px;text-align:left;font-weight:600;color:#aaa;border-bottom:2px solid #2d2d2d;white-space:nowrap;font-size:11px;text-transform:uppercase;letter-spacing:.3px}
.at td{padding:7px 10px;border-bottom:1px solid #232323;vertical-align:top}
.at tr:hover{background:#1e1e1e}
.eid{font-weight:600;color:#fff;white-space:nowrap}
.s-ok{color:#25b644}
.s-w{color:#cca700}
.s-e{color:#f14c4c}
.s-na{color:#555}
.code{font-family:Consolas,''Courier New'',monospace;font-size:11px;background:#1e1e1e;padding:1px 5px;border-radius:3px;border:1px solid #333;color:#4ec9b0;white-space:nowrap}
.game{font-size:11px;color:#999;font-style:italic}
.chk{text-align:center;font-size:14px}
.note{background:rgba(78,201,176,0.08);border-left:3px solid #4ec9b0;padding:14px 18px;margin:14px 0;border-radius:0 8px 8px 0;font-size:13px;color:#b0b0b0}
.note strong{color:#4ec9b0}
.report-footer{text-align:center;padding:40px;border-top:1px solid #2d2d2d;margin-top:40px}
.report-footer p{font-size:11px;color:#555}
.logo-sm{height:16px;vertical-align:middle;margin-bottom:0}
.rule-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0 24px}
.rule-card{background:#1c1c1c;border:1px solid #2d2d2d;border-radius:10px;padding:18px 20px}
.rule-card h4{color:#fff;font-size:13px;margin-bottom:8px}
.rule-card code{font-family:Consolas,monospace;font-size:11px;background:#1e1e1e;padding:2px 6px;border-radius:3px;border:1px solid #333;color:#4ec9b0}
.rule-card p{font-size:12px;color:#999;margin:4px 0}
@media(max-width:768px){.cards{grid-template-columns:1fr}.content{padding:0 16px 40px}.report-nav{padding:10px 16px}.at{font-size:11px}.rule-grid{grid-template-columns:1fr}}
</style>
</head>
<body>')

# HEADER
[void]$html.AppendLine('
<div class="report-header">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:6px;">
    <img class="logo" src="../../assets/pg-logo.svg" alt="PromptGrid">
    <span style="font-size:22px;font-weight:600;color:#fff;letter-spacing:-0.5px;">PromptGrid</span>
  </div>
  <div class="gnb-line" style="margin-bottom:24px;"><img src="../../assets/gnb-favicon.svg" alt="GNB"><span>Specially for GNB Agency</span></div>

  <div class="lang-switcher">
    <button class="lang-btn active" data-set-lang="en">EN</button>
    <button class="lang-btn" data-set-lang="ua">UA</button>
    <button class="lang-btn" data-set-lang="ru">RU</button>
  </div>

  <h1 data-lang="en" class="active">Celsius — Text Audit Report</h1>
  <p class="meta" data-lang="en"><span>Celsius Casino / Celsius Sport</span> &bull; <span>2025</span> &bull; Comprehensive per-email audit of 6 campaigns &middot; 159 emails</p>
  <h1 data-lang="ua">Celsius — Аудит текстів</h1>
  <p class="meta" data-lang="ua"><span>Celsius Casino / Celsius Sport</span> &bull; <span>2025</span> &bull; Детальний поемейловий аудит 6 кампаній &middot; 159 листів</p>
  <h1 data-lang="ru">Celsius — Аудит текстов</h1>
  <p class="meta" data-lang="ru"><span>Celsius Casino / Celsius Sport</span> &bull; <span>2025</span> &bull; Детальный поемейловый аудит 6 кампаний &middot; 159 писем</p>
</div>')

# NAV
[void]$html.AppendLine('
<nav class="report-nav">
  <a class="nav-link active" href="#summary"><span class="nav-num">0</span>
    <span data-lang="en" class="active">Summary</span><span data-lang="ua">Підсумок</span><span data-lang="ru">Итоги</span></a>
  <a class="nav-link" href="#rules"><span class="nav-num">1</span>
    <span data-lang="en" class="active">Rules</span><span data-lang="ua">Правила</span><span data-lang="ru">Правила</span></a>
  <a class="nav-link" href="#dep-retention"><span class="nav-num">2</span>DEP Retention</a>
  <a class="nav-link" href="#ftd-retention"><span class="nav-num">3</span>FTD Retention</a>
  <a class="nav-link" href="#nutrition-2"><span class="nav-num">4</span>Nutrition #2</a>
  <a class="nav-link" href="#nutrition-3"><span class="nav-num">5</span>Nutrition #3</a>
  <a class="nav-link" href="#su-retention"><span class="nav-num">6</span>SU Retention</a>
  <a class="nav-link" href="#welcome-flow"><span class="nav-num">7</span>Welcome Flow</a>
</nav>')

# CONTENT START
[void]$html.AppendLine('
<div class="content">')

# SUMMARY
[void]$html.AppendLine("
<div class=""section section-anchor"" id=""summary"">
  <h2>
    <span data-lang=""en"" class=""active"">Summary</span>
    <span data-lang=""ua"">Підсумок</span>
    <span data-lang=""ru"">Итоги</span>
  </h2>
  <div class=""cards"">
    <div class=""card"">
      <div class=""card-value"">$totalEmails</div>
      <div class=""card-label"">
        <span data-lang=""en"" class=""active"">Total Emails</span>
        <span data-lang=""ua"">Всього листів</span>
        <span data-lang=""ru"">Всего писем</span>
      </div>
    </div>
    <div class=""card"">
      <div class=""card-value"">$totalWithCode</div>
      <div class=""card-label"">
        <span data-lang=""en"" class=""active"">With Promo Code</span>
        <span data-lang=""ua"">З промокодом</span>
        <span data-lang=""ru"">С промокодом</span>
      </div>
    </div>
    <div class=""card"">
      <div class=""card-value$(if($totalIssues -gt 0){' warn'})"">$totalIssues</div>
      <div class=""card-label"">
        <span data-lang=""en"" class=""active"">Issues Found</span>
        <span data-lang=""ua"">Знайдено проблем</span>
        <span data-lang=""ru"">Найдено проблем</span>
      </div>
    </div>
  </div>")

# Summary table
[void]$html.AppendLine('  <table class="at">
    <thead><tr>
      <th><span data-lang="en" class="active">Campaign</span><span data-lang="ua">Кампанія</span><span data-lang="ru">Кампания</span></th>
      <th><span data-lang="en" class="active">Emails</span><span data-lang="ua">Листів</span><span data-lang="ru">Писем</span></th>
      <th><span data-lang="en" class="active">With Code</span><span data-lang="ua">З кодом</span><span data-lang="ru">С кодом</span></th>
      <th><span data-lang="en" class="active">No Bonus</span><span data-lang="ua">Без бонусу</span><span data-lang="ru">Без бонуса</span></th>
      <th><span data-lang="en" class="active">Issues</span><span data-lang="ua">Проблем</span><span data-lang="ru">Проблем</span></th>
    </tr></thead>
    <tbody>')
$tCnt = 0; $tCode = 0; $tNoB = 0; $tIss = 0
foreach($c in $allCampaigns) {
    $issClass = if($c.issues -gt 0){"s-w"}else{"s-ok"}
    [void]$html.AppendLine("      <tr><td class=""eid"">$($c.name)</td><td>$($c.count)</td><td>$($c.withCode)</td><td>$($c.noBonus)</td><td class=""$issClass"">$($c.issues)</td></tr>")
    $tCnt += $c.count; $tCode += $c.withCode; $tNoB += $c.noBonus; $tIss += $c.issues
}
$tIssClass = if($tIss -gt 0){"s-w"}else{"s-ok"}
[void]$html.AppendLine("      <tr style=""font-weight:700;border-top:2px solid #4ec9b0""><td class=""eid"">TOTAL</td><td>$tCnt</td><td>$tCode</td><td>$tNoB</td><td class=""$tIssClass"">$tIss</td></tr>")
[void]$html.AppendLine('    </tbody>
  </table>
</div>')

# RULES SECTION
[void]$html.AppendLine('
<div class="section section-anchor" id="rules">
  <h2>
    <span data-lang="en" class="active">1. Promo Code Rules</span>
    <span data-lang="ua">1. Правила промокодів</span>
    <span data-lang="ru">1. Правила промокодов</span>
  </h2>
  <p class="desc">
    <span data-lang="en" class="active">How promo codes are placed in each email.</span>
    <span data-lang="ua">Як промокоди розміщені у кожному листі.</span>
    <span data-lang="ru">Как промокоды размещены в каждом письме.</span>
  </p>
  <div class="rule-grid">
    <div class="rule-card">
      <h4><span data-lang="en" class="active">Body — Wrapper</span><span data-lang="ua">Тіло — Обгортка</span><span data-lang="ru">Тело — Обёртка</span></h4>
      <p><span data-lang="en" class="active">In the email body, each promo code is wrapped in:</span><span data-lang="ua">У тілі листа кожен промокод обгорнутий у:</span><span data-lang="ru">В теле письма каждый промокод обёрнут в:</span></p>
      <p style="margin-top:8px"><code>&lt;strong class="promocode"&gt;CODE&lt;/strong&gt;</code></p>
      <p style="margin-top:6px"><span data-lang="en" class="active">This ensures the code is visually highlighted and can be automatically copied.</span><span data-lang="ua">Це забезпечує візуальне виділення коду та можливість автоматичного копіювання.</span><span data-lang="ru">Это обеспечивает визуальное выделение кода и возможность автоматического копирования.</span></p>
    </div>
    <div class="rule-card">
      <h4><span data-lang="en" class="active">Header — data-promocode</span><span data-lang="ua">Шапка — data-promocode</span><span data-lang="ru">Шапка — data-promocode</span></h4>
      <p><span data-lang="en" class="active">The same promo code(s) must be present in the HTML <code>&lt;html&gt;</code> tag attribute:</span><span data-lang="ua">Ті самі промокоди мають бути в атрибуті HTML-тегу <code>&lt;html&gt;</code>:</span><span data-lang="ru">Те же промокоды должны быть в атрибуте HTML-тега <code>&lt;html&gt;</code>:</span></p>
      <p style="margin-top:8px"><code>data-promocode="CODE1, CODE2"</code></p>
      <p style="margin-top:6px"><span data-lang="en" class="active">Header codes should match body codes exactly.</span><span data-lang="ua">Коди у шапці мають точно відповідати кодам у тілі.</span><span data-lang="ru">Коды в шапке должны точно соответствовать кодам в теле.</span></p>
    </div>
  </div>
  <div class="note">
    <span data-lang="en" class="active"><strong>Status legend:</strong> <span class="s-ok">✅ OK</span> — all codes match &amp; wrapped correctly. <span class="s-w">⚠️ Warning</span> — mismatch or missing code (e.g., bonus described but no promo code, or header/body code count differs). <span class="s-na">— N/A</span> — email has no bonus/promo content (engagement or social proof email).</span>
    <span data-lang="ua"><strong>Легенда статусів:</strong> <span class="s-ok">✅ OK</span> — всі коди збігаються та обгорнуті правильно. <span class="s-w">⚠️ Попередження</span> — невідповідність чи відсутність коду. <span class="s-na">— Н/Д</span> — лист без бонусу (лист залучення або соц. доказ).</span>
    <span data-lang="ru"><strong>Легенда статусов:</strong> <span class="s-ok">✅ OK</span> — все коды совпадают и обёрнуты правильно. <span class="s-w">⚠️ Предупреждение</span> — несоответствие или отсутствие кода. <span class="s-na">— Н/Д</span> — письмо без бонуса (вовлекающее или соц. доказательство).</span>
  </div>
</div>')

# ── CAMPAIGN SECTIONS ──
$secNum = 2
foreach($camp in $allCampaigns) {
    $anchor = $camp.id
    $cname = $camp.name
    $cnt = $camp.count
    $wc = $camp.withCode
    $iss = $camp.issues
    
    $skipW = $camp.skipWrapper
    
    # Section header
    [void]$html.AppendLine("
<div class=""section section-anchor"" id=""$anchor"">
  <h2>
    <span data-lang=""en"" class=""active"">$secNum. $cname — $cnt emails</span>
    <span data-lang=""ua"">$secNum. $cname — $cnt листів</span>
    <span data-lang=""ru"">$secNum. $cname — $cnt писем</span>
  </h2>
  <p class=""desc"">
    <span data-lang=""en"" class=""active"">$wc with promo code, $($cnt - $wc) without. $(if($iss -gt 0){"$iss issue(s) found."}else{"All clean — no issues."})</span>
    <span data-lang=""ua"">$wc з промокодом, $($cnt - $wc) без. $(if($iss -gt 0){"$iss проблем(и)."}else{"Все чисто — проблем немає."})</span>
    <span data-lang=""ru"">$wc с промокодом, $($cnt - $wc) без. $(if($iss -gt 0){"$iss проблем(ы)."}else{"Всё чисто — проблем нет."})</span>
  </p>")
    
    # Table header
    if($skipW) {
        [void]$html.AppendLine('  <table class="at">
    <thead><tr>
      <th>#</th>
      <th>Email</th>
      <th><span data-lang="en" class="active">Bonus</span><span data-lang="ua">Бонус</span><span data-lang="ru">Бонус</span></th>
      <th><span data-lang="en" class="active">Game</span><span data-lang="ua">Гра</span><span data-lang="ru">Игра</span></th>
      <th><span data-lang="en" class="active">Promo Code</span><span data-lang="ua">Промокод</span><span data-lang="ru">Промокод</span></th>
      <th><span data-lang="en" class="active">Header</span><span data-lang="ua">Шапка</span><span data-lang="ru">Шапка</span></th>
      <th><span data-lang="en" class="active">Status</span><span data-lang="ua">Статус</span><span data-lang="ru">Статус</span></th>
    </tr></thead>
    <tbody>')
    } else {
        [void]$html.AppendLine('  <table class="at">
    <thead><tr>
      <th>#</th>
      <th>Email</th>
      <th><span data-lang="en" class="active">Bonus</span><span data-lang="ua">Бонус</span><span data-lang="ru">Бонус</span></th>
      <th><span data-lang="en" class="active">Game</span><span data-lang="ua">Гра</span><span data-lang="ru">Игра</span></th>
      <th><span data-lang="en" class="active">Promo Code</span><span data-lang="ua">Промокод</span><span data-lang="ru">Промокод</span></th>
      <th><span data-lang="en" class="active">Header</span><span data-lang="ua">Шапка</span><span data-lang="ru">Шапка</span></th>
      <th><span data-lang="en" class="active">Wrapper</span><span data-lang="ua">Обгортка</span><span data-lang="ru">Обёртка</span></th>
      <th><span data-lang="en" class="active">Status</span><span data-lang="ua">Статус</span><span data-lang="ru">Статус</span></th>
    </tr></thead>
    <tbody>')
    }
    
    # Table rows
    $n = 0
    foreach($e in $camp.emails) {
        $n++
        
        # Bonus cell
        $bonusHtml = if($e.bonuses.Count -gt 0) { 
            (Esc ($e.bonuses -join ", "))
        } else { '<span class="s-na">—</span>' }
        
        # Game cell
        $gameHtml = if($e.games.Count -gt 0) {
            '<span class="game">' + (Esc ($e.games -join ", ")) + '</span>'
        } else { '<span class="s-na">—</span>' }
        
        # Code cell
        $codeHtml = ""
        $allCodes = @()
        if($e.bodyCodes.Count -gt 0) { $allCodes = $e.bodyCodes }
        elseif($e.headerCodes.Count -gt 0) { $allCodes = $e.headerCodes }
        if($allCodes.Count -gt 0) {
            $spans = @()
            foreach($code in $allCodes) { $spans += '<span class="code">' + (Esc $code) + '</span>' }
            $codeHtml = $spans -join " "
        } else { $codeHtml = '<span class="s-na">—</span>' }
        
        # Header check
        $hdrHtml = if($e.hasHeader) { '<span class="s-ok">✅</span>' } else {
            if($allCodes.Count -gt 0) { '<span class="s-e">❌</span>' } else { '<span class="s-na">—</span>' }
        }
        
        # Wrapper check
        $wrpHtml = if($e.hasWrapper) { '<span class="s-ok">✅</span>' } else {
            if($allCodes.Count -gt 0) { '<span class="s-e">❌</span>' } else { '<span class="s-na">—</span>' }
        }
        
        # Status
        $stHtml = ""
        switch($e.status) {
            "ok" {
                if($allCodes.Count -eq 0 -and $e.bonuses.Count -eq 0) {
                    $stHtml = '<span class="s-na">—</span>'
                } else {
                    $stHtml = '<span class="s-ok">OK</span>'
                }
            }
            "warn" { $stHtml = '<span class="s-w" title="' + (Esc $e.statusNote) + '">⚠️ ' + (Esc $e.statusNote) + '</span>' }
            "error" { $stHtml = '<span class="s-e">❌ ERROR</span>' }
        }
        
        if($skipW) {
            [void]$html.AppendLine("<tr><td>$n</td><td class=""eid"">$($e.name)</td><td>$bonusHtml</td><td>$gameHtml</td><td>$codeHtml</td><td class=""chk"">$hdrHtml</td><td>$stHtml</td></tr>")
        } else {
            [void]$html.AppendLine("<tr><td>$n</td><td class=""eid"">$($e.name)</td><td>$bonusHtml</td><td>$gameHtml</td><td>$codeHtml</td><td class=""chk"">$hdrHtml</td><td class=""chk"">$wrpHtml</td><td>$stHtml</td></tr>")
        }
    }
    
    [void]$html.AppendLine('    </tbody>
  </table>
</div>')
    $secNum++
}

# CONTENT END
[void]$html.AppendLine('
</div><!-- /content -->')

# FOOTER
[void]$html.AppendLine('
<div class="report-footer">
  <div style="display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:8px">
    <img class="logo-sm" src="../../assets/pg-logo.svg" alt="PromptGrid">
    <span style="font-size:13px;font-weight:600;color:#888;letter-spacing:-.3px">PromptGrid</span>
  </div>
  <div class="gnb-line" style="margin-bottom:10px"><img src="../../assets/gnb-favicon.svg" alt="GNB"><span>Specially for GNB Agency</span></div>
  <p>&copy; 2025 PromptGrid &bull; Automation &bull; Precision &bull; Results</p>
</div>')

# SCRIPT
[void]$html.AppendLine('
<script>
(function(){
  var LANGS=["ru","ua","en"];
  var buttons=document.querySelectorAll("[data-set-lang]");
  var elements=document.querySelectorAll("[data-lang]");
  function setLang(lang){
    elements.forEach(function(el){el.classList.toggle("active",el.getAttribute("data-lang")===lang)});
    buttons.forEach(function(btn){btn.classList.toggle("active",btn.getAttribute("data-set-lang")===lang)});
    document.documentElement.lang=lang==="ua"?"uk":lang;
  }
  buttons.forEach(function(btn){btn.addEventListener("click",function(){setLang(btn.getAttribute("data-set-lang"))})});
  var nav=document.querySelector(".report-nav");
  var navLinks=document.querySelectorAll(".nav-link");
  var anchors=Array.from(document.querySelectorAll(".section-anchor"));
  function scrollNavToActive(link){
    var navRect=nav.getBoundingClientRect();
    var linkRect=link.getBoundingClientRect();
    var pad=60;
    if(linkRect.right+pad>navRect.right)nav.scrollBy({left:linkRect.right-navRect.right+pad,behavior:"smooth"});
    else if(linkRect.left-pad<navRect.left)nav.scrollBy({left:linkRect.left-navRect.left-pad,behavior:"smooth"});
  }
  navLinks.forEach(function(link){link.addEventListener("click",function(){setTimeout(function(){scrollNavToActive(link)},50)})});
  function updateActiveNav(){
    var atBottom=(window.innerHeight+window.scrollY)>=(document.documentElement.scrollHeight-2);
    var current=0;
    if(atBottom){current=anchors.length-1}
    else{for(var i=anchors.length-1;i>=0;i--){if(anchors[i]&&anchors[i].getBoundingClientRect().top<=80){current=i;break}}}
    navLinks.forEach(function(link,idx){link.classList.toggle("active",idx===current)});
    if(navLinks[current])scrollNavToActive(navLinks[current]);
  }
  window.addEventListener("scroll",updateActiveNav,{passive:true});
  updateActiveNav();
  setLang("en");
})();
</script>
</body>
</html>')

# WRITE OUTPUT
$html.ToString() | Out-File -FilePath $outPath -Encoding UTF8
Write-Host "Report generated: $outPath" -ForegroundColor Green
Write-Host "Total: $totalEmails emails, $totalWithCode with code, $totalIssues issues"
