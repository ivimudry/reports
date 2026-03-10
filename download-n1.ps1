Add-Type -AssemblyName System.Drawing

$outDir = "C:\Projects\REPORTS\NUTRITION #1 - Banners"

# Ensure folders exist
New-Item -ItemType Directory -Path "$outDir\Original" -Force | Out-Null
New-Item -ItemType Directory -Path "$outDir\UZ" -Force | Out-Null

# Clean existing files
Get-ChildItem "$outDir\Original" -File -ErrorAction SilentlyContinue | Remove-Item -Force
Get-ChildItem "$outDir\UZ" -File -ErrorAction SilentlyContinue | Remove-Item -Force

$bannerFile = "C:\Projects\REPORTS\NUTRITION #1 - banners.txt"
$lines = [IO.File]::ReadAllLines($bannerFile)
$name = ""
$ok = 0
$fail = 0

for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    if ($line -match '^name:\s*(.+)$') {
        $name = $Matches[1].Trim()
    }
    elseif ($line -match '^banner_src:\s*(.+)$') {
        $url = $Matches[1].Trim()
        
        # Skip BD, IN, PH, PK locales
        if ($name -match '\s+(BD|IN|PH|PK)$') { continue }
        
        $safeName = $name -replace '[\\/:*?"<>|]', '_'
        if ($name -match '\s+UZ$') {
            $folder = "$outDir\UZ"
        } else {
            $folder = "$outDir\Original"
        }
        
        $pngPath = "$folder\$safeName.png"
        $jpgPath = "$folder\$safeName.jpg"
        
        try {
            Write-Host -NoNewline "  $name ... "
            
            # Use curl.exe for download (more reliable than Invoke-WebRequest)
            $curlArgs = @('-s', '-L', '-o', $pngPath, $url)
            & curl.exe @curlArgs
            
            if (-not (Test-Path $pngPath) -or (Get-Item $pngPath).Length -eq 0) {
                throw "Download failed or empty file"
            }
            
            # Convert PNG to JPG
            $img = [System.Drawing.Image]::FromFile($pngPath)
            $img.Save($jpgPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
            $img.Dispose()
            Remove-Item $pngPath -Force
            
            $size = [math]::Round((Get-Item $jpgPath).Length / 1KB)
            $ok++
            Write-Host "OK (${size}KB)"
        }
        catch {
            $fail++
            Write-Host "FAIL: $($_.Exception.Message)"
            if (Test-Path $pngPath) { Remove-Item $pngPath -Force -ErrorAction SilentlyContinue }
        }
    }
}

Write-Host ""
Write-Host "=== RESULT ==="
Write-Host "OK: $ok"
Write-Host "FAIL: $fail"
Write-Host "Original: $(@(Get-ChildItem "$outDir\Original" -File).Count) files"
Write-Host "UZ: $(@(Get-ChildItem "$outDir\UZ" -File).Count) files"
