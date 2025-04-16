from typing import Dict, Type, Any, Optional, List
from pydantic import BaseModel
import importlib
import logging
import os
from pathlib import Path
from .base import BaseMapper

class MapperController:
    """
    Controller for selecting and using appropriate mappers
    """
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Will be populated dynamically
        self.fix_mappers: Dict[str, Type[BaseMapper]] = {}
        self.fpml_mappers: Dict[str, Type[BaseMapper]] = {}
        
        # Initialize mappers
        self._initialize_mappers()
    
    def _initialize_mappers(self):
        """
        Dynamically discover and initialize mappers
        """
        # Import fix mappers
        try:
            from .fix import mappers as fix_mappers
            for name, mapper in fix_mappers.items():
                self.fix_mappers[name] = mapper
        except (ImportError, AttributeError) as e:
            self.logger.warning(f"Failed to import FIX mappers: {str(e)}")
        
        # Import fpml mappers
        try:
            from .fpml import mappers as fpml_mappers
            for name, mapper in fpml_mappers.items():
                self.fpml_mappers[name] = mapper
        except (ImportError, AttributeError) as e:
            self.logger.warning(f"Failed to import FPML mappers: {str(e)}")
    
    def get_fix_mapper(self, message_type: str) -> Optional[BaseMapper]:
        """
        Get appropriate FIX mapper based on message type
        
        Args:
            message_type: FIX message type
            
        Returns:
            Appropriate mapper instance or None if not found
        """
        if message_type in self.fix_mappers:
            try:
                return self.fix_mappers[message_type]()
            except Exception as e:
                self.logger.error(f"Error creating FIX mapper for {message_type}: {str(e)}")
                return None
        else:
            self.logger.warning(f"No mapper available for FIX message type: {message_type}")
            return None
    
    def get_fpml_mapper(self, trade_type: str) -> Optional[BaseMapper]:
        """
        Get appropriate FPML mapper based on trade type
        
        Args:
            trade_type: FPML trade type
            
        Returns:
            Appropriate mapper instance or None if not found
        """
        if trade_type in self.fpml_mappers:
            try:
                return self.fpml_mappers[trade_type]()
            except Exception as e:
                self.logger.error(f"Error creating FPML mapper for {trade_type}: {str(e)}")
                return None
        else:
            self.logger.warning(f"No mapper available for FPML trade type: {trade_type}")
            return None
    
    def map_fix_to_cdm(self, fix_message: BaseModel) -> Optional[BaseModel]:
        """
        Map a FIX message to CDM object
        
        Args:
            fix_message: FIX message to map
            
        Returns:
            Mapped CDM object or None if mapping failed
        """
        # Get message type from FIX message
        message_type = self._get_fix_message_type(fix_message)
        if not message_type:
            self.logger.error("Could not determine FIX message type")
            return None
        
        # Get appropriate mapper
        mapper = self.get_fix_mapper(message_type)
        if not mapper:
            return None
        
        # Map and return result
        try:
            return mapper.map(fix_message)
        except Exception as e:
            self.logger.error(f"Error mapping FIX {message_type} to CDM: {str(e)}")
            return None
    
    def map_fpml_to_cdm(self, fpml_obj: BaseModel) -> Optional[BaseModel]:
        """
        Map an FPML object to CDM object
        
        Args:
            fpml_obj: FPML object to map
            
        Returns:
            Mapped CDM object or None if mapping failed
        """
        # Get type from FPML object
        trade_type = self._get_fpml_type(fpml_obj)
        if not trade_type:
            self.logger.error("Could not determine FPML type")
            return None
        
        # Get appropriate mapper
        mapper = self.get_fpml_mapper(trade_type)
        if not mapper:
            return None
        
        # Map and return result
        try:
            return mapper.map(fpml_obj)
        except Exception as e:
            self.logger.error(f"Error mapping FPML {trade_type} to CDM: {str(e)}")
            return None
    
    def _get_fix_message_type(self, fix_message: BaseModel) -> Optional[str]:
        """
        Get message type from FIX message object
        
        Args:
            fix_message: FIX message object
            
        Returns:
            Message type string or None if not found
        """
        # Check class name first
        class_name = fix_message.__class__.__name__
        if class_name in self.fix_mappers:
            return class_name
        
        # Look for msgType attribute
        msg_type = getattr(fix_message, 'msgType', None)
        if msg_type:
            # Convert FIX message type code to class name
            # This mapping should be defined somewhere in the application
            msg_type_map = {
                # Common FIX message types
                '8': 'ExecutionReport',
                'D': 'NewOrderSingle',
                'AE': 'TradeCaptureReport',
                # Add more as needed
            }
            return msg_type_map.get(msg_type, None)
        
        return None
    
    def _get_fpml_type(self, fpml_obj: BaseModel) -> Optional[str]:
        """
        Get type from FPML object
        
        Args:
            fpml_obj: FPML object
            
        Returns:
            Type string or None if not found
        """
        # Check class name
        class_name = fpml_obj.__class__.__name__
        if class_name in self.fpml_mappers:
            return class_name
        
        # You might need to implement more complex type detection logic here
        # based on the structure of your FPML objects
        
        return None
    
    def get_all_mappers(self) -> Dict[str, List[str]]:
        """
        Get all available mappers
        
        Returns:
            Dict with mapper types and available mappers
        """
        return {
            'FIX': list(self.fix_mappers.keys()),
            'FPML': list(self.fpml_mappers.keys())
        } 