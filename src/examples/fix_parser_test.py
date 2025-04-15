#!/usr/bin/env python3
"""
Test script for the updated FIX parsers with new models
"""
import asyncio
import logging
import simplefix
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import parsers
from src.parsers.fix.parser import FIXParser
from src.models.fix.generated.messages.newordersingle import NewOrderSingleMessage
from src.models.fix.generated.messages.bidresponse import BidResponseMessage

async def test_new_order_single_parser():
    """Test parsing a NewOrderSingle FIX message."""
    # Create a FIX parser
    parser = FIXParser()
    
    # Create a simplefix message
    msg = simplefix.FixMessage()
    msg.append_pair(8, "FIX.4.4")  # BeginString
    msg.append_pair(9, "100")      # BodyLength (placeholder)
    msg.append_pair(35, "D")       # MsgType = NewOrderSingle
    msg.append_pair(49, "SENDER")  # SenderCompID
    msg.append_pair(56, "TARGET")  # TargetCompID
    msg.append_pair(34, "1")       # MsgSeqNum
    msg.append_pair(52, datetime.now().strftime("%Y%m%d-%H:%M:%S.%f"))  # SendingTime
    
    # Add NewOrderSingle specific fields
    msg.append_pair(11, "ORDER123")        # ClOrdID
    msg.append_pair(21, "1")               # HandlInst
    msg.append_pair(55, "AAPL")            # Symbol
    msg.append_pair(54, "1")               # Side (Buy)
    msg.append_pair(60, datetime.now().strftime("%Y%m%d-%H:%M:%S.%f"))  # TransactTime
    msg.append_pair(40, "2")               # OrdType (Limit)
    msg.append_pair(44, "150.50")          # Price
    msg.append_pair(38, "100")             # OrderQty
    
    # Convert to bytes for parsing
    msg_bytes = msg.encode()
    
    logger.info(f"Created FIX message: {msg_bytes}")
    
    try:
        # Parse the message
        if await parser.validate(msg_bytes):
            result = await parser.parse(msg_bytes)
            logger.info(f"Successfully parsed message: {result}")
            logger.info(f"Message type: {result.__class__.__name__}")
            logger.info(f"ClOrdID: {result.ClOrdID}")
            logger.info(f"Symbol: {result.Instrument.Symbol if result.Instrument else 'No instrument'}")
            
            # Serialize to dict
            data = result.model_dump()
            logger.info(f"Model dump: {str(data)[:100]}...")
            
            return True
        else:
            logger.error("Message validation failed")
            return False
    except Exception as e:
        logger.error(f"Error parsing message: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

async def test_bid_response_parser():
    """Test parsing a BidResponse FIX message."""
    # Create a FIX parser
    parser = FIXParser()
    
    # Create a simplefix message
    msg = simplefix.FixMessage()
    msg.append_pair(8, "FIX.4.4")  # BeginString
    msg.append_pair(9, "100")      # BodyLength (placeholder)
    msg.append_pair(35, "l")       # MsgType = BidResponse
    msg.append_pair(49, "SENDER")  # SenderCompID
    msg.append_pair(56, "TARGET")  # TargetCompID
    msg.append_pair(34, "1")       # MsgSeqNum
    msg.append_pair(52, datetime.now().strftime("%Y%m%d-%H:%M:%S.%f"))  # SendingTime
    
    # Add BidResponse specific fields
    msg.append_pair(390, "BID123")        # BidID
    msg.append_pair(391, "CLIENT456")     # ClientBidID
    msg.append_pair(66, "LIST789")        # ListID
    msg.append_pair(420, "1")             # NoBidComponents
    
    # Add component fields
    msg.append_pair(12, "0.25")           # Commission
    msg.append_pair(13, "3")              # CommType (Absolute)
    msg.append_pair(54, "1")              # Side (Buy)
    msg.append_pair(44, "120.75")         # Price
    
    # Convert to bytes for parsing
    msg_bytes = msg.encode()
    
    logger.info(f"Created FIX message: {msg_bytes}")
    
    try:
        # Parse the message
        if await parser.validate(msg_bytes):
            result = await parser.parse(msg_bytes)
            logger.info(f"Successfully parsed message: {result}")
            logger.info(f"Message type: {result.__class__.__name__}")
            logger.info(f"BidID: {result.BidID}")
            
            # Check components
            if hasattr(result, 'CommissionData') and result.CommissionData:
                logger.info(f"Commission: {result.CommissionData.Commission}")
            
            if hasattr(result, 'BidCompRspGrp') and result.BidCompRspGrp:
                logger.info(f"Number of bid components: {result.BidCompRspGrp.NoBidComponents}")
                if result.BidCompRspGrp.NoBidComponents_items:
                    for i, comp in enumerate(result.BidCompRspGrp.NoBidComponents_items):
                        logger.info(f"Component {i+1}: {comp}")
            
            # Serialize to dict
            data = result.model_dump()
            logger.info(f"Model dump: {str(data)[:100]}...")
            
            return True
        else:
            logger.error("Message validation failed")
            return False
    except Exception as e:
        logger.error(f"Error parsing message: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

async def main():
    """Run all tests."""
    logger.info("Starting FIX parser tests...")
    
    # Test NewOrderSingle parser
    logger.info("\n=== Testing NewOrderSingle parser ===")
    new_order_result = await test_new_order_single_parser()
    
    # Test BidResponse parser
    logger.info("\n=== Testing BidResponse parser ===")
    bid_response_result = await test_bid_response_parser()
    
    # Report results
    logger.info("\n=== Test Results ===")
    logger.info(f"NewOrderSingle parser test: {'PASSED' if new_order_result else 'FAILED'}")
    logger.info(f"BidResponse parser test: {'PASSED' if bid_response_result else 'FAILED'}")
    
    if new_order_result and bid_response_result:
        logger.info("All tests passed!")
    else:
        logger.error("Some tests failed.")

if __name__ == "__main__":
    asyncio.run(main()) 