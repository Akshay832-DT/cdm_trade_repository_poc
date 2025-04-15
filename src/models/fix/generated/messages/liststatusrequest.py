"""FIX message model for ListStatusRequest (M).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class ListStatusRequestMessage(FIXMessageBase):
    """FIX message model for ListStatusRequest."""

    MsgType: str = Field("M", alias="35")

    ListID: str = Field(..., alias='66', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

