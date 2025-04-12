"""
FIX 4.4 SecurityStatus Message

This module contains the Pydantic model for the SecurityStatus message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.instrumentextension import InstrumentExtension
from ..components.undinstrmtgrp import UndInstrmtGrp


class SecurityStatus(TradeModel):
    """
    FIX 4.4 SecurityStatus Message
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
    MsgType: Literal["f"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    SecurityStatusReqID: Optional[str] = Field(None, description='', alias='324')
    Currency: Optional[str] = Field(None, description='', alias='15')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    UnsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    SecurityTradingStatus: Optional[int] = Field(None, description='', alias='326')
    FinancialStatus: Optional[List[str]] = Field(None, description='', alias='291')
    CorporateAction: Optional[List[str]] = Field(None, description='', alias='292')
    HaltReasonChar: Optional[str] = Field(None, description='', alias='327')
    InViewOfCommon: Optional[bool] = Field(None, description='', alias='328')
    DueToRelated: Optional[bool] = Field(None, description='', alias='329')
    BuyVolume: Optional[float] = Field(None, description='', alias='330')
    SellVolume: Optional[float] = Field(None, description='', alias='331')
    HighPx: Optional[float] = Field(None, description='', alias='332')
    LowPx: Optional[float] = Field(None, description='', alias='333')
    LastPx: Optional[float] = Field(None, description='', alias='31')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    Adjustment: Optional[int] = Field(None, description='', alias='334')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Instrument: Instrument = Field(..., description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtension] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None

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
