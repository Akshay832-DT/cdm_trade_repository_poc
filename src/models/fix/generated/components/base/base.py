"""
Base class for FIX component models.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Dict, Any, Optional
from datetime import datetime, date, time

class FIXComponentBase(BaseModel):
    """Base class for all FIX component models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    # Additional fields dictionary
    additional_fields: Dict[str, Any] = Field(default_factory=dict)
    
    def model_dump(self, *args, **kwargs):
        """Convert the component to a dictionary."""
        data = super().model_dump(*args, **kwargs)
        # Process nested components and groups
        for key, value in data.items():
            if hasattr(value, 'model_dump'):
                data[key] = value.model_dump(*args, **kwargs)
            elif isinstance(value, list) and value and hasattr(value[0], 'model_dump'):
                data[key] = [item.model_dump(*args, **kwargs) for item in value]
        return data
        
    def __str__(self):
        return f"{self.__class__.__name__}()"
