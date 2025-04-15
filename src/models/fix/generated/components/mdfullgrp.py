"""
FIX Component Model - MDFullGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoMDEntriesGroup(FIXComponentBase):

    """FIX Group - NoMDEntries"""

    MDEntryType: str = Field(alias='269', description='')
    MDEntryPx: Optional[float] = Field(None, alias='270', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    MDEntrySize: Optional[float] = Field(None, alias='271', description='')
    MDEntryDate: Optional[date] = Field(None, alias='272', description='')
    MDEntryTime: Optional[time] = Field(None, alias='273', description='')
    TickDirection: Optional[str] = Field(None, alias='274', description='')
    MDMkt: Optional[str] = Field(None, alias='275', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    QuoteCondition: Optional[str] = Field(None, alias='276', description='')
    TradeCondition: Optional[str] = Field(None, alias='277', description='')
    MDEntryOriginator: Optional[str] = Field(None, alias='282', description='')
    LocationID: Optional[str] = Field(None, alias='283', description='')
    DeskID: Optional[str] = Field(None, alias='284', description='')
    OpenCloseSettlFlag: Optional[str] = Field(None, alias='286', description='')
    TimeInForce: Optional[str] = Field(None, alias='59', description='')
    ExpireDate: Optional[date] = Field(None, alias='432', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    MinQty: Optional[float] = Field(None, alias='110', description='')
    ExecInst: Optional[str] = Field(None, alias='18', description='')
    SellerDays: Optional[int] = Field(None, alias='287', description='')
    OrderID: Optional[str] = Field(None, alias='37', description='')
    QuoteEntryID: Optional[str] = Field(None, alias='299', description='')
    MDEntryBuyer: Optional[str] = Field(None, alias='288', description='')
    MDEntrySeller: Optional[str] = Field(None, alias='289', description='')
    NumberOfOrders: Optional[int] = Field(None, alias='346', description='')
    MDEntryPositionNo: Optional[int] = Field(None, alias='290', description='')
    Scope: Optional[str] = Field(None, alias='546', description='')
    PriceDelta: Optional[float] = Field(None, alias='811', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')



class MDFullGrpComponent(FIXComponentBase):
    """FIX Component - MDFullGrp"""


