"""FIX message model for Heartbeat (0).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class HeartbeatMessage(FIXMessageBase):
    """FIX message model for Heartbeat."""

    MsgType: str = Field("0", alias="35")

    TestReqID: Optional[str] = Field(None, alias='112', description='')

