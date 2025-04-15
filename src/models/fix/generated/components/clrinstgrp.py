"""
FIX Component Model - ClrInstGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoClearingInstructionsGroup(FIXComponentBase):

    """FIX Group - NoClearingInstructions"""

    ClearingInstruction: Optional[int] = Field(None, alias='577', description='')



class ClrInstGrpComponent(FIXComponentBase):
    """FIX Component - ClrInstGrp"""


