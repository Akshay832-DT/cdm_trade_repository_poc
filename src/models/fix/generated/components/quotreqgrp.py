"""
FIX 4.4 QuotReqGrp Component

This module contains the Pydantic model for the QuotReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.quotreqlegsgrp import QuotReqLegsGrp
from src.models.fix.generated.components.quotqualgrp import QuotQualGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.yielddata import YieldData
from src.models.fix.generated.components.parties import Parties


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
    validUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    priceType: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    price2: Optional[float] = Field(None, description='', alias='640')


class QuotReqGrp(FIXMessageBase):
    """
    FIX 4.4 QuotReqGrp Component
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
    
    instrument: Instrument = Field(..., description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    orderQtyData: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    quotReqLegsGrp: Optional[QuotReqLegsGrp] = Field(None, description='QuotReqLegsGrp component')
    quotQualGrp: Optional[QuotQualGrp] = Field(None, description='QuotQualGrp component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')
    parties: Optional[Parties] = Field(None, description='Parties component')
    noRelatedSym: Optional[int] = Field(None, description='Number of NoRelatedSym entries', alias='146')
    noRelatedSym_items: List[NoRelatedSym] = Field(default_factory=list)
