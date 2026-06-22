# Install openspec-superpowers-bridge to Cursor personal skills (all projects).
$ErrorActionPreference = "Stop"
$src = Split-Path $PSScriptRoot -Parent
if (-not (Test-Path (Join-Path $src "SKILL.md"))) {
    $src = "D:\workspace-baofu\account-skills\skills\openspec-superpowers-bridge"
}
$dst = Join-Path $env:USERPROFILE ".cursor\skills\openspec-superpowers-bridge"
New-Item -ItemType Directory -Force -Path (Split-Path $dst -Parent) | Out-Null

if (Test-Path $dst) {
    $existing = Get-Item $dst -Force
    if ($existing.LinkType -eq "Junction") {
        Remove-Item $dst -Force
    }
}

# Prefer junction so updates in account-skills apply automatically
$junctionOk = $false
try {
    cmd /c mklink /J "$dst" "$src" 2>$null | Out-Null
    if (Test-Path (Join-Path $dst "SKILL.md")) { $junctionOk = $true }
} catch {
    $junctionOk = $false
}

if (-not $junctionOk) {
    if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
    robocopy $src $dst /E /XD .git /NFL /NDL /NJH /NJS | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy failed with exit $LASTEXITCODE" }
}

Write-Host "Installed: $dst"
Write-Host "Source:    $src"
if (-not (Test-Path (Join-Path $dst "SKILL.md"))) {
    throw "VERIFY FAILED: SKILL.md missing at destination"
}
Write-Host "OK: SKILL.md present. Restart Cursor or start a new Agent chat."
