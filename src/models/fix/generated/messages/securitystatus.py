"""FIX message model for SecurityStatus (f).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.instrumentextension import InstrumentExtensionComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class SecurityStatusMessage(FIXMessageBase):
    """FIX message model for SecurityStatus."""

    MsgType: str = Field("f", alias="35")

    SecurityStatusReqID: Optional[str] = Field(None, alias='324', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    UnsolicitedIndicator: Optional[bool] = Field(None, alias='325', description='')
    SecurityTradingStatus: Optional[int] = Field(None, alias='326', description='')
    FinancialStatus: Optional[List[str]] = Field(None, alias='291', description='')
    CorporateAction: Optional[List[str]] = Field(None, alias='292', description='')
    HaltReasonChar: Optional[str] = Field(None, alias='327', description='')
    InViewOfCommon: Optional[bool] = Field(None, alias='328', description='')
    DueToRelated: Optional[bool] = Field(None, alias='329', description='')
    BuyVolume: Optional[float] = Field(None, alias='330', description='')
    SellVolume: Optional[float] = Field(None, alias='331', description='')
    HighPx: Optional[float] = Field(None, alias='332', description='')
    LowPx: Optional[float] = Field(None, alias='333', description='')
    LastPx: Optional[float] = Field(None, alias='31', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    Adjustment: Optional[int] = Field(None, alias='334', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')

