#!/usr/bin/env python3
"""
Generate FIX 4.4 Models

This script executes the FIX 4.4 model generation process.
"""
import os
import sys
import logging
from pathlib import Path

# Add src directory to path so we can import from src
sys.path.insert(0, str(Path(__file__).parent))

from src.generators.fix_spec_downloader import download_fix_spec, parse_fix_spec
from src.generators.fix_model_generator import main as generate_models

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Execute the FIX 4.4 model generation process."""
    logger.info("Starting FIX 4.4 model generation process")
    
    # Ensure the specifications directory exists
    os.makedirs("specifications/fix", exist_ok=True)
    
    # Download the FIX 4.4 specification if needed
    spec_path = Path("specifications/fix/FIX44.xml")
    if not spec_path.exists():
        download_fix_spec()
    
    # Generate the models
    generate_models()
    
    logger.info("FIX 4.4 model generation process completed")

if __name__ == "__main__":
    main() 