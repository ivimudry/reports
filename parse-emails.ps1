# Parse 6 email campaign data files and extract structured data
# Output: JSON with all emails from all campaigns

$basePath = "c:\Projects\REPORTS\тексти"
$files = @(
    "FTD Retention Flow - Table data.txt",
    "Welcome Flow - Table data.txt",
    "DEP Retention - Table data.txt",
    "SU Retention - Table data.txt",
    "Nutrition #2 - Table data.txt",
    "Nutrition #3 - Table data.txt"
)

$allCampaigns = @()

foreach ($file in $files) {
    $filePath = Join-Path $basePath $file
    $campaignName = $file -replace ' - Table data\.txt$', ''
    $content = Get-Content $filePath -Raw -Encoding UTF8

    # Split into email blocks by "name: Email" pattern
    # Each block starts with a field (could be name: or subject: etc.)
    # We split on blank lines patterns, then group fields into blocks
    $lines = Get-Content $filePath -Encoding UTF8
    
    $emails = @()
    $currentEmail = @{}
    $currentFieldName = $null
    
    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($trimmed)) { continue }
        
        # Check if this line starts a new field (key: value)
        if ($trimmed -match '^(name|locale|subject|preheader|header_html_tag|text_1|text_2|text_3|button_text_1|promocode_button_1):\s*(.*)$') {
            $key = $Matches[1]
            $value = $Matches[2]
            
            # If we hit a new "name:" field and we already have data, save previous email
            if ($key -eq 'name' -and $currentEmail.Count -gt 0) {
                $emails += ,$currentEmail
                $currentEmail = @{}
            }
            
            $currentEmail[$key] = $value
            $currentFieldName = $key
        }
    }
    # Don't forget the last email block
    if ($currentEmail.Count -gt 0) {
        $emails += ,$currentEmail
    }
    
    $campaignEmails = @()
    
    foreach ($email in $emails) {
        $emailName = if ($email.ContainsKey('name')) { $email['name'] } else { 'Unknown' }
        $subject = if ($email.ContainsKey('subject')) { $email['subject'] } else { '' }
        $preheader = if ($email.ContainsKey('preheader')) { $email['preheader'] } else { '' }
        $headerTag = if ($email.ContainsKey('header_html_tag')) { $email['header_html_tag'] } else { '' }
        $buttonText = if ($email.ContainsKey('button_text_1')) { $email['button_text_1'] } else { '' }
        
        # Collect all text fields
        $textFields = @()
        if ($email.ContainsKey('text_2')) { $textFields += $email['text_2'] }
        if ($email.ContainsKey('text_3')) { $textFields += $email['text_3'] }
        if ($email.ContainsKey('promocode_button_1')) { $textFields += $email['promocode_button_1'] }
        $bodyHtml = $textFields -join ' '
        
        # Decode HTML entities
        $bodyDecoded = $bodyHtml -replace '&lt;', '<' -replace '&gt;', '>' -replace '&amp;', '&' -replace '&quot;', '"'
        
        # --- Extract header promo codes ---
        $headerCodes = @()
        if ($headerTag -match 'data-promocode="([^"]+)"') {
            $rawCodes = $Matches[1]
            $headerCodes = ($rawCodes -split ',\s*') | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' }
        }
        
        # --- Extract body promo codes (with <strong class="promocode"> wrapper) ---
        $bodyCodesWrapped = @()
        $wrappedMatches = [regex]::Matches($bodyDecoded, '<strong\s+class="promocode">([^<]+)</strong>')
        foreach ($m in $wrappedMatches) {
            $code = $m.Groups[1].Value.Trim()
            if ($code -ne '' -and $bodyCodesWrapped -notcontains $code) {
                $bodyCodesWrapped += $code
            }
        }
        
        # Also check for codes in promocode_button_1 field specifically
        $promoButtonCodes = @()
        if ($email.ContainsKey('promocode_button_1')) {
            $btnDecoded = $email['promocode_button_1'] -replace '&lt;', '<' -replace '&gt;', '>' -replace '&amp;', '&'
            $btnMatches = [regex]::Matches($btnDecoded, '<strong\s+class="promocode">([^<]+)</strong>')
            foreach ($m in $btnMatches) {
                $code = $m.Groups[1].Value.Trim()
                if ($code -ne '' -and $promoButtonCodes -notcontains $code) {
                    $promoButtonCodes += $code
                }
            }
        }
        
        # --- Extract bonus descriptions ---
        # Look for <strong>BONUS_TEXT</strong> patterns that describe bonuses
        $bonusDescriptions = @()
        $strongMatches = [regex]::Matches($bodyDecoded, '<strong>([^<]+)</strong>')
        foreach ($m in $strongMatches) {
            $text = $m.Groups[1].Value.Trim()
            # Filter for bonus-like descriptions (percentages, free spins, freebet, cashback, etc.)
            if ($text -match '\d+%|Free\s*Spin|FreeBet|Cashback|Bonus|NoRisk|Free\s*Bet') {
                $bonusDescriptions += $text
            }
        }
        
        # --- Extract game names ---
        # Pattern: "Game Name by Provider" inside <strong> tags or in text
        $gameNames = @()
        # From <strong> tags
        foreach ($m in $strongMatches) {
            $text = $m.Groups[1].Value.Trim()
            if ($text -match '\b(by\s+(Hacksaw\s+Gaming|Pragmatic\s+Play|Play.n.Go|Push\s+Gaming|Nolimit\s+City|ELK\s+Studios|BGaming|Red\s+Tiger|NetEnt|Microgaming|Evolution|Yggdrasil|Thunderkick|Relax\s+Gaming|Big\s+Time\s+Gaming|Blueprint\s+Gaming|iSoftBet|Quickspin|Endorphina|Wazdan|Betsoft|Booming\s+Games|Tom\s+Horn|Amatic|Spinomenal|Habanero|Playson|1x2\s+Gaming|Iron\s+Dog\s+Studio|Peter\s+&\s+Sons|Fantasma\s+Games|TrueLab\s+Games|GameArt|Platipus|CT\s+Interactive|Casino\s+Technology))\b') {
                $gameNames += $text
            }
        }
        # Also search in body text for "on GAME by PROVIDER" patterns
        $gamePatterns = [regex]::Matches($bodyDecoded, '(?:on|play)\s+([\w\s''&:!]+?\s+by\s+(?:Hacksaw\s+Gaming|Pragmatic\s+Play|Play.n.Go|Push\s+Gaming|Nolimit\s+City|ELK\s+Studios|BGaming|Red\s+Tiger))', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
        foreach ($m in $gamePatterns) {
            $game = $m.Groups[1].Value.Trim()
            if ($gameNames -notcontains $game) {
                $gameNames += $game
            }
        }
        # Extract from strong tags that contain "on GAME" in bonus descriptions
        foreach ($bonus in $bonusDescriptions) {
            if ($bonus -match 'on\s+(.+)$') {
                $gamePart = $Matches[1].Trim()
                if ($gamePart -and $gameNames -notcontains $gamePart) {
                    $gameNames += $gamePart
                }
            }
        }
        
        # --- Check header vs body codes match ---
        $allBodyCodes = $bodyCodesWrapped + $promoButtonCodes | Select-Object -Unique
        
        $headerMatchesBody = $false
        $mismatchDetails = ''
        if ($headerCodes.Count -gt 0 -and $allBodyCodes.Count -gt 0) {
            $headerSet = $headerCodes | Sort-Object
            $bodySet = $allBodyCodes | Sort-Object
            $headerMatchesBody = ($headerSet -join ',') -eq ($bodySet -join ',')
            if (-not $headerMatchesBody) {
                $mismatchDetails = "Header: [$($headerSet -join ', ')] vs Body: [$($bodySet -join ', ')]"
            }
        } elseif ($headerCodes.Count -eq 0 -and $allBodyCodes.Count -eq 0) {
            $headerMatchesBody = $true  # Both empty = match (no codes)
        } else {
            $mismatchDetails = if ($headerCodes.Count -eq 0) { "Header has NO codes, Body has: [$($allBodyCodes -join ', ')]" } else { "Header has: [$($headerCodes -join ', ')], Body has NO codes" }
        }
        
        $hasPromocodeWrapper = $bodyCodesWrapped.Count -gt 0
        
        $emailData = [ordered]@{
            email_name           = $emailName
            subject              = $subject
            preheader            = $preheader
            header_codes         = $headerCodes
            body_codes_wrapped   = $bodyCodesWrapped
            promo_button_codes   = $promoButtonCodes
            all_body_codes       = @($allBodyCodes)
            has_promocode_wrapper = $hasPromocodeWrapper
            header_matches_body  = $headerMatchesBody
            mismatch_details     = $mismatchDetails
            bonus_descriptions   = $bonusDescriptions
            game_names           = $gameNames
            button_text          = $buttonText
        }
        
        $campaignEmails += ,$emailData
    }
    
    $campaignData = [ordered]@{
        campaign    = $campaignName
        file        = $file
        email_count = $campaignEmails.Count
        emails      = $campaignEmails
    }
    
    $allCampaigns += ,$campaignData
}

# Output as JSON
$json = $allCampaigns | ConvertTo-Json -Depth 10
$outputPath = "c:\Projects\REPORTS\parsed-emails.json"
$json | Out-File -FilePath $outputPath -Encoding UTF8
Write-Host "Saved to $outputPath"
Write-Host ""

# Also print a summary table
foreach ($campaign in $allCampaigns) {
    Write-Host "=== $($campaign.campaign) ($($campaign.email_count) emails) ===" -ForegroundColor Cyan
    Write-Host ""
    foreach ($email in $campaign.emails) {
        $name = $email.email_name
        $hCodes = if ($email.header_codes.Count -gt 0) { $email.header_codes -join ', ' } else { '(none)' }
        $bCodes = if ($email.all_body_codes.Count -gt 0) { $email.all_body_codes -join ', ' } else { '(none)' }
        $wrapped = if ($email.has_promocode_wrapper) { 'YES' } else { 'NO' }
        $match = if ($email.header_matches_body) { 'MATCH' } else { 'MISMATCH' }
        $bonus = if ($email.bonus_descriptions.Count -gt 0) { $email.bonus_descriptions -join ' | ' } else { '(none)' }
        $games = if ($email.game_names.Count -gt 0) { $email.game_names -join ' | ' } else { '(none)' }
        
        Write-Host "  $name" -ForegroundColor Yellow -NoNewline
        Write-Host ""
        Write-Host "    Header codes : $hCodes"
        Write-Host "    Body codes   : $bCodes"
        Write-Host "    Wrapped      : $wrapped"
        Write-Host "    Match        : $match" -ForegroundColor $(if ($match -eq 'MATCH') { 'Green' } else { 'Red' })
        if ($email.mismatch_details) {
            Write-Host "    Mismatch     : $($email.mismatch_details)" -ForegroundColor Red
        }
        Write-Host "    Bonus        : $bonus"
        Write-Host "    Games        : $games"
        Write-Host ""
    }
}

# Print totals
$totalEmails = ($allCampaigns | ForEach-Object { $_.email_count } | Measure-Object -Sum).Sum
$mismatches = 0
$noWrapper = 0
foreach ($c in $allCampaigns) {
    foreach ($e in $c.emails) {
        if (-not $e.header_matches_body) { $mismatches++ }
        if ($e.all_body_codes.Count -gt 0 -and -not $e.has_promocode_wrapper) { $noWrapper++ }
    }
}
Write-Host "=== TOTALS ===" -ForegroundColor Magenta
Write-Host "  Total emails     : $totalEmails"
Write-Host "  Code mismatches  : $mismatches" -ForegroundColor $(if ($mismatches -gt 0) { 'Red' } else { 'Green' })
Write-Host "  Body codes without wrapper: $noWrapper" -ForegroundColor $(if ($noWrapper -gt 0) { 'Red' } else { 'Green' })
