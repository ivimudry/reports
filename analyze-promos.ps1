$files = @(
    "C:\Projects\REPORTS\тексти\Welcome Flow - Table data.txt",
    "C:\Projects\REPORTS\тексти\FTD Retention Flow - Table data.txt",
    "C:\Projects\REPORTS\тексти\Nutrition #2 - Table data.txt",
    "C:\Projects\REPORTS\тексти\Nutrition #3 - Table data.txt",
    "C:\Projects\REPORTS\тексти\SU Retention - Table data.txt",
    "C:\Projects\REPORTS\тексти\DEP Retention - Table data.txt"
)

foreach ($file in $files) {
    $fname = [IO.Path]::GetFileNameWithoutExtension($file)
    Write-Host "============================================"
    Write-Host "CAMPAIGN: $fname"
    Write-Host "============================================"
    
    $lines = [IO.File]::ReadAllLines($file)
    $currentName = ""
    $currentLocale = ""
    $headerTag = ""
    $text2 = ""
    $buttonText = ""
    
    $emails = @{}
    
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        
        if ($line -match '^name:\s*(.+)$') {
            $currentName = $Matches[1].Trim()
        }
        elseif ($line -match '^locale:\s*(.+)$') {
            $currentLocale = $Matches[1].Trim()
        }
        elseif ($line -match '^header_html_tag:\s*(.+)$') {
            $headerTag = $Matches[1].Trim()
        }
        elseif ($line -match '^text_2:\s*(.+)$') {
            $text2 = $Matches[1].Trim()
        }
        elseif ($line -match '^button_text_1:\s*(.+)$') {
            $buttonText = $Matches[1].Trim()
            
            # Only process Default locale
            if ($currentLocale -eq "Default") {
                $key = $currentName
                
                # Extract data-promocode from header
                $headerPromos = @()
                if ($headerTag -match 'data-promocode="([^"]+)"') {
                    $headerPromos = $Matches[1] -split ',\s*'
                }
                
                # Extract promocode wrappers from text_2
                $wrapperPromos = @()
                $wraps = [regex]::Matches($text2, 'class="promocode">([^<]+)<')
                foreach ($w in $wraps) { $wrapperPromos += $w.Groups[1].Value }
                
                # Extract all promo codes mentioned (both wrapped and unwrapped)
                $allPromos = @()
                $boldMatches = [regex]::Matches($text2, '<strong[^>]*>([^<]+)</strong>')
                foreach ($m in $boldMatches) {
                    $val = $m.Groups[1].Value.Trim()
                    if ($val -match '^[A-Z0-9_]+$' -and $val.Length -ge 4) {
                        if ($allPromos -notcontains $val) { $allPromos += $val }
                    }
                }
                # Also from wrapper
                foreach ($wp in $wrapperPromos) {
                    if ($allPromos -notcontains $wp) { $allPromos += $wp }
                }
                
                # Extract bonus info from subject line - get it from previous lines
                $subject = ""
                for ($j = $i; $j -ge [Math]::Max(0, $i-10); $j--) {
                    if ($lines[$j] -match '^subject:\s*(.+)$') { $subject = $Matches[1].Trim(); break }
                }
                
                # Extract game names from text_2
                $games = @()
                # Common pattern: "on <strong>GameName</strong>" or "in <strong>GameName</strong>"
                $gameMatches = [regex]::Matches($text2, '(?:on|in)\s+<strong[^>]*>([^<]+)</strong>')
                foreach ($gm in $gameMatches) {
                    $gval = $gm.Groups[1].Value.Trim()
                    if ($gval -notmatch '^\d' -and $gval -notmatch 'bonus|deposit|NoRisk|FreeBet' -and $gval.Length -gt 3) {
                        $games += ($gval -replace '\s*by\s+.*$', '')
                    }
                }
                # Also check pattern: "Free Spins on <strong>GameName by Provider</strong>"
                $gameMatches2 = [regex]::Matches($text2, 'Spins\s+(?:on|in)\s+<strong[^>]*>([^<]+)</strong>')
                foreach ($gm2 in $gameMatches2) {
                    $gval2 = ($gm2.Groups[1].Value.Trim() -replace '\s*by\s+.*$', '')
                    if ($games -notcontains $gval2 -and $gval2.Length -gt 3) { $games += $gval2 }
                }
                # Check for "on <strong>GameName</strong> <strong>by Provider</strong>"
                $gameMatches3 = [regex]::Matches($text2, '(?:on|in)\s*<strong[^>]*>\s*([A-Z][^<]+?)\s*</strong>\s*<strong[^>]*>\s*by\s')
                foreach ($gm3 in $gameMatches3) {
                    $gval3 = $gm3.Groups[1].Value.Trim()
                    if ($games -notcontains $gval3 -and $gval3.Length -gt 3) { $games += $gval3 }
                }
                
                # Check for bonus_button promo (DEP Retention specific)
                $bonusButton = ""
                for ($j = $i + 1; $j -le [Math]::Min($lines.Count - 1, $i + 5); $j++) {
                    if ($lines[$j] -match '^bonus_button_\d+:\s*(.+)$') {
                        $bonusButton = $Matches[1].Trim()
                    }
                }
                # Also check lines before next entry
                for ($j = $i - 8; $j -le $i; $j++) {
                    if ($j -ge 0 -and $lines[$j] -match '^bonus_button_\d+:\s*(.+)$') {
                        $bonusButton = $Matches[1].Trim()
                    }
                }
                
                Write-Host ""
                Write-Host "--- $currentName ---"
                Write-Host "  Subject: $subject"
                Write-Host "  Promos in text: $($allPromos -join ', ')"
                Write-Host "  Wrapped promos: $($wrapperPromos -join ', ')"
                Write-Host "  Header promos: $($headerPromos -join ', ')"
                Write-Host "  Games: $($games -join ', ')"
                Write-Host "  Button: $buttonText"
                if ($bonusButton) { Write-Host "  BonusButton: $bonusButton" }
                
                # Check header vs text match
                $headerOk = "N/A"
                if ($allPromos.Count -gt 0) {
                    $allInHeader = $true
                    foreach ($p in $allPromos) {
                        if ($headerPromos -notcontains $p) { $allInHeader = $false }
                    }
                    $headerOk = if ($allInHeader -and $headerPromos.Count -ge $allPromos.Count) { "YES" } else { "MISSING" }
                }
                
                $wrapOk = "N/A"
                if ($allPromos.Count -gt 0) {
                    $allWrapped = $true
                    foreach ($p in $allPromos) {
                        if ($wrapperPromos -notcontains $p) { $allWrapped = $false }
                    }
                    $wrapOk = if ($allWrapped) { "YES" } else { "MISSING" }
                }
                
                Write-Host "  >> Header check: $headerOk"
                Write-Host "  >> Wrap check: $wrapOk"
            }
        }
    }
    Write-Host ""
}
