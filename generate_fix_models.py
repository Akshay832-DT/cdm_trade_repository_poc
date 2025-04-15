#!/usr/bin/env python3
"""
FIX 4.4 Pydantic Model Generation Script

This script runs the FIX model generator to create Pydantic models based on the FIX44.xml specification.
"""
import os
import sys
import logging
import argparse
import shutil
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate FIX 4.4 Pydantic models")
    
    parser.add_argument("--spec", default="specifications/fix/FIX44.xml",
                      help="Path to FIX 4.4 XML specification file (default: %(default)s)")
    parser.add_argument("--output", default="src/models/generated",
                      help="Output directory for generated models (default: %(default)s)")
    parser.add_argument("--backup", action="store_true",
                      help="Backup existing generated models before generating new ones")
    parser.add_argument("--no-clean", action="store_true",
                      help="Don't clean output directory before generation")
    
    return parser.parse_args()

def backup_existing_models(output_dir: Path):
    """Backup existing generated models."""
    if not output_dir.exists():
        logger.info(f"No existing models to backup at {output_dir}")
        return
    
    backup_dir = output_dir.parent / f"{output_dir.name}_backup"
    if backup_dir.exists():
        shutil.rmtree(backup_dir)
    
    shutil.copytree(output_dir, backup_dir)
    logger.info(f"Backed up existing models to {backup_dir}")

def clean_output_directory(output_dir: Path):
    """Clean output directory before generation."""
    if not output_dir.exists():
        logger.info(f"Output directory {output_dir} does not exist, creating")
        os.makedirs(output_dir, exist_ok=True)
        return
    
    # Remove all contents but keep directory structure
    for item in output_dir.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    
    logger.info(f"Cleaned output directory {output_dir}")

def main():
    """Main entry point for the script."""
    args = parse_arguments()
    
    try:
        # Convert paths to Path objects
        spec_path = Path(args.spec)
        output_dir = Path(args.output)
        
        # Validate spec file exists
        if not spec_path.exists():
            logger.error(f"FIX specification file not found: {spec_path}")
            sys.exit(1)
        
        # Backup existing models if requested
        if args.backup:
            backup_existing_models(output_dir)
        
        # Clean output directory if not disabled
        if not args.no_clean:
            clean_output_directory(output_dir)
        
        # Import and run the generator
        try:
            from src.generators.fix_model_generator import parse_fix_spec, create_output_directories
            from src.generators.fix_model_generator import generate_field_models, generate_component_models
            from src.generators.fix_model_generator import generate_message_models, generate_init_file
            
            # Override constants from the generator
            import src.generators.fix_model_generator as generator
            generator.SPEC_PATH = spec_path
            generator.OUTPUT_DIR = output_dir
            generator.FIELDS_DIR = output_dir / "fields"
            generator.COMPONENTS_DIR = output_dir / "components"
            generator.MESSAGES_DIR = output_dir / "messages"
            
            # Create output directories
            create_output_directories()
            
            # Parse FIX specification
            fields, components, messages = parse_fix_spec(spec_path)
            logger.info(f"Parsed {len(fields)} fields, {len(components)} components, and {len(messages)} messages")
            
            # Generate field models
            generate_field_models(fields, generator.FIELDS_DIR)
            
            # Generate component models
            generate_component_models(components, generator.COMPONENTS_DIR, fields)
            
            # Generate message models
            generate_message_models(messages, generator.MESSAGES_DIR, fields, components)
            
            # Generate main __init__.py
            generate_init_file(output_dir, messages, components)
            
            logger.info("FIX model generation completed successfully")
            
        except ImportError as e:
            logger.error(f"Error importing generator module: {e}")
            sys.exit(1)
        
    except Exception as e:
        logger.error(f"Error during FIX model generation: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main() 