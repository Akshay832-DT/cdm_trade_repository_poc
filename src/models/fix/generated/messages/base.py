"""
Base class for FIX message models.
"""
from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import Dict, Any, Optional, List, ForwardRef, TYPE_CHECKING
from datetime import datetime, date, time

class FIXMessageBase(BaseModel):
    """Base class for all FIX message models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    # Standard FIX header fields
    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: str = Field(..., description='', alias='52')
    
    # Standard FIX trailer fields
    CheckSum: Optional[str] = Field(None, description='', alias='10')
    
    # Additional fields dictionary
    additional_fields: Dict[str, Any] = Field(default_factory=dict)
    
    def model_dump(self, *args, **kwargs):
        """Convert the message to a dictionary."""
        data = super().model_dump(*args, **kwargs)
        # Process nested components and groups
        for key, value in data.items():
            if hasattr(value, 'model_dump'):
                data[key] = value.model_dump(*args, **kwargs)
            elif isinstance(value, list) and value and hasattr(value[0], 'model_dump'):
                data[key] = [item.model_dump(*args, **kwargs) for item in value]
        return data
        
    def __str__(self):
        return f"{self.__class__.__name__}({self.MsgType})"
