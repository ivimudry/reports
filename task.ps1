$base = "C:\Projects\REPORTS\" + [char]0x0442 + [char]0x0435 + [char]0x043A + [char]0x0441 + [char]0x0442 + [char]0x0438 + " " + [char]0x0441 + [char]0x0442 + [char]0x0430 + [char]0x0440 + [char]0x0456
$suPath = Join-Path $base "SU Retention - Table data.txt"

$suLines = [System.IO.File]::ReadAllLines($suPath, [System.Text.Encoding]::UTF8)
Write-Host "Total lines: $($suLines.Count)"
Write-Host "First 15 lines:"
for ($i = 0; $i -lt 15 -and $i -lt $suLines.Count; $i++) {
    $line = $suLines[$i]
    $show = $line.Substring(0, [Math]::Min(60, $line.Length))
    Write-Host "[$i] $show"
}
