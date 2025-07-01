# PowerShell script to combine Jupyter notebooks

# Input notebook files
$inputFiles = @(
    "APR_Grupo_9_fixed_ultimate_part1.ipynb",
    "APR_Grupo_9_fixed_ultimate_part2.ipynb",
    "APR_Grupo_9_fixed_ultimate_part3.ipynb"
)

# Output notebook file
$outputFile = "APR_Grupo_9_fixed_ultimate_combined.ipynb"

Write-Host "Combining notebooks..."

# Read the first notebook
$firstNotebook = Get-Content -Raw -Path $inputFiles[0] | ConvertFrom-Json

# Initialize cells array if it doesn't exist
if (-not $firstNotebook.cells) {
    $firstNotebook | Add-Member -MemberType NoteProperty -Name "cells" -Value @()
}

# Add cells from other notebooks
foreach ($file in $inputFiles[1..($inputFiles.Length-1)]) {
    Write-Host "Processing $file..."
    $notebook = Get-Content -Raw -Path $file | ConvertFrom-Json
    
    if ($notebook.cells) {
        $firstNotebook.cells += $notebook.cells
    }
}

# Write the combined notebook to the output file
$firstNotebook | ConvertTo-Json -Depth 100 | Set-Content -Path $outputFile

Write-Host "Combined notebook saved to $outputFile"
