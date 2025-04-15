"""FIX message model for TradingSessionStatusRequest (g).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class TradingSessionStatusRequestMessage(FIXMessageBase):
    """FIX message model for TradingSessionStatusRequest."""

    MsgType: str = Field("g", alias="35")

    TradSesReqID: str = Field(..., alias='335', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    TradSesMethod: Optional[int] = Field(None, alias='338', description='')
    TradSesMode: Optional[int] = Field(None, alias='339', description='')
    SubscriptionRequestType: str = Field(..., alias='263', description='')

