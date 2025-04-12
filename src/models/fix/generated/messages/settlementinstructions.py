"""
FIX 4.4 SettlementInstructions Message

This module contains the Pydantic model for the SettlementInstructions message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.settlinstgrp import SettlInstGrp


class SettlementInstructions(FIXMessageBase):
    """
    FIX 4.4 SettlementInstructions Message
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
    msgType: Literal["T"] = Field("T", alias='35')
    
    # Message-specific fields
    settlInstMsgID: Optional[str] = Field(None, description='', alias='777')
    settlInstReqID: Optional[str] = Field(None, description='', alias='791')
    settlInstMode: Optional[str] = Field(None, description='', alias='160')
    settlInstReqRejCode: Optional[int] = Field(None, description='', alias='792')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    settlInstGrp: Optional[SettlInstGrp] = Field(None, description='SettlInstGrp component')

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
