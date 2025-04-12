"""
FIX 4.4 OrderCancelReject Message

This module contains the Pydantic model for the OrderCancelReject message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class OrderCancelReject(TradeModel):
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
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["9"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    OrderID: str = Field(None, description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ClOrdID: str = Field(None, description='', alias='11')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    OrigClOrdID: str = Field(None, description='', alias='41')
    OrdStatus: str = Field(None, description='', alias='39')
    WorkingIndicator: Optional[bool] = Field(None, description='', alias='636')
    OrigOrdModTime: Optional[datetime] = Field(None, description='', alias='586')
    ListID: Optional[str] = Field(None, description='', alias='66')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    CxlRejResponseTo: str = Field(None, description='', alias='434')
    CxlRejReason: Optional[int] = Field(None, description='', alias='102')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"No{field_name[:-1]}"  # Remove 's' from plural
                if no_field in self.__fields__:
                    data[no_field] = len(value)
        
        return {k: v for k, v in data.items() if v is not None and (not isinstance(v, list) or v)}
