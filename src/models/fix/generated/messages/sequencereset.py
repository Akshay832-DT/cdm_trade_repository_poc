"""FIX message model for SequenceReset (4).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class SequenceResetMessage(FIXMessageBase):
    """FIX message model for SequenceReset."""

    MsgType: str = Field("4", alias="35")

    GapFillFlag: Optional[bool] = Field(None, alias='123', description='')
    NewSeqNo: int = Field(..., alias='36', description='')

