"""
FIX 4.4 QuotReqRjctGrp Component

This module contains the Pydantic model for the QuotReqRjctGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoRelatedSymGroup(FIXComponentBase):
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
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    Price2: Optional[float] = Field(None, description='', alias='640')


class QuotReqRjctGrpComponent(FIXComponentBase):
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
    
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='OrderQtyData component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    QuotReqLegsGrp: Optional[QuotReqLegsGrpComponent] = Field(None, description='QuotReqLegsGrp component')
    QuotQualGrp: Optional[QuotQualGrpComponent] = Field(None, description='QuotQualGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    NoRelatedSym: Optional[int] = Field(None, description='Number of NoRelatedSym entries', alias='')
    NoRelatedSym_items: List[NoRelatedSymGroup] = Field(default_factory=list)
