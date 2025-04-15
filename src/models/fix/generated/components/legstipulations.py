"""
FIX Component Model - LegStipulations
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegStipulationsGroup(FIXComponentBase):

    """FIX Group - NoLegStipulations"""

    LegStipulationType: Optional[str] = Field(None, alias='688', description='')
    LegStipulationValue: Optional[str] = Field(None, alias='689', description='')



class LegStipulationsComponent(FIXComponentBase):
    """FIX Component - LegStipulations"""


