"""
FIX 4.4 QuotEntryGrp Component

This module contains the Pydantic model for the QuotEntryGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp


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
    
    quoteEntryID: str = Field(..., description='', alias='299')
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
    
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    noQuoteEntries: Optional[int] = Field(None, description='Number of NoQuoteEntries entries', alias='295')
    noQuoteEntries_items: List[NoQuoteEntries] = Field(default_factory=list)
