"""
FIX Base Models

This module contains base models for all FIX messages.
"""
from datetime import datetime
from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..base import TradeModel

class FIXMessageBase(TradeModel):
    """
    Base class for all FIX messages.
    
    This includes common header and trailer fields.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )

    BeginString: Literal["FIX.4.4"] = Field("FIX.4.4", alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: str = Field(..., alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    CheckSum: Optional[str] = Field(None, alias='10')
    
    # Additional fields will be stored in a dictionary
    additional_fields: Dict[str, Any] = Field(default_factory=dict)

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """
        Convert the message to a dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the message
        """
        # Get base fields
        data = super().model_dump(**kwargs)
        # Add additional fields
        if self.additional_fields:
            data.update(self.additional_fields)
        return {k: v for k, v in data.items() if v is not None} 