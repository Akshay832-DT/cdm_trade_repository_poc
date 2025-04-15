"""FIX message model for MarketDataSnapshotFullRefresh (W).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.mdfullgrp import MDFullGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class MarketDataSnapshotFullRefreshMessage(FIXMessageBase):
    """FIX message model for MarketDataSnapshotFullRefresh."""

    MsgType: str = Field("W", alias="35")

    MDReqID: Optional[str] = Field(None, alias='262', description='')
    FinancialStatus: Optional[List[str]] = Field(None, alias='291', description='')
    CorporateAction: Optional[List[str]] = Field(None, alias='292', description='')
    NetChgPrevDay: Optional[float] = Field(None, alias='451', description='')
    ApplQueueDepth: Optional[int] = Field(None, alias='813', description='')
    ApplQueueResolution: Optional[int] = Field(None, alias='814', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    MDFullGrp: MDFullGrpComponent = Field(..., description='')

