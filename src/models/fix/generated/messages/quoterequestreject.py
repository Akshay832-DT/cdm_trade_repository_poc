"""FIX message model for QuoteRequestReject (AG).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.quotreqrjctgrp import QuotReqRjctGrpComponent

class QuoteRequestRejectMessage(FIXMessageBase):
    """FIX message model for QuoteRequestReject."""

    MsgType: str = Field("AG", alias="35")

    QuoteReqID: str = Field(..., alias='131', description='')
    RFQReqID: Optional[str] = Field(None, alias='644', description='')
    QuoteRequestRejectReason: int = Field(..., alias='658', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    QuotReqRjctGrp: QuotReqRjctGrpComponent = Field(..., description='')

