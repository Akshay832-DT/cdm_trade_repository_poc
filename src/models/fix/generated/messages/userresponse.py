"""
FIX 4.4 UserResponse Message

This module contains the Pydantic model for the UserResponse message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *


class UserResponse(FIXMessageBase):
    """
    FIX 4.4 UserResponse Message
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    # Set the message type for this message
    msgType: Literal["BF"] = Field("BF", alias='35')
    
    # Message-specific fields
    userRequestID: Optional[str] = Field(None, description='', alias='923')
    username: Optional[str] = Field(None, description='', alias='553')
    userStatus: Optional[int] = Field(None, description='', alias='926')
    userStatusText: Optional[str] = Field(None, description='', alias='927')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
