#!/usr/bin/env python3
"""
Fix Field parameter issues in CDM generated model files.

This script scans the generated CDM model files and fixes incorrect Field parameter usage.
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

def fix_field_parameters(file_path: Path):
    """Fix Field parameters in a file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check for problematic Field parameters
    original_content = content
    file_modified = False
    
    # Fix pattern: Field(None, description="...", default=...)
    # Change to: Field(default=..., description="...")
    pattern = r'Field\(None,\s+description="([^"]+)",\s+default=\.\.\.\)'
    replacement = r'Field(default=..., description="\1")'
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        file_modified = True
    
    # Write the modified content back if changes were made
    if file_modified or content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        logger.info(f"Fixed Field parameters in {file_path.relative_to(MODELS_DIR.parent.parent)}")
        return True
    
    return False

def main():
    """Main function."""
    logger.info("Starting Field parameter fixes for CDM models")
    
    fixed_count = 0
    
    # Scan all Python files in the models directory
    for file_path in MODELS_DIR.glob("**/*.py"):
        if file_path.is_file():
            if fix_field_parameters(file_path):
                fixed_count += 1
    
    logger.info(f"Fixed Field parameters in {fixed_count} files")

if __name__ == "__main__":
    main() 