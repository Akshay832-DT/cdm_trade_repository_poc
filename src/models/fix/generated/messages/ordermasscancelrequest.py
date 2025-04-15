"""FIX message model for OrderMassCancelRequest (q).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrument import InstrumentComponent
from ..components.underlyinginstrument import UnderlyingInstrumentComponent

class OrderMassCancelRequestMessage(FIXMessageBase):
    """FIX message model for OrderMassCancelRequest."""

    MsgType: str = Field("q", alias="35")

    ClOrdID: str = Field(..., alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    MassCancelRequestType: str = Field(..., alias='530', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')

