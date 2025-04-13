from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class ListExecute(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    listid: str = Field(..., description='', alias='66')
    clientbidid: Optional[str] = Field(None, description='', alias='391')
    bidid: Optional[str] = Field(None, description='', alias='390')
    transacttime: datetime = Field(..., description='', alias='60')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')

