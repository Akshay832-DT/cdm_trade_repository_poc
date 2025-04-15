"""
FIX Component Model - TrdgSesGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoTradingSessionsGroup(FIXComponentBase):

    """FIX Group - NoTradingSessions"""

    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')



class TrdgSesGrpComponent(FIXComponentBase):
    """FIX Component - TrdgSesGrp"""


