"""
FIX Component Model - InstrmtLegIOIGrp
"""

from ..base import FIXComponentBase
from .instrumentleg import InstrumentLegComponent
from .legstipulations import LegStipulationsComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegsGroup(FIXComponentBase):

    """FIX Group - NoLegs"""

    LegIOIQty: Optional[str] = Field(None, alias='682', description='')
    InstrumentLeg: Optional[InstrumentLegComponent] = Field(None, description='')
    LegStipulations: Optional[LegStipulationsComponent] = Field(None, description='')



class InstrmtLegIOIGrpComponent(FIXComponentBase):
    """FIX Component - InstrmtLegIOIGrp"""


