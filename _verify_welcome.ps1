$root = 'c:\Projects\CLIENTS\CHEEL4REEL'
$files = @()
$files += Get-ChildItem -LiteralPath "$root\тексти\WELCOME 1","$root\тексти\WELCOME 2","$root\тексти\WELCOME 3","$root\тексти\WELCOME 4" -File
$files += Get-ChildItem -LiteralPath "$root\html" -Filter 'Chill4Reel Welcome*.html' -File

$bad = @(
    "Pragmatic Play's Sweet Bonanza",
    "Pragmatic Play's Big Bass Splash",
    "Pragmatic Play's Sugar Rush 1000",
    "Wagering applies to Sweet Bonanza, Gates of Olympus, Big Bass Splash, Sugar Rush 1000"
)
$badRegex = @(
    "Pragmatic Play's Gates of Olympus(?! Super Scatter)"
)

Write-Output "=== STALE LITERAL MATCHES ==="
foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName)
    foreach ($p in $bad) {
        if ($content.Contains($p)) {
            $count = ([regex]::Matches($content, [regex]::Escape($p))).Count
            Write-Output "$($f.FullName): [$count x] $p"
        }
    }
    foreach ($p in $badRegex) {
        $m = [regex]::Matches($content, $p)
        if ($m.Count -gt 0) {
            Write-Output "$($f.FullName): [$($m.Count) x regex] $p"
        }
    }
}

Write-Output ""
Write-Output "=== NEW CANON SLOT MENTIONS (sanity check) ==="
$good = @(
    "Gates of Olympus Super Scatter",
    "3 Super Hot Chillies",
    "Joker Streak XL: Hold and Win",
    "The Count"
)
foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName)
    $line = "$($f.Name): "
    $tags = @()
    foreach ($p in $good) {
        $c = ([regex]::Matches($content, [regex]::Escape($p))).Count
        if ($c -gt 0) { $tags += "$p=$c" }
    }
    if ($tags.Count -gt 0) { Write-Output ($line + ($tags -join ' | ')) }
}

Write-Output ""
Write-Output "=== W2 Day 2 batch `$150 -> `$250 verification ==="
$w2t = "$root\тексти\WELCOME 2\chill4reel welcome 2 texts EN-CA.txt"
Get-Content -LiteralPath $w2t | Select-String -Pattern '3 Super Hot Chillies|Max win from Free Spins|Max FS win' | Select-Object -First 30 | ForEach-Object { Write-Output $_ }