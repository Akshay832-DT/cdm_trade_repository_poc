#!/usr/bin/env python3
"""
Simple FIX Message Example - Direct Import

This script demonstrates a simple FIX heartbeat message using direct imports.
"""
import sys
import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import specific base class and message directly
from src.models.generated.messages.base import FIXMessageBase
from pydantic import Field, BaseModel, ConfigDict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define a minimal Heartbeat message class directly
class HeartbeatMessage(FIXMessageBase):
    """FIX Heartbeat Message"""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    MsgType: str = Field("0", description="Message Type", alias="35")
    TestReqID: Optional[str] = Field(None, description="Test Request ID", alias="112")

def main():
    """Main function to demonstrate a simple FIX heartbeat message."""
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