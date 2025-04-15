"""FIX message model for Logout (5).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class LogoutMessage(FIXMessageBase):
    """FIX message model for Logout."""

    MsgType: str = Field("5", alias="35")

    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

