"""
FIX Message Parser

This module contains the main parser for FIX messages.
"""
import logging
from typing import Dict, Any, Type, Union
import simplefix
from pathlib import Path

from src.models.fix.generated.base.base import FIXMessageBase
from src.parsers.fix.base_parser import FIXMessageParser
from src.parsers.fix.message_parsers.bid_response_parser import BidResponseParser
from src.parsers.fix.message_parsers.new_order_single_parser import NewOrderSingleParser
from src.parsers.base import BaseParser

class FIXParser(BaseParser):
    """Main parser for FIX messages."""
    
    def __init__(self):
        """Initialize the parser."""
        self.logger = logging.getLogger(__name__)
        self.message_parsers = self._load_message_parsers()
        
    def _load_message_parsers(self) -> Dict[str, FIXMessageParser]:
        """
        Load message-specific parsers.
        
        Returns:
            Dict[str, FIXMessageParser]: Dictionary mapping message types to their parsers
        """
        # Map message types to their parsers
        # Use the MsgType value (FIX tag 35) as the key
        return {
            'l': BidResponseParser(),     # BidResponse - MsgType: l
            'D': NewOrderSingleParser()   # NewOrderSingle - MsgType: D
        }
        
    def _parse_fields(self, message: simplefix.FixMessage) -> Dict[str, Any]:
        """
        Parse fields from a FIX message into a dictionary.
        
        Args:
            message (simplefix.FixMessage): The FIX message to parse
            
        Returns:
            Dict[str, Any]: Dictionary mapping tag numbers to their values
        """
        fields = {}
        for tag, value in message.pairs:
            if value is not None:
                # Convert tag to integer for consistent lookup
                tag_int = int(tag)
                # Decode bytes to string if necessary
                if isinstance(value, bytes):
                    value = value.decode()
                fields[tag_int] = value
        return fields
        
    async def validate(self, message: Union[str, bytes, simplefix.FixMessage]) -> bool:
        """
        Validate a FIX message.
        
        Args:
            message (Union[str, bytes, simplefix.FixMessage]): The FIX message to validate
            
        Returns:
            bool: True if the message is valid, False otherwise
        """
        try:
            if isinstance(message, (str, bytes)):
                parser = simplefix.FixParser()
                if isinstance(message, str):
                    message = message.encode()
                parser.append_buffer(message)
                message = parser.get_message()
                
            if not message:
                self.logger.error("Invalid message format")
                return False
                
            msg_type = message.get(35)
            if not msg_type:
                self.logger.error("Missing message type (tag 35)")
                return False
                
            msg_type = msg_type.decode() if isinstance(msg_type, bytes) else msg_type
            if msg_type not in self.message_parsers:
                self.logger.warning(f"Unsupported message type: {msg_type}")
                return False
                
            return True
        except Exception as e:
            self.logger.error(f"Error validating message: {e}")
            return False
            
    async def parse(self, message: Union[str, bytes, simplefix.FixMessage]) -> FIXMessageBase:
        """
        Parse a FIX message.
        
        Args:
            message (Union[str, bytes, simplefix.FixMessage]): The FIX message to parse
            
        Returns:
            FIXMessageBase: The parsed message model instance
            
        Raises:
            ValueError: If the message type is not supported
        """
        try:
            if isinstance(message, (str, bytes)):
                parser = simplefix.FixParser()
                if isinstance(message, str):
                    message = message.encode()
                parser.append_buffer(message)
                message = parser.get_message()
                
            if not message:
                raise ValueError("Invalid message format")
                
            msg_type = message.get(35)
            if not msg_type:
                raise ValueError("Missing message type (tag 35)")
                
            msg_type = msg_type.decode() if isinstance(msg_type, bytes) else msg_type
            if msg_type not in self.message_parsers:
                raise ValueError(f"Unsupported message type: {msg_type}")
                
            parser = self.message_parsers[msg_type]
            return await parser.parse(message)
            
        except Exception as e:
            self.logger.error(f"Error parsing message: {e}")
            raise