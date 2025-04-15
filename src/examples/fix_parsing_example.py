#!/usr/bin/env python3
"""
FIX Message Parsing Example

This script demonstrates how to use the generated FIX models to parse FIX messages.
"""
import sys
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.models.generated import MESSAGE_TYPES
from src.models.generated.fields.types import *
from src.models.generated.messages.base import FIXMessageBase

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def parse_fix_message(message: str) -> Optional[FIXMessageBase]:
    """
    Parse a FIX message string into a Pydantic model.
    
    Args:
        message: The FIX message string
        
    Returns:
        A FIX message model if parsing was successful, None otherwise
    """
    try:
        # Split the message into fields
        fields = message.strip().split('\x01')
        
        # Extract data as key-value pairs
        data = {}
        for field in fields:
            if '=' in field:
                tag, value = field.split('=', 1)
                data[tag] = value
        
        # Get the message type
        msg_type = data.get('35')
        if not msg_type:
            logger.error("Message type (tag 35) not found in the message")
            return None
        
        # Find the corresponding message model class
        message_class = MESSAGE_TYPES.get(msg_type)
        if not message_class:
            logger.error(f"Unknown message type: {msg_type}")
            return None
        
        # Convert field values to appropriate types
        # Datetime fields
        datetime_fields = {'52', '60', '122', '779'}
        for tag in datetime_fields:
            if tag in data:
                try:
                    # Handle both formats: YYYYMMDD-HH:MM:SS.sss and YYYYMMDD-HH:MM:SS
                    if '.' in data[tag]:
                        data[tag] = datetime.strptime(data[tag], '%Y%m%d-%H:%M:%S.%f')
                    else:
                        data[tag] = datetime.strptime(data[tag], '%Y%m%d-%H:%M:%S')
                except ValueError:
                    logger.warning(f"Could not parse datetime for tag {tag}: {data[tag]}")
        
        # Create the message object
        message_obj = message_class(**data)
        return message_obj
    
    except Exception as e:
        logger.error(f"Error parsing FIX message: {e}")
        return None

def format_fix_message(message: FIXMessageBase) -> str:
    """
    Format a FIX message model into a FIX message string.
    
    Args:
        message: The FIX message model
        
    Returns:
        The formatted FIX message string
    """
    try:
        # Dump the message to a dictionary
        data = message.model_dump(exclude_none=True)
        
        # Format the fields
        fields = []
        
        # Handle header fields first
        header_fields = [
            ('8', 'BeginString'),
            ('9', 'BodyLength'),
            ('35', 'MsgType'),
            ('49', 'SenderCompID'),
            ('56', 'TargetCompID'),
            ('34', 'MsgSeqNum'),
            ('52', 'SendingTime')
        ]
        
        for tag, field_name in header_fields:
            if field_name in data:
                value = data[field_name]
                # Format datetime fields
                if isinstance(value, datetime):
                    value = value.strftime('%Y%m%d-%H:%M:%S.%f')[:-3]
                fields.append(f"{tag}={value}")
                
        # Handle other fields
        for key, value in data.items():
            # Skip header fields
            if key in [field_name for _, field_name in header_fields]:
                continue
                
            # Skip additional_fields dictionary
            if key == 'additional_fields':
                continue
                
            # Find the tag for this field
            tag = None
            field_info = getattr(message.__class__, key, None)
            if field_info is not None and hasattr(field_info, 'alias'):
                tag = field_info.alias
            
            if tag is not None:
                # Format datetime fields
                if isinstance(value, datetime):
                    value = value.strftime('%Y%m%d-%H:%M:%S.%f')[:-3]
                fields.append(f"{tag}={value}")
        
        # Add any additional fields
        if 'additional_fields' in data:
            for tag, value in data['additional_fields'].items():
                fields.append(f"{tag}={value}")
        
        # Join fields with SOH delimiter
        return '\x01'.join(fields) + '\x01'
    
    except Exception as e:
        logger.error(f"Error formatting FIX message: {e}")
        return ""

def main():
    """Main function to demonstrate FIX message parsing."""
    # Example FIX message (new order single)
    fix_message = (
        "8=FIX.4.4\x019=145\x0135=D\x0134=1\x0149=SENDER\x0156=TARGET\x0152=20250413-18:30:00\x01"
        "11=ClientOrderID\x0121=1\x0155=AAPL\x0154=1\x0160=20250413-18:30:00\x0138=100\x0140=2\x01"
        "44=155.50\x0159=0\x0110=123\x01"
    )
    
    logger.info("Original FIX message:")
    logger.info(fix_message.replace('\x01', '|'))
    
    # Parse the message
    message_obj = parse_fix_message(fix_message)
    
    if message_obj:
        logger.info("\nParsed message:")
        logger.info(f"Message Type: {message_obj.MsgType}")
        logger.info(f"Order ID: {message_obj.ClOrdID}")
        logger.info(f"Symbol: {message_obj.Symbol}")
        logger.info(f"Side: {message_obj.Side}")
        logger.info(f"Price: {message_obj.Price}")
        logger.info(f"Quantity: {message_obj.OrderQty}")
        
        # Modify the message
        message_obj.OrderQty = 200
        message_obj.Price = 156.75
        
        # Format back to FIX message
        formatted_message = format_fix_message(message_obj)
        
        logger.info("\nModified FIX message:")
        logger.info(formatted_message.replace('\x01', '|'))
    else:
        logger.error("Failed to parse the message")

if __name__ == "__main__":
    main() 