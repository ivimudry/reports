
# Comprehensive parser: extracts bonus, game, promo code data from all 6 email campaign data files
# Outputs JSON file with complete structured data for HTML report generation

function Strip-Html($text) {
    $text = $text -replace '<br\s*/?>', "`n"
    $text = $text -replace '<[^>]+>', ''
    $text = $text -replace '&nbsp;', ' '
    $text = $text -replace '&amp;', '&'
    $text = $text -replace '&lt;', '<'
    $text = $text -replace '&gt;', '>'
    $text = $text -replace '\s+', ' '
    return $text.Trim()
}

function Extract-Bonuses($text) {
    $clean = Strip-Html $text
    $bonuses = @()
    
    # Pattern: X% bonus + Y Free Spins / FS
    $matches = [regex]::Matches($clean, '(\d+%)\s*(?:bonus)?\s*\+\s*(\d+)\s*(?:Free Spins?|FS)', 'IgnoreCase')
    foreach($m in $matches) { $bonuses += "$($m.Groups[1].Value) + $($m.Groups[2].Value) FS" }
    
    # Pattern: X% + Y FS (without "bonus" word)
    if($bonuses.Count -eq 0) {
        $matches = [regex]::Matches($clean, '(\d+%)\s*\+\s*(\d+)\s*(?:Free Spins?|FS)', 'IgnoreCase')
        foreach($m in $matches) { $bonuses += "$($m.Groups[1].Value) + $($m.Groups[2].Value) FS" }
    }
    
    # Pattern: Y Free Spins / Y FS (standalone)
    $matches = [regex]::Matches($clean, '(?<!\+\s*)(\d+)\s*(?:Free Spins?|FS)(?!\s*(?:in|on))', 'IgnoreCase')
    foreach($m in $matches) {
        $val = "$($m.Groups[1].Value) FS"
        if($bonuses -notcontains $val -and -not ($bonuses | Where-Object { $_ -match "\+ $($m.Groups[1].Value) FS" })) {
            $bonuses += $val
        }
    }
    
    # Pattern: X% NoRisk FreeBet / NRF
    $matches = [regex]::Matches($clean, '(\d+%)\s*(?:NoRisk\s*(?:Free\s*Bet|FreeBet|Freebet)|NRF)', 'IgnoreCase')
    foreach($m in $matches) {
        $val = "$($m.Groups[1].Value) NRF"
        if($bonuses -notcontains $val) { $bonuses += $val }
    }
    
    # Pattern: X% Cashback / CB
    $matches = [regex]::Matches($clean, '(\d+%)\s*(?:Cashback|CB)', 'IgnoreCase')
    foreach($m in $matches) {
        $val = "$($m.Groups[1].Value) CB"
        if($bonuses -notcontains $val) { $bonuses += $val }
    }
    
    # Pattern: X% FreeBets (sport)
    $matches = [regex]::Matches($clean, '(\d+%)\s*(?:Free\s*Bets?(?!\s*on))', 'IgnoreCase')
    foreach($m in $matches) {
        $val = "$($m.Groups[1].Value) FreeBets"
        $already = $bonuses | Where-Object { $_ -match "^$([regex]::Escape($m.Groups[1].Value))" }
        if(-not $already) { $bonuses += $val }
    }
    
    # Pattern: standalone X% (high percentages like 100%, 140%, etc.)  
    $matches = [regex]::Matches($clean, '(?<!\+\s)\b(\d{2,3})%(?!\s*\+|\s*(?:NoRisk|NRF|Cashback|CB|Free|back|of|bonus))', 'IgnoreCase')
    foreach($m in $matches) {
        $pct = [int]$m.Groups[1].Value
        $val = "$($m.Groups[1].Value)%"
        if($pct -ge 50 -and ($bonuses -notcontains $val) -and -not ($bonuses | Where-Object { $_ -match "^$val" })) {
            # Only add if not part of existing bonus
            $partOfExisting = $false
            foreach($b in $bonuses) { if($b -match "^$val") { $partOfExisting = $true; break } }
            if(-not $partOfExisting) { $bonuses += $val }
        }
    }
    
    return ($bonuses | Select-Object -Unique)
}

function Extract-Games($text) {
    $clean = Strip-Html $text  
    $games = @()
    
    # Pattern: "in GameName by Provider" or "on GameName by Provider"
    $matches = [regex]::Matches($text, '(?:in|on)\s+<strong>([^<]+?)</strong>\s*<strong>by\s+([^<]+)</strong>', 'IgnoreCase')
    foreach($m in $matches) { $games += "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())" }
    
    # Alternative: "in GameName by Provider" in single strong tag
    if($games.Count -eq 0) {
        $matches = [regex]::Matches($text, '(?:in|on)\s+<strong>([^<]+?)\s+by\s+([^<]+)</strong>', 'IgnoreCase')
        foreach($m in $matches) { $games += "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())" }
    }
    
    # Alternative in clean text: "in GAME by PROVIDER"
    if($games.Count -eq 0) {
        $matches = [regex]::Matches($clean, '(?:in|on)\s+([\w\s'']+?)\s+by\s+([\w\s'']+?(?:Gaming|Play|City|Go))', 'IgnoreCase')
        foreach($m in $matches) { 
            $game = "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())"
            if($game -notmatch 'your|the game|favor') { $games += $game }
        }
    }
    
    return ($games | Select-Object -Unique)
}

function Parse-Campaign($filePath) {
    $content = Get-Content $filePath -Encoding UTF8 -Raw
    $blocks = $content -split '(?=\nname: Email )' | Where-Object { $_ -match 'name: Email' }
    $emails = @()
    
    foreach($block in $blocks) {
        $e = @{}
        
        # Name
        if($block -match 'name: Email\s+(.+)') { $e.name = $Matches[1].Trim() } else { continue }
        
        # Subject
        if($block -match 'subject:\s*(.+)') { $e.subject = $Matches[1].Trim() } else { $e.subject = "" }
        
        # Header codes
        $e.headerCodes = @()
        if($block -match 'data-promocode\s*=\s*"([^"]+)"') {
            $e.headerCodes = @(($Matches[1] -split ',\s*') | ForEach-Object { $_.Trim() } | Where-Object { $_ })
        }
        
        # Combine all text fields
        $bodyText = ""
        $textMatches = [regex]::Matches($block, 'text_\d+:\s*(.+?)(?=\n(?:text_\d+|button_text|name):|$)', 'Singleline')
        foreach($m in $textMatches) { $bodyText += " " + $m.Groups[1].Value }
        
        # Body wrapped codes
        $e.bodyCodes = @()
        $wrappedMatches = [regex]::Matches($bodyText, '<strong class="promocode">([A-Z0-9]+)\s*</strong>')
        foreach($m in $wrappedMatches) { $e.bodyCodes += $m.Groups[1].Value.Trim() }
        $e.bodyCodes = @($e.bodyCodes | Select-Object -Unique)
        
        # Extract bonuses
        $e.bonuses = @(Extract-Bonuses $bodyText)
        
        # Extract games
        $e.games = @(Extract-Games $bodyText)
        
        # Wrapper check
        $e.allWrapped = ($e.bodyCodes.Count -gt 0)
        
        # Header check
        $e.hasHeader = ($e.headerCodes.Count -gt 0)
        
        # Match check
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
        
        # Has bonus content?
        $cleanBody = Strip-Html $bodyText
        $e.hasBonus = ($cleanBody -match '\d+%|\d+\s*FS|\d+\s*Free Spin|FreeBet|Cashback|NoRisk')
        
        # Status
        $e.status = "ok"
        $e.statusNote = ""
        
        if($e.bodyCodes.Count -eq 0 -and $e.headerCodes.Count -eq 0) {
            if($e.hasBonus -and $e.bonuses.Count -gt 0) {
                $e.status = "warn"
                $e.statusNote = "Bonus without promo code"
            }
            # else: no bonus, no code = OK (general/engagement email)
        } elseif(-not $e.headerMatchesBody) {
            if($e.headerCodes.Count -eq 0 -and $e.bodyCodes.Count -gt 0) {
                $e.status = "warn"
                $e.statusNote = "Body code but no header code"
            } elseif($e.headerCodes.Count -gt 0 -and $e.bodyCodes.Count -eq 0) {
                $e.status = "warn"
                $e.statusNote = "Header code but no body code"
            } else {
                $e.status = "warn"
                $e.statusNote = "Header/body mismatch"
            }
        }
        
        $emails += $e
    }
    return $emails
}

# Parse all campaigns
$campaigns = @(
    @{id="wf"; name="Welcome Flow"; file="Welcome Flow - Table data.txt"},
    @{id="ftd"; name="FTD Retention"; file="FTD Retention Flow - Table data.txt"},
    @{id="dep"; name="DEP Retention"; file="DEP Retention - Table data.txt"},
    @{id="su"; name="SU Retention"; file="SU Retention - Table data.txt"},
    @{id="n2"; name="Nutrition #2"; file="Nutrition #2 - Table data.txt"},
    @{id="n3"; name="Nutrition #3"; file="Nutrition #3 - Table data.txt"}
)

$allData = @()
foreach($c in $campaigns) {
    $emails = Parse-Campaign $c.file
    $allData += @{
        id = $c.id
        name = $c.name
        emails = $emails
        count = $emails.Count
        withCode = @($emails | Where-Object { $_.bodyCodes.Count -gt 0 -or $_.headerCodes.Count -gt 0 }).Count
        okCount = @($emails | Where-Object { $_.status -eq "ok" }).Count
        warnCount = @($emails | Where-Object { $_.status -eq "warn" }).Count
        errCount = @($emails | Where-Object { $_.status -eq "error" }).Count
    }
}

# Output detailed text report
$totalEmails = 0; $totalWithCode = 0; $totalWarn = 0
foreach($c in $allData) {
    $totalEmails += $c.count
    $totalWithCode += $c.withCode
    $totalWarn += $c.warnCount
    Write-Host "`n========== $($c.name) ($($c.count) emails, $($c.withCode) with code, $($c.warnCount) warnings) ==========" -Fore Cyan
    $n = 0
    foreach($e in $c.emails) {
        $n++
        $codes = @()
        if($e.bodyCodes.Count -gt 0) { $codes = $e.bodyCodes }
        elseif($e.headerCodes.Count -gt 0) { $codes = $e.headerCodes }
        
        $codesStr = if($codes.Count -gt 0){ $codes -join ", " } else { "-" }
        $bonusStr = if($e.bonuses.Count -gt 0){ $e.bonuses -join " | " } else { "-" }
        $gameStr = if($e.games.Count -gt 0){ $e.games -join " | " } else { "-" }
        $hdr = if($e.hasHeader){"Y"}else{"N"}
        $wrp = if($e.allWrapped){"Y"}else{"N"}
        $st = $e.status.ToUpper()
        if($e.statusNote) { $st += " ($($e.statusNote))" }
        
        Write-Host "  $n. $($e.name) | H=$hdr W=$wrp | $codesStr | bonus: $bonusStr | game: $gameStr | $st"
    }
}
Write-Host "`n===== TOTALS: $totalEmails emails, $totalWithCode with code, $totalWarn warnings =====" -Fore Green

# Save as JSON
$allData | ConvertTo-Json -Depth 5 | Out-File "report-data.json" -Encoding UTF8
Write-Host "JSON saved to report-data.json"
