"""
FIX Component Model - InstrmtLegExecGrp
"""

from ..base import FIXComponentBase
from .instrumentleg import InstrumentLegComponent
from .legstipulations import LegStipulationsComponent
from .nestedparties import NestedPartiesComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegsGroup(FIXComponentBase):

    """FIX Group - NoLegs"""

    LegQty: Optional[float] = Field(None, alias='687', description='')
    LegSwapType: Optional[int] = Field(None, alias='690', description='')
    LegPositionEffect: Optional[str] = Field(None, alias='564', description='')
    LegCoveredOrUncovered: Optional[int] = Field(None, alias='565', description='')
    LegRefID: Optional[str] = Field(None, alias='654', description='')
    LegPrice: Optional[float] = Field(None, alias='566', description='')
    LegSettlType: Optional[str] = Field(None, alias='587', description='')
    LegSettlDate: Optional[date] = Field(None, alias='588', description='')
    LegLastPx: Optional[float] = Field(None, alias='637', description='')
    InstrumentLeg: Optional[InstrumentLegComponent] = Field(None, description='')
    LegStipulations: Optional[LegStipulationsComponent] = Field(None, description='')
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='')



class InstrmtLegExecGrpComponent(FIXComponentBase):
    """FIX Component - InstrmtLegExecGrp"""


