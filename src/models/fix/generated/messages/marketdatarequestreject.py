"""FIX message model for MarketDataRequestReject (Y).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.mdrjctgrp import MDRjctGrpComponent

class MarketDataRequestRejectMessage(FIXMessageBase):
    """FIX message model for MarketDataRequestReject."""

    MsgType: str = Field("Y", alias="35")

    MDReqID: str = Field(..., alias='262', description='')
    MDReqRejReason: Optional[str] = Field(None, alias='281', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    MDRjctGrp: Optional[MDRjctGrpComponent] = Field(None, description='')

