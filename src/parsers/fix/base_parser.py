"""
Base parser for FIX messages.

This module contains the base parser class for FIX message types.
"""
from typing import Dict, Any, Optional, Type
import simplefix
import logging
from datetime import datetime, date
from abc import ABC, abstractmethod
from src.models.fix.generated.base.base import FIXMessageBase

class FIXMessageParser(ABC):
    """Base class for FIX message parsers."""
    
    def __init__(self):
        """Initialize the parser."""
        self.logger = logging.getLogger(__name__)

    @abstractmethod
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
    
    def _parse_date(self, value: str) -> date:
        """
        Parse a date string into a date object.
        
        Args:
            value (str): The date string to parse (format: YYYYMMDD)
            
        Returns:
            date: The parsed date
        """
        try:
            return datetime.strptime(value, "%Y%m%d").date()
        except ValueError as e:
            self.logger.error(f"Error parsing date {value}: {e}")
            raise
    
    def _parse_datetime(self, value: str) -> datetime:
        """
        Parse a datetime string into a datetime object.
        
        Args:
            value (str): The datetime string to parse (format: YYYYMMDD-HH:MM:SS)
            
        Returns:
            datetime: The parsed datetime
        """
        try:
            return datetime.strptime(value, "%Y%m%d-%H:%M:%S")
        except ValueError as e:
            self.logger.error(f"Error parsing datetime {value}: {e}")
            raise 