"""
FIX Component Model - QuotReqGrp
"""

from ..base import FIXComponentBase
from .financingdetails import FinancingDetailsComponent
from .instrument import InstrumentComponent
from .orderqtydata import OrderQtyDataComponent
from .parties import PartiesComponent
from .quotqualgrp import QuotQualGrpComponent
from .quotreqlegsgrp import QuotReqLegsGrpComponent
from .spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from .stipulations import StipulationsComponent
from .undinstrmtgrp import UndInstrmtGrpComponent
from .yielddata import YieldDataComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoRelatedSymGroup(FIXComponentBase):

    """FIX Group - NoRelatedSym"""

    PrevClosePx: Optional[float] = Field(None, alias='140', description='')
    QuoteRequestType: Optional[int] = Field(None, alias='303', description='')
    QuoteType: Optional[int] = Field(None, alias='537', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    TradeOriginationDate: Optional[date] = Field(None, alias='229', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    SettlDate2: Optional[date] = Field(None, alias='193', description='')
    OrderQty2: Optional[float] = Field(None, alias='192', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    QuotePriceType: Optional[int] = Field(None, alias='692', description='')
    OrdType: Optional[str] = Field(None, alias='40', description='')
    ValidUntilTime: Optional[datetime] = Field(None, alias='62', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    Price2: Optional[float] = Field(None, alias='640', description='')
    Instrument: InstrumentComponent
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    QuotReqLegsGrp: Optional[QuotReqLegsGrpComponent] = Field(None, description='')
    QuotQualGrp: Optional[QuotQualGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')



class QuotReqGrpComponent(FIXComponentBase):
    """FIX Component - QuotReqGrp"""


