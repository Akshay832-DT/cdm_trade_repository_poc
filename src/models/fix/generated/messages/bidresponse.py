"""FIX message model for BidResponse (l).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.bidcomprspgrp import BidCompRspGrpComponent

class BidResponseMessage(FIXMessageBase):
    """FIX message model for BidResponse."""

    MsgType: str = Field("l", alias="35")

    BidID: Optional[str] = Field(None, alias='390', description='')
    ClientBidID: Optional[str] = Field(None, alias='391', description='')
    BidCompRspGrp: BidCompRspGrpComponent = Field(..., description='')

