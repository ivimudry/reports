$base = "C:\Projects\REPORTS\" + [char]0x0442 + [char]0x0435 + [char]0x043A + [char]0x0441 + [char]0x0442 + [char]0x0438 + " " + [char]0x0441 + [char]0x0442 + [char]0x0430 + [char]0x0440 + [char]0x0456
$p = Join-Path $base "SU Retention - Table data.txt"
$lines = [System.IO.File]::ReadAllLines($p, [System.Text.Encoding]::UTF8)

# Find Email 1C, 2C, and 1M (as reference for promo format)
$targets = @("Email 1C", "Email 2C", "Email 1M")
foreach ($target in $targets) {
    Write-Host "========== $target =========="
    $found = $false
    $lineNum = 0
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -eq "name: $target") {
            $found = $true
            $lineNum = $i
        }
        if ($found) {
            # Print until next "name:" or end
            if ($i -gt $lineNum -and $lines[$i] -match "^name: ") { break }
            Write-Host "L$($i): $($lines[$i])"
        }
    }
    Write-Host ""
}
