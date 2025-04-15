"""FIX message model for NetworkCounterpartySystemStatusRequest (BC).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.compidreqgrp import CompIDReqGrpComponent

class NetworkCounterpartySystemStatusRequestMessage(FIXMessageBase):
    """FIX message model for NetworkCounterpartySystemStatusRequest."""

    MsgType: str = Field("BC", alias="35")

    NetworkRequestType: int = Field(..., alias='935', description='')
    NetworkRequestID: str = Field(..., alias='933', description='')
    CompIDReqGrp: Optional[CompIDReqGrpComponent] = Field(None, description='')

