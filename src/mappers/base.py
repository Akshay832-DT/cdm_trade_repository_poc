from abc import ABC, abstractmethod
import yaml
from typing import Dict, Any, Type, Optional, List, Set
from pydantic import BaseModel
import os
import logging
from pathlib import Path

class MappingStats:
    """
    Class to track mapping statistics
    """
    
    def __init__(self):
        self.mapped_fields: Set[str] = set()
        self.unmapped_fields: Set[str] = set()
        self.total_source_fields: int = 0
        self.total_target_fields: int = 0
    
    def add_mapped_field(self, source_field: str):
        """Add a successfully mapped field"""
        self.mapped_fields.add(source_field)
    
    def add_unmapped_field(self, source_field: str):
        """Add a field that couldn't be mapped"""
        self.unmapped_fields.add(source_field)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get mapping statistics as dictionary"""
        coverage = 0
        if self.total_source_fields > 0:
            coverage = (len(self.mapped_fields) / self.total_source_fields) * 100
            
        return {
            "mapped_fields": sorted(list(self.mapped_fields)),
            "unmapped_fields": sorted(list(self.unmapped_fields)),
            "total_source_fields": self.total_source_fields,
            "total_target_fields": self.total_target_fields,
            "coverage_percentage": coverage
        }

class BaseMapper(ABC):
    """
    Base mapper interface for mapping between different data models
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the mapper with optional configuration file
        
        Args:
            config_file: Path to YAML configuration file
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.stats = MappingStats()
        self.config = {}
        
        if config_file:
            self.config = self.load_config(config_file)
    
    @abstractmethod
    def map(self, source_obj: BaseModel) -> BaseModel:
        """
        Map source object to target object
        
        Args:
            source_obj: Source object to map from
            
        Returns:
            Mapped target object
        """
        pass
    
    def get_mapping_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the mapping process
        
        Returns:
            Dict with mapping statistics
        """
        return self.stats.get_stats()
    
    @classmethod
    def load_config(cls, config_path: str) -> Dict[str, Any]:
        """
        Load mapping configuration from YAML file
        
        Args:
            config_path: Path to YAML configuration file
            
        Returns:
            Dict with mapping configuration
        """
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            logging.error(f"Error loading config file {config_path}: {str(e)}")
            return {}
    
    def apply_field_mapping(self, source_obj: BaseModel, target_obj: BaseModel,
                           source_field: str, target_field: str,
                           transformer: Optional[str] = None,
                           transformer_params: Optional[Dict[str, Any]] = None) -> bool:
        """
        Apply a single field mapping from source to target object
        
        Args:
            source_obj: Source object to map from
            target_obj: Target object to map to
            source_field: Field path in source object
            target_field: Field path in target object
            transformer: Optional transformer to apply to the value
            transformer_params: Optional parameters for the transformer
            
        Returns:
            bool: True if mapping was successful, False otherwise
        """
        try:
            # Get source value (handle nested paths with dots)
            source_value = self._get_nested_attr(source_obj, source_field)
            
            if source_value is None:
                self.stats.add_unmapped_field(source_field)
                return False
            
            # Transform value if needed
            if transformer:
                transformed_value = self._apply_transformer(
                    source_value, transformer, transformer_params
                )
            else:
                transformed_value = source_value
            
            # Set target value (handle nested paths with dots)
            self._set_nested_attr(target_obj, target_field, transformed_value)
            
            self.stats.add_mapped_field(source_field)
            return True
        except Exception as e:
            self.logger.error(f"Error mapping {source_field} to {target_field}: {str(e)}")
            self.stats.add_unmapped_field(source_field)
            return False
    
    def _get_nested_attr(self, obj: Any, attr_path: str) -> Any:
        """
        Get nested attribute value from an object using dot notation
        
        Args:
            obj: Object to get attribute from
            attr_path: Attribute path in dot notation (e.g. 'a.b.c')
            
        Returns:
            Attribute value or None if not found
        """
        current = obj
        
        # Handle array indexing in path (e.g. 'a[0].b')
        for part in attr_path.split('.'):
            if '[' in part and ']' in part:
                # Parse array index
                idx_start = part.index('[')
                idx_end = part.index(']')
                array_name = part[:idx_start]
                index = int(part[idx_start+1:idx_end])
                
                # Get array and element
                if hasattr(current, array_name):
                    array = getattr(current, array_name, None)
                    if array is not None and len(array) > index:
                        current = array[index]
                    else:
                        return None
                else:
                    return None
            else:
                # Regular attribute access
                current = getattr(current, part, None)
                if current is None:
                    return None
        
        return current
    
    def _set_nested_attr(self, obj: Any, attr_path: str, value: Any) -> None:
        """
        Set nested attribute value on an object using dot notation
        
        Args:
            obj: Object to set attribute on
            attr_path: Attribute path in dot notation (e.g. 'a.b.c')
            value: Value to set
        """
        parts = attr_path.split('.')
        current = obj
        
        # Navigate to the second-to-last part to set the attribute
        for i, part in enumerate(parts[:-1]):
            if '[' in part and ']' in part:
                # Parse array index
                idx_start = part.index('[')
                idx_end = part.index(']')
                array_name = part[:idx_start]
                index = int(part[idx_start+1:idx_end])
                
                # Get or create array
                if not hasattr(current, array_name):
                    setattr(current, array_name, [])
                
                array = getattr(current, array_name)
                
                # Ensure array has enough elements
                while len(array) <= index:
                    array.append(None)
                
                # Get or create element
                if array[index] is None:
                    # Determine type to create
                    next_part = parts[i+1] if i+1 < len(parts) else None
                    if next_part and '[' in next_part:
                        # If next part is an array, create a container object
                        array[index] = type('DynamicObject', (), {})
                    else:
                        array[index] = type('DynamicObject', (), {})
                
                current = array[index]
            else:
                # Regular attribute access
                if not hasattr(current, part):
                    setattr(current, part, type('DynamicObject', (), {}))
                current = getattr(current, part)
        
        # Set the final attribute
        last_part = parts[-1]
        if '[' in last_part and ']' in last_part:
            # Parse array index
            idx_start = last_part.index('[')
            idx_end = last_part.index(']')
            array_name = last_part[:idx_start]
            index = int(last_part[idx_start+1:idx_end])
            
            # Get or create array
            if not hasattr(current, array_name):
                setattr(current, array_name, [])
            
            array = getattr(current, array_name)
            
            # Ensure array has enough elements
            while len(array) <= index:
                array.append(None)
            
            # Set element
            array[index] = value
        else:
            # Regular attribute setting
            setattr(current, last_part, value)
    
    def _apply_transformer(self, value: Any, transformer: str, 
                          params: Optional[Dict[str, Any]] = None) -> Any:
        """
        Apply a transformer to a value
        
        Args:
            value: Value to transform
            transformer: Transformer name
            params: Optional transformer parameters
            
        Returns:
            Transformed value
        """
        if params is None:
            params = {}
            
        if transformer == 'direct':
            return value
        elif transformer == 'date_format':
            return self._transform_date(value, params.get('format', None))
        elif transformer == 'enum_map':
            mappings = params.get('mappings', {})
            return mappings.get(str(value), mappings.get('default', value))
        elif transformer == 'bool_transform':
            true_values = params.get('true_values', ['Y', 'YES', 'TRUE', '1'])
            return value in true_values
        elif transformer == 'number_transform':
            return float(value)
        elif transformer == 'string_transform':
            return str(value)
        elif transformer == 'custom':
            # Custom transformers should be implemented in subclasses
            raise NotImplementedError("Custom transformer must be implemented in a subclass")
        else:
            self.logger.warning(f"Unknown transformer: {transformer}")
            return value
    
    def _transform_date(self, value: Any, date_format: Optional[str] = None) -> Any:
        """
        Transform date values based on format
        
        Args:
            value: Date value to transform
            date_format: Optional date format
            
        Returns:
            Transformed date
        """
        import datetime
        from dateutil import parser
        
        if isinstance(value, (datetime.date, datetime.datetime)):
            return value
            
        try:
            if date_format:
                return datetime.datetime.strptime(value, date_format)
            else:
                return parser.parse(value)
        except:
            self.logger.error(f"Error parsing date: {value}")
            return value 