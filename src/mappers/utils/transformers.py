"""
Utility functions for data transformations during mapping
"""
from typing import Dict, Any, List, Optional, Union, Callable, TypeVar
from datetime import datetime, date
import re
import decimal
from enum import Enum

T = TypeVar('T')

def transform_date(value: Any, format_str: Optional[str] = None, 
                  output_format: Optional[str] = None) -> Union[str, datetime, date, None]:
    """
    Transform a date value
    
    Args:
        value: Date value to transform
        format_str: Input format string for parsing
        output_format: Optional output format string
        
    Returns:
        Transformed date
    """
    if value is None:
        return None
    
    # If already a date/datetime, no parsing needed
    if isinstance(value, (date, datetime)):
        dt_obj = value
    else:
        # Try to parse the date
        try:
            if format_str:
                dt_obj = datetime.strptime(str(value), format_str)
            else:
                # Try common formats
                formats = [
                    '%Y%m%d', # 20210315
                    '%Y-%m-%d', # 2021-03-15
                    '%Y/%m/%d', # 2021/03/15
                    '%d/%m/%Y', # 15/03/2021
                    '%d-%m-%Y', # 15-03-2021
                    '%Y%m%d%H%M%S', # 20210315123045
                    '%Y-%m-%dT%H:%M:%S', # 2021-03-15T12:30:45
                    '%Y-%m-%dT%H:%M:%S.%f', # 2021-03-15T12:30:45.123
                    '%Y-%m-%dT%H:%M:%SZ', # 2021-03-15T12:30:45Z
                ]
                
                for fmt in formats:
                    try:
                        dt_obj = datetime.strptime(str(value), fmt)
                        break
                    except ValueError:
                        continue
                else:
                    # If no format matched, try dateutil parser as fallback
                    from dateutil import parser
                    dt_obj = parser.parse(str(value))
        except Exception as e:
            raise ValueError(f"Could not parse date: {value}, error: {str(e)}")
    
    # Return in requested format
    if output_format:
        return dt_obj.strftime(output_format)
    return dt_obj

def transform_enum(value: Any, mapping: Dict[str, Any], 
                  default: Optional[Any] = None) -> Any:
    """
    Transform a value using enum mapping
    
    Args:
        value: Value to transform
        mapping: Dictionary mapping input values to output values
        default: Default value if not found in mapping
        
    Returns:
        Transformed value
    """
    if value is None:
        return default
    
    str_value = str(value)
    return mapping.get(str_value, default)

def transform_bool(value: Any, true_values: Optional[List[str]] = None) -> bool:
    """
    Transform a value to boolean
    
    Args:
        value: Value to transform
        true_values: List of values that should be considered True
        
    Returns:
        Boolean value
    """
    if value is None:
        return False
    
    if isinstance(value, bool):
        return value
    
    if true_values is None:
        true_values = ['Y', 'YES', 'TRUE', '1', 'T', 'ON']
    
    return str(value).upper() in [v.upper() for v in true_values]

def transform_number(value: Any, decimal_places: Optional[int] = None,
                    allow_negative: bool = True) -> Union[int, float, decimal.Decimal, None]:
    """
    Transform a value to a number
    
    Args:
        value: Value to transform
        decimal_places: Number of decimal places to round to
        allow_negative: Whether to allow negative values
        
    Returns:
        Numeric value
    """
    if value is None:
        return None
    
    # Strip non-numeric characters (except decimal point and minus sign)
    if isinstance(value, str):
        # Keep only digits, decimal points, and minus signs
        value = re.sub(r'[^\d.-]', '', value)
        
        # Handle empty string
        if not value or value == '-' or value == '.':
            return 0
    
    try:
        # Convert to Decimal for precise handling
        num_value = decimal.Decimal(value)
        
        # Apply constraints
        if not allow_negative and num_value < 0:
            num_value = abs(num_value)
        
        if decimal_places is not None:
            num_value = round(num_value, decimal_places)
            
            # If decimal_places is 0, convert to int
            if decimal_places == 0:
                return int(num_value)
        
        # Convert to float for general use
        return float(num_value)
    except:
        return 0

def transform_string(value: Any, max_length: Optional[int] = None,
                    strip: bool = True, upper: bool = False, 
                    lower: bool = False) -> Optional[str]:
    """
    Transform a value to string with formatting options
    
    Args:
        value: Value to transform
        max_length: Maximum length of the string
        strip: Whether to strip whitespace
        upper: Convert to uppercase
        lower: Convert to lowercase
        
    Returns:
        Formatted string
    """
    if value is None:
        return None
    
    # Convert to string
    result = str(value)
    
    # Apply formatting
    if strip:
        result = result.strip()
    
    if upper:
        result = result.upper()
    
    if lower:
        result = result.lower()
    
    # Apply length constraint
    if max_length is not None and len(result) > max_length:
        result = result[:max_length]
    
    return result

def apply_transform_pipeline(value: Any, transformers: List[Dict[str, Any]]) -> Any:
    """
    Apply a pipeline of transformations to a value
    
    Args:
        value: Value to transform
        transformers: List of transformer configurations, each with:
            - type: Transformer type name
            - params: Parameters for the transformer
        
    Returns:
        Transformed value
    """
    result = value
    
    for transformer in transformers:
        transform_type = transformer.get('type')
        params = transformer.get('params', {})
        
        if transform_type == 'date':
            result = transform_date(
                result, 
                format_str=params.get('format'),
                output_format=params.get('output_format')
            )
        elif transform_type == 'enum':
            result = transform_enum(
                result,
                mapping=params.get('mapping', {}),
                default=params.get('default')
            )
        elif transform_type == 'bool':
            result = transform_bool(
                result,
                true_values=params.get('true_values')
            )
        elif transform_type == 'number':
            result = transform_number(
                result,
                decimal_places=params.get('decimal_places'),
                allow_negative=params.get('allow_negative', True)
            )
        elif transform_type == 'string':
            result = transform_string(
                result,
                max_length=params.get('max_length'),
                strip=params.get('strip', True),
                upper=params.get('upper', False),
                lower=params.get('lower', False)
            )
        # Add more transformer types as needed
    
    return result

def combine_values(values: List[Any], separator: str = ' ') -> str:
    """
    Combine multiple values into a single string
    
    Args:
        values: List of values to combine
        separator: Separator string
        
    Returns:
        Combined string
    """
    # Filter out None values
    filtered_values = [str(v) for v in values if v is not None]
    return separator.join(filtered_values) 