"""FIX message model for QuoteRequest (R).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.quotreqgrp import QuotReqGrpComponent

class QuoteRequestMessage(FIXMessageBase):
    """FIX message model for QuoteRequest."""

    MsgType: str = Field("R", alias="35")

    QuoteReqID: str = Field(..., alias='131', description='')
    RFQReqID: Optional[str] = Field(None, alias='644', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    OrderCapacity: Optional[str] = Field(None, alias='528', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    QuotReqGrp: QuotReqGrpComponent = Field(..., description='')

