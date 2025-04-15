"""FIX message model for Reject (3).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class RejectMessage(FIXMessageBase):
    """FIX message model for Reject."""

    MsgType: str = Field("3", alias="35")

    RefSeqNum: int = Field(..., alias='45', description='')
    RefTagID: Optional[int] = Field(None, alias='371', description='')
    RefMsgType: Optional[str] = Field(None, alias='372', description='')
    SessionRejectReason: Optional[int] = Field(None, alias='373', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

