$base = "c:\Projects\REPORTS\тексти"
$out = "c:\Projects\REPORTS\old-audit-result.txt"
$files = @(
    @{n="Welcome Flow"; f="Welcome Flow - Table data.txt"},
    @{n="SU Retention"; f="SU Retention - Table data.txt"},
    @{n="FTD Retention"; f="FTD Retention Flow - Table data.txt"},
    @{n="Nutrition #2"; f="Nutrition #2 - Table data.txt"},
    @{n="Nutrition #3"; f="Nutrition #3 - Table data.txt"},
    @{n="DEP Retention"; f="DEP Retention - Table data.txt"}
)
$sb = [System.Text.StringBuilder]::new()
foreach($fi in $files){
    $path = Join-Path $base $fi.f
    $content = Get-Content $path -Raw
    $blocks = $content -split "(?=^name: Email )" | Where-Object { $_.Trim() -ne "" }
    $emails = @()
    foreach($b in $blocks){
        $lines = $b -split "`n" | ForEach-Object { $_.TrimEnd("`r") }
        $name = ""; $locale = ""; $hp = ""; $tpCode = ""; $pb = ""
        $hasTP = $false; $hasHP = $false; $hasPB = $false
        foreach($l in $lines){
            if($l -match "^name: (.+)$"){ $name = $Matches[1].Trim() }
            elseif($l -match "^locale: (.+)$"){ $locale = $Matches[1].Trim() }
            elseif($l -match "^header_html_tag: (.+)$"){
                $hdr = $Matches[1]
                if($hdr -match 'data-promocode="([^"]+)"'){ $hasHP = $true; $hp = $Matches[1] }
            }
            elseif($l -match "^text_[23]: (.+)$"){
                $txt = $Matches[1]
                $m = [regex]::Matches($txt, 'class="promocode">([^<]+)<')
                if($m.Count -gt 0){
                    $hasTP = $true
                    foreach($mm in $m){
                        if($tpCode -ne ""){ $tpCode += ", " }
                        $tpCode += $mm.Groups[1].Value
                    }
                }
            }
            elseif($l -match "^promocode_button_1: (.+)$"){ $hasPB = $true; $pb = $Matches[1].Trim() }
        }
        if($locale -eq "Default"){
            $id = $name -replace "^Email ",""
            $code = if($hasTP){ $tpCode } elseif($hasHP){ $hp } else { "" }
            $emails += [PSCustomObject]@{
                ID=$id; HP=$hasHP; HPCode=$hp; TP=$hasTP; TPCode=$tpCode; PB=$hasPB; PBCode=$pb; Code=$code
            }
        }
    }
    $withPromo = ($emails | Where-Object { $_.TP -or $_.HP }).Count
    $issues = 0
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("=== $($fi.n) === ($($emails.Count) emails, $withPromo with promo)")
    foreach($e in $emails){
        $tpMark = if($e.TP){"Y"}else{"-"}
        $hpMark = if($e.HP){"Y"}else{"-"}
        $pbMark = if($e.PB){"Y"}else{"-"}
        $code = if($e.Code){$e.Code}else{"(none)"}
        $issue = ""
        if($e.TP -and -not $e.HP){ $issue = " !! TP_NO_HP"; $issues++ }
        if($e.HP -and -not $e.TP){ $issue += " (HP_ONLY)" }
        if($fi.n -eq "DEP Retention" -and $e.HP -and -not $e.PB){ $issue += " !! HP_NO_PB"; $issues++ }
        $pbStr = if($fi.n -eq "DEP Retention"){" PB=$pbMark"}else{""}
        [void]$sb.AppendLine("  $($e.ID): TP=$tpMark HP=$hpMark$pbStr Code=$code$issue")
    }
    [void]$sb.AppendLine("  Issues: $issues")
}
$sb.ToString() | Set-Content $out -Encoding UTF8
Write-Host "Done: $out"
