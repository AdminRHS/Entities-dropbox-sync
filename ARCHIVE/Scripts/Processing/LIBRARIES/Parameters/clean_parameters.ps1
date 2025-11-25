# Clean parameters.json - Remove source_files and _source_file fields

$filePath = "C:\Users\Dell\Dropbox\Nov25\Taxonomy\Framework\Entities\LIBRARIES\Parameters\parameters.json"

Write-Host "Reading parameters.json..."
$content = Get-Content $filePath -Raw -Encoding UTF8

Write-Host "Parsing JSON..."
$json = $content | ConvertFrom-Json

# Remove source_files from metadata
if ($json.metadata.source_files) {
    Write-Host "Removing source_files from metadata..."
    $json.metadata.PSObject.Properties.Remove('source_files')
}

# Remove _source_file and _chunk_number from all entries
if ($json.data) {
    Write-Host "Cleaning entries..."
    $cleaned = 0
    foreach ($entry in $json.data) {
        if ($entry.PSObject.Properties.Name -contains '_source_file') {
            $entry.PSObject.Properties.Remove('_source_file')
            $cleaned++
        }
        if ($entry.PSObject.Properties.Name -contains '_chunk_number') {
            $entry.PSObject.Properties.Remove('_chunk_number')
        }
    }
    Write-Host "Removed _source_file from $cleaned entries"
}

# Convert back to JSON and save
Write-Host "Saving cleaned file..."
$json | ConvertTo-Json -Depth 100 | Set-Content $filePath -Encoding UTF8

Write-Host "Done!"

