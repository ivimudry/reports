Add-Type -AssemblyName System.Drawing

$outDir = "C:\Projects\REPORTS\NUTRITION #2 - Banners\UZ"

$banners = @(
    @{ Name="Email C1.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236888088_Email%20C1.1_01KHJZ43NB9BT6R2TEAQPP626V.png" },
    @{ Name="Email C2.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236888819_Email%20C2.1_01KHJZ44C6RGPQBP15HKYZSXR7.png" },
    @{ Name="Email C3.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236889509_Email%20C3.1_01KHJZ4523EAFFT57GQ39J449A.png" },
    @{ Name="Email C4.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236890267_Email%20C4.1_01KHJZ45SN1DEG54KB0TCWJZS6.png" },
    @{ Name="Email C5.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236890933_Email%20C5.1_01KHJZ46EGRH5AD97GQMAKZ5BH.png" },
    @{ Name="Email C6.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236891644_Email%20C6.1_01KHJZ474KX2A8YS0G5M71BG32.png" },
    @{ Name="Email C7.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236892417_Email%20C7.1_01KHJZ47WT0W0YB2WDT60VGAD3.png" },
    @{ Name="Email C8.1 UZ"; URL="https://userimg-assets-eu.customeriomail.com/images/client-env-202060/1771236893114_Email%20C8.1_01KHJZ48JHHM86YBJMQ1VC1K6C.png" }
)

$ok = 0; $fail = 0

foreach ($b in $banners) {
    $pngPath = "$outDir\$($b.Name).png"
    $jpgPath = "$outDir\$($b.Name).jpg"
    
    # Remove old jpg if exists
    if (Test-Path $jpgPath) { Remove-Item $jpgPath -Force }
    
    try {
        Write-Host -NoNewline "  $($b.Name) ... "
        & curl.exe -s -L -o $pngPath $b.URL
        
        if (-not (Test-Path $pngPath) -or (Get-Item $pngPath).Length -eq 0) {
            throw "Download failed"
        }
        
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

Write-Host "`n=== RESULT ==="
Write-Host "OK: $ok, FAIL: $fail"
