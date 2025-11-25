Write-Host 'PHASE 5: Scanning for references to old Prompts paths...'
Write-Host ''
$outDir = 'C:\Users\Dell\Dropbox\Taxonomy\Migration_Reports'
$root = 'C:\Users\Dell\Dropbox\Taxonomy\Entities'

# Create output directory
if (!(Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

Write-Host '[1/8] Scanning .md files for LIBRARIES/Prompts...'
Get-ChildItem -Path $root -Filter *.md -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern 'LIBRARIES/Prompts' -ErrorAction SilentlyContinue | Out-File "$outDir\References_LIBRARIES_Prompts_MD.txt"

Write-Host '[2/8] Scanning .json files for LIBRARIES/Prompts...'
Get-ChildItem -Path $root -Filter *.json -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern 'LIBRARIES/Prompts' -ErrorAction SilentlyContinue | Out-File "$outDir\References_LIBRARIES_Prompts_JSON.txt"

Write-Host '[3/8] Scanning TASK_MANAGERS (CRITICAL)...'
Get-ChildItem -Path "$root\TASK_MANAGERS" -Include *.md,*.json -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern 'Prompts' -ErrorAction SilentlyContinue | Out-File "$outDir\References_TASK_MANAGERS.txt"

Write-Host '[4/8] Scanning Transcribations (CRITICAL)...'
if (Test-Path "$root\LIBRARIES\Transcribations") {
    Get-ChildItem -Path "$root\LIBRARIES\Transcribations" -Filter *.md -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern 'Prompts' -ErrorAction SilentlyContinue | Out-File "$outDir\References_Transcribations.txt"
}

Write-Host '[5/8] Scanning Researches...'
if (Test-Path "$root\LIBRARIES\Researches") {
    Get-ChildItem -Path "$root\LIBRARIES\Researches" -Filter *.md -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern 'Prompts' -ErrorAction SilentlyContinue | Out-File "$outDir\References_Researches.txt"
}

Write-Host '[6/8] Scanning LIBRARIES main files (CRITICAL)...'
Get-ChildItem -Path "$root\LIBRARIES" -Filter *.md -ErrorAction SilentlyContinue | Where-Object {!$_.PSIsContainer} | Select-String -Pattern 'Prompts' -ErrorAction SilentlyContinue | Out-File "$outDir\References_LIBRARIES_Main.txt"

Write-Host '[7/8] Counting total references found...'
$mdRefs = (Get-Content "$outDir\References_LIBRARIES_Prompts_MD.txt" -ErrorAction SilentlyContinue | Measure-Object -Line).Lines
$jsonRefs = (Get-Content "$outDir\References_LIBRARIES_Prompts_JSON.txt" -ErrorAction SilentlyContinue | Measure-Object -Line).Lines
$taskRefs = (Get-Content "$outDir\References_TASK_MANAGERS.txt" -ErrorAction SilentlyContinue | Measure-Object -Line).Lines

Write-Host ''
Write-Host '===================='
Write-Host 'SCAN RESULTS:'
Write-Host '===================='
Write-Host "  .md files with LIBRARIES/Prompts: $mdRefs references"
Write-Host "  .json files with LIBRARIES/Prompts: $jsonRefs references"
Write-Host "  TASK_MANAGERS files: $taskRefs references"
Write-Host ''
Write-Host "All reports saved to: $outDir"
Write-Host ''
Write-Host 'Next step: Review reports and update file paths'
