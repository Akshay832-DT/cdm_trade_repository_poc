#!/usr/bin/env python3
"""
ExecutionReport Serialization Example

This script demonstrates how to serialize and deserialize ExecutionReport messages
to and from JSON and FIX formats.
"""
import sys
import os
import json
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

def create_sample_execution_report():
    """Create a sample ExecutionReport for demonstration."""
    from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
    from src.models.fix.generated.components.instrument import InstrumentComponent
    
    # Create an Instrument component
    instrument = InstrumentComponent(
        Symbol="AAPL",
        SecurityID="037833100",
        SecurityIDSource="1"  # CUSIP
    )
    
    # Create a sample ExecutionReport
    execution_report = ExecutionReportMessage(
        # Standard header fields
        BeginString="FIX.4.4",
        BodyLength=0,  # Will be calculated when sending
        MsgType="8",   # ExecutionReport
        SenderCompID="BROKER",
        TargetCompID="CLIENT",
        MsgSeqNum=1,
        SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")[:-3],
        
        # Required ExecutionReport fields
        OrderID="ORDER123",
        ExecID="EXEC123",
        ExecType="F",  # Trade (partial fill or fill)
        OrdStatus="1", # Partially filled
        Side="1",      # Buy
        LeavesQty=50,  # Quantity remaining
        CumQty=50,     # Cumulative quantity filled
        AvgPx=175.25,  # Average fill price
        
        # Fill-specific fields
        LastQty=50,           # Quantity of this fill
        LastPx=175.25,        # Price of this fill
        TransactTime=datetime.now(),
        
        # Reference fields
        ClOrdID="CLIENT_ORDER_123",
        
        # Components
        Instrument=instrument
    )
    
    logger.info("Sample ExecutionReport created:")
    logger.info(f"  OrderID: {execution_report.OrderID}")
    logger.info(f"  ExecType: {execution_report.ExecType}")
    logger.info(f"  LastQty: {execution_report.LastQty}")
    logger.info(f"  LastPx: {execution_report.LastPx}")
    
    return execution_report

def serialize_to_json(execution_report):
    """Serialize an ExecutionReport to JSON."""
    logger.info("\nSerializing ExecutionReport to JSON:")
    
    # Convert the message to a dictionary
    msg_dict = execution_report.model_dump()
    
    # Convert datetime objects to ISO format strings for JSON serialization
    def convert_datetime(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")
    
    # Serialize to JSON
    json_str = json.dumps(msg_dict, default=convert_datetime, indent=2)
    
    logger.info(f"JSON output (sample):\n{json_str[:500]}...")
    return json_str

def deserialize_from_json(json_str):
    """Deserialize an ExecutionReport from JSON."""
    logger.info("\nDeserializing ExecutionReport from JSON:")
    
    from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
    
    # Parse the JSON string to a dictionary
    msg_dict = json.loads(json_str)
    
    # Convert ISO format strings back to datetime objects
    for key, value in msg_dict.items():
        if isinstance(value, str) and 'T' in value and value.endswith('Z'):
            try:
                msg_dict[key] = datetime.fromisoformat(value.replace('Z', '+00:00'))
            except ValueError:
                pass
    
    # Deserialize to an ExecutionReportMessage object
    execution_report = ExecutionReportMessage.model_validate(msg_dict)
    
    logger.info("Deserialized ExecutionReport:")
    logger.info(f"  OrderID: {execution_report.OrderID}")
    logger.info(f"  ExecType: {execution_report.ExecType}")
    logger.info(f"  LastQty: {execution_report.LastQty}")
    logger.info(f"  Symbol: {execution_report.Instrument.Symbol}")
    
    return execution_report

def serialize_to_fix(execution_report):
    """Serialize an ExecutionReport to FIX format."""
    logger.info("\nSerializing ExecutionReport to FIX format:")
    
    # Get all fields as a dictionary
    data = execution_report.model_dump(exclude_none=True)
    
    # Format fields in the correct order
    fields = []
    
    # Standard header fields first (BeginString must be first, BodyLength second)
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
    
    # Now add ExecutionReport specific fields
    exec_fields = [
        ("37", "OrderID"),
        ("17", "ExecID"),
        ("150", "ExecType"),
        ("39", "OrdStatus"),
        ("54", "Side"),
        ("151", "LeavesQty"),
        ("14", "CumQty"),
        ("6", "AvgPx"),
        ("32", "LastQty"),
        ("31", "LastPx"),
        ("60", "TransactTime"),
        ("11", "ClOrdID"),
    ]
    
    for tag, field_name in exec_fields:
        if field_name in data:
            value = data[field_name]
            
            # Format datetime fields
            if isinstance(value, datetime):
                value = value.strftime("%Y%m%d-%H:%M:%S.%f")[:-3]
                
            fields.append(f"{tag}={value}")
    
    # Add Instrument component fields
    if "Instrument" in data:
        instrument = data["Instrument"]
        if "Symbol" in instrument:
            fields.append(f"55={instrument['Symbol']}")
        if "SecurityID" in instrument:
            fields.append(f"48={instrument['SecurityID']}")
        if "SecurityIDSource" in instrument:
            fields.append(f"22={instrument['SecurityIDSource']}")
    
    # Calculate body length (excluding BeginString, BodyLength fields)
    body = "\x01".join(fields[2:]) + "\x01"
    body_length = len(body)
    
    # Insert BodyLength after BeginString
    fields.insert(1, f"9={body_length}")
    
    # Calculate CheckSum (sum of ASCII values modulo 256)
    message_with_length = "\x01".join(fields) + "\x01"
    checksum = sum(ord(c) for c in message_with_length) % 256
    
    # Add CheckSum field
    fields.append(f"10={checksum:03d}")
    
    # Join fields with SOH delimiter
    fix_message = "\x01".join(fields) + "\x01"
    
    # Display the message (replacing SOH with | for readability)
    logger.info(f"FIX message (SOH replaced with | for readability):")
    logger.info(fix_message.replace("\x01", "|"))
    
    return fix_message

def deserialize_from_fix(fix_message):
    """Deserialize an ExecutionReport from FIX format."""
    logger.info("\nDeserializing ExecutionReport from FIX format:")
    
    from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
    from src.models.fix.generated.components.instrument import InstrumentComponent
    
    # Split the message by SOH delimiter and extract fields
    fields = {}
    for field in fix_message.split("\x01"):
        if "=" in field:
            tag, value = field.split("=", 1)
            fields[tag] = value
    
    # Verify it's an ExecutionReport (MsgType=8)
    if fields.get("35") != "8":
        raise ValueError(f"Not an ExecutionReport message. MsgType: {fields.get('35')}")
    
    # Create the Instrument component
    instrument = InstrumentComponent(
        Symbol=fields.get("55", ""),
        SecurityID=fields.get("48", ""),
        SecurityIDSource=fields.get("22", "")
    )
    
    # Parse datetime fields
    sending_time = fields.get("52", "")
    transact_time = fields.get("60", "")
    
    if sending_time:
        try:
            sending_time = datetime.strptime(sending_time, "%Y%m%d-%H:%M:%S.%f")
        except ValueError:
            try:
                sending_time = datetime.strptime(sending_time, "%Y%m%d-%H:%M:%S")
            except ValueError:
                sending_time = datetime.now()
    
    if transact_time:
        try:
            transact_time = datetime.strptime(transact_time, "%Y%m%d-%H:%M:%S.%f")
        except ValueError:
            try:
                transact_time = datetime.strptime(transact_time, "%Y%m%d-%H:%M:%S")
            except ValueError:
                transact_time = datetime.now()
    
    # Create the ExecutionReport message
    execution_report = ExecutionReportMessage(
        # Standard header fields
        BeginString=fields.get("8", "FIX.4.4"),
        BodyLength=int(fields.get("9", 0)),
        MsgType=fields.get("35", "8"),
        SenderCompID=fields.get("49", ""),
        TargetCompID=fields.get("56", ""),
        MsgSeqNum=int(fields.get("34", 0)),
        SendingTime=sending_time,
        
        # ExecutionReport fields
        OrderID=fields.get("37", ""),
        ExecID=fields.get("17", ""),
        ExecType=fields.get("150", ""),
        OrdStatus=fields.get("39", ""),
        Side=fields.get("54", ""),
        LeavesQty=float(fields.get("151", 0)),
        CumQty=float(fields.get("14", 0)),
        AvgPx=float(fields.get("6", 0)),
        
        # Optional fields
        LastQty=float(fields.get("32", 0)) if "32" in fields else None,
        LastPx=float(fields.get("31", 0)) if "31" in fields else None,
        TransactTime=transact_time if transact_time else None,
        ClOrdID=fields.get("11", None),
        
        # Components
        Instrument=instrument
    )
    
    logger.info("Deserialized ExecutionReport from FIX:")
    logger.info(f"  OrderID: {execution_report.OrderID}")
    logger.info(f"  ExecType: {execution_report.ExecType}")
    logger.info(f"  OrdStatus: {execution_report.OrdStatus}")
    logger.info(f"  Side: {execution_report.Side}")
    logger.info(f"  Symbol: {execution_report.Instrument.Symbol}")
    
    return execution_report

def main():
    """Run the ExecutionReport serialization examples."""
    logger.info("ExecutionReport Serialization Examples")
    
    try:
        # Create a sample ExecutionReport
        execution_report = create_sample_execution_report()
        
        # JSON serialization and deserialization
        json_str = serialize_to_json(execution_report)
        deserialized_from_json = deserialize_from_json(json_str)
        
        # FIX serialization and deserialization
        fix_message = serialize_to_fix(execution_report)
        deserialized_from_fix = deserialize_from_fix(fix_message)
        
        logger.info("\nAll serialization examples completed successfully")
    except Exception as e:
        logger.error(f"Error in serialization examples: {e}", exc_info=True)

if __name__ == "__main__":
    main() 