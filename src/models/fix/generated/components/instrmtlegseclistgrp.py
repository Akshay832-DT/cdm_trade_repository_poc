"""
FIX Component Model - InstrmtLegSecListGrp
"""

from ..base import FIXComponentBase
from .instrumentleg import InstrumentLegComponent
from .legbenchmarkcurvedata import LegBenchmarkCurveDataComponent
from .legstipulations import LegStipulationsComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegsGroup(FIXComponentBase):

    """FIX Group - NoLegs"""

    LegSwapType: Optional[int] = Field(None, alias='690', description='')
    LegSettlType: Optional[str] = Field(None, alias='587', description='')
    InstrumentLeg: Optional[InstrumentLegComponent] = Field(None, description='')
    LegStipulations: Optional[LegStipulationsComponent] = Field(None, description='')
    LegBenchmarkCurveData: Optional[LegBenchmarkCurveDataComponent] = Field(None, description='')



class InstrmtLegSecListGrpComponent(FIXComponentBase):
    """FIX Component - InstrmtLegSecListGrp"""


