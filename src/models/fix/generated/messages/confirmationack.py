from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class ConfirmationAck(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    confirmid: str = Field(..., description='', alias='664')
    tradedate: date = Field(..., description='', alias='75')
    transacttime: datetime = Field(..., description='', alias='60')
    affirmstatus: int = Field(..., description='', alias='940')
    confirmrejreason: Optional[int] = Field(None, description='', alias='774')
    matchstatus: Optional[str] = Field(None, description='', alias='573')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')

