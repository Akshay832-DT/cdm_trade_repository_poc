"""
FIX 4.4 OrderCancelReject Message

This module contains the Pydantic model for the OrderCancelReject message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *


class OrderCancelReject(FIXMessageBase):
    """
    FIX 4.4 OrderCancelReject Message
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
    msgType: Literal["9"] = Field("9", alias='35')
    
    # Message-specific fields
    orderID: Optional[str] = Field(None, description='', alias='37')
    secondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    clOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    origClOrdID: Optional[str] = Field(None, description='', alias='41')
    ordStatus: Optional[str] = Field(None, description='', alias='39')
    workingIndicator: Optional[bool] = Field(None, description='', alias='636')
    origOrdModTime: Optional[datetime] = Field(None, description='', alias='586')
    listID: Optional[str] = Field(None, description='', alias='66')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    cxlRejResponseTo: Optional[str] = Field(None, description='', alias='434')
    cxlRejReason: Optional[int] = Field(None, description='', alias='102')
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
