"""
FIX 4.4 Quote Message

This module contains the Pydantic model for the Quote message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.legquotgrp import LegQuotGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.quotqualgrp import QuotQualGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.yielddata import YieldData


class Quote(FIXMessageBase):
    """
    FIX 4.4 Quote Message
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
    
    # Set the message type for this message
    msgType: Literal["S"] = Field("S", alias='35')
    
    # Message-specific fields
    quoteReqID: Optional[str] = Field(None, description='', alias='131')
    quoteID: Optional[str] = Field(None, description='', alias='117')
    quoteRespID: Optional[str] = Field(None, description='', alias='693')
    quoteType: Optional[int] = Field(None, description='', alias='537')
    quoteResponseLevel: Optional[int] = Field(None, description='', alias='301')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    side: Optional[str] = Field(None, description='', alias='54')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    settlDate2: Optional[date] = Field(None, description='', alias='193')
    orderQty2: Optional[float] = Field(None, description='', alias='192')
    currency: Optional[str] = Field(None, description='', alias='15')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    bidPx: Optional[float] = Field(None, description='', alias='132')
    offerPx: Optional[float] = Field(None, description='', alias='133')
    mktBidPx: Optional[float] = Field(None, description='', alias='645')
    mktOfferPx: Optional[float] = Field(None, description='', alias='646')
    minBidSize: Optional[float] = Field(None, description='', alias='647')
    bidSize: Optional[float] = Field(None, description='', alias='134')
    minOfferSize: Optional[float] = Field(None, description='', alias='648')
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
    ordType: Optional[str] = Field(None, description='', alias='40')
    bidForwardPoints2: Optional[float] = Field(None, description='', alias='642')
    offerForwardPoints2: Optional[float] = Field(None, description='', alias='643')
    settlCurrBidFxRate: Optional[float] = Field(None, description='', alias='656')
    settlCurrOfferFxRate: Optional[float] = Field(None, description='', alias='657')
    settlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    commType: Optional[str] = Field(None, description='', alias='13')
    commission: Optional[float] = Field(None, description='', alias='12')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    exDestination: Optional[str] = Field(None, description='', alias='100')
    orderCapacity: Optional[str] = Field(None, description='', alias='528')
    priceType: Optional[int] = Field(None, description='', alias='423')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    quotQualGrp: Optional[QuotQualGrp] = Field(None, description='QuotQualGrp component')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    orderQtyData: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    legQuotGrp: Optional[LegQuotGrp] = Field(None, description='LegQuotGrp component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
