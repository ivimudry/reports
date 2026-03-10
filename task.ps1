$base = "C:\Projects\REPORTS\" + [char]0x0442 + [char]0x0435 + [char]0x043A + [char]0x0441 + [char]0x0442 + [char]0x0438 + " " + [char]0x0441 + [char]0x0442 + [char]0x0430 + [char]0x0440 + [char]0x0456

$files = @(
    @{ Name="DEP Retention"; File="DEP Retention - Table data.txt" },
    @{ Name="FTD Retention"; File="FTD Retention Flow - Table data.txt" },
    @{ Name="Nutrition #2"; File="Nutrition #2 - Table data.txt" },
    @{ Name="Nutrition #3"; File="Nutrition #3 - Table data.txt" },
    @{ Name="SU Retention"; File="SU Retention - Table data.txt" },
    @{ Name="Welcome Flow"; File="Welcome Flow - Table data.txt" }
)

# For each file, parse emails and find ones that have bonus info in text but NO promocode wrapper and NO data-promocode
foreach ($f in $files) {
    $path = Join-Path $base $f.File
    $lines = [System.IO.File]::ReadAllLines($path, [System.Text.Encoding]::UTF8)
    
    # Parse into email blocks
    $emails = @()
    $current = $null
    foreach ($line in $lines) {
        if ($line -match "^name: (.+)$") {
            if ($current) { $emails += $current }
            $current = @{ Name=$Matches[1]; Lines=@($line); HasPromoWrapper=$false; HasHeaderPromo=$false; HasPromoBtn=$false; HasBonus=$false; Subject="" }
        } elseif ($current) {
            $current.Lines += $line
            if ($line -match "^subject: (.+)$") { $current.Subject = $Matches[1] }
            if ($line -match 'class="promocode"') { $current.HasPromoWrapper = $true }
            if ($line -match 'data-promocode') { $current.HasHeaderPromo = $true }
            if ($line -match "^promocode_button_1:") { 
                $val = $line -replace "^promocode_button_1:\s*", ""
                if ($val.Trim().Length -gt 0) { $current.HasPromoBtn = $true }
            }
            # Check for bonus indicators in subject
            if ($line -match "^subject:" -and ($line -match "bonus|free\s*spin|FS |NRF|FreeBet|cashback|deposit|NoRisk|spins|%")) {
                $current.HasBonus = $true
            }
        }
    }
    if ($current) { $emails += $current }
    
    # Find emails with bonus but no promo code
    $noPromo = $emails | Where-Object { 
        $_.HasBonus -and (-not $_.HasPromoWrapper) -and (-not $_.HasHeaderPromo) -and (-not $_.HasPromoBtn)
    }
    
    if ($noPromo.Count -gt 0) {
        Write-Host "=== $($f.Name) ==="
        foreach ($e in $noPromo) {
            Write-Host "  $($e.Name) | $($e.Subject)"
        }
        Write-Host ""
    }
}

Write-Host "=== DONE ==="
