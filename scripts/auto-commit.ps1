# Auto-commit & push on file changes for REPORTS
# Watches for file changes, waits 30s after the last change, then commits & pushes.
# Run: powershell -ExecutionPolicy Bypass -File scripts/auto-commit.ps1

$projectDir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $projectDir

$debounceSeconds = 30
$lastChangeTime = $null

Write-Host "[auto-commit] Watching $projectDir (debounce: ${debounceSeconds}s)" -ForegroundColor Green
Write-Host "[auto-commit] Press Ctrl+C to stop" -ForegroundColor Yellow

function Test-HasChanges {
    $status = & git status --porcelain 2>&1
    return [bool]$status
}

function Invoke-CommitAndPush {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    & git add -A 2>&1 | Out-Null
    $status = & git diff --cached --stat 2>&1
    if (-not $status) { return }

    $changedCount = (& git diff --cached --name-only 2>&1 | Measure-Object).Count
    & git commit -m "auto: $timestamp ($changedCount files)" 2>&1 | Out-Null

    $pushResult = & git push 2>&1
    if ($LASTEXITCODE -ne 0) {
        # Try pull --rebase then push again
        & git pull --rebase 2>&1 | Out-Null
        $pushResult = & git push 2>&1
    }
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[auto-commit] $timestamp - pushed $changedCount file(s)" -ForegroundColor Green
    } else {
        Write-Host "[auto-commit] $timestamp - push failed: $pushResult" -ForegroundColor Red
    }
}

# Main loop: check every 5s, commit only after debounce
while ($true) {
    if (Test-HasChanges) {
        if (-not $lastChangeTime) {
            $lastChangeTime = Get-Date
            $now = Get-Date -Format "HH:mm:ss"
            Write-Host "[auto-commit] $now - changes detected, waiting ${debounceSeconds}s..." -ForegroundColor Yellow
        } else {
            # Check if debounce period passed
            $elapsed = (Get-Date) - $lastChangeTime
            if ($elapsed.TotalSeconds -ge $debounceSeconds) {
                # Re-check if still changing
                Start-Sleep -Seconds 2
                if (Test-HasChanges) {
                    Invoke-CommitAndPush
                }
                $lastChangeTime = $null
            }
        }
        Start-Sleep -Seconds 5
    } else {
        $lastChangeTime = $null
        Start-Sleep -Seconds 10
    }
}
