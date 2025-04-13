from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class Logon(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    encryptmethod: int = Field(..., description='', alias='98')
    heartbtint: int = Field(..., description='', alias='108')
    rawdatalength: Optional[int] = Field(None, description='', alias='95')
    rawdata: Optional[str] = Field(None, description='', alias='96')
    resetseqnumflag: Optional[bool] = Field(None, description='', alias='141')
    nextexpectedmsgseqnum: Optional[int] = Field(None, description='', alias='789')
    maxmessagesize: Optional[int] = Field(None, description='', alias='383')
    refmsgtype: Optional[str] = Field(None, description='', alias='372')
    msgdirection: Optional[str] = Field(None, description='', alias='385')
    testmessageindicator: Optional[bool] = Field(None, description='', alias='464')
    username: Optional[str] = Field(None, description='', alias='553')
    password: Optional[str] = Field(None, description='', alias='554')
    nomsgtypes: Optional[int] = Field(None, description='', alias='384')

