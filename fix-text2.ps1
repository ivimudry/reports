$dir = (Get-ChildItem "C:\Projects\REPORTS" -Directory | Where-Object { $_.Name -match '^\u0442\u0435\u043a\u0441\u0442' })[0].FullName
$path = (Get-ChildItem $dir -Filter "Welcome Flow*" | Where-Object { $_.Name -notlike "*Table*" })[0].FullName
Write-Host "Processing: $path"
$content = [IO.File]::ReadAllText($path)
$eol = if ($content.Contains("`r`n")) { "`r`n" } else { "`n" }
$lines = $content -split "`r?`n"

$pTag = '<p style="Margin:0;mso-line-height-rule:exactly;font-family:Montserrat, helvetica, arial, sans-serif;line-height:21px;letter-spacing:0;color:#FFFFFF;font-size:14px">'
$regex = [regex]'<(?:p|h4)[^>]*>(.*?)</(?:p|h4)>'
$changed = 0

for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^text_2: (.+)$') {
        $html = $Matches[1]
        
        if ($html -match '^(<td[^>]*>)(.+)(</td>)\s*$') {
            $tdOpen = $Matches[1]
            $inner = $Matches[2]
            $tdClose = $Matches[3]
            
            $segments = [System.Collections.Generic.List[string]]::new()
            $ms = $regex.Matches($inner)
            
            foreach ($m in $ms) {
                $seg = $m.Groups[1].Value
                if ($seg -eq '') { continue }
                if ($seg -eq '<br>' -or $seg -eq '<strong><br></strong>') {
                    $segments.Add('')
                    continue
                }
                $segments.Add($seg)
            }
            
            $joined = $segments -join '<br>'
            $lines[$i] = "text_2: $tdOpen$pTag$joined</p>$tdClose"
            $changed++
        }
    }
}

$result = $lines -join $eol
[IO.File]::WriteAllText($path, $result, [System.Text.UTF8Encoding]::new($false))
Write-Host "Done. Modified $changed text_2 lines."
