"""
FIX Component Model - TrdCapDtGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoDatesGroup(FIXComponentBase):

    """FIX Group - NoDates"""

    TradeDate: Optional[date] = Field(None, alias='75', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')



class TrdCapDtGrpComponent(FIXComponentBase):
    """FIX Component - TrdCapDtGrp"""


