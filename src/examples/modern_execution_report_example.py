#!/usr/bin/env python3
"""
Modern ExecutionReport Message Example

This script demonstrates how to create and use ExecutionReportMessage objects
with the newly generated Pydantic 2 models that properly handle forward references.
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

# Import the generated models
from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.parties import PartiesComponent, NoPartyIDsGroup
from src.models.fix.generated.components.order_qty_data import OrderQtyDataComponent
from src.models.fix.generated.components.sec_alt_id_grp import SecAltIDGrpComponent
from src.models.fix.generated.components.evnt_grp import EvntGrpComponent
from src.models.fix.generated.components.commission_data import CommissionDataComponent
from src.models.fix.generated.components.cont_amt_grp import ContAmtGrpComponent
from src.models.fix.generated.components.contra_grp import ContraGrpComponent
from src.models.fix.generated.components.discretion_instructions import DiscretionInstructionsComponent
from src.models.fix.generated.components.financing_details import FinancingDetailsComponent
from src.models.fix.generated.components.instrmt_leg_exec_grp import InstrmtLegExecGrpComponent
from src.models.fix.generated.components.misc_fees_grp import MiscFeesGrpComponent
from src.models.fix.generated.components.peg_instructions import PegInstructionsComponent
from src.models.fix.generated.components.spread_or_benchmark_curve_data import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.und_instrmt_grp import UndInstrmtGrpComponent
from src.models.fix.generated.components.yield_data import YieldDataComponent

# Rebuild models to resolve forward references
InstrumentComponent.model_rebuild()
ExecutionReportMessage.model_rebuild()

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
        # Required base message fields
        BeginString="FIX.4.4",
        BodyLength=0,  # Will be calculated
        MsgType="ExecutionReport",  # ExecutionReport message type
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=1,
        SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")[:-3],
        
        # ExecutionReport specific fields
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
    
    # Create Parties component
    parties = PartiesComponent(
        NoPartyIDs=[NoPartyIDsGroup(
            PartyID="BROKER123",
            PartyIDSource="D",  # Proprietary/Custom code
            PartyRole=1         # Executing Firm
        ), NoPartyIDsGroup(
            PartyID="TRADER456",
            PartyIDSource="D",  # Proprietary/Custom code
            PartyRole=12        # Executing Trader
        )]
    )
    
    # Create an ExecutionReport for a filled order
    execution_report = ExecutionReportMessage(
        # Required base message fields
        BeginString="FIX.4.4",
        BodyLength=0,  # Will be calculated
        MsgType="ExecutionReport",  # ExecutionReport message type
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=2,
        SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S.%f")[:-3],
        
        # ExecutionReport specific fields
        OrderID="ORDER456",
        ExecID="EXEC456",
        ExecType="F",         # Trade (partial fill or fill)
        OrdStatus="2",        # Filled
        Side="1",             # Buy
        LeavesQty=0,          # No quantity left
        CumQty=200,           # Cumulative quantity filled
        AvgPx=155.75,         # Average fill price
        
        # Fill-specific fields
        LastQty=200,          # Quantity of this fill
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
    
    # Print party information
    if execution_report.Parties and execution_report.Parties.NoPartyIDs:
        for i, party in enumerate(execution_report.Parties.NoPartyIDs):
            logger.info(f"  Party {i+1}: ID={party.PartyID}, Role={party.PartyRole}")
    
    return execution_report

def demonstrate_serialization(execution_report):
    """Demonstrate different serialization methods."""
    logger.info("\nSerialization Examples:")
    
    # Convert to JSON
    json_data = execution_report.model_dump_json(indent=2)
    logger.info("JSON representation:")
    logger.info(json_data)
    
    # Convert to dictionary
    dict_data = execution_report.model_dump()
    logger.info("\nDictionary representation (keys are field names):")
    logger.info(str(dict_data)[:200] + "...")  # Show first 200 chars
    
    # Convert to dictionary with FIX field IDs as keys
    fix_dict = execution_report.model_dump(by_alias=True)
    logger.info("\nDictionary representation with FIX field IDs (keys are field IDs):")
    logger.info(str(fix_dict)[:200] + "...")  # Show first 200 chars
    
    return json_data, dict_data, fix_dict

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