$dir = "C:\Projects\REPORTS\тексти"
$files = Get-ChildItem $dir -Filter "*.txt" | Sort-Object Name

foreach ($f in $files) {
    $lines = [IO.File]::ReadAllLines($f.FullName)
    Write-Host "========================================"
    Write-Host "CAMPAIGN: $($f.Name)"
    Write-Host "========================================"
    
    $name = ""; $locale = ""; $subject = ""; $header = ""; $texts = ""; $promoBtn = ""
    $inEmail = $false
    
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        
        if ($line -match '^name:\s*(.+)$') {
            # Print previous email if exists
            if ($name -ne "" -and $locale -eq "Default") {
                # Extract data-promocode from header
                $headerPromo = ""
                if ($header -match 'data-promocode="([^"]*)"') { $headerPromo = $Matches[1] }
                
                # Extract promocode class wraps from all text fields
                $promoWraps = @()
                $allText = $texts
                $regex = [regex]'class="promocode">([^<]+)<'
                $matches2 = $regex.Matches($allText)
                foreach ($m in $matches2) { $promoWraps += $m.Groups[1].Value }
                $promoWrapsStr = if ($promoWraps.Count -gt 0) { $promoWraps -join ", " } else { "NONE" }
                
                # Extract game names (bold text that looks like game names)
                $games = @()
                $gameRegex = [regex]'<strong>([^<]*(?:Spins on |Spins in )[^<]*)</strong>'
                $gMatches = $gameRegex.Matches($allText)
                foreach ($gm in $gMatches) { $games += $gm.Groups[1].Value }
                
                # Also look for "on <strong>GameName</strong>" pattern
                $gameRegex2 = [regex]'(?:on|in)\s+<strong>([^<]+)</strong>\s*(?:<strong>)?(?:by [^<]+)?'
                $gMatches2 = $gameRegex2.Matches($allText)
                foreach ($gm in $gMatches2) { 
                    $gn = $gm.Groups[1].Value.Trim()
                    if ($gn -notmatch '^\d+%' -and $gn -notmatch 'Celsius' -and $gn -notmatch 'NoRisk' -and $gn -notmatch 'bonus' -and $gn.Length -gt 3) {
                        if ($games -notcontains $gn) { $games += $gn }
                    }
                }
                
                $gamesStr = if ($games.Count -gt 0) { $games -join ", " } else { "-" }
                
                # Extract bonus from subject
                $bonus = $subject -replace '^[^\s]+\s*', ''
                
                Write-Host "---"
                Write-Host "EMAIL: $name"
                Write-Host "SUBJECT: $subject"
                Write-Host "BONUS_SHORT: $bonus"
                Write-Host "HEADER_PROMOCODE: $headerPromo"
                Write-Host "TEXT_PROMOCODE_WRAPS: $promoWrapsStr"
                Write-Host "GAMES: $gamesStr"
                if ($promoBtn -ne "") { Write-Host "PROMOCODE_BUTTON: $promoBtn" }
            }
            
            $name = $Matches[1].Trim()
            $locale = ""; $subject = ""; $header = ""; $texts = ""; $promoBtn = ""
        }
        elseif ($line -match '^locale:\s*(.+)$') { $locale = $Matches[1].Trim() }
        elseif ($line -match '^subject:\s*(.+)$') { $subject = $Matches[1].Trim() }
        elseif ($line -match '^header_html_tag:\s*(.+)$') { $header = $Matches[1].Trim() }
        elseif ($line -match '^text_\d+:\s*(.+)$') { $texts += " " + $Matches[1].Trim() }
        elseif ($line -match '^promocode_button_\d+:\s*(.+)$') { $promoBtn += $Matches[1].Trim() + " " }
    }
    
    # Print last email
    if ($name -ne "" -and $locale -eq "Default") {
        $headerPromo = ""
        if ($header -match 'data-promocode="([^"]*)"') { $headerPromo = $Matches[1] }
        $promoWraps = @()
        $allText = $texts
        $regex = [regex]'class="promocode">([^<]+)<'
        $matches2 = $regex.Matches($allText)
        foreach ($m in $matches2) { $promoWraps += $m.Groups[1].Value }
        $promoWrapsStr = if ($promoWraps.Count -gt 0) { $promoWraps -join ", " } else { "NONE" }
        $games = @()
        $gameRegex2 = [regex]'(?:on|in)\s+<strong>([^<]+)</strong>'
        $gMatches2 = $gameRegex2.Matches($allText)
        foreach ($gm in $gMatches2) { 
            $gn = $gm.Groups[1].Value.Trim()
            if ($gn -notmatch '^\d+%' -and $gn -notmatch 'Celsius' -and $gn -notmatch 'NoRisk' -and $gn -notmatch 'bonus' -and $gn.Length -gt 3) {
                if ($games -notcontains $gn) { $games += $gn }
            }
        }
        $gamesStr = if ($games.Count -gt 0) { $games -join ", " } else { "-" }
        $bonus = $subject -replace '^[^\s]+\s*', ''
        
        Write-Host "---"
        Write-Host "EMAIL: $name"
        Write-Host "SUBJECT: $subject"
        Write-Host "BONUS_SHORT: $bonus"
        Write-Host "HEADER_PROMOCODE: $headerPromo"
        Write-Host "TEXT_PROMOCODE_WRAPS: $promoWrapsStr"
        Write-Host "GAMES: $gamesStr"
        if ($promoBtn -ne "") { Write-Host "PROMOCODE_BUTTON: $promoBtn" }
    }
    
    Write-Host ""
}
