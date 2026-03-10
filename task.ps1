$base = "C:\Projects\REPORTS\" + [char]0x0442 + [char]0x0435 + [char]0x043A + [char]0x0441 + [char]0x0442 + [char]0x0438 + " " + [char]0x0441 + [char]0x0442 + [char]0x0430 + [char]0x0440 + [char]0x0456

# ====== TASK 1: SU - Remove CFS emails ======
$suPath = Join-Path $base "SU Retention - Table data.txt"
$suLines = [System.IO.File]::ReadAllLines($suPath, [System.Text.Encoding]::UTF8)

# List all email names first
Write-Host "=== SU: ALL EMAIL NAMES ==="
foreach ($line in $suLines) {
    if ($line -match "^name: Email (.+)$") {
        Write-Host $Matches[1]
    }
}

Write-Host ""

# Filter out CFS email blocks
$newLines = [System.Collections.ArrayList]::new()
$skip = $false
$removedCount = 0
for ($i = 0; $i -lt $suLines.Count; $i++) {
    $line = $suLines[$i]
    if ($line -match "^name: Email \d+CFS$") {
        $skip = $true
        $removedCount++
        continue
    }
    if ($skip) {
        # Skip until next "name:" or end of file
        if ($line -match "^name: " -or $i -eq $suLines.Count - 1) {
            $skip = $false
            # Don't skip this line - it's the start of next email
            [void]$newLines.Add($line)
        }
        # else skip this line (part of CFS block)
        continue
    }
    [void]$newLines.Add($line)
}

# Clean up trailing empty lines between blocks
$cleaned = [System.Collections.ArrayList]::new()
$prevEmpty = $false
foreach ($line in $newLines) {
    $isEmpty = [string]::IsNullOrWhiteSpace($line)
    if ($isEmpty -and $prevEmpty) { continue }
    [void]$cleaned.Add($line)
    $prevEmpty = $isEmpty
}

# Write back
[System.IO.File]::WriteAllLines($suPath, $cleaned, [System.Text.Encoding]::UTF8)
Write-Host "SU: Removed $removedCount CFS emails"
Write-Host "SU: Lines before=$($suLines.Count), after=$($cleaned.Count)"

# Verify
$verify = [System.IO.File]::ReadAllLines($suPath, [System.Text.Encoding]::UTF8)
Write-Host "=== SU: REMAINING EMAILS ==="
foreach ($line in $verify) {
    if ($line -match "^name: Email (.+)$") {
        Write-Host $Matches[1]
    }
}

Write-Host ""
Write-Host "=============================="

# ====== TASK 2: DEP - Rename C1.1 -> 1C ======
$depPath = Join-Path $base "DEP Retention - Table data.txt"
$depLines = [System.IO.File]::ReadAllLines($depPath, [System.Text.Encoding]::UTF8)

Write-Host "=== DEP: BEFORE RENAME ==="
foreach ($line in $depLines) {
    if ($line -match "^name: Email (.+)$") {
        Write-Host $Matches[1]
    }
}

# Replace pattern: "Email C1.1" -> "Email 1C", "Email S1.1" -> "Email 1S"
$depNew = [System.Collections.ArrayList]::new()
foreach ($line in $depLines) {
    if ($line -match "^name: Email ([CS])(\d+)\.1$") {
        $letter = $Matches[1]
        $num = $Matches[2]
        $newName = "name: Email ${num}${letter}"
        [void]$depNew.Add($newName)
    } else {
        [void]$depNew.Add($line)
    }
}
[System.IO.File]::WriteAllLines($depPath, $depNew, [System.Text.Encoding]::UTF8)

Write-Host ""
Write-Host "=== DEP: AFTER RENAME ==="
$depVerify = [System.IO.File]::ReadAllLines($depPath, [System.Text.Encoding]::UTF8)
foreach ($line in $depVerify) {
    if ($line -match "^name: Email (.+)$") {
        Write-Host $Matches[1]
    }
}
