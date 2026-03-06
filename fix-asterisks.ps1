$path = "c:\Projects\REPORTS\тексти\Welcome Flow - новий.txt"
$content = [IO.File]::ReadAllText($path, [Text.Encoding]::UTF8)
$bullet = [char]0x2022  # •
$result = [regex]::Replace($content, '(?<=\w)\*+(?=\w)', {
    param($m)
    [string]::new($bullet, $m.Value.Length)
})
[IO.File]::WriteAllText($path, $result, [Text.Encoding]::UTF8)
$remaining = [regex]::Matches($result, '(?<=\w)\*+(?=\w)').Count
$bullets = [regex]::Matches($result, "$bullet+").Count
Write-Host "Remaining asterisks: $remaining"
Write-Host "Bullet sequences: $bullets"
