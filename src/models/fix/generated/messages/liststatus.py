"""
FIX 4.4 ListStatus Message

This module contains the Pydantic model for the ListStatus message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.ordliststatgrp import OrdListStatGrp


class ListStatus(TradeModel):
    """
    FIX 4.4 ListStatus Message
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
    MsgType: Literal["N"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    ListID: str = Field(None, description='', alias='66')
    ListStatusType: int = Field(None, description='', alias='429')
    NoRpts: int = Field(None, description='', alias='82')
    ListOrderStatus: int = Field(None, description='', alias='431')
    RptSeq: int = Field(None, description='', alias='83')
    ListStatusText: Optional[str] = Field(None, description='', alias='444')
    EncodedListStatusTextLen: Optional[int] = Field(None, description='', alias='445')
    EncodedListStatusText: Optional[str] = Field(None, description='', alias='446')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    TotNoOrders: int = Field(None, description='', alias='68')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    OrdListStatGrp: OrdListStatGrp = Field(..., description='OrdListStatGrp component')

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
