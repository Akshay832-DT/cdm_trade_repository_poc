"""FIX message model for TestRequest (1).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class TestRequestMessage(FIXMessageBase):
    """FIX message model for TestRequest."""

    MsgType: str = Field("1", alias="35")

    TestReqID: str = Field(..., alias='112', description='')

