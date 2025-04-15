#!/usr/bin/env python3
"""
Fix import paths in CDM generated model files.

This script scans the generated CDM model files and fixes incorrect import paths,
particularly for cross-directory imports.
"""
import os
import re
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
MODELS_DIR = Path("src/models/cdm/generated")

def fix_bad_imports(file_path: Path):
    """Fix imports in a file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check for problematic imports
    original_content = content
    file_modified = False
    
    # Get relative path components to use for fixing imports
    rel_path = file_path.relative_to(MODELS_DIR)
    parent_dirs = len(rel_path.parts) - 1  # Number of parent directories
    
    # Fix #1: Incorrect imports from other directories
    # Pattern: from ..product.common -> from ...product.common
    if "from ..product.common" in content:
        content = content.replace("from ..product.common", "from ...product.common")
        file_modified = True
    
    # Fix #2: Special case for base.staticdata imports in product/template directory
    # Pattern: from ..base.staticdata -> from ...base.staticdata
    if "from ..base.staticdata" in content:
        content = content.replace("from ..base.staticdata", "from ...base.staticdata")
        file_modified = True
    
    # Fix #3: General pattern for fixing relative imports to other modules
    modules = ["product", "base", "event", "legaldocumentation", "margin", 
               "observable", "regulation", "rosetta", "metafields"]
    
    for module in modules:
        # Skip if we're already in that module directory
        if rel_path.parts and module == rel_path.parts[0]:
            continue
            
        # Wrong format: from ..{module}
        pattern = rf"from \.\.[^\.]{module}\."
        if re.search(pattern, content):
            # Fix to use correct number of dots based on directory depth
            correct_dots = "." * (parent_dirs + 1)
            content = re.sub(pattern, f"from {correct_dots}{module}.", content)
            file_modified = True
    
    # Fix #4: Incorrect imports of the format from ..base.base
    if "from ..base.base import" in content:
        content = content.replace("from ..base.base import", "from ...base.base import")
        file_modified = True
    
    # Write the modified content back if changes were made
    if file_modified or content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        logger.info(f"Fixed imports in {file_path.relative_to(MODELS_DIR.parent.parent)}")
        return True
    
    return False

def fix_specific_file(file_path: str):
    """Fix a specific file with known issues."""
    file_path = Path(file_path)
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        return False
    
    logger.info(f"Fixing specific file: {file_path}")
    return fix_bad_imports(file_path)

def main():
    """Main function."""
    logger.info("Starting import path fixes for CDM models")
    
    # Fix specific files first
    specific_files = [
        "src/models/cdm/generated/product/template/asian.py",
        "src/models/cdm/generated/product/template/transferable_product.py",
        "src/models/cdm/generated/product/template/product.py",
    ]
    
    for file_path in specific_files:
        fix_specific_file(file_path)
    
    # Then scan and fix all Python files
    fixed_count = 0
    
    for file_path in MODELS_DIR.glob("**/*.py"):
        if file_path.is_file() and str(file_path) not in specific_files:
            if fix_bad_imports(file_path):
                fixed_count += 1
    
    logger.info(f"Fixed imports in {fixed_count} files")

if __name__ == "__main__":
    main() 