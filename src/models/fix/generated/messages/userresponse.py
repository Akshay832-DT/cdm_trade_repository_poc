"""FIX message model for UserResponse (BF).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class UserResponseMessage(FIXMessageBase):
    """FIX message model for UserResponse."""

    MsgType: str = Field("BF", alias="35")

    UserRequestID: str = Field(..., alias='923', description='')
    Username: str = Field(..., alias='553', description='')
    UserStatus: Optional[int] = Field(None, alias='926', description='')
    UserStatusText: Optional[str] = Field(None, alias='927', description='')

