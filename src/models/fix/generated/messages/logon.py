from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class Logon(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    EncryptMethod: int = Field(..., description='', alias='98')
    HeartBtInt: int = Field(..., description='', alias='108')
    RawDataLength: Optional[int] = Field(None, description='', alias='95')
    RawData: Optional[str] = Field(None, description='', alias='96')
    ResetSeqNumFlag: Optional[bool] = Field(None, description='', alias='141')
    NextExpectedMsgSeqNum: Optional[int] = Field(None, description='', alias='789')
    MaxMessageSize: Optional[int] = Field(None, description='', alias='383')
    RefMsgType: Optional[str] = Field(None, description='', alias='372')
    MsgDirection: Optional[str] = Field(None, description='', alias='385')
    TestMessageIndicator: Optional[bool] = Field(None, description='', alias='464')
    Username: Optional[str] = Field(None, description='', alias='553')
    Password: Optional[str] = Field(None, description='', alias='554')
    NoMsgTypes: Optional[int] = Field(None, description='', alias='384')

