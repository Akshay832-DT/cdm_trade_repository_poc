"""
FIX Component Model - ContAmtGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoContAmtsGroup(FIXComponentBase):

    """FIX Group - NoContAmts"""

    ContAmtType: Optional[int] = Field(None, alias='519', description='')
    ContAmtValue: Optional[float] = Field(None, alias='520', description='')
    ContAmtCurr: Optional[str] = Field(None, alias='521', description='')



class ContAmtGrpComponent(FIXComponentBase):
    """FIX Component - ContAmtGrp"""


