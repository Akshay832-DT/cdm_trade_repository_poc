"""
FIX 4.4 TradingSessionStatus Message

This module contains the Pydantic model for the TradingSessionStatus message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *


class TradingSessionStatus(FIXMessageBase):
    """
    FIX 4.4 TradingSessionStatus Message
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
    msgType: Literal["h"] = Field("h", alias='35')
    
    # Message-specific fields
    tradSesReqID: Optional[str] = Field(None, description='', alias='335')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    tradSesMethod: Optional[int] = Field(None, description='', alias='338')
    tradSesMode: Optional[int] = Field(None, description='', alias='339')
    unsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    tradSesStatus: Optional[int] = Field(None, description='', alias='340')
    tradSesStatusRejReason: Optional[int] = Field(None, description='', alias='567')
    tradSesStartTime: Optional[datetime] = Field(None, description='', alias='341')
    tradSesOpenTime: Optional[datetime] = Field(None, description='', alias='342')
    tradSesPreCloseTime: Optional[datetime] = Field(None, description='', alias='343')
    tradSesCloseTime: Optional[datetime] = Field(None, description='', alias='344')
    tradSesEndTime: Optional[datetime] = Field(None, description='', alias='345')
    totalVolumeTraded: Optional[float] = Field(None, description='', alias='387')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')

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
