from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class UserRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    UserRequestID: str = Field(..., description='', alias='923')
    UserRequestType: int = Field(..., description='', alias='924')
    Username: str = Field(..., description='', alias='553')
    Password: Optional[str] = Field(None, description='', alias='554')
    NewPassword: Optional[str] = Field(None, description='', alias='925')
    RawDataLength: Optional[int] = Field(None, description='', alias='95')
    RawData: Optional[str] = Field(None, description='', alias='96')

