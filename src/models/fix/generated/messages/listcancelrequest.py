"""FIX message model for ListCancelRequest (K).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class ListCancelRequestMessage(FIXMessageBase):
    """FIX message model for ListCancelRequest."""

    MsgType: str = Field("K", alias="35")

    ListID: str = Field(..., alias='66', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    TradeOriginationDate: Optional[date] = Field(None, alias='229', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

