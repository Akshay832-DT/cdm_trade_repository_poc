"""FIX message model for CrossOrderCancelRequest (u).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.sidecrossordcxlgrp import SideCrossOrdCxlGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class CrossOrderCancelRequestMessage(FIXMessageBase):
    """FIX message model for CrossOrderCancelRequest."""

    MsgType: str = Field("u", alias="35")

    OrderID: Optional[str] = Field(None, alias='37', description='')
    CrossID: str = Field(..., alias='548', description='')
    OrigCrossID: str = Field(..., alias='551', description='')
    CrossType: int = Field(..., alias='549', description='')
    CrossPrioritization: int = Field(..., alias='550', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    SideCrossOrdCxlGrp: SideCrossOrdCxlGrpComponent = Field(..., description='')
    Instrument: InstrumentComponent = Field(..., description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')

