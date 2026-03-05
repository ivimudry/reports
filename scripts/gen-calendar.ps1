$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false
$workbook = $excel.Workbooks.Add()
while ($workbook.Worksheets.Count -gt 1) {
    $workbook.Worksheets.Item($workbook.Worksheets.Count).Delete()
}

$monthNames = @(
    [char]0x0421 + [char]0x0456 + [char]0x0447 + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x041B + [char]0x044E + [char]0x0442 + [char]0x0438 + [char]0x0439,
    [char]0x0411 + [char]0x0435 + [char]0x0440 + [char]0x0435 + [char]0x0437 + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x041A + [char]0x0432 + [char]0x0456 + [char]0x0442 + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x0422 + [char]0x0440 + [char]0x0430 + [char]0x0432 + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x0427 + [char]0x0435 + [char]0x0440 + [char]0x0432 + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x041B + [char]0x0438 + [char]0x043F + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x0421 + [char]0x0435 + [char]0x0440 + [char]0x043F + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x0412 + [char]0x0435 + [char]0x0440 + [char]0x0435 + [char]0x0441 + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x0416 + [char]0x043E + [char]0x0432 + [char]0x0442 + [char]0x0435 + [char]0x043D + [char]0x044C,
    [char]0x041B + [char]0x0438 + [char]0x0441 + [char]0x0442 + [char]0x043E + [char]0x043F + [char]0x0430 + [char]0x0434,
    [char]0x0413 + [char]0x0440 + [char]0x0443 + [char]0x0434 + [char]0x0435 + [char]0x043D + [char]0x044C
)

$dayNames = @(
    [char]0x041F + [char]0x043D,
    [char]0x0412 + [char]0x0442,
    [char]0x0421 + [char]0x0440,
    [char]0x0427 + [char]0x0442,
    [char]0x041F + [char]0x0442,
    [char]0x0421 + [char]0x0431,
    [char]0x041D + [char]0x0434
)

$years = @(2025, 2026, 2027)

for ($yi = 0; $yi -lt $years.Count; $yi++) {
    $year = $years[$yi]
    if ($yi -eq 0) {
        $sheet = $workbook.Worksheets.Item(1)
    } else {
        $sheet = $workbook.Worksheets.Add([System.Reflection.Missing]::Value, $workbook.Worksheets.Item($workbook.Worksheets.Count))
    }
    $sheet.Name = "$year"
    $row = 1

    for ($m = 0; $m -lt 12; $m++) {
        $monthNum = $m + 1

        $sheet.Cells.Item($row, 1) = $monthNames[$m]
        $sheet.Cells.Item($row, 2).NumberFormat = "@"
        $sheet.Cells.Item($row, 2) = "$year"
        $hdr = $sheet.Range($sheet.Cells.Item($row, 1), $sheet.Cells.Item($row, 7))
        $hdr.Font.Bold = $true
        $hdr.Font.Size = 12
        $row++

        for ($d = 0; $d -lt 7; $d++) {
            $sheet.Cells.Item($row, $d + 1) = $dayNames[$d]
        }
        $dn = $sheet.Range($sheet.Cells.Item($row, 1), $sheet.Cells.Item($row, 7))
        $dn.Font.Bold = $true
        $dn.HorizontalAlignment = -4108
        $dn.Interior.Color = 15917529
        $dn.Borders.LineStyle = 1
        $dn.Borders.Weight = 2
        $dn.Borders.Color = 12632256
        $row++

        $gridStart = $row
        $daysInMonth = [DateTime]::DaysInMonth($year, $monthNum)
        $dow = [int](Get-Date -Year $year -Month $monthNum -Day 1).DayOfWeek
        $col = if ($dow -eq 0) { 6 } else { $dow - 1 }

        $cr = $gridStart
        for ($day = 1; $day -le $daysInMonth; $day++) {
            $sheet.Cells.Item($cr, $col + 1) = $day
            $sheet.Cells.Item($cr, $col + 1).HorizontalAlignment = -4108
            $col++
            if ($col -gt 6) { $col = 0; $cr++ }
        }

        $gridEnd = $gridStart + 5
        $gridRange = $sheet.Range($sheet.Cells.Item($gridStart, 1), $sheet.Cells.Item($gridEnd, 7))
        $gridRange.Borders.LineStyle = 1
        $gridRange.Borders.Weight = 2
        $gridRange.Borders.Color = 12632256

        $wkEnd = $sheet.Range($sheet.Cells.Item($gridStart, 6), $sheet.Cells.Item($gridEnd, 7))
        $wkEnd.Interior.Color = 13553358

        $row = $gridEnd + 2
    }

    for ($c = 1; $c -le 7; $c++) {
        $sheet.Columns.Item($c).ColumnWidth = 6
    }
}

$savePath = "C:\Projects\REPORTS\Calendar_2025-2027.xlsx"
if (Test-Path $savePath) { Remove-Item $savePath -Force }
$workbook.SaveAs($savePath, 51)
$workbook.Close($false)
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($sheet) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($workbook) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Write-Host "Done"
