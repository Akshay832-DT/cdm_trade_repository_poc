#!/usr/bin/env python3
"""
FpML Schema Downloader

This script downloads FpML schema files (XSD) from the official FpML repository.
It handles downloading all necessary schemas for a specific FpML version.
"""
import os
import sys
import logging
import requests
import zipfile
import io
from pathlib import Path
import argparse
import shutil
from typing import List, Optional, Dict
import xml.etree.ElementTree as ET
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
FPML_VERSIONS = {
    "5-10": "http://www.fpml.org/spec/fpml-5-10-6-rec-1.zip",
    "5-9": "http://www.fpml.org/spec/fpml-5-9-7-rec-1.zip",
    "5-8": "http://www.fpml.org/spec/fpml-5-8-7-rec-1.zip",
    "5-7": "http://www.fpml.org/spec/fpml-5-7-5-rec-1.zip",
    "5-6": "http://www.fpml.org/spec/fpml-5-6-5-rec-1.zip",
}

DEFAULT_VERSION = "5-10"
SCHEMA_DIR = Path("specifications/fpml")
CACHE_DIR = SCHEMA_DIR / "cache"
XSD_DIR = SCHEMA_DIR / "xsd"

def ensure_directories() -> None:
    """Ensure that the necessary directories exist."""
    SCHEMA_DIR.mkdir(exist_ok=True)
    CACHE_DIR.mkdir(exist_ok=True)
    XSD_DIR.mkdir(exist_ok=True)

def download_fpml_schemas(version: str = DEFAULT_VERSION, force: bool = False) -> None:
    """
    Download FpML schema files for the specified version.
    
    Args:
        version: FpML version to download (e.g., "5-10")
        force: Force download even if files already exist
    """
    ensure_directories()
    
    # Check if version is supported
    if version not in FPML_VERSIONS:
        logger.error(f"FpML version {version} is not supported. Available versions: {', '.join(FPML_VERSIONS.keys())}")
        return
    
    # Check if already downloaded
    version_dir = XSD_DIR / version
    if version_dir.exists() and not force:
        logger.info(f"FpML version {version} already downloaded. Use --force to redownload.")
        return
    
    # Download URL
    url = FPML_VERSIONS[version]
    zip_path = CACHE_DIR / f"fpml-{version}.zip"
    
    # Download the zip file
    logger.info(f"Downloading FpML {version} schemas from {url}")
    try:
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        
        # Save to cache
        with open(zip_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        logger.info(f"Downloaded schemas to {zip_path}")
        
        # Extract schemas
        if version_dir.exists():
            shutil.rmtree(version_dir)
        version_dir.mkdir(exist_ok=True)
        
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            # Extract only XSD files
            for file in zip_ref.namelist():
                if file.endswith(".xsd"):
                    # Simplify path by removing any directories
                    output_path = version_dir / Path(file).name
                    with zip_ref.open(file) as source, open(output_path, "wb") as target:
                        shutil.copyfileobj(source, target)
        
        logger.info(f"Extracted {version} schemas to {version_dir}")
        
    except requests.RequestException as e:
        logger.error(f"Error downloading FpML schemas: {str(e)}")
        return

def list_schema_files(version: str = DEFAULT_VERSION) -> List[Path]:
    """
    List all schema files for a specific FpML version.
    
    Args:
        version: FpML version (e.g., "5-10")
        
    Returns:
        List of paths to schema files
    """
    version_dir = XSD_DIR / version
    if not version_dir.exists():
        logger.error(f"FpML version {version} not downloaded. Use download_fpml_schemas() first.")
        return []
    
    return list(version_dir.glob("*.xsd"))

def identify_main_schema(version: str = DEFAULT_VERSION) -> Optional[Path]:
    """
    Identify the main schema file that should be used as the entry point.
    This is usually the confirmation.xsd file in FpML.
    
    Args:
        version: FpML version (e.g., "5-10")
        
    Returns:
        Path to the main schema file, or None if not found
    """
    version_dir = XSD_DIR / version
    main_candidates = [
        "confirmation.xsd",
        "fpml-main.xsd",
        "fpml-doc.xsd",
        "fpml.xsd"
    ]
    
    for candidate in main_candidates:
        path = version_dir / candidate
        if path.exists():
            logger.info(f"Identified main schema file: {path}")
            return path
    
    logger.warning(f"Could not identify main schema file for FpML {version}")
    return None

def validate_schema_files(version: str = DEFAULT_VERSION) -> bool:
    """
    Validate that the downloaded schema files are correctly formatted.
    
    Args:
        version: FpML version (e.g., "5-10")
        
    Returns:
        True if valid, False otherwise
    """
    schema_files = list_schema_files(version)
    if not schema_files:
        return False
    
    try:
        for schema_file in schema_files:
            tree = ET.parse(schema_file)
            root = tree.getroot()
            if root.tag.endswith("schema"):
                logger.debug(f"Validated schema file: {schema_file}")
            else:
                logger.warning(f"File {schema_file} does not appear to be a valid XSD schema")
        return True
    except ET.ParseError as e:
        logger.error(f"Error parsing schema files: {str(e)}")
        return False

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Download FpML schema files")
    parser.add_argument(
        "--version", 
        choices=FPML_VERSIONS.keys(), 
        default=DEFAULT_VERSION,
        help=f"FpML version to download (default: {DEFAULT_VERSION})"
    )
    parser.add_argument(
        "--force", 
        action="store_true", 
        help="Force download even if files already exist"
    )
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_arguments()
    
    # Download schemas
    download_fpml_schemas(args.version, args.force)
    
    # Validate schemas
    if validate_schema_files(args.version):
        logger.info(f"Successfully downloaded and validated FpML {args.version} schemas")
        
        # Identify main schema
        main_schema = identify_main_schema(args.version)
        if main_schema:
            logger.info(f"Main schema file: {main_schema}")
        
        # List all schema files
        schema_files = list_schema_files(args.version)
        logger.info(f"Downloaded {len(schema_files)} schema files")
    else:
        logger.error(f"Failed to validate FpML {args.version} schemas")
        sys.exit(1)

if __name__ == "__main__":
    main() 