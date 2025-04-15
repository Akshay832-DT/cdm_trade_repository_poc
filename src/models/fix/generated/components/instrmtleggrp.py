"""
FIX Component Model - InstrmtLegGrp
"""

from ..base import FIXComponentBase
from .instrumentleg import InstrumentLegComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegsGroup(FIXComponentBase):

    """FIX Group - NoLegs"""

    InstrumentLeg: Optional[InstrumentLegComponent] = Field(None, description='')



class InstrmtLegGrpComponent(FIXComponentBase):
    """FIX Component - InstrmtLegGrp"""


