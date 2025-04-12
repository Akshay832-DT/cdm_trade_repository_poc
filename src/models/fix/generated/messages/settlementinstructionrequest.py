"""
FIX 4.4 SettlementInstructionRequest Message

This module contains the Pydantic model for the SettlementInstructionRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.parties import Parties


class SettlementInstructionRequest(FIXMessageBase):
    """
    FIX 4.4 SettlementInstructionRequest Message
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
    msgType: Literal["AV"] = Field("AV", alias='35')
    
    # Message-specific fields
    settlInstReqID: Optional[str] = Field(None, description='', alias='791')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    allocAccount: Optional[str] = Field(None, description='', alias='79')
    allocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    side: Optional[str] = Field(None, description='', alias='54')
    product: Optional[int] = Field(None, description='', alias='460')
    securityType: Optional[str] = Field(None, description='', alias='167')
    cFICode: Optional[str] = Field(None, description='', alias='461')
    effectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    lastUpdateTime: Optional[datetime] = Field(None, description='', alias='779')
    standInstDbType: Optional[int] = Field(None, description='', alias='169')
    standInstDbName: Optional[str] = Field(None, description='', alias='170')
    standInstDbID: Optional[str] = Field(None, description='', alias='171')
    parties: Optional[Parties] = Field(None, description='Parties component')

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
