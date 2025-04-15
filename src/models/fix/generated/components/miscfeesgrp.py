"""
FIX Component Model - MiscFeesGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoMiscFeesGroup(FIXComponentBase):

    """FIX Group - NoMiscFees"""

    MiscFeeAmt: Optional[float] = Field(None, alias='137', description='')
    MiscFeeCurr: Optional[str] = Field(None, alias='138', description='')
    MiscFeeType: Optional[str] = Field(None, alias='139', description='')
    MiscFeeBasis: Optional[int] = Field(None, alias='891', description='')



class MiscFeesGrpComponent(FIXComponentBase):
    """FIX Component - MiscFeesGrp"""


