"""FIX message model for RFQRequest (AH).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.rfqreqgrp import RFQReqGrpComponent

class RFQRequestMessage(FIXMessageBase):
    """FIX message model for RFQRequest."""

    MsgType: str = Field("AH", alias="35")

    RFQReqID: str = Field(..., alias='644', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    RFQReqGrp: RFQReqGrpComponent = Field(..., description='')

