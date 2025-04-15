"""FIX message model for ResendRequest (2).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class ResendRequestMessage(FIXMessageBase):
    """FIX message model for ResendRequest."""

    MsgType: str = Field("2", alias="35")

    BeginSeqNo: int = Field(..., alias='7', description='')
    EndSeqNo: int = Field(..., alias='16', description='')

