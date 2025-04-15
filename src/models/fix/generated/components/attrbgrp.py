"""
FIX Component Model - AttrbGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoInstrAttribGroup(FIXComponentBase):

    """FIX Group - NoInstrAttrib"""

    InstrAttribType: Optional[int] = Field(None, alias='871', description='')
    InstrAttribValue: Optional[str] = Field(None, alias='872', description='')



class AttrbGrpComponent(FIXComponentBase):
    """FIX Component - AttrbGrp"""


