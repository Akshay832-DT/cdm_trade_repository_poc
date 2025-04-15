#!/usr/bin/env python3
"""
ExecutionReport Message Examples

This script demonstrates how to create and use ExecutionReportMessage objects
with different field combinations and components.
"""
import sys
import os
import logging
from datetime import datetime, date
from typing import Dict, Any, Optional, List

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import base classes
from pydantic import BaseModel, Field, ConfigDict

# Define simplified component classes
class SimpleInstrumentComponent(BaseModel):
    """Simplified Instrument Component for examples"""
    model_config = ConfigDict(populate_by_name=True)
    
    Symbol: Optional[str] = Field(None, alias="55", description="")
    SecurityID: Optional[str] = Field(None, alias="48", description="")
    SecurityIDSource: Optional[str] = Field(None, alias="22", description="")
    
    def __str__(self):
        return f"SimpleInstrumentComponent({self.Symbol})"

class SimpleOrderQtyDataComponent(BaseModel):
    """Simplified OrderQtyData Component for examples"""
    model_config = ConfigDict(populate_by_name=True)
    
    OrderQty: Optional[float] = Field(None, alias="38", description="")
    
    def __str__(self):
        return f"SimpleOrderQtyDataComponent({self.OrderQty})"

class SimpleExecutionReportMessage(BaseModel):
    """Simplified ExecutionReport Message for examples"""
    model_config = ConfigDict(populate_by_name=True)
    
    # Standard FIX header fields
    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: str = Field(..., description='', alias='52')
    
    # Essential ExecutionReport fields
    OrderID: str = Field(..., alias="37", description="")
    ExecID: str = Field(..., alias="17", description="")
    ExecType: str = Field(..., alias="150", description="")
    OrdStatus: str = Field(..., alias="39", description="")
    Side: str = Field(..., alias="54", description="")
    LeavesQty: float = Field(..., alias="151", description="")
    CumQty: float = Field(..., alias="14", description="")
    AvgPx: float = Field(..., alias="6", description="")
    
    # Optional fields
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    OrigClOrdID: Optional[str] = Field(None, alias="41", description="")
    LastQty: Optional[float] = Field(None, alias="32", description="")
    LastPx: Optional[float] = Field(None, alias="31", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    ExecTransType: Optional[str] = Field(None, alias="20", description="")
    OrdRejReason: Optional[int] = Field(None, alias="103", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    
    # Components
    Instrument: SimpleInstrumentComponent = Field(..., description="")
    OrderQtyData: Optional[SimpleOrderQtyDataComponent] = Field(None, description="")
    
    def __str__(self):
        return f"SimpleExecutionReportMessage({self.MsgType})"
    
    def model_dump(self):
        """Convert to dictionary"""
        data = {
            "BeginString": self.BeginString,
            "BodyLength": self.BodyLength,
            "MsgType": self.MsgType,
            "SenderCompID": self.SenderCompID,
            "TargetCompID": self.TargetCompID,
            "MsgSeqNum": self.MsgSeqNum,
            "SendingTime": self.SendingTime,
            "OrderID": self.OrderID,
            "ExecID": self.ExecID,
            "ExecType": self.ExecType,
            "OrdStatus": self.OrdStatus,
            "Side": self.Side,
            "LeavesQty": self.LeavesQty,
            "CumQty": self.CumQty,
            "AvgPx": self.AvgPx,
        }
        
        if self.ClOrdID is not None:
            data["ClOrdID"] = self.ClOrdID
        if self.OrigClOrdID is not None:
            data["OrigClOrdID"] = self.OrigClOrdID
        if self.LastQty is not None:
            data["LastQty"] = self.LastQty
        if self.LastPx is not None:
            data["LastPx"] = self.LastPx
        if self.TransactTime is not None:
            data["TransactTime"] = self.TransactTime
        if self.ExecTransType is not None:
            data["ExecTransType"] = self.ExecTransType
        if self.OrdRejReason is not None:
            data["OrdRejReason"] = self.OrdRejReason
        if self.Text is not None:
            data["Text"] = self.Text
        
        data["Instrument"] = {
            "Symbol": self.Instrument.Symbol,
            "SecurityID": self.Instrument.SecurityID,
            "SecurityIDSource": self.Instrument.SecurityIDSource
        }
        
        if self.OrderQtyData is not None:
            data["OrderQtyData"] = {"OrderQty": self.OrderQtyData.OrderQty}
        
        return data

def create_basic_execution_report():
    """Create a simple ExecutionReport with minimal required fields."""
    # Create an Instrument component
    instrument = SimpleInstrumentComponent(
        Symbol="AAPL",
        SecurityID="037833100",
        SecurityIDSource="1"  # CUSIP
    )
    
    # Create a basic ExecutionReport
    execution_report = SimpleExecutionReportMessage(
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
        ExecType="0",  # New
        OrdStatus="0", # New
        Side="1",      # Buy
        LeavesQty=100,
        CumQty=0,
        AvgPx=0,
        
        # Optional fields
        ClOrdID="CLIENT_ORDER_123",
        
        # Components
        Instrument=instrument
    )
    
    logger.info("Basic ExecutionReport created:")
    logger.info(f"  MsgType: {execution_report.MsgType}")
    logger.info(f"  OrderID: {execution_report.OrderID}")
    logger.info(f"  ExecType: {execution_report.ExecType}")
    logger.info(f"  Symbol: {execution_report.Instrument.Symbol}")
    
    return execution_report

def create_fill_execution_report():
    """Create an ExecutionReport for a filled order with price and quantity information."""
    # Create an Instrument component
    instrument = SimpleInstrumentComponent(
        Symbol="MSFT",
        SecurityID="594918104",
        SecurityIDSource="1"  # CUSIP
    )
    
    # Create OrderQtyData component
    order_qty_data = SimpleOrderQtyDataComponent(
        OrderQty=200
    )
    
    # Create an ExecutionReport for a filled order
    execution_report = SimpleExecutionReportMessage(
        # Standard header fields
        BeginString="FIX.4.4",
        BodyLength=0,  # Will be calculated when sending
        MsgType="8",   # ExecutionReport
        SenderCompID="BROKER",
        TargetCompID="CLIENT",
        MsgSeqNum=2,
        SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")[:-3],
        
        # Required ExecutionReport fields
        OrderID="ORDER456",
        ExecID="EXEC456",
        ExecType="F",  # Trade (partial fill or fill)
        OrdStatus="2", # Filled
        Side="1",      # Buy
        LeavesQty=0,   # No quantity left
        CumQty=200,    # Cumulative quantity filled
        AvgPx=155.75,  # Average fill price
        
        # Fill-specific fields
        LastQty=200,           # Quantity of this fill
        LastPx=155.75,         # Price of this fill
        TransactTime=datetime.now(),
        ExecTransType="0",     # New
        
        # Order reference fields
        ClOrdID="CLIENT_ORDER_456",
        OrigClOrdID="CLIENT_ORDER_ORIG_456",
        
        # Components
        Instrument=instrument,
        OrderQtyData=order_qty_data
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

def create_rejected_execution_report():
    """Create an ExecutionReport for a rejected order with rejection reason."""
    # Create an Instrument component
    instrument = SimpleInstrumentComponent(
        Symbol="GOOG",
        SecurityID="02079K107",
        SecurityIDSource="1"  # CUSIP
    )
    
    # Create an ExecutionReport for a rejected order
    execution_report = SimpleExecutionReportMessage(
        # Standard header fields
        BeginString="FIX.4.4",
        BodyLength=0,  # Will be calculated when sending
        MsgType="8",   # ExecutionReport
        SenderCompID="BROKER",
        TargetCompID="CLIENT",
        MsgSeqNum=3,
        SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")[:-3],
        
        # Required ExecutionReport fields
        OrderID="ORDER789",
        ExecID="EXEC789",
        ExecType="8",  # Rejected
        OrdStatus="8", # Rejected
        Side="1",      # Buy
        LeavesQty=0,   # No quantity left after rejection
        CumQty=0,      # No quantity filled
        AvgPx=0,       # No average price
        
        # Rejection fields
        OrdRejReason=1,  # Unknown symbol
        Text="Symbol not found in exchange",
        
        # Order reference fields
        ClOrdID="CLIENT_ORDER_789",
        
        # Components
        Instrument=instrument
    )
    
    logger.info("\nRejected ExecutionReport created:")
    logger.info(f"  ExecType: {execution_report.ExecType}")
    logger.info(f"  OrdStatus: {execution_report.OrdStatus}")
    logger.info(f"  OrdRejReason: {execution_report.OrdRejReason}")
    logger.info(f"  Text: {execution_report.Text}")
    
    return execution_report

def manipulate_execution_report(execution_report):
    """Demonstrate how to manipulate and update an ExecutionReport object."""
    logger.info("\nManipulating ExecutionReport:")
    
    # Update basic fields
    execution_report.TransactTime = datetime.now()
    execution_report.Text = "Updated execution report"
    
    # Update nested component
    execution_report.Instrument.Symbol = "AAPL.US"
    execution_report.Instrument.SecurityIDSource = "4"  # ISIN
    execution_report.Instrument.SecurityID = "US0378331005"
    
    # Print updated values
    logger.info(f"  Updated Symbol: {execution_report.Instrument.Symbol}")
    logger.info(f"  Updated SecurityID: {execution_report.Instrument.SecurityID}")
    logger.info(f"  Updated SecurityIDSource: {execution_report.Instrument.SecurityIDSource}")
    logger.info(f"  Updated Text: {execution_report.Text}")
    
    # Convert to dictionary for serialization
    report_dict = execution_report.model_dump()
    logger.info(f"  Dict representation (partial): {list(report_dict.keys())}")
    
    return report_dict

def main():
    """Run the ExecutionReport examples."""
    logger.info("ExecutionReport Message Examples")
    
    try:
        # Create different types of ExecutionReport messages
        basic_report = create_basic_execution_report()
        fill_report = create_fill_execution_report()
        reject_report = create_rejected_execution_report()
        
        # Demonstrate manipulating an ExecutionReport
        report_dict = manipulate_execution_report(basic_report)
        
        logger.info("\nAll examples completed successfully")
    except Exception as e:
        logger.error(f"Error in ExecutionReport examples: {e}", exc_info=True)

if __name__ == "__main__":
    main()

"""
Example showing how to use ExecutionReportMessage
"""
from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
from src.models.fix.generated.components.instrument import InstrumentComponent

# Create an Instrument component
instrument = InstrumentComponent(
    Symbol="AAPL",
    SecurityID="037833100",
    SecurityIDSource="1",  # CUSIP
    SecurityType="CS",  # Common Stock
)

# Create an ExecutionReport message
execution_report = ExecutionReportMessage(
    OrderID="ORD12345",
    ExecID="EXEC78901",
    ExecType="0",        # New
    OrdStatus="0",       # New
    Side="1",            # Buy
    LeavesQty=100,
    CumQty=0,
    AvgPx=0,
    Instrument=instrument,
    TransactTime=datetime.now()
)

# Print the execution report
print(f"Created ExecutionReport: {execution_report}")
print(f"Order ID: {execution_report.OrderID}")
print(f"Symbol: {execution_report.Instrument.Symbol}")
print(f"Security ID: {execution_report.Instrument.SecurityID}")

# Convert to JSON
json_data = execution_report.model_dump_json(indent=2)
print("\nJSON representation:")
print(json_data)

# Convert to dictionary
dict_data = execution_report.model_dump()
print("\nDictionary representation:")
print(dict_data)

# You can also serialize with FIX field IDs as keys (using aliases)
fix_dict = execution_report.model_dump(by_alias=True)
print("\nFIX Field representation:")
print(fix_dict) 