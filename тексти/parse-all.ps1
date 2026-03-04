function Parse-Campaign($file) {
    $content = Get-Content $file -Encoding UTF8 -Raw
    # Split into email blocks by "name: Email"
    $blocks = $content -split '(?=\nname: Email )' | Where-Object { $_ -match 'name: Email' }
    $emails = @()
    foreach($block in $blocks) {
        $e = @{}
        # Name
        if($block -match 'name: Email\s+(.+)') { $e.name = $Matches[1].Trim() } else { continue }
        # Header codes
        $e.headerCodes = @()
        if($block -match 'data-promocode\s*=\s*"([^"]+)"') {
            $e.headerCodes = ($Matches[1] -split ',\s*') | ForEach-Object { $_.Trim() } | Where-Object { $_ }
        }
        # Body wrapped codes <strong class="promocode">CODE</strong>
        $e.bodyCodes = @()
        $wrappedMatches = [regex]::Matches($block, '<strong class="promocode">([A-Z0-9]+)\s*</strong>')
        foreach($m in $wrappedMatches) { $e.bodyCodes += $m.Groups[1].Value.Trim() }
        $e.bodyCodes = $e.bodyCodes | Select-Object -Unique
        # Bonus extraction from text_2 (simplified - look for bold patterns)
        $e.bonuses = @()
        $bonusPatterns = [regex]::Matches($block, '<strong>([^<]+)</strong>', 'IgnoreCase')
        foreach($m in $bonusPatterns) {
            $val = $m.Groups[1].Value.Trim()
            if($val -match '(\d+%.*?(?:FS|Free Spin|Cashback|CB|NoRisk|FreeBet|NRF|deposit|bonus)|\d+\s*(?:FS|Free Spin)|(?:NoRisk|NRF)\s*\d+%|\d+%\s*(?:bonus|on dep)|(?:100|110|120|130|140|150|155|160|165|170|180|200|210|220|225|230|250)%)') {
                $e.bonuses += $val
            }
            if($val -match '^\d+%$' -and [int]($val -replace '%','') -ge 50) { $e.bonuses += $val }
        }
        # Games
        $e.games = @()
        $gameMatches = [regex]::Matches($block, '(?:in|on)\s+<strong>([^<]+?)\s*</strong>\s*<strong>by\s+([^<]+)</strong>', 'IgnoreCase')
        foreach($m in $gameMatches) { $e.games += "$($m.Groups[1].Value.Trim()) by $($m.Groups[2].Value.Trim())" }
        if($e.games.Count -eq 0) {
            $gameMatches2 = [regex]::Matches($block, '(?:in|on)\s+<strong>([^<]+?by\s+[^<]+)</strong>', 'IgnoreCase')
            foreach($m in $gameMatches2) { $e.games += $m.Groups[1].Value.Trim() }
        }
        $e.games = $e.games | Select-Object -Unique
        # Has bonus but no code?
        $e.hasBonus = ($block -match '\d+%|\d+\s*FS|Free Spin|FreeBet|Cashback|NoRisk')
        # Check wrapper
        $e.allWrapped = ($e.bodyCodes.Count -eq 0 -and $e.headerCodes.Count -eq 0) -or ($e.bodyCodes.Count -gt 0)
        # Check header matches body
        $e.headerMatch = $true
        if($e.headerCodes.Count -gt 0 -and $e.bodyCodes.Count -gt 0) {
            foreach($hc in $e.headerCodes) {
                if($e.bodyCodes -notcontains $hc) { $e.headerMatch = $false }
            }
            foreach($bc in $e.bodyCodes) {
                if($e.headerCodes -notcontains $bc) { $e.headerMatch = $false }
            }
        } elseif($e.headerCodes.Count -gt 0 -and $e.bodyCodes.Count -eq 0) {
            $e.headerMatch = $false
        } elseif($e.headerCodes.Count -eq 0 -and $e.bodyCodes.Count -gt 0) {
            $e.headerMatch = $false
        }
        $emails += $e
    }
    return $emails
}
$files = @(
    @{name="WF"; file="Welcome Flow - Table data.txt"},
    @{name="FTD"; file="FTD Retention Flow - Table data.txt"},
    @{name="DEP"; file="DEP Retention - Table data.txt"},
    @{name="SU"; file="SU Retention - Table data.txt"},
    @{name="N2"; file="Nutrition #2 - Table data.txt"},
    @{name="N3"; file="Nutrition #3 - Table data.txt"}
)
foreach($f in $files) {
    $emails = Parse-Campaign $f.file
    Write-Host "=== $($f.name) === ($($emails.Count) emails)" -Fore Cyan
    foreach($e in $emails) {
        $hdr = if($e.headerCodes.Count -gt 0){"Y"}else{"N"}
        $wrp = if($e.bodyCodes.Count -gt 0){"Y"}else{"N"}
        $codes = if($e.bodyCodes.Count -gt 0){$e.bodyCodes -join ", "}elseif($e.headerCodes.Count -gt 0){$e.headerCodes -join ", "}else{"-"}
        $games = if($e.games.Count -gt 0){$e.games -join "; "}else{"-"}
        $status = "OK"
        if($e.bodyCodes.Count -eq 0 -and $e.headerCodes.Count -eq 0 -and $e.hasBonus) { $status = "WARN:no-code" }
        if(-not $e.headerMatch -and ($e.headerCodes.Count -gt 0 -or $e.bodyCodes.Count -gt 0)) { $status = "WARN:mismatch" }
        Write-Host "  $($e.name) | hdr=$hdr wrp=$wrp | codes=$codes | games=$games | status=$status"
    }
    Write-Host ""
}
