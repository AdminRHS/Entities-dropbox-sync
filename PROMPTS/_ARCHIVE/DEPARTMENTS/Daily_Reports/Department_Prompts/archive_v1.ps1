$srcDir = "C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DEPARTMENTS\Daily_Reports\Department_Prompts"
$dstDir = Join-Path $srcDir "_ARCHIVE"

New-Item -ItemType Directory -Force -Path $dstDir | Out-Null

$files = @(
    "PMT-033_AI_Daily_Report.md",
    "PMT-034_Content_Daily_Report.md",
    "PMT-035_Design_Daily_Report.md",
    "PMT-036_Dev_Daily_Report.md",
    "PMT-037_Finance_Daily_Report.md",
    "PMT-038_HR_Daily_Report.md",
    "PMT-039_LG_Daily_Report.md",
    "PMT-040_Marketing_Daily_Report.md",
    "PMT-041_Sales_Daily_Report.md",
    "PMT-042_SMM_Daily_Report.md",
    "PMT-043_Video_Daily_Report.md"
)

foreach ($f in $files) {
    $src = Join-Path $srcDir $f
    if (Test-Path $src) {
        $newName = $f -replace '\.md$', '_v1.0.md'
        $dst = Join-Path $dstDir $newName
        Move-Item $src $dst -Force
        Write-Host "Archived: $f -> $newName"
    }
}
