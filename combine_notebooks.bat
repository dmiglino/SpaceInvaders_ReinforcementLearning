@echo off
echo Combining notebooks...

echo import json > combine.py
echo. >> combine.py
echo def combine_notebooks(input_files, output_file): >> combine.py
echo     # Initialize the combined notebook with metadata from the first notebook >> combine.py
echo     with open(input_files[0], 'r', encoding='utf-8') as f: >> combine.py
echo         combined_notebook = json.load(f) >> combine.py
echo. >> combine.py
echo     # Initialize cells list if it doesn't exist >> combine.py
echo     if 'cells' not in combined_notebook: >> combine.py
echo         combined_notebook['cells'] = [] >> combine.py
echo. >> combine.py
echo     # Add cells from all notebooks (skipping the first one's cells which are already included) >> combine.py
echo     for i, file in enumerate(input_files): >> combine.py
echo         if i == 0: >> combine.py
echo             continue  # Skip the first file as we already loaded it >> combine.py
echo. >> combine.py
echo         with open(file, 'r', encoding='utf-8') as f: >> combine.py
echo             notebook = json.load(f) >> combine.py
echo. >> combine.py
echo         if 'cells' in notebook: >> combine.py
echo             combined_notebook['cells'].extend(notebook['cells']) >> combine.py
echo. >> combine.py
echo     # Write the combined notebook to the output file >> combine.py
echo     with open(output_file, 'w', encoding='utf-8') as f: >> combine.py
echo         json.dump(combined_notebook, f, indent=1) >> combine.py
echo. >> combine.py
echo     print(f"Combined notebook saved to {output_file}") >> combine.py
echo. >> combine.py
echo # Input notebook files >> combine.py
echo input_files = [ >> combine.py
echo     "APR_Grupo_9_ultimate_part1.ipynb", >> combine.py
echo     "APR_Grupo_9_ultimate_part2.ipynb", >> combine.py
echo     "APR_Grupo_9_ultimate_part3.ipynb" >> combine.py
echo ] >> combine.py
echo. >> combine.py
echo # Output notebook file >> combine.py
echo output_file = "APR_Grupo_9_ultimate.ipynb" >> combine.py
echo. >> combine.py
echo # Combine the notebooks >> combine.py
echo combine_notebooks(input_files, output_file) >> combine.py

python combine.py
if %ERRORLEVEL% NEQ 0 (
    echo Python not found in PATH. Trying with python3...
    python3 combine.py
    if %ERRORLEVEL% NEQ 0 (
        echo Python3 not found in PATH. Trying with py...
        py combine.py
        if %ERRORLEVEL% NEQ 0 (
            echo Failed to run Python script. Please run combine.py manually with your Python interpreter.
        )
    )
)

echo Done.
