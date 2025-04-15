"""
FIX Component Model - InstrmtGrp
"""

from ..base import FIXComponentBase
from .instrument import InstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoRelatedSymGroup(FIXComponentBase):

    """FIX Group - NoRelatedSym"""

    Instrument: Optional[InstrumentComponent] = Field(None, description='')



class InstrmtGrpComponent(FIXComponentBase):
    """FIX Component - InstrmtGrp"""


