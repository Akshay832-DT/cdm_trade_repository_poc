#!/usr/bin/env python3
"""
Fix indentation issues in generated FIX models.

This script finds and fixes indentation issues in the generated FIX model files.
"""
import os
import sys
import glob
import re

def fix_indentation_issues(file_path):
    """Fix indentation issues in a file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix indented imports
    fixed_content = re.sub(r'^\s+from', 'from', content, flags=re.MULTILINE)
    fixed_content = re.sub(r'^\s+import', 'import', fixed_content, flags=re.MULTILINE)
    
    # Fix TYPE_CHECKING block issue
    fixed_content = re.sub(r'if TYPE_CHECKING:\s*\n\s*\n', 'if TYPE_CHECKING:\n    pass\n\n', fixed_content)
    
    # Write fixed content back to the file
    with open(file_path, 'w') as f:
        f.write(fixed_content)

def main():
    """Fix indentation issues in all generated files."""
    base_dir = "src/models/generated"
    
    # Fix message files
    print(f"Fixing message files...")
    message_files = glob.glob(f"{base_dir}/messages/*.py")
    for file_path in message_files:
        print(f"  Fixing {file_path}")
        fix_indentation_issues(file_path)
    
    # Fix component files
    print(f"Fixing component files...")
    component_files = glob.glob(f"{base_dir}/components/*.py")
    for file_path in component_files:
        print(f"  Fixing {file_path}")
        fix_indentation_issues(file_path)
    
    print("Done!")

if __name__ == "__main__":
    main() 