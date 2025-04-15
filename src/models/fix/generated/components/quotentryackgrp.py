"""
FIX Component Model - QuotEntryAckGrp
"""

from ..base import FIXComponentBase
from .instrmtleggrp import InstrmtLegGrpComponent
from .instrument import InstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoQuoteEntriesGroup(FIXComponentBase):

    """FIX Group - NoQuoteEntries"""

    QuoteEntryID: Optional[str] = Field(None, alias='299', description='')
    BidPx: Optional[float] = Field(None, alias='132', description='')
    OfferPx: Optional[float] = Field(None, alias='133', description='')
    BidSize: Optional[float] = Field(None, alias='134', description='')
    OfferSize: Optional[float] = Field(None, alias='135', description='')
    ValidUntilTime: Optional[datetime] = Field(None, alias='62', description='')
    BidSpotRate: Optional[float] = Field(None, alias='188', description='')
    OfferSpotRate: Optional[float] = Field(None, alias='190', description='')
    BidForwardPoints: Optional[float] = Field(None, alias='189', description='')
    OfferForwardPoints: Optional[float] = Field(None, alias='191', description='')
    MidPx: Optional[float] = Field(None, alias='631', description='')
    BidYield: Optional[float] = Field(None, alias='632', description='')
    MidYield: Optional[float] = Field(None, alias='633', description='')
    OfferYield: Optional[float] = Field(None, alias='634', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    OrdType: Optional[str] = Field(None, alias='40', description='')
    SettlDate2: Optional[date] = Field(None, alias='193', description='')
    OrderQty2: Optional[float] = Field(None, alias='192', description='')
    BidForwardPoints2: Optional[float] = Field(None, alias='642', description='')
    OfferForwardPoints2: Optional[float] = Field(None, alias='643', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    QuoteEntryRejectReason: Optional[int] = Field(None, alias='368', description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')



class QuotEntryAckGrpComponent(FIXComponentBase):
    """FIX Component - QuotEntryAckGrp"""


