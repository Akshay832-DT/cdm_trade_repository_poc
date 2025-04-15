"""FIX message model for DerivativeSecurityListRequest (z).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.underlyinginstrument import UnderlyingInstrumentComponent

class DerivativeSecurityListRequestMessage(FIXMessageBase):
    """FIX message model for DerivativeSecurityListRequest."""

    MsgType: str = Field("z", alias="35")

    SecurityReqID: str = Field(..., alias='320', description='')
    SecurityListRequestType: int = Field(..., alias='559', description='')
    SecuritySubType: Optional[str] = Field(None, alias='762', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')

