from abc import ABC, abstractmethod
from typing import Dict, Any
from ..models.base import TradeModel

class BaseParser(ABC):
    """
    Base parser interface that all format-specific parsers must implement.
    """
    
    @abstractmethod
    async def validate(self, message: str) -> bool:
        """
        Validate if the message is properly formatted according to the specific format.
        
        Args:
            message: The raw message string to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        pass
    
    @abstractmethod
    async def parse(self, message: str) -> TradeModel:
        """
        Parse the message into a standardized TradeModel.
        
        Args:
            message: The raw message string to parse
            
        Returns:
            TradeModel: The parsed message as a model
            
        Raises:
            ValueError: If the message is invalid or cannot be parsed
        """
        pass 