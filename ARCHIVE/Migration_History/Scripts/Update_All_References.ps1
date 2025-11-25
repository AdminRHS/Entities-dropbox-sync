# Prompts Migration - Bulk Reference Update Script
# Updates all references from LIBRARIES/Prompts to LIBRARIES/DEPARTMENTS/_SHARED/Prompts

Write-Host "====================================================================="
Write-Host "  PROMPTS MIGRATION - BULK REFERENCE UPDATE"
Write-Host "  Updating all 362 references from old to new paths"
Write-Host "====================================================================="
Write-Host ""

$root = "C:\Users\Dell\Dropbox\Taxonomy\Entities"
$updatedFiles = @()
$totalReplacements = 0

# Define search and replace patterns
$patterns = @(
    @{
        Old = "Dropbox\\Taxonomy\\Entities\\LIBRARIES\\Prompts\\"
        New = "Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\"
        Description = "Dropbox relative paths (double backslash)"
    },
    @{
        Old = "Dropbox\Entities\LIBRARIES\Prompts\"
        New = "Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\"
        Description = "Dropbox relative paths (single backslash)"
    },
    @{
        Old = "Dropbox/Entities/LIBRARIES/Prompts/"
        New = "Dropbox/Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/"
        Description = "Dropbox relative paths (forward slash)"
    },
    @{
        Old = "LIBRARIES/Prompts/"
        New = "LIBRARIES/DEPARTMENTS/_SHARED/Prompts/"
        Description = "Taxonomy relative paths (forward slash)"
    },
    @{
        Old = "LIBRARIES\Prompts\"
        New = "LIBRARIES\DEPARTMENTS\_SHARED\Prompts\"
        Description = "Taxonomy relative paths (backslash)"
    },
    @{
        Old = "Entities/LIBRARIES/Prompts/"
        New = "Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/"
        Description = "Entities-relative paths"
    }
)

# Get all markdown and JSON files (excluding the new location to avoid changing it)
Write-Host "[1/4] Scanning for files to update..."
$files = Get-ChildItem -Path $root -Include *.md,*.json -Recurse -File |
    Where-Object { $_.FullName -notmatch "LIBRARIES\DEPARTMENTS\\_SHARED\\Prompts" -and
                   $_.FullName -notmatch "Migration_Reports" -and
                   $_.FullName -notmatch "BACKUP" }

Write-Host "  Found $($files.Count) files to scan"
Write-Host ""

# Process each file
Write-Host "[2/4] Updating file references..."
$fileCount = 0
foreach ($file in $files) {
    $fileCount++
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue

    if (-not $content) { continue }

    $originalContent = $content
    $fileUpdated = $false
    $fileReplacements = 0

    # Apply each pattern
    foreach ($pattern in $patterns) {
        if ($content -match [regex]::Escape($pattern.Old)) {
            $before = $content
            $content = $content -replace [regex]::Escape($pattern.Old), $pattern.New
            $count = ($before -split [regex]::Escape($pattern.Old)).Count - 1
            if ($count -gt 0) {
                $fileReplacements += $count
                $fileUpdated = $true
            }
        }
    }

    # Save if changed
    if ($fileUpdated) {
        try {
            Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
            $updatedFiles += [PSCustomObject]@{
                File = $file.FullName.Replace($root + "\", "")
                Replacements = $fileReplacements
            }
            $totalReplacements += $fileReplacements
            Write-Host "  [$fileCount/$($files.Count)] Updated: $($file.Name) ($fileReplacements replacements)"
        }
        catch {
            Write-Host "  [ERROR] Could not update: $($file.Name) - $($_.Exception.Message)" -ForegroundColor Red
        }
    }

    # Progress indicator every 10 files
    if ($fileCount % 10 -eq 0) {
        $percent = [math]::Round(($fileCount / $files.Count) * 100)
        Write-Host "  Progress: $fileCount/$($files.Count) files ($percent%)"
    }
}

Write-Host ""
Write-Host "[3/4] Generating update report..."

# Generate detailed report
$reportPath = "C:\Users\Dell\Dropbox\Taxonomy\Reference_Update_Report.txt"
$report = @"
PROMPTS MIGRATION - REFERENCE UPDATE REPORT
Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

SUMMARY
=======
Total files scanned: $($files.Count)
Total files updated: $($updatedFiles.Count)
Total replacements made: $totalReplacements

PATTERNS APPLIED
================
"@

foreach ($pattern in $patterns) {
    $report += "`n$($pattern.Description):`n"
    $report += "  Old: $($pattern.Old)`n"
    $report += "  New: $($pattern.New)`n"
}

$report += "`n`nFILES UPDATED`n=============`n"
$report += "File Path                                                           | Replacements`n"
$report += "-------------------------------------------------------------------|-------------`n"

foreach ($file in $updatedFiles | Sort-Object File) {
    $report += "$($file.File.PadRight(67)) | $($file.Replacements)`n"
}

$report | Out-File -FilePath $reportPath -Encoding UTF8

Write-Host "  Report saved to: $reportPath"
Write-Host ""

# Verify no old references remain
Write-Host "[4/4] Verifying all references updated..."
$remainingRefs = Get-ChildItem -Path $root -Include *.md,*.json -Recurse -File |
    Where-Object { $_.FullName -notmatch "LIBRARIES\DEPARTMENTS\\_SHARED\\Prompts" -and
                   $_.FullName -notmatch "Migration_Reports" -and
                   $_.FullName -notmatch "BACKUP" -and
                   $_.FullName -notmatch "Migration_Summary" -and
                   $_.FullName -notmatch "PROMPT_Move_Prompts" } |
    Select-String -Pattern "LIBRARIES/Prompts|LIBRARIES\\Prompts" -ErrorAction SilentlyContinue

if ($remainingRefs) {
    $count = ($remainingRefs | Measure-Object).Count
    Write-Host "  WARNING: Found $count remaining references to old path!" -ForegroundColor Yellow
    Write-Host "  These may be in migration documentation or need manual review."
    Write-Host "  See: C:\Users\Dell\Dropbox\Taxonomy\Remaining_References.txt"

    $remainingRefs | Out-File -FilePath "C:\Users\Dell\Dropbox\Taxonomy\Remaining_References.txt"
} else {
    Write-Host "  SUCCESS: No remaining references found!" -ForegroundColor Green
}

Write-Host ""
Write-Host "====================================================================="
Write-Host "  UPDATE COMPLETE"
Write-Host "====================================================================="
Write-Host ""
Write-Host "RESULTS:"
Write-Host "  Files Updated: $($updatedFiles.Count)"
Write-Host "  Total Replacements: $totalReplacements"
Write-Host ""
Write-Host "NEXT STEPS:"
Write-Host "  1. Review update report: $reportPath"
Write-Host "  2. Test critical workflows (video processing, task templates)"
Write-Host "  3. Run verification script: Migrate_Prompts_Phase4-7_Helper.bat [7]"
Write-Host "  4. Delete old location: LIBRARIES\Prompts\"
Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
