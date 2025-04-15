"""
FIX Component Model - BidCompRspGrp
"""

from ..base import FIXComponentBase
from .commissiondata import CommissionDataComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoBidComponentsGroup(FIXComponentBase):

    """FIX Group - NoBidComponents"""

    ListID: Optional[str] = Field(None, alias='66', description='')
    Country: Optional[str] = Field(None, alias='421', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    FairValue: Optional[float] = Field(None, alias='406', description='')
    NetGrossInd: Optional[int] = Field(None, alias='430', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    CommissionData: CommissionDataComponent



class BidCompRspGrpComponent(FIXComponentBase):
    """FIX Component - BidCompRspGrp"""


