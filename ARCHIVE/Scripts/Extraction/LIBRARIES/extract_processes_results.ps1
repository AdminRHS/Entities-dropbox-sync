# Extract Processes and Results libraries from actions.json
# Created: 2025-11-25

$ErrorActionPreference = "Stop"

# Load actions.json
Write-Host "Loading actions.json..." -ForegroundColor Cyan
$actions = Get-Content "actions.json" -Raw | ConvertFrom-Json
Write-Host "Loaded $($actions.Count) action entries" -ForegroundColor Green

# Extract unique processes with their metadata
Write-Host "`nExtracting Processes..." -ForegroundColor Cyan
$processesDict = @{}
foreach ($action in $actions) {
    if ($action.Processes) {
        $processKey = $action.Processes.Trim().ToLower()
        if (-not $processesDict.ContainsKey($processKey)) {
            $processesDict[$processKey] = @{
                original = $action.Processes.Trim()
                actions = @()
                departments = @()
                professions = @()
            }
        }
        if ($action.Actions -and $action.Actions.Trim()) {
            $processesDict[$processKey].actions += $action.Actions.Trim()
        }
        if ($action.Departments -and $action.Departments.Trim()) {
            $processesDict[$processKey].departments += $action.Departments.Trim()
        }
        if ($action.Professions -and $action.Professions.Trim()) {
            $processesDict[$processKey].professions += $action.Professions.Trim()
        }
    }
}

# Extract unique results with their metadata
Write-Host "Extracting Results..." -ForegroundColor Cyan
$resultsDict = @{}
foreach ($action in $actions) {
    if ($action.Results) {
        $resultKey = $action.Results.Trim().ToLower()
        if (-not $resultsDict.ContainsKey($resultKey)) {
            $resultsDict[$resultKey] = @{
                original = $action.Results.Trim()
                actions = @()
                departments = @()
                professions = @()
            }
        }
        if ($action.Actions -and $action.Actions.Trim()) {
            $resultsDict[$resultKey].actions += $action.Actions.Trim()
        }
        if ($action.Departments -and $action.Departments.Trim()) {
            $resultsDict[$resultKey].departments += $action.Departments.Trim()
        }
        if ($action.Professions -and $action.Professions.Trim()) {
            $resultsDict[$resultKey].professions += $action.Professions.Trim()
        }
    }
}

Write-Host "Found $($processesDict.Count) unique processes" -ForegroundColor Green
Write-Host "Found $($resultsDict.Count) unique results" -ForegroundColor Green

# Function to categorize processes
function Get-ProcessCategory {
    param([string]$processName)
    $processLower = $processName.ToLower()
    
    if ($processLower -match "communicat|send|notify|contact|respond|follow|share|distribute") { return "Communication" }
    if ($processLower -match "creat|generat|build|design|develop|draft|write|make") { return "Creation" }
    if ($processLower -match "analyz|review|evaluat|assess|research|examin|investigat|compar") { return "Analysis" }
    if ($processLower -match "manag|organiz|coordinat|track|monitor|updat|maintain") { return "Management" }
    if ($processLower -match "process|transform|convert|export|import|format|refine") { return "Processing" }
    if ($processLower -match "verif|check|confirm|validat|test|audit") { return "Verification" }
    if ($processLower -match "stor|archiv|save|file|log|record") { return "Storage" }
    
    return "General"
}

# Function to categorize results
function Get-ResultCategory {
    param([string]$resultName)
    $resultLower = $resultName.ToLower()
    
    if ($resultLower -match "sent|notified|contacted|responded|shared|distributed|communicated") { return "Communication" }
    if ($resultLower -match "created|generated|built|designed|developed|drafted|written|made") { return "Creation" }
    if ($resultLower -match "analyzed|reviewed|evaluated|assessed|researched|examined|compared") { return "Analysis" }
    if ($resultLower -match "managed|organized|coordinated|tracked|monitored|updated") { return "Management" }
    if ($resultLower -match "processed|transformed|converted|exported|imported|formatted|refined") { return "Processing" }
    if ($resultLower -match "verified|checked|confirmed|validated|tested|audited") { return "Verification" }
    if ($resultLower -match "stored|archived|saved|filed|logged|recorded") { return "Storage" }
    
    return "General"
}

# Create Processes directory
$processesDir = "Processes"
if (-not (Test-Path $processesDir)) {
    New-Item -ItemType Directory -Path $processesDir | Out-Null
}

# Organize processes by category
Write-Host "`nOrganizing Processes by category..." -ForegroundColor Cyan
$categorizedProcesses = @{}
foreach ($key in $processesDict.Keys) {
    $process = $processesDict[$key]
    $category = Get-ProcessCategory -processName $process.original
    
    if (-not $categorizedProcesses.ContainsKey($category)) {
        $categorizedProcesses[$category] = @()
    }
    
    $uniqueActions = $process.actions | Sort-Object -Unique
    $uniqueDepts = $process.departments | Sort-Object -Unique
    $uniqueProfs = $process.professions | Sort-Object -Unique
    
    $processEntry = @{
        process_id = "PROC-$($category.Substring(0, [Math]::Min(4, $category.Length)).ToUpper())-$($categorizedProcesses[$category].Count + 1 | ForEach-Object { $_.ToString("000") })"
        process_name = $process.original
        category = $category
        description = "The ongoing action of $($process.original)"
        related_actions = $uniqueActions
        common_departments = $uniqueDepts
        common_professions = $uniqueProfs
        usage_count = $process.actions.Count
        tags = @($category.ToLower(), ($process.original.ToLower() -replace " ", "_"))
    }
    
    $categorizedProcesses[$category] += $processEntry
}

# Create Processes library files
Write-Host "Creating Processes library files..." -ForegroundColor Cyan
foreach ($category in $categorizedProcesses.Keys) {
    $processesList = $categorizedProcesses[$category] | Sort-Object -Property process_name
    
    $libraryData = @{
        entity_type = "LIBRARIES"
        sub_entity = "Processes"
        category = $category
        processes = $processesList
        version = "1.0"
        created = (Get-Date -Format "yyyy-MM-dd")
        last_updated = (Get-Date -Format "yyyy-MM-dd")
        total_processes = $processesList.Count
    }
    
    $filename = "$processesDir\$($category)_Processes.json"
    $libraryData | ConvertTo-Json -Depth 10 | Set-Content -Path $filename -Encoding UTF8
    Write-Host "  Created $filename with $($processesList.Count) processes" -ForegroundColor Green
}

# Create Results directory
$resultsDir = "Results"
if (-not (Test-Path $resultsDir)) {
    New-Item -ItemType Directory -Path $resultsDir | Out-Null
}

# Organize results by category
Write-Host "`nOrganizing Results by category..." -ForegroundColor Cyan
$categorizedResults = @{}
foreach ($key in $resultsDict.Keys) {
    $result = $resultsDict[$key]
    $category = Get-ResultCategory -resultName $result.original
    
    if (-not $categorizedResults.ContainsKey($category)) {
        $categorizedResults[$category] = @()
    }
    
    $uniqueActions = $result.actions | Sort-Object -Unique
    $uniqueDepts = $result.departments | Sort-Object -Unique
    $uniqueProfs = $result.professions | Sort-Object -Unique
    
    $resultEntry = @{
        result_id = "RES-$($category.Substring(0, [Math]::Min(4, $category.Length)).ToUpper())-$($categorizedResults[$category].Count + 1 | ForEach-Object { $_.ToString("000") })"
        result_name = $result.original
        category = $category
        description = "The completed state of having $($result.original)"
        related_actions = $uniqueActions
        common_departments = $uniqueDepts
        common_professions = $uniqueProfs
        usage_count = $result.actions.Count
        tags = @($category.ToLower(), ($result.original.ToLower() -replace " ", "_"))
    }
    
    $categorizedResults[$category] += $resultEntry
}

# Create Results library files
Write-Host "Creating Results library files..." -ForegroundColor Cyan
foreach ($category in $categorizedResults.Keys) {
    $resultsList = $categorizedResults[$category] | Sort-Object -Property result_name
    
    $libraryData = @{
        entity_type = "LIBRARIES"
        sub_entity = "Results"
        category = $category
        results = $resultsList
        version = "1.0"
        created = (Get-Date -Format "yyyy-MM-dd")
        last_updated = (Get-Date -Format "yyyy-MM-dd")
        total_results = $resultsList.Count
    }
    
    $filename = "$resultsDir\$($category)_Results.json"
    $libraryData | ConvertTo-Json -Depth 10 | Set-Content -Path $filename -Encoding UTF8
    Write-Host "  Created $filename with $($resultsList.Count) results" -ForegroundColor Green
}

Write-Host "`n✅ Extraction complete!" -ForegroundColor Green
Write-Host "Processes library: $processesDir/" -ForegroundColor Cyan
Write-Host "Results library: $resultsDir/" -ForegroundColor Cyan

