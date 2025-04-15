#!/usr/bin/env python3
"""
Simple FIX Message Example

This script demonstrates parsing a simple FIX message using the generated models.
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

def main():
    """Main function to demonstrate reading/parsing a simple FIX message."""
    # Import specific message class directly (avoiding circular imports)
    from src.models.generated.messages.heartbeat import HeartbeatMessage
    
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
    
    # Print the message
    logger.info(f"Created Heartbeat message:")
    logger.info(f"MsgType: {heartbeat.MsgType}")
    logger.info(f"SenderCompID: {heartbeat.SenderCompID}")
    logger.info(f"TargetCompID: {heartbeat.TargetCompID}")
    logger.info(f"TestReqID: {heartbeat.TestReqID}")
    
    # Convert to dictionary
    data = heartbeat.model_dump()
    logger.info(f"\nMessage as dictionary: {data}")

if __name__ == "__main__":
    main() 