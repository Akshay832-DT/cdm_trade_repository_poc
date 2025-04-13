from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class UserResponse(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    UserRequestID: str = Field(..., description='', alias='923')
    Username: str = Field(..., description='', alias='553')
    UserStatus: Optional[int] = Field(None, description='', alias='926')
    UserStatusText: Optional[str] = Field(None, description='', alias='927')

