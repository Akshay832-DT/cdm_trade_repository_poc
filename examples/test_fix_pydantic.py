#!/usr/bin/env python3
"""
Simple test script for FIX models with Pydantic
"""
import sys
import os
import logging
from datetime import datetime

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import the models
try:
    from models.fix.generated.messages.executionreport import ExecutionReportMessage
    from models.fix.generated.components.instrument import InstrumentComponent
    logger.info("Successfully imported FIX models")
except ImportError as e:
    logger.error(f"Failed to import FIX models: {e}")
    sys.exit(1)

def main():
    """Simple test to verify that models work"""
    logger.info("Creating a simple instrument component...")
    
    try:
        # Create a simple instrument
        instrument = InstrumentComponent(
            Symbol="AAPL",
            SecurityID="037833100",
            SecurityIDSource="1"
        )
        logger.info(f"Created instrument: {instrument}")
        
        # Create a simple execution report
        execution_report = ExecutionReportMessage(
            BeginString="FIX.4.4",
            BodyLength=0,
            SenderCompID="SENDER",
            TargetCompID="TARGET",
            MsgSeqNum=1,
            SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S"),
            OrderID="ORD123",
            ExecID="EXEC456",
            ExecType="0",
            OrdStatus="0",
            Side="1",
            LeavesQty=100,
            CumQty=0,
            AvgPx=0,
            Instrument=instrument
        )
        logger.info(f"Created execution report: {execution_report}")
        
        # Serialize to dict
        data = execution_report.model_dump()
        logger.info(f"Model dump: {str(data)[:100]}...")
        
        logger.info("Test completed successfully!")
        return True
    
    except Exception as e:
        logger.error(f"Test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

if __name__ == "__main__":
    main() 