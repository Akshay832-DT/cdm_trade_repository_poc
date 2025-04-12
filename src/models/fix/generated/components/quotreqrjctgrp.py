"""
FIX 4.4 QuotReqRjctGrp Component

This module contains the Pydantic model for the QuotReqRjctGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class QuotReqRjctGrp(FIXMessageBase):
    """
    FIX 4.4 QuotReqRjctGrp Component
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
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
    quoteRequestType: Optional[int] = Field(None, description='', alias='303')
    quoteType: Optional[int] = Field(None, description='', alias='537')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    side: Optional[str] = Field(None, description='', alias='54')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    settlDate2: Optional[date] = Field(None, description='', alias='193')
    orderQty2: Optional[float] = Field(None, description='', alias='192')
    currency: Optional[str] = Field(None, description='', alias='15')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    quotePriceType: Optional[int] = Field(None, description='', alias='692')
    ordType: Optional[str] = Field(None, description='', alias='40')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    priceType: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    price2: Optional[float] = Field(None, description='', alias='640')
    instrument: str = Field(None)
    financingDetails: Optional[str] = Field(None)
    undInstrmtGrp: Optional[str] = Field(None)
    orderQtyData: Optional[str] = Field(None)
    stipulations: Optional[str] = Field(None)
    quotReqLegsGrp: Optional[str] = Field(None)
    quotQualGrp: Optional[str] = Field(None)
    spreadOrBenchmarkCurveData: Optional[str] = Field(None)
    yieldData: Optional[str] = Field(None)
    parties: Optional[str] = Field(None)


class NoRelatedSym(FIXMessageBase):
    """
    NoRelatedSym group fields
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
    prevClosePx: Optional[int] = Field(None, description='', alias='146')
    quoteRequestType: Optional[int] = Field(None, description='', alias='146')
    quoteType: Optional[int] = Field(None, description='', alias='146')
    tradingSessionID: Optional[int] = Field(None, description='', alias='146')
    tradingSessionSubID: Optional[int] = Field(None, description='', alias='146')
    tradeOriginationDate: Optional[int] = Field(None, description='', alias='146')
    side: Optional[int] = Field(None, description='', alias='146')
    qtyType: Optional[int] = Field(None, description='', alias='146')
    settlType: Optional[int] = Field(None, description='', alias='146')
    settlDate: Optional[int] = Field(None, description='', alias='146')
    settlDate2: Optional[int] = Field(None, description='', alias='146')
    orderQty2: Optional[int] = Field(None, description='', alias='146')
    currency: Optional[int] = Field(None, description='', alias='146')
    account: Optional[int] = Field(None, description='', alias='146')
    acctIDSource: Optional[int] = Field(None, description='', alias='146')
    accountType: Optional[int] = Field(None, description='', alias='146')
    quotePriceType: Optional[int] = Field(None, description='', alias='146')
    ordType: Optional[int] = Field(None, description='', alias='146')
    expireTime: Optional[int] = Field(None, description='', alias='146')
    transactTime: Optional[int] = Field(None, description='', alias='146')
    priceType: Optional[int] = Field(None, description='', alias='146')
    price: Optional[int] = Field(None, description='', alias='146')
    price2: Optional[int] = Field(None, description='', alias='146')

    noRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
