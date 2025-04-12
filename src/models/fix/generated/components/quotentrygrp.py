"""
FIX 4.4 QuotEntryGrp Component

This module contains the Pydantic model for the QuotEntryGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class QuotEntryGrp(TradeModel):
    """
    FIX 4.4 QuotEntryGrp Component
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    QuoteEntryID: str = Field(None, description='', alias='299')
    BidPx: Optional[float] = Field(None, description='', alias='132')
    OfferPx: Optional[float] = Field(None, description='', alias='133')
    BidSize: Optional[float] = Field(None, description='', alias='134')
    OfferSize: Optional[float] = Field(None, description='', alias='135')
    ValidUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    BidSpotRate: Optional[float] = Field(None, description='', alias='188')
    OfferSpotRate: Optional[float] = Field(None, description='', alias='190')
    BidForwardPoints: Optional[float] = Field(None, description='', alias='189')
    OfferForwardPoints: Optional[float] = Field(None, description='', alias='191')
    MidPx: Optional[float] = Field(None, description='', alias='631')
    BidYield: Optional[float] = Field(None, description='', alias='632')
    MidYield: Optional[float] = Field(None, description='', alias='633')
    OfferYield: Optional[float] = Field(None, description='', alias='634')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    BidForwardPoints2: Optional[float] = Field(None, description='', alias='642')
    OfferForwardPoints2: Optional[float] = Field(None, description='', alias='643')
    Currency: Optional[str] = Field(None, description='', alias='15')
    Instrument: Optional[str] = Field(None)
    InstrmtLegGrp: Optional[str] = Field(None)


class NoQuoteEntries(TradeModel):
    """
    NoQuoteEntries group fields
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    QuoteEntryID: str = Field(None, description='', alias='299')
    BidPx: Optional[float] = Field(None, description='', alias='132')
    OfferPx: Optional[float] = Field(None, description='', alias='133')
    BidSize: Optional[float] = Field(None, description='', alias='134')
    OfferSize: Optional[float] = Field(None, description='', alias='135')
    ValidUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    BidSpotRate: Optional[float] = Field(None, description='', alias='188')
    OfferSpotRate: Optional[float] = Field(None, description='', alias='190')
    BidForwardPoints: Optional[float] = Field(None, description='', alias='189')
    OfferForwardPoints: Optional[float] = Field(None, description='', alias='191')
    MidPx: Optional[float] = Field(None, description='', alias='631')
    BidYield: Optional[float] = Field(None, description='', alias='632')
    MidYield: Optional[float] = Field(None, description='', alias='633')
    OfferYield: Optional[float] = Field(None, description='', alias='634')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    BidForwardPoints2: Optional[float] = Field(None, description='', alias='642')
    OfferForwardPoints2: Optional[float] = Field(None, description='', alias='643')
    Currency: Optional[str] = Field(None, description='', alias='15')

    NoQuoteEntriess: List[NoQuoteEntries] = Field(default_factory=list)
