"""FIX message model for UserRequest (BE).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class UserRequestMessage(FIXMessageBase):
    """FIX message model for UserRequest."""

    MsgType: str = Field("BE", alias="35")

    UserRequestID: str = Field(..., alias='923', description='')
    UserRequestType: int = Field(..., alias='924', description='')
    Username: str = Field(..., alias='553', description='')
    Password: Optional[str] = Field(None, alias='554', description='')
    NewPassword: Optional[str] = Field(None, alias='925', description='')
    RawDataLength: Optional[int] = Field(None, alias='95', description='')
    RawData: Optional[str] = Field(None, alias='96', description='')

