"""FIX message model for Advertisement (7).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class AdvertisementMessage(FIXMessageBase):
    """FIX message model for Advertisement."""

    MsgType: str = Field("7", alias="35")

    AdvId: str = Field(..., alias='2', description='')
    AdvTransType: str = Field(..., alias='5', description='')
    AdvRefID: Optional[str] = Field(None, alias='3', description='')
    AdvSide: str = Field(..., alias='4', description='')
    Quantity: float = Field(..., alias='53', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    URLLink: Optional[str] = Field(None, alias='149', description='')
    LastMkt: Optional[str] = Field(None, alias='30', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')

