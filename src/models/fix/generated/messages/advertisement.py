from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent

class Advertisement(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    AdvId: str = Field(..., description='', alias='2')
    AdvTransType: str = Field(..., description='', alias='5')
    AdvRefID: Optional[str] = Field(None, description='', alias='3')
    AdvSide: str = Field(..., description='', alias='4')
    Quantity: float = Field(..., description='', alias='53')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    Price: Optional[float] = Field(None, description='', alias='44')
    Currency: Optional[str] = Field(None, description='', alias='15')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    URLLink: Optional[str] = Field(None, description='', alias='149')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')

