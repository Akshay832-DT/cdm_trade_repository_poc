"""
FIX Component Model - Stipulations
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoStipulationsGroup(FIXComponentBase):

    """FIX Group - NoStipulations"""

    StipulationType: Optional[str] = Field(None, alias='233', description='')
    StipulationValue: Optional[str] = Field(None, alias='234', description='')



class StipulationsComponent(FIXComponentBase):
    """FIX Component - Stipulations"""


