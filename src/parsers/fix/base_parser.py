"""
Base parser for FIX messages.

This module contains the base parser class for FIX message types.
"""
from typing import Dict, Any, Optional, Type
import simplefix
import logging
from datetime import datetime
from src.models.fix.generated.messages.base import FIXMessageBase

class FIXMessageParser:
    """Base class for FIX message type parsers."""
    
    def __init__(self):
        """Initialize the parser."""
        self.logger = logging.getLogger(__name__)

    async def parse(self, message: simplefix.FixMessage) -> FIXMessageBase:
        """
        Parse a FIX message into a model instance.
        
        Args:
            message (simplefix.FixMessage): The FIX message to parse
            
        Returns:
            FIXMessageBase: The parsed message model instance
            
        Raises:
            NotImplementedError: This method must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement parse()")

    async def validate(self, message: str | simplefix.FixMessage) -> bool:
        """
        Validate a FIX message.
        
        Args:
            message (Union[str, simplefix.FixMessage]): The FIX message to validate
            
        Returns:
            bool: True if the message is valid, False otherwise
        """
        try:
            if isinstance(message, str):
                parser = simplefix.FixParser()
                parser.append_buffer(message.encode())
                message = parser.get_message()
            
            if not message:
                self.logger.error("Invalid message format")
                return False
            
            msg_type = message.get(35)
            if not msg_type:
                self.logger.error("Missing message type (tag 35)")
                return False
                
            return True
        except Exception as e:
            self.logger.error(f"Error validating message: {str(e)}")
            return False

    async def _parse_common_fields(self, message: simplefix.FixMessage) -> Dict[str, Any]:
        """
        Parse common FIX message fields.
        
        Args:
            message (simplefix.FixMessage): The FIX message to parse
            
        Returns:
            Dict[str, Any]: Dictionary of common field values
        """
        common_fields = {
            8: 'BeginString',
            9: 'BodyLength',
            35: 'MsgType',
            49: 'SenderCompID',
            56: 'TargetCompID',
            34: 'MsgSeqNum',
            52: 'SendingTime',
            10: 'CheckSum'
        }
        
        result = {}
        for tag, field_name in common_fields.items():
            value = message.get(tag)
            if value is not None:
                if isinstance(value, bytes):
                    if tag == 52:  # SendingTime
                        try:
                            value = datetime.strptime(value.decode(), '%Y%m%d-%H:%M:%S.%f')
                        except ValueError:
                            try:
                                value = datetime.strptime(value.decode(), '%Y%m%d-%H:%M:%S')
                            except ValueError:
                                self.logger.warning(f"Could not parse SendingTime: {value}")
                                value = value.decode()
                    else:
                        value = value.decode()
                result[field_name] = value
        
        return result 