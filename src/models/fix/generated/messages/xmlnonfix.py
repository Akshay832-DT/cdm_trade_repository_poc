"""FIX message model for XMLnonFIX (n).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class XMLnonFIXMessage(FIXMessageBase):
    """FIX message model for XMLnonFIX."""

    MsgType: str = Field("n", alias="35")


