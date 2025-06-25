import json 
 
def combine_notebooks(input_files, output_file): 
    # Initialize the combined notebook with metadata from the first notebook 
    with open(input_files[0], 'r', encoding='utf-8') as f: 
        combined_notebook = json.load(f) 
 
    # Initialize cells list if it doesn't exist 
    if 'cells' not in combined_notebook: 
        combined_notebook['cells'] = [] 
 
    # Add cells from all notebooks (skipping the first one's cells which are already included) 
    for i, file in enumerate(input_files): 
        if i == 0: 
            continue  # Skip the first file as we already loaded it 
 
        with open(file, 'r', encoding='utf-8') as f: 
            notebook = json.load(f) 
 
        if 'cells' in notebook: 
            combined_notebook['cells'].extend(notebook['cells']) 
 
    # Write the combined notebook to the output file 
    with open(output_file, 'w', encoding='utf-8') as f: 
        json.dump(combined_notebook, f, indent=1) 
 
    print(f"Combined notebook saved to {output_file}") 
 
# Input notebook files 
input_files = [ 
    "APR_Grupo_9_ultimate_part1.ipynb", 
    "APR_Grupo_9_ultimate_part2.ipynb", 
    "APR_Grupo_9_ultimate_part3.ipynb" 
] 
 
# Output notebook file 
output_file = "APR_Grupo_9_ultimate.ipynb" 
 
# Combine the notebooks 
combine_notebooks(input_files, output_file) 
