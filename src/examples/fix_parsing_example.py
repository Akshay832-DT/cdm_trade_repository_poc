#!/usr/bin/env python3
"""
FIX 4.4 Parsing Example

This example demonstrates how to use the comprehensive FIX 4.4 models.
"""
import asyncio
import logging
from ..parsers.controller import ParserController
from ..models.fix.generated.messages import NewOrderSingle, ExecutionReport

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Example FIX 4.4 Messages
NEW_ORDER_SINGLE = """8=FIX.4.4|9=176|35=D|34=124|49=FIXTEST|52=20220101-10:10:10|56=FIXSERVER|11=ABC123|21=1|38=100|40=2|44=150.5|54=1|55=AAPL|59=0|60=20220101-10:10:10|10=120|"""

EXECUTION_REPORT = """8=FIX.4.4|9=252|35=8|34=125|49=FIXSERVER|52=20220101-10:10:11|56=FIXTEST|6=0|11=ABC123|14=100|17=1|20=0|31=150.5|32=100|37=1|38=100|39=2|40=2|54=1|55=AAPL|60=20220101-10:10:11|150=2|151=0|10=148|"""

async def parse_examples():
    """Parse example FIX messages using both generic and specific models."""
    parser_controller = ParserController()
    
    try:
        # Parse New Order Single message
        logger.info("Parsing New Order Single message...")
        new_order = await parser_controller.parse_message(NEW_ORDER_SINGLE, "FIX")
        
        # Check if we got the specific model or generic model
        if isinstance(new_order, NewOrderSingle):
            logger.info("Parsed as NewOrderSingle model")
        else:
            logger.info("Parsed as generic FIXMessage model")
        
        # Access fields using model attributes
        logger.info(f"Order ID: {new_order.ClOrdID}")
        logger.info(f"Symbol: {new_order.Symbol}")
        logger.info(f"Order Qty: {new_order.OrderQty}")
        
        # Convert to JSON
        logger.info(f"New Order JSON: {new_order.to_json()}")
        
        # Parse Execution Report message
        logger.info("\nParsing Execution Report message...")
        exec_report = await parser_controller.parse_message(EXECUTION_REPORT, "FIX")
        
        # Check if we got the specific model or generic model
        if isinstance(exec_report, ExecutionReport):
            logger.info("Parsed as ExecutionReport model")
        else:
            logger.info("Parsed as generic FIXMessage model")
        
        # Access fields using model attributes
        logger.info(f"Order ID: {exec_report.ClOrdID}")
        logger.info(f"Exec ID: {exec_report.ExecID}")
        logger.info(f"Exec Type: {exec_report.ExecType}")
        logger.info(f"Order Status: {exec_report.OrdStatus}")
        
        # Convert to JSON
        logger.info(f"Execution Report JSON: {exec_report.to_json()}")
        
    except Exception as e:
        logger.error(f"Error parsing FIX messages: {str(e)}")

if __name__ == "__main__":
    asyncio.run(parse_examples()) 