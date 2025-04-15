"""FIX message model for MarketDataIncrementalRefresh (X).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.mdincgrp import MDIncGrpComponent

class MarketDataIncrementalRefreshMessage(FIXMessageBase):
    """FIX message model for MarketDataIncrementalRefresh."""

    MsgType: str = Field("X", alias="35")

    MDReqID: Optional[str] = Field(None, alias='262', description='')
    ApplQueueDepth: Optional[int] = Field(None, alias='813', description='')
    ApplQueueResolution: Optional[int] = Field(None, alias='814', description='')
    MDIncGrp: MDIncGrpComponent = Field(..., description='')

