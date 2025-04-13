from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrumentextension import InstrumentExtensionComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent

class SecurityStatus(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
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
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='InstrumentExtension component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')

