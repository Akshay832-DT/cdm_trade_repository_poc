"""FIX message model for BusinessMessageReject (j).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class BusinessMessageRejectMessage(FIXMessageBase):
    """FIX message model for BusinessMessageReject."""

    MsgType: str = Field("j", alias="35")

    RefSeqNum: Optional[int] = Field(None, alias='45', description='')
    RefMsgType: str = Field(..., alias='372', description='')
    BusinessRejectRefID: Optional[str] = Field(None, alias='379', description='')
    BusinessRejectReason: int = Field(..., alias='380', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

