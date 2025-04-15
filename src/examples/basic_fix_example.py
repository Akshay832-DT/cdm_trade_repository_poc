#!/usr/bin/env python3
"""
Basic FIX Message Example

This script demonstrates how to create and parse FIX messages using Pydantic
without relying on the generated models.
"""
import sys
import os
import logging
import re
from datetime import datetime
from typing import Dict, Any, Optional, List, Union
from pydantic import BaseModel, Field, ConfigDict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define a base FIX message class
class FIXMessageBase(BaseModel):
    """Base class for FIX messages."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )
    
    # Standard header fields
    BeginString: str = Field("FIX.4.4", description="FIX protocol version", alias="8")
    BodyLength: Optional[int] = Field(None, description="Message body length", alias="9")
    MsgType: str = Field(..., description="Message type", alias="35")
    SenderCompID: str = Field(..., description="Sender's CompID", alias="49")
    TargetCompID: str = Field(..., description="Target's CompID", alias="56")
    MsgSeqNum: int = Field(..., description="Message sequence number", alias="34")
    SendingTime: datetime = Field(..., description="Time message was sent", alias="52")
    
    # Additional fields stored in a dictionary
    additional_fields: Dict[str, Any] = Field(default_factory=dict, exclude=True)
    
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Convert message to a dictionary."""
        data = super().model_dump(**kwargs)
        
        # Add additional fields
        if 'exclude_none' in kwargs and kwargs['exclude_none']:
            data.update({k: v for k, v in self.additional_fields.items() if v is not None})
        else:
            data.update(self.additional_fields)
            
        return data

# Define some specific message types
class HeartbeatMessage(FIXMessageBase):
    """FIX Heartbeat Message (MsgType=0)."""
    MsgType: str = Field("0", description="Heartbeat message type", alias="35")
    TestReqID: Optional[str] = Field(None, description="Test request ID", alias="112")

class NewOrderSingleMessage(FIXMessageBase):
    """FIX New Order Single Message (MsgType=D)."""
    MsgType: str = Field("D", description="New Order Single message type", alias="35")
    ClOrdID: str = Field(..., description="Client Order ID", alias="11")
    Symbol: str = Field(..., description="Ticker symbol", alias="55")
    Side: str = Field(..., description="Order side (1=Buy, 2=Sell)", alias="54")
    OrderQty: float = Field(..., description="Order quantity", alias="38")
    OrdType: str = Field(..., description="Order type (1=Market, 2=Limit)", alias="40")
    Price: Optional[float] = Field(None, description="Price (required for limit orders)", alias="44")
    TimeInForce: Optional[str] = Field(None, description="Time in force", alias="59")
    TransactTime: datetime = Field(..., description="Transaction time", alias="60")

def parse_fix_message(message_str: str) -> Optional[FIXMessageBase]:
    """
    Parse a FIX message string into an appropriate message model.
    
    Args:
        message_str: The FIX message string
        
    Returns:
        A FIX message model if parsing succeeds, None otherwise
    """
    try:
        # Split the message by SOH delimiter and extract fields
        fields = {}
        for field in message_str.split("\x01"):
            if "=" in field:
                tag, value = field.split("=", 1)
                fields[tag] = value
                
        # Determine message type
        msg_type = fields.get("35")
        if not msg_type:
            logger.error("Message type (tag 35) not found")
            return None
            
        # Convert datetime fields
        datetime_fields = {"52", "60", "122"}
        for tag in datetime_fields:
            if tag in fields:
                try:
                    if "." in fields[tag]:
                        fields[tag] = datetime.strptime(fields[tag], "%Y%m%d-%H:%M:%S.%f")
                    else:
                        fields[tag] = datetime.strptime(fields[tag], "%Y%m%d-%H:%M:%S")
                except ValueError:
                    logger.warning(f"Could not parse datetime for tag {tag}: {fields[tag]}")
                    
        # Create appropriate message object based on message type
        if msg_type == "0":
            # Heartbeat
            message = HeartbeatMessage(
                BeginString=fields.get("8", "FIX.4.4"),
                MsgType=msg_type,
                SenderCompID=fields.get("49", ""),
                TargetCompID=fields.get("56", ""),
                MsgSeqNum=int(fields.get("34", "0")),
                SendingTime=fields.get("52", datetime.now()),
                TestReqID=fields.get("112")
            )
        elif msg_type == "D":
            # New Order Single
            message = NewOrderSingleMessage(
                BeginString=fields.get("8", "FIX.4.4"),
                MsgType=msg_type,
                SenderCompID=fields.get("49", ""),
                TargetCompID=fields.get("56", ""),
                MsgSeqNum=int(fields.get("34", "0")),
                SendingTime=fields.get("52", datetime.now()),
                ClOrdID=fields.get("11", ""),
                Symbol=fields.get("55", ""),
                Side=fields.get("54", ""),
                OrderQty=float(fields.get("38", "0")),
                OrdType=fields.get("40", ""),
                Price=float(fields.get("44")) if "44" in fields else None,
                TimeInForce=fields.get("59"),
                TransactTime=fields.get("60", datetime.now())
            )
        else:
            # Generic message
            message = FIXMessageBase(
                BeginString=fields.get("8", "FIX.4.4"),
                MsgType=msg_type,
                SenderCompID=fields.get("49", ""),
                TargetCompID=fields.get("56", ""),
                MsgSeqNum=int(fields.get("34", "0")),
                SendingTime=fields.get("52", datetime.now())
            )
            
        # Add any additional fields not explicitly defined in the model
        for tag, value in fields.items():
            if tag not in {"8", "9", "35", "49", "56", "34", "52"}:
                if msg_type == "0" and tag == "112":
                    continue  # TestReqID is already handled
                elif msg_type == "D" and tag in {"11", "55", "54", "38", "40", "44", "59", "60"}:
                    continue  # These fields are already handled for NewOrderSingle
                    
                # Add to additional_fields
                message.additional_fields[tag] = value
                
        return message
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
        
        # Message-specific fields
        msg_type = data.get("MsgType")
        if msg_type == "0" and "TestReqID" in data:
            fields.append(f"112={data['TestReqID']}")
        elif msg_type == "D":
            # New Order Single specific fields
            order_fields = [
                ("11", "ClOrdID"),
                ("55", "Symbol"),
                ("54", "Side"),
                ("38", "OrderQty"),
                ("40", "OrdType"),
                ("44", "Price"),
                ("59", "TimeInForce"),
                ("60", "TransactTime")
            ]
            
            for tag, field_name in order_fields:
                if field_name in data:
                    value = data[field_name]
                    
                    # Format datetime fields
                    if isinstance(value, datetime):
                        value = value.strftime("%Y%m%d-%H:%M:%S.%f")[:-3]
                        
                    fields.append(f"{tag}={value}")
        
        # Add additional fields
        for tag, value in data.get("additional_fields", {}).items():
            fields.append(f"{tag}={value}")
        
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
        return "\x01".join(fields) + "\x01"
    except Exception as e:
        logger.error(f"Error formatting FIX message: {e}")
        return ""

def main():
    """Main function demonstrating FIX message parsing and formatting."""
    # Example FIX message (New Order Single)
    fix_message = (
        "8=FIX.4.4\x019=145\x0135=D\x0134=1\x0149=SENDER\x0156=TARGET\x0152=20250413-18:30:00\x01"
        "11=ClientOrderID\x0121=1\x0155=AAPL\x0154=1\x0160=20250413-18:30:00\x0138=100\x0140=2\x01"
        "44=155.50\x0159=0\x0110=123\x01"
    )
    
    # Print the original message
    logger.info("Original FIX message:")
    logger.info(fix_message.replace("\x01", "|"))
    
    # Parse the message
    message = parse_fix_message(fix_message)
    
    if message:
        logger.info("\nParsed message:")
        logger.info(f"Message Type: {message.MsgType}")
        
        if isinstance(message, NewOrderSingleMessage):
            logger.info(f"Client Order ID: {message.ClOrdID}")
            logger.info(f"Symbol: {message.Symbol}")
            logger.info(f"Side: {message.Side}")
            logger.info(f"Quantity: {message.OrderQty}")
            logger.info(f"Price: {message.Price}")
            
            # Modify the message
            message.OrderQty = 200
            message.Price = 156.75
            
        # Format the message back to FIX format
        formatted_message = format_fix_message(message)
        
        logger.info("\nModified FIX message:")
        logger.info(formatted_message.replace("\x01", "|"))
    else:
        logger.error("Failed to parse the message")
    
    # Create a Heartbeat message directly
    heartbeat = HeartbeatMessage(
        MsgType="0",
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=2,
        SendingTime=datetime.now(),
        TestReqID="TEST123"
    )
    
    # Format the Heartbeat message
    heartbeat_fix = format_fix_message(heartbeat)
    
    logger.info("\nHeartbeat message:")
    logger.info(heartbeat_fix.replace("\x01", "|"))

if __name__ == "__main__":
    main() 