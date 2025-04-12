"""
FIX 4.4 QuotReqGrp Component

This module contains the Pydantic model for the QuotReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class QuotReqGrp(TradeModel):
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
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    QuoteRequestType: Optional[int] = Field(None, description='', alias='303')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    Side: Optional[str] = Field(None, description='', alias='54')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    Currency: Optional[str] = Field(None, description='', alias='15')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    QuotePriceType: Optional[int] = Field(None, description='', alias='692')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    ValidUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    Price2: Optional[float] = Field(None, description='', alias='640')
    Instrument: str = Field(None)
    FinancingDetails: Optional[str] = Field(None)
    UndInstrmtGrp: Optional[str] = Field(None)
    OrderQtyData: Optional[str] = Field(None)
    Stipulations: Optional[str] = Field(None)
    QuotReqLegsGrp: Optional[str] = Field(None)
    QuotQualGrp: Optional[str] = Field(None)
    SpreadOrBenchmarkCurveData: Optional[str] = Field(None)
    YieldData: Optional[str] = Field(None)
    Parties: Optional[str] = Field(None)


class NoRelatedSym(TradeModel):
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
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    QuoteRequestType: Optional[int] = Field(None, description='', alias='303')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    Side: Optional[str] = Field(None, description='', alias='54')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    Currency: Optional[str] = Field(None, description='', alias='15')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    QuotePriceType: Optional[int] = Field(None, description='', alias='692')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    ValidUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    Price2: Optional[float] = Field(None, description='', alias='640')

    NoRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
