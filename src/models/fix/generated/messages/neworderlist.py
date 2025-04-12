"""
FIX 4.4 NewOrderList Message

This module contains the Pydantic model for the NewOrderList message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.listordgrp import ListOrdGrp


class NewOrderList(TradeModel):
    """
    FIX 4.4 NewOrderList Message
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
    MsgType: Literal["E"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    ListID: str = Field(None, description='', alias='66')
    BidID: Optional[str] = Field(None, description='', alias='390')
    ClientBidID: Optional[str] = Field(None, description='', alias='391')
    ProgRptReqs: Optional[int] = Field(None, description='', alias='414')
    BidType: int = Field(None, description='', alias='394')
    ProgPeriodInterval: Optional[int] = Field(None, description='', alias='415')
    CancellationRights: Optional[str] = Field(None, description='', alias='480')
    MoneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    RegistID: Optional[str] = Field(None, description='', alias='513')
    ListExecInstType: Optional[str] = Field(None, description='', alias='433')
    ListExecInst: Optional[str] = Field(None, description='', alias='69')
    EncodedListExecInstLen: Optional[int] = Field(None, description='', alias='352')
    EncodedListExecInst: Optional[str] = Field(None, description='', alias='353')
    AllowableOneSidednessPct: Optional[float] = Field(None, description='', alias='765')
    AllowableOneSidednessValue: Optional[float] = Field(None, description='', alias='766')
    AllowableOneSidednessCurr: Optional[str] = Field(None, description='', alias='767')
    TotNoOrders: int = Field(None, description='', alias='68')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    ListOrdGrp: ListOrdGrp = Field(..., description='ListOrdGrp component')

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
