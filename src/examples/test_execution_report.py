#!/usr/bin/env python3
"""
Test ExecutionReport Message

This script demonstrates how to create and use an ExecutionReportMessage.
"""
import sys
import os
import logging
from datetime import datetime

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_execution_report():
    """Create and demonstrate the use of an ExecutionReportMessage."""
    from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
    from src.models.fix.generated.components.instrument import InstrumentComponent
    
    # Create the required Instrument component
    instrument = InstrumentComponent(
        Symbol="AAPL",
        SecurityID="AAPL",
        SecurityIDSource="4"  # ISIN number
    )
    
    # Create an ExecutionReportMessage
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
        ExecType="0",  # New
        OrdStatus="0", # New
        Side="1",      # Buy
        LeavesQty=100,
        CumQty=0,
        AvgPx=0,
        
        # Optional fields
        ClOrdID="CLIENT_ORDER_123",
        TransactTime=datetime.now(),
        LastQty=0,
        LastPx=0,
        Text="New order execution report",
        
        # Required components
        Instrument=instrument
    )
    
    logger.info(f"Created ExecutionReport: {execution_report}")
    
    # Demonstrate accessing fields
    logger.info(f"OrderID: {execution_report.OrderID}")
    logger.info(f"ExecType: {execution_report.ExecType}")
    logger.info(f"OrdStatus: {execution_report.OrdStatus}")
    logger.info(f"Symbol: {execution_report.Instrument.Symbol}")
    
    # Convert to dict for serialization
    execution_report_dict = execution_report.model_dump()
    logger.info(f"ExecutionReport as dict: {execution_report_dict}")
    
    return execution_report

def main():
    """Run the ExecutionReport example."""
    logger.info("Testing ExecutionReport Message")
    
    try:
        create_execution_report()
        logger.info("ExecutionReport test passed")
    except Exception as e:
        logger.error(f"ExecutionReport test failed: {e}", exc_info=True)
    
    logger.info("Test completed")

if __name__ == "__main__":
    main() 