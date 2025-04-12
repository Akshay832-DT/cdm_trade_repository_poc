"""
FIX Message Models

This module contains Pydantic models for FIX messages.
It serves as a compatibility layer for the initial simplified 
implementation and the comprehensive generated models.
"""
from pydantic import BaseModel, Field
from typing import Dict, Optional, Any
from datetime import datetime
from ..base import TradeModel
from .base import FIXMessageBase

# This class is kept for backward compatibility
class FIXMessage(FIXMessageBase):
    """
    Generic FIX Message Model.
    
    This is a simplified representation that captures the essential header fields
    and stores all other fields in additional_fields.
    
    For a more comprehensive model that represents the full FIX 4.4 specification,
    use the generated models in the 'generated' package.
    """
    pass

    BeginString: Optional[str] = Field(None, alias='8')
    BodyLength: Optional[str] = Field(None, alias='9')
    MsgType: Optional[str] = Field(None, alias='35')
    SenderCompID: Optional[str] = Field(None, alias='49')
    TargetCompID: Optional[str] = Field(None, alias='56')
    MsgSeqNum: Optional[str] = Field(None, alias='34')
    SendingTime: Optional[datetime] = Field(None, alias='52')
    CheckSum: Optional[str] = Field(None, alias='10')
    
    # Additional fields will be stored in a dictionary
    additional_fields: Dict[str, str] = Field(default_factory=dict)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

    def to_json(self) -> dict:
        base_dict = self.model_dump(by_alias=True, exclude={'additional_fields'})
        base_dict.update(self.additional_fields)
        return base_dict 