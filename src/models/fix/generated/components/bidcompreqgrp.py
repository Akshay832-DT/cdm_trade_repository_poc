"""
FIX Component Model - BidCompReqGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoBidComponentsGroup(FIXComponentBase):

    """FIX Group - NoBidComponents"""

    ListID: Optional[str] = Field(None, alias='66', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    NetGrossInd: Optional[int] = Field(None, alias='430', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')



class BidCompReqGrpComponent(FIXComponentBase):
    """FIX Component - BidCompReqGrp"""


