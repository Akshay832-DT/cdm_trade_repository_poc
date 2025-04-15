"""FIX message model for ConfirmationAck (AU).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class ConfirmationAckMessage(FIXMessageBase):
    """FIX message model for ConfirmationAck."""

    MsgType: str = Field("AU", alias="35")

    ConfirmID: str = Field(..., alias='664', description='')
    TradeDate: date = Field(..., alias='75', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    AffirmStatus: int = Field(..., alias='940', description='')
    ConfirmRejReason: Optional[int] = Field(None, alias='774', description='')
    MatchStatus: Optional[str] = Field(None, alias='573', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

