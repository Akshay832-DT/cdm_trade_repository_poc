"""FIX message model for Logon (A).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class LogonMessage(FIXMessageBase):
    """FIX message model for Logon."""

    MsgType: str = Field("A", alias="35")

    EncryptMethod: int = Field(..., alias='98', description='')
    HeartBtInt: int = Field(..., alias='108', description='')
    RawDataLength: Optional[int] = Field(None, alias='95', description='')
    RawData: Optional[str] = Field(None, alias='96', description='')
    ResetSeqNumFlag: Optional[bool] = Field(None, alias='141', description='')
    NextExpectedMsgSeqNum: Optional[int] = Field(None, alias='789', description='')
    MaxMessageSize: Optional[int] = Field(None, alias='383', description='')
    TestMessageIndicator: Optional[bool] = Field(None, alias='464', description='')
    Username: Optional[str] = Field(None, alias='553', description='')
    Password: Optional[str] = Field(None, alias='554', description='')

