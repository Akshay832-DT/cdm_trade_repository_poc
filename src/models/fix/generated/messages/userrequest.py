from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class UserRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    userrequestid: str = Field(..., description='', alias='923')
    userrequesttype: int = Field(..., description='', alias='924')
    username: str = Field(..., description='', alias='553')
    password: Optional[str] = Field(None, description='', alias='554')
    newpassword: Optional[str] = Field(None, description='', alias='925')
    rawdatalength: Optional[int] = Field(None, description='', alias='95')
    rawdata: Optional[str] = Field(None, description='', alias='96')

