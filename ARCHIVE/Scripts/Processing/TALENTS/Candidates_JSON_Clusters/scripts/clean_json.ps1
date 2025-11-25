# Script to clean JSON by removing null values, empty strings, and empty arrays
# Usage: .\clean_json.ps1 -InputFile "input.json" -OutputFile "output.json"

param(
    [Parameter(Mandatory=$true)]
    [string]$InputFile,
    
    [Parameter(Mandatory=$true)]
    [string]$OutputFile
)

function Clean-Object {
    param($obj)
    
    if ($obj -is [PSCustomObject]) {
        $result = @{}
        foreach ($prop in $obj.PSObject.Properties) {
            $val = $prop.Value
            
            if ($val -is [PSCustomObject]) {
                $cleaned = Clean-Object $val
                if ($cleaned -ne $null -and $cleaned.Count -gt 0) {
                    $result[$prop.Name] = $cleaned
                }
            }
            elseif ($val -is [Array]) {
                $arr = @()
                foreach ($item in $val) {
                    if ($item -is [PSCustomObject]) {
                        $c = Clean-Object $item
                        if ($c -ne $null) {
                            $arr += $c
                        }
                    }
                    elseif ($item -ne $null -and $item -ne '') {
                        $arr += $item
                    }
                }
                if ($arr.Count -gt 0) {
                    $result[$prop.Name] = $arr
                }
            }
            elseif ($val -ne $null -and $val -ne '') {
                $result[$prop.Name] = $val
            }
        }
        return $result
    }
}

Write-Host "Loading JSON from: $InputFile"
$json = Get-Content $InputFile -Raw | ConvertFrom-Json

Write-Host "Cleaning $($json.Count) records..."
$cleaned = $json | ForEach-Object { Clean-Object $_ }

Write-Host "Saving cleaned JSON to: $OutputFile"
$cleaned | ConvertTo-Json -Depth 100 | Set-Content $OutputFile -Encoding UTF8

$originalSize = (Get-Item $InputFile).Length
$cleanedSize = (Get-Item $OutputFile).Length
$reduction = [math]::Round((1 - ($cleanedSize / $originalSize)) * 100, 2)

Write-Host "Done! Cleaned file saved to: $OutputFile"
Write-Host "Size reduction: $reduction% ($([math]::Round($originalSize/1MB, 2)) MB -> $([math]::Round($cleanedSize/1MB, 2)) MB)"

