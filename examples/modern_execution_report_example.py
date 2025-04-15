#!/usr/bin/env python3
"""
Modern ExecutionReport Message Example

This script demonstrates how to create and use ExecutionReportMessage objects
with the newly generated Pydantic models that properly handle forward references.
"""
import logging
from datetime import datetime, date
from typing import Dict, Any, Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import the generated models
from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent

def create_basic_execution_report():
    """Create a simple ExecutionReport with minimal required fields."""
    # Create an Instrument component
    instrument = InstrumentComponent(
        Symbol="AAPL",
        SecurityID="037833100",
        SecurityIDSource="1",  # CUSIP
        SecurityType="CS",     # Common Stock
    )
    
    # Create an ExecutionReport message
    execution_report = ExecutionReportMessage(
        BeginString="FIX.4.4",
        BodyLength=0,  # Will be calculated
        MsgType="8",   # ExecutionReport
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=1,
        SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S.%f"),
        CheckSum="000",  # Required header field
        OrderID="ORD12345",
        ExecID="EXEC78901",
        ExecType="0",        # New
        OrdStatus="0",       # New
        Side="1",            # Buy
        LeavesQty=100.0,     # Required field
        CumQty=0.0,          # Required field
        AvgPx=0.0,           # Required field
        Instrument=instrument,  # Required field
        TransactTime=datetime.now()
    )
    
    logger.info("Basic ExecutionReport created:")
    logger.info(f"  Message: {execution_report}")
    logger.info(f"  OrderID: {execution_report.OrderID}")
    logger.info(f"  Symbol: {execution_report.Instrument.Symbol}")
    logger.info(f"  Security ID: {execution_report.Instrument.SecurityID}")
    
    return execution_report

def create_fill_execution_report():
    """Create an ExecutionReport for a filled order with price and quantity information."""
    # Create an Instrument component
    instrument = InstrumentComponent(
        Symbol="MSFT",
        SecurityID="594918104",
        SecurityIDSource="1",  # CUSIP
        SecurityType="CS",     # Common Stock
    )
    
    # Create OrderQtyData component
    order_qty_data = OrderQtyDataComponent(
        OrderQty=200
    )
    
    # Create Parties component with NoParty items
    parties = PartiesComponent(
        NoParty=1,
        NoParty_items=[
            {
                "PartyID": "BROKER123",
                "PartyIDSource": "D",  # Proprietary/Custom code
                "PartyRole": "1"       # Executing Firm
            }
        ]
    )
    
    # Create an ExecutionReport for a filled order
    execution_report = ExecutionReportMessage(
        BeginString="FIX.4.4",
        BodyLength=0,  # Will be calculated
        MsgType="8",   # ExecutionReport
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=1,
        SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S.%f"),
        CheckSum="000",  # Required header field
        OrderID="ORDER456",
        ExecID="EXEC456",
        ExecType="F",         # Trade (partial fill or fill)
        OrdStatus="2",        # Filled
        Side="1",             # Buy
        LeavesQty=0.0,        # No quantity left
        CumQty=200.0,         # Cumulative quantity filled
        AvgPx=155.75,         # Average fill price
        
        # Fill-specific fields
        LastQty=200.0,        # Quantity of this fill
        LastPx=155.75,        # Price of this fill
        TransactTime=datetime.now(),
        
        # Order reference fields
        ClOrdID="CLIENT_ORDER_456",
        
        # Components
        Instrument=instrument,
        OrderQtyData=order_qty_data,
        Parties=parties
    )
    
    logger.info("\nFill ExecutionReport created:")
    logger.info(f"  ExecType: {execution_report.ExecType}")
    logger.info(f"  OrdStatus: {execution_report.OrdStatus}")
    logger.info(f"  LastQty: {execution_report.LastQty}")
    logger.info(f"  LastPx: {execution_report.LastPx}")
    logger.info(f"  CumQty: {execution_report.CumQty}")
    logger.info(f"  LeavesQty: {execution_report.LeavesQty}")
    logger.info(f"  AvgPx: {execution_report.AvgPx}")
    
    return execution_report

def demonstrate_serialization(execution_report):
    """Demonstrate different serialization methods."""
    logger.info("\nSerialization Examples:")
    
    # Convert to dictionary
    dict_data = execution_report.model_dump()
    logger.info("Dictionary representation (keys are field names):")
    logger.info(str(dict_data)[:200] + "...")  # Show first 200 chars
    
    # Convert to dictionary with FIX field IDs as keys
    fix_dict = execution_report.model_dump(by_alias=True)
    logger.info("\nDictionary representation with FIX field IDs (keys are field IDs):")
    logger.info(str(fix_dict)[:200] + "...")  # Show first 200 chars
    
    return dict_data, fix_dict

def main():
    """Main function to run the examples."""
    logger.info("Starting ExecutionReport examples...")
    
    # Create a basic ExecutionReport
    basic_report = create_basic_execution_report()
    
    # Create a filled ExecutionReport
    fill_report = create_fill_execution_report()
    
    # Demonstrate serialization
    demonstrate_serialization(fill_report)
    
    logger.info("Examples completed successfully.")

if __name__ == "__main__":
    main() 