"""
FIX Component Model - LegQuotGrp
"""

from ..base import FIXComponentBase
from .instrumentleg import InstrumentLegComponent
from .legbenchmarkcurvedata import LegBenchmarkCurveDataComponent
from .legstipulations import LegStipulationsComponent
from .nestedparties import NestedPartiesComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegsGroup(FIXComponentBase):

    """FIX Group - NoLegs"""

    LegQty: Optional[float] = Field(None, alias='687', description='')
    LegSwapType: Optional[int] = Field(None, alias='690', description='')
    LegSettlType: Optional[str] = Field(None, alias='587', description='')
    LegSettlDate: Optional[date] = Field(None, alias='588', description='')
    LegPriceType: Optional[int] = Field(None, alias='686', description='')
    LegBidPx: Optional[float] = Field(None, alias='681', description='')
    LegOfferPx: Optional[float] = Field(None, alias='684', description='')
    InstrumentLeg: Optional[InstrumentLegComponent] = Field(None, description='')
    LegStipulations: Optional[LegStipulationsComponent] = Field(None, description='')
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='')
    LegBenchmarkCurveData: Optional[LegBenchmarkCurveDataComponent] = Field(None, description='')



class LegQuotGrpComponent(FIXComponentBase):
    """FIX Component - LegQuotGrp"""


