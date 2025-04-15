"""
Parser for ISDA CDM JSON messages.
"""
import json
import logging
from typing import Any, Dict, List, Optional, Union
import importlib

from src.models.cdm.generated.base.base import CdmModelBase

logger = logging.getLogger(__name__)

class CdmParser:
    """Parser for ISDA CDM JSON messages."""
    
    def __init__(self):
        """Initialize the CDM parser."""
        self.model_mapping = {
            # Map message types to model classes
            # These will need to be updated based on actual message types
            "TradableProduct": "src.models.cdm.generated.product.template.tradable_product.TradableProduct",
            "TransferableProduct": "src.models.cdm.generated.product.template.transferable_product.TransferableProduct",
            "NonTransferableProduct": "src.models.cdm.generated.product.template.non_transferable_product.NonTransferableProduct",
            "Product": "src.models.cdm.generated.product.template.product.Product"
        }
    
    async def validate(self, message: str) -> bool:
        """Validate a CDM JSON message.
        
        Args:
            message: CDM message string in JSON format
            
        Returns:
            True if valid, False otherwise
        """
        try:
            # Parse the JSON message
            data = json.loads(message)
            
            # Determine message type
            message_type = self._determine_message_type(data)
            
            # Get model class
            model_class = self._get_model_class(message_type)
            
            # Validate by parsing
            model_class.model_validate(data)
            
            return True
        except Exception as e:
            logger.error(f"Validation error: {str(e)}")
            return False
    
    async def parse(self, message: str) -> Optional[CdmModelBase]:
        """Parse a CDM JSON message into a model.
        
        Args:
            message: CDM message string in JSON format
            
        Returns:
            Parsed CDM model object or None if parsing fails
        """
        try:
            # Parse the JSON message
            data = json.loads(message)
            
            # Determine message type
            message_type = self._determine_message_type(data)
            
            # Get model class
            model_class = self._get_model_class(message_type)
            
            # Parse using model class
            return model_class.model_validate(data)
        except Exception as e:
            logger.error(f"Parsing error: {str(e)}")
            return None
    
    def _determine_message_type(self, data: Dict[str, Any]) -> str:
        """Determine the type of a CDM message.
        
        Args:
            data: Parsed JSON data
            
        Returns:
            Message type string
            
        Raises:
            ValueError: If message type cannot be determined
        """
        # Look for key identifiers in the message
        # This will need to be updated based on CDM message structure
        if "TradableProduct" in data:
            return "TradableProduct"
        elif "TransferableProduct" in data.get("product", {}):
            return "TransferableProduct"
        elif "NonTransferableProduct" in data.get("product", {}):
            return "NonTransferableProduct"
        elif "product" in data:
            return "Product"
        
        # If no known type is found, look for any key that might be a type
        for key in data.keys():
            if key[0].isupper() and key in self.model_mapping:
                return key
        
        # If we can't determine type, raise an error
        raise ValueError("Unable to determine CDM message type")
    
    def _get_model_class(self, message_type: str) -> Any:
        """Get the model class for a message type.
        
        Args:
            message_type: Message type string
            
        Returns:
            Model class
            
        Raises:
            ImportError: If model class cannot be imported
            KeyError: If message type is not in model mapping
        """
        if message_type not in self.model_mapping:
            raise KeyError(f"No model mapping found for message type: {message_type}")
        
        # Get module path and class name
        module_path = self.model_mapping[message_type]
        
        # Split into module path and class name
        module_parts = module_path.split(".")
        class_name = module_parts[-1]
        module_path = ".".join(module_parts[:-1])
        
        # Import module and get class
        try:
            module = importlib.import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Error importing model class for {message_type}: {str(e)}") 