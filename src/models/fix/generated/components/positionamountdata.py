"""
FIX Component Model - PositionAmountData
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoPosAmtGroup(FIXComponentBase):

    """FIX Group - NoPosAmt"""

    PosAmtType: Optional[str] = Field(None, alias='707', description='')
    PosAmt: Optional[float] = Field(None, alias='708', description='')



class PositionAmountDataComponent(FIXComponentBase):
    """FIX Component - PositionAmountData"""


