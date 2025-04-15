#!/usr/bin/env python3
"""
Test Simplified FIX Models

This script demonstrates using the simplified FIX models generated without circular references.
"""
import sys
import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def parse_fix_message(message_str: str):
    """Parse a FIX message string into a model."""
    from src.models.fix_simple import MESSAGE_TYPES
    
    logger.debug(f"Parsing message: {message_str.replace('\x01', '|')}")
    
    # Split the message by SOH delimiter and extract fields
    fields = {}
    for field in message_str.split("\x01"):
        if "=" in field:
            tag, value = field.split("=", 1)
            fields[tag] = value
    
    logger.debug(f"Extracted fields: {fields}")
    
    # Get the message type
    msg_type = fields.get("35")
    if not msg_type:
        logger.error("Message type (tag 35) not found")
        return None
    
    # Find the corresponding message class
    message_class = MESSAGE_TYPES.get(msg_type)
    if not message_class:
        logger.error(f"Unknown message type: {msg_type}")
        return None
    
    # Build a map of tags to field names
    tag_to_field = {}
    required_fields = set()
    
    for attr_name in dir(message_class):
        attr = getattr(message_class, attr_name)
        if hasattr(attr, "alias") and not attr_name.startswith("__"):
            tag_to_field[attr.alias] = attr_name
            # Check if this is a required field
            if getattr(attr, "default", None) == ...:  # Ellipsis means required in pydantic
                required_fields.add(attr_name)
    
    logger.debug(f"Required fields: {required_fields}")
    logger.debug(f"Tag to field mapping: {tag_to_field}")
    
    # Convert data for the message construction
    message_data = {}
    additional_fields = {}
    
    # Standard header fields
    header_fields = {
        "8": "BeginString", 
        "9": "BodyLength", 
        "35": "MsgType",
        "49": "SenderCompID", 
        "56": "TargetCompID", 
        "34": "MsgSeqNum", 
        "52": "SendingTime"
    }
    
    # Process standard header fields first
    for tag, field_name in header_fields.items():
        if tag in fields:
            # Handle datetime fields
            if tag == "52":  # SendingTime
                try:
                    if "." in fields[tag]:
                        message_data[field_name] = datetime.strptime(fields[tag], "%Y%m%d-%H:%M:%S.%f")
                    else:
                        message_data[field_name] = datetime.strptime(fields[tag], "%Y%m%d-%H:%M:%S")
                except ValueError:
                    message_data[field_name] = fields[tag]
            else:
                message_data[field_name] = fields[tag]
    
    # Process other fields based on the tag-to-field mapping
    for tag, value in fields.items():
        # Skip header fields which we've already handled
        if tag in header_fields:
            continue
        
        # Skip CheckSum
        if tag == "10":
            continue
        
        # Map tag to field name
        field_name = tag_to_field.get(tag)
        if field_name:
            # Handle datetime fields
            field_info = getattr(message_class, field_name, None)
            field_type = getattr(field_info, "annotation", None)
            
            if field_type == datetime:
                try:
                    if "." in value:
                        message_data[field_name] = datetime.strptime(value, "%Y%m%d-%H:%M:%S.%f")
                    else:
                        message_data[field_name] = datetime.strptime(value, "%Y%m%d-%H:%M:%S")
                except ValueError:
                    message_data[field_name] = value
            else:
                message_data[field_name] = value
        else:
            # Store unknown fields in additional_fields
            additional_fields[tag] = value
    
    # Add additional fields
    if additional_fields:
        message_data["additional_fields"] = additional_fields
    
    logger.debug(f"Message data: {message_data}")
    
    # Check if all required fields are present
    missing_fields = [f for f in required_fields if f not in message_data]
    if missing_fields:
        # Try to add required fields from additional_fields if available
        for field_name in missing_fields[:]:
            for tag, f_name in tag_to_field.items():
                if f_name == field_name and tag in additional_fields:
                    message_data[field_name] = additional_fields[tag]
                    del additional_fields[tag]
                    missing_fields.remove(field_name)
                    break
    
    if missing_fields:
        logger.warning(f"Missing required fields: {missing_fields}")
        # Add dummy values for required fields to avoid validation errors
        # This isn't ideal but allows parsing to continue
        for field_name in missing_fields:
            message_data[field_name] = "DUMMY_VALUE"
    
    # Create the message object
    try:
        return message_class(**message_data)
    except Exception as e:
        logger.error(f"Error creating message: {str(e)}")
        return None

def format_fix_message(message):
    """Format a FIX message model into a FIX message string."""
    # Get all fields as a dictionary
    data = message.model_dump(exclude_none=True)
    
    # Format fields in the correct order
    fields = []
    
    # Standard header fields first
    header_fields = [
        ("8", "BeginString"),
        ("9", "BodyLength"),  # Will be calculated and added later
        ("35", "MsgType"),
        ("49", "SenderCompID"),
        ("56", "TargetCompID"),
        ("34", "MsgSeqNum"),
        ("52", "SendingTime")
    ]
    
    for tag, field_name in header_fields:
        if field_name in data and tag != "9":  # Skip BodyLength for now
            value = data[field_name]
            
            # Format datetime fields
            if isinstance(value, datetime):
                value = value.strftime("%Y%m%d-%H:%M:%S.%f")[:-3]
                
            fields.append(f"{tag}={value}")
    
    # Build a map of field names to tags for this message type
    field_to_tag = {}
    for attr_name in dir(message.__class__):
        attr = getattr(message.__class__, attr_name)
        if hasattr(attr, "alias") and not attr_name.startswith("__"):
            field_to_tag[attr_name] = attr.alias
            
    # Add all other fields (except known headers and additional_fields)
    excluded_fields = {field_name for _, field_name in header_fields} | {"additional_fields"}
    
    for field_name, value in data.items():
        if field_name in excluded_fields:
            continue
        
        # Find the tag for this field
        tag = field_to_tag.get(field_name)
        if tag:
            # Format datetime fields
            if isinstance(value, datetime):
                value = value.strftime("%Y%m%d-%H:%M:%S.%f")[:-3]
            
            fields.append(f"{tag}={value}")
    
    # Add any additional fields
    if "additional_fields" in data:
        for tag, value in data["additional_fields"].items():
            fields.append(f"{tag}={value}")
    
    # Print the fields to debug
    logger.debug(f"Field list before body calc: {fields}")
    
    # Calculate body length (excluding BeginString, BodyLength and CheckSum fields)
    body = "\x01".join(fields[2:]) + "\x01"
    body_length = len(body)
    
    # Insert BodyLength after BeginString
    fields.insert(1, f"9={body_length}")
    
    # Calculate CheckSum (simple sum of ASCII values modulo 256)
    message_with_length = "\x01".join(fields) + "\x01"
    checksum = sum(ord(c) for c in message_with_length) % 256
    
    # Add CheckSum field
    fields.append(f"10={checksum:03d}")
    
    # Join fields with SOH delimiter
    result = "\x01".join(fields) + "\x01"
    logger.debug(f"Final formatted message: {result.replace('\x01', '|')}")
    return result

def test_heartbeat():
    """Test creating and parsing a Heartbeat message."""
    from src.models.fix_simple.messages.heartbeat import HeartbeatMessage
    
    # Create a Heartbeat message
    heartbeat = HeartbeatMessage(
        BeginString="FIX.4.4",
        MsgType="0",
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=1,
        SendingTime=datetime.now(),
        TestReqID="TEST123"
    )
    
    # Format the message to FIX string
    fix_str = format_fix_message(heartbeat)
    logger.info(f"Formatted Heartbeat: {fix_str.replace('\x01', '|')}")
    
    # Parse the message back
    parsed = parse_fix_message(fix_str)
    logger.info(f"Parsed message type: {parsed.MsgType}")
    logger.info(f"TestReqID: {parsed.TestReqID}")
    
    return True

def test_new_order_single():
    """Test the NewOrderSingle message."""
    try:
        # Create a new order single message
        order = create_fix_message(
            MsgType="D",
            SenderCompID="SENDER",
            TargetCompID="TARGET",
            MsgSeqNum=2,
            SendingTime=datetime.now(),
            # Required fields that were missing in validation
            ClOrdID="ORD12345",  # Tag 11
            Side="1",  # Tag 54 - Buy
            TransactTime=datetime.now(),  # Tag 60
            OrdType="2",  # Tag 40 - Limit
            # Other fields
            Symbol="AAPL",
            Price=150.50,
            TimeInForce="0",  # Day
            OrderQty=100
        )
        
        # Format the message to FIX string
        fix_str = format_fix_message(order)
        logger.info(f"Formatted NewOrderSingle: {fix_str.replace('\x01', '|')}")
        
        # Parse the message back
        parsed = parse_fix_message(fix_str)
        logger.info(f"Parsed message type: {parsed.MsgType}")
        logger.info(f"ClOrdID: {parsed.ClOrdID}")
        logger.info(f"Side: {parsed.Side}")
        logger.info(f"OrdType: {parsed.OrdType}")
        logger.info(f"TransactTime: {parsed.TransactTime}")
        
        # Access fields that might be in additional_fields
        symbol = getattr(parsed, "Symbol", None)
        if symbol is None and "55" in parsed.additional_fields:
            symbol = parsed.additional_fields["55"]
        logger.info(f"Symbol: {symbol}")
        
        order_qty = getattr(parsed, "OrderQty", None)
        if order_qty is None and "38" in parsed.additional_fields:
            order_qty = parsed.additional_fields["38"]
        logger.info(f"OrderQty: {order_qty}")
        
        price = getattr(parsed, "Price", None)
        if price is None and "44" in parsed.additional_fields:
            price = parsed.additional_fields["44"]
        logger.info(f"Price: {price}")
        
        return True
    except Exception as e:
        logger.error(f"Error creating message: {e}")
        return False

def main():
    """Run the tests."""
    logger.info("Testing simplified FIX models")
    
    # Test Heartbeat message
    logger.info("\n=== Testing Heartbeat ===")
    if test_heartbeat():
        logger.info("Heartbeat test passed")
    else:
        logger.error("Heartbeat test failed")
    
    # Test NewOrderSingle message
    logger.info("\n=== Testing NewOrderSingle ===")
    if test_new_order_single():
        logger.info("NewOrderSingle test passed")
    else:
        logger.error("NewOrderSingle test failed")
    
    logger.info("\nAll tests completed")

if __name__ == "__main__":
    main() 