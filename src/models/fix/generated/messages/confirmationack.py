from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class ConfirmationAck(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ConfirmID: str = Field(..., description='', alias='664')
    TradeDate: date = Field(..., description='', alias='75')
    TransactTime: datetime = Field(..., description='', alias='60')
    AffirmStatus: int = Field(..., description='', alias='940')
    ConfirmRejReason: Optional[int] = Field(None, description='', alias='774')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

