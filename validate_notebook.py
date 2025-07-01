import json
import sys

def validate_notebook(notebook_path):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check for required fields
        required_fields = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        for field in required_fields:
            if field not in notebook:
                print(f"Error: Missing required field '{field}'")
                return False
        
        # Check cells structure
        if not isinstance(notebook['cells'], list):
            print("Error: 'cells' is not a list")
            return False
        
        for i, cell in enumerate(notebook['cells']):
            if 'cell_type' not in cell:
                print(f"Error: Cell {i} is missing 'cell_type'")
                return False
            
            if cell['cell_type'] == 'code' and 'source' not in cell:
                print(f"Error: Code cell {i} is missing 'source'")
                return False
            
            if cell['cell_type'] == 'markdown' and 'source' not in cell:
                print(f"Error: Markdown cell {i} is missing 'source'")
                return False
        
        print(f"Notebook '{notebook_path}' is valid!")
        print(f"Contains {len(notebook['cells'])} cells")
        return True
    
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_notebook.py <notebook_path>")
        sys.exit(1)
    
    notebook_path = sys.argv[1]
    validate_notebook(notebook_path)
