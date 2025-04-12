"""
FIX 4.4 QuotEntryGrp Component

This module contains the Pydantic model for the QuotEntryGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class QuotEntryGrp(FIXMessageBase):
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
    quoteEntryID: str = Field(None, description='', alias='299')
    bidPx: Optional[float] = Field(None, description='', alias='132')
    offerPx: Optional[float] = Field(None, description='', alias='133')
    bidSize: Optional[float] = Field(None, description='', alias='134')
    offerSize: Optional[float] = Field(None, description='', alias='135')
    validUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    bidSpotRate: Optional[float] = Field(None, description='', alias='188')
    offerSpotRate: Optional[float] = Field(None, description='', alias='190')
    bidForwardPoints: Optional[float] = Field(None, description='', alias='189')
    offerForwardPoints: Optional[float] = Field(None, description='', alias='191')
    midPx: Optional[float] = Field(None, description='', alias='631')
    bidYield: Optional[float] = Field(None, description='', alias='632')
    midYield: Optional[float] = Field(None, description='', alias='633')
    offerYield: Optional[float] = Field(None, description='', alias='634')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    ordType: Optional[str] = Field(None, description='', alias='40')
    settlDate2: Optional[date] = Field(None, description='', alias='193')
    orderQty2: Optional[float] = Field(None, description='', alias='192')
    bidForwardPoints2: Optional[float] = Field(None, description='', alias='642')
    offerForwardPoints2: Optional[float] = Field(None, description='', alias='643')
    currency: Optional[str] = Field(None, description='', alias='15')
    instrument: Optional[str] = Field(None)
    instrmtLegGrp: Optional[str] = Field(None)


class NoQuoteEntries(FIXMessageBase):
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
    quoteEntryID: int = Field(None, description='', alias='295')
    bidPx: Optional[int] = Field(None, description='', alias='295')
    offerPx: Optional[int] = Field(None, description='', alias='295')
    bidSize: Optional[int] = Field(None, description='', alias='295')
    offerSize: Optional[int] = Field(None, description='', alias='295')
    validUntilTime: Optional[int] = Field(None, description='', alias='295')
    bidSpotRate: Optional[int] = Field(None, description='', alias='295')
    offerSpotRate: Optional[int] = Field(None, description='', alias='295')
    bidForwardPoints: Optional[int] = Field(None, description='', alias='295')
    offerForwardPoints: Optional[int] = Field(None, description='', alias='295')
    midPx: Optional[int] = Field(None, description='', alias='295')
    bidYield: Optional[int] = Field(None, description='', alias='295')
    midYield: Optional[int] = Field(None, description='', alias='295')
    offerYield: Optional[int] = Field(None, description='', alias='295')
    transactTime: Optional[int] = Field(None, description='', alias='295')
    tradingSessionID: Optional[int] = Field(None, description='', alias='295')
    tradingSessionSubID: Optional[int] = Field(None, description='', alias='295')
    settlDate: Optional[int] = Field(None, description='', alias='295')
    ordType: Optional[int] = Field(None, description='', alias='295')
    settlDate2: Optional[int] = Field(None, description='', alias='295')
    orderQty2: Optional[int] = Field(None, description='', alias='295')
    bidForwardPoints2: Optional[int] = Field(None, description='', alias='295')
    offerForwardPoints2: Optional[int] = Field(None, description='', alias='295')
    currency: Optional[int] = Field(None, description='', alias='295')

    noQuoteEntriess: List[NoQuoteEntries] = Field(default_factory=list)
