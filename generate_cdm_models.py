#!/usr/bin/env python3
"""
ISDA CDM 6.4 Pydantic Model Generation Script

This script runs the CDM model generator to create Pydantic models based on the ISDA CDM 6.4 JSON schemas.
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
    parser = argparse.ArgumentParser(description="Generate ISDA CDM 6.4 Pydantic models")
    
    parser.add_argument("--schema-dir", default="specifications/cdm_json",
                      help="Path to CDM JSON schema directory (default: %(default)s)")
    parser.add_argument("--output", default="src/models/cdm/generated",
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
        schema_dir = Path(args.schema_dir)
        output_dir = Path(args.output)
        
        # Validate schema directory exists
        if not schema_dir.exists():
            logger.error(f"CDM schema directory not found: {schema_dir}")
            sys.exit(1)
        
        # Backup existing models if requested
        if args.backup:
            backup_existing_models(output_dir)
        
        # Clean output directory if not disabled
        if not args.no_clean:
            clean_output_directory(output_dir)
        
        # Import and run the generator
        try:
            from src.generators.cdm_model_generator import parse_json_schemas, create_output_directories
            from src.generators.cdm_model_generator import generate_base_classes, determine_object_dependencies
            from src.generators.cdm_model_generator import generate_cdm_models, generate_init_files
            
            # Override constants from the generator
            import src.generators.cdm_model_generator as generator
            generator.SCHEMA_DIR = schema_dir
            generator.OUTPUT_DIR = output_dir
            
            # Create output directories
            create_output_directories()
            
            # Generate base classes
            generate_base_classes()
            
            # Parse schemas
            schemas = parse_json_schemas()
            
            # Generate models
            generate_cdm_models(schemas, list(schemas.keys()))
            
            # Generate __init__ files
            generate_init_files()
            
            logger.info("CDM model generation completed successfully")
            
        except ImportError as e:
            logger.error(f"Error importing generator module: {e}")
            sys.exit(1)
        
    except Exception as e:
        logger.error(f"Error during CDM model generation: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main() 