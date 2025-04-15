"""FIX message model for MarketDataRequest (V).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtmdreqgrp import InstrmtMDReqGrpComponent
from ..components.mdreqgrp import MDReqGrpComponent
from ..components.trdgsesgrp import TrdgSesGrpComponent

class MarketDataRequestMessage(FIXMessageBase):
    """FIX message model for MarketDataRequest."""

    MsgType: str = Field("V", alias="35")

    MDReqID: str = Field(..., alias='262', description='')
    SubscriptionRequestType: str = Field(..., alias='263', description='')
    MarketDepth: int = Field(..., alias='264', description='')
    MDUpdateType: Optional[int] = Field(None, alias='265', description='')
    AggregatedBook: Optional[bool] = Field(None, alias='266', description='')
    OpenCloseSettlFlag: Optional[List[str]] = Field(None, alias='286', description='')
    Scope: Optional[List[str]] = Field(None, alias='546', description='')
    MDImplicitDelete: Optional[bool] = Field(None, alias='547', description='')
    ApplQueueAction: Optional[int] = Field(None, alias='815', description='')
    ApplQueueMax: Optional[int] = Field(None, alias='812', description='')
    MDReqGrp: MDReqGrpComponent = Field(..., description='')
    InstrmtMDReqGrp: InstrmtMDReqGrpComponent = Field(..., description='')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='')

