#!/usr/bin/env python3
"""
FIX 4.4 Specification Downloader

This script downloads the FIX 4.4 specification from a public source and saves it for further processing.
"""
import os
import sys
import logging
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# URL for the FIX 4.4 specification XML
FIX_44_SPEC_URL = "https://raw.githubusercontent.com/quickfix/quickfix/master/spec/FIX44.xml"
LOCAL_SPEC_PATH = Path("specifications/fix/FIX44.xml")

def download_fix_spec():
    """
    Download the FIX 4.4 specification XML from the official repository.
    """
    logger.info(f"Downloading FIX 4.4 specification from {FIX_44_SPEC_URL}")
    
    try:
        response = requests.get(FIX_44_SPEC_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Create directory if it doesn't exist
        os.makedirs(LOCAL_SPEC_PATH.parent, exist_ok=True)
        
        # Save the specification locally
        with open(LOCAL_SPEC_PATH, 'wb') as f:
            f.write(response.content)
        
        logger.info(f"Successfully downloaded FIX 4.4 specification to {LOCAL_SPEC_PATH}")
        return LOCAL_SPEC_PATH
    except requests.RequestException as e:
        logger.error(f"Error downloading FIX 4.4 specification: {str(e)}")
        return None

def parse_fix_spec(xml_content: str) -> Dict[str, Any]:
    """Parse FIX 4.4 specification XML and extract fields, components, and messages."""
    try:
        # If xml_content is a string, assume it's a file path
        if isinstance(xml_content, str):
            tree = ET.parse(xml_content)
            root = tree.getroot()
        else:
            root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        logger.error(f"Error parsing XML content: {str(e)}")
        return None

    fields = {}
    components = {}
    messages = {}

    # First pass: collect all field definitions from the fields section
    for field in root.findall(".//fields/field"):
        tag = field.get('number')
        name = field.get('name')
        if not tag:
            logger.warning(f"Field {name} has no tag number, skipping")
            continue
        fields[name] = {
            'name': name,
            'tag': tag,
            'type': field.get('type'),
            'values': {value.get('enum'): value.get('description') 
                      for value in field.findall('value')}
        }

    # Second pass: collect all component definitions
    for component in root.findall(".//components/component"):
        comp_name = component.get('name')
        if not comp_name:
            continue
        
        comp_fields = []
        for field_ref in component.findall('.//field'):
            field_name = field_ref.get('name')
            if field_name in fields:
                comp_fields.append({
                    'name': field_name,
                    'required': field_ref.get('required') == 'Y',
                    **fields[field_name]
                })
            else:
                logger.warning(f"Field {field_name} in component {comp_name} not found in field definitions")
        
        # Handle nested components
        for nested_comp in component.findall('.//component'):
            nested_name = nested_comp.get('name')
            if nested_name:
                comp_fields.append({
                    'name': nested_name,
                    'required': nested_comp.get('required') == 'Y',
                    'is_component': True
                })

        # Handle groups
        for group in component.findall('.//group'):
            group_name = group.get('name')
            if group_name:
                group_fields = []
                for group_field in group.findall('.//field'):
                    field_name = group_field.get('name')
                    if field_name in fields:
                        group_fields.append({
                            'name': field_name,
                            'required': group_field.get('required') == 'Y',
                            **fields[field_name]
                        })
                comp_fields.append({
                    'name': group_name,
                    'required': group.get('required') == 'Y',
                    'is_group': True,
                    'fields': group_fields
                })

        components[comp_name] = comp_fields

    # Third pass: collect all message definitions
    for message in root.findall(".//messages/message"):
        msg_name = message.get('name')
        if not msg_name:
            continue
        
        msg_fields = []
        # Add header fields
        msg_fields.extend([{
            'name': field_name,
            'required': True,
            **fields[field_name]
        } for field_name in ['BeginString', 'BodyLength', 'MsgType', 'SenderCompID', 
                           'TargetCompID', 'MsgSeqNum', 'SendingTime'] 
                           if field_name in fields])

        # Add message-specific fields
        for field_ref in message.findall('.//field'):
            field_name = field_ref.get('name')
            if field_name in fields:
                msg_fields.append({
                    'name': field_name,
                    'required': field_ref.get('required') == 'Y',
                    **fields[field_name]
                })

        # Add components
        for comp_ref in message.findall('.//component'):
            comp_name = comp_ref.get('name')
            if comp_name in components:
                msg_fields.append({
                    'name': comp_name,
                    'required': comp_ref.get('required') == 'Y',
                    'is_component': True,
                    'fields': components[comp_name]
                })

        # Add groups
        for group in message.findall('.//group'):
            group_name = group.get('name')
            if group_name:
                group_fields = []
                for group_field in group.findall('.//field'):
                    field_name = group_field.get('name')
                    if field_name in fields:
                        group_fields.append({
                            'name': field_name,
                            'required': group_field.get('required') == 'Y',
                            **fields[field_name]
                        })
                msg_fields.append({
                    'name': group_name,
                    'required': group.get('required') == 'Y',
                    'is_group': True,
                    'fields': group_fields
                })

        messages[msg_name] = {
            'msgtype': message.get('msgtype'),
            'fields': msg_fields
        }

    return {
        'fields': fields,
        'components': components,
        'messages': messages
    }

if __name__ == "__main__":
    # Download the specification if it doesn't exist locally
    if not os.path.exists(LOCAL_SPEC_PATH):
        download_fix_spec()
    
    # Read and parse the specification
    try:
        spec_data = parse_fix_spec(str(LOCAL_SPEC_PATH))
        if spec_data:
            logger.info(f"Successfully parsed FIX 4.4 specification")
            logger.info(f"Found {len(spec_data['messages'])} message types")
            logger.info(f"Found {len(spec_data['fields'])} fields")
            logger.info(f"Found {len(spec_data['components'])} components")
        else:
            logger.error("Failed to parse FIX 4.4 specification")
            sys.exit(1)
    except Exception as e:
        logger.error(f"Error reading or parsing FIX specification: {str(e)}")
        sys.exit(1) 