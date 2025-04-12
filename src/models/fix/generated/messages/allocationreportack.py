"""
FIX 4.4 AllocationReportAck Message

This module contains the Pydantic model for the AllocationReportAck message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.allocackgrp import AllocAckGrp
from ..components.parties import Parties


class AllocationReportAck(TradeModel):
    """
    FIX 4.4 AllocationReportAck Message
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
    MsgType: Literal["AT"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    AllocReportID: str = Field(None, description='', alias='755')
    AllocID: str = Field(None, description='', alias='70')
    SecondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: datetime = Field(None, description='', alias='60')
    AllocStatus: int = Field(None, description='', alias='87')
    AllocRejCode: Optional[int] = Field(None, description='', alias='88')
    AllocReportType: Optional[int] = Field(None, description='', alias='794')
    AllocIntermedReqType: Optional[int] = Field(None, description='', alias='808')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    Product: Optional[int] = Field(None, description='', alias='460')
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[Parties] = None
    AllocAckGrp: Optional[AllocAckGrp] = None

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
