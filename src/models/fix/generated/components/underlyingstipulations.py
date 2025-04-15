"""
FIX Component Model - UnderlyingStipulations
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoUnderlyingStipsGroup(FIXComponentBase):

    """FIX Group - NoUnderlyingStips"""

    UnderlyingStipType: Optional[str] = Field(None, alias='888', description='')
    UnderlyingStipValue: Optional[str] = Field(None, alias='889', description='')



class UnderlyingStipulationsComponent(FIXComponentBase):
    """FIX Component - UnderlyingStipulations"""


