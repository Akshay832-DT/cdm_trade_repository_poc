"""
FIX Component Model - TrdCollGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoTradesGroup(FIXComponentBase):

    """FIX Group - NoTrades"""

    TradeReportID: Optional[str] = Field(None, alias='571', description='')
    SecondaryTradeReportID: Optional[str] = Field(None, alias='818', description='')



class TrdCollGrpComponent(FIXComponentBase):
    """FIX Component - TrdCollGrp"""


