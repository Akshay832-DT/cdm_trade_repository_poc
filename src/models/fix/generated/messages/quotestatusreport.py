"""FIX message model for QuoteStatusReport (AI).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrument import InstrumentComponent
from ..components.legquotstatgrp import LegQuotStatGrpComponent
from ..components.orderqtydata import OrderQtyDataComponent
from ..components.parties import PartiesComponent
from ..components.quotqualgrp import QuotQualGrpComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.stipulations import StipulationsComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent
from ..components.yielddata import YieldDataComponent

class QuoteStatusReportMessage(FIXMessageBase):
    """FIX message model for QuoteStatusReport."""

    MsgType: str = Field("AI", alias="35")

    QuoteStatusReqID: Optional[str] = Field(None, alias='649', description='')
    QuoteReqID: Optional[str] = Field(None, alias='131', description='')
    QuoteID: str = Field(..., alias='117', description='')
    QuoteRespID: Optional[str] = Field(None, alias='693', description='')
    QuoteType: Optional[int] = Field(None, alias='537', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    SettlDate2: Optional[date] = Field(None, alias='193', description='')
    OrderQty2: Optional[float] = Field(None, alias='192', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    BidPx: Optional[float] = Field(None, alias='132', description='')
    OfferPx: Optional[float] = Field(None, alias='133', description='')
    MktBidPx: Optional[float] = Field(None, alias='645', description='')
    MktOfferPx: Optional[float] = Field(None, alias='646', description='')
    MinBidSize: Optional[float] = Field(None, alias='647', description='')
    BidSize: Optional[float] = Field(None, alias='134', description='')
    MinOfferSize: Optional[float] = Field(None, alias='648', description='')
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
    OrdType: Optional[str] = Field(None, alias='40', description='')
    BidForwardPoints2: Optional[float] = Field(None, alias='642', description='')
    OfferForwardPoints2: Optional[float] = Field(None, alias='643', description='')
    SettlCurrBidFxRate: Optional[float] = Field(None, alias='656', description='')
    SettlCurrOfferFxRate: Optional[float] = Field(None, alias='657', description='')
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias='156', description='')
    CommType: Optional[str] = Field(None, alias='13', description='')
    Commission: Optional[float] = Field(None, alias='12', description='')
    CustOrderCapacity: Optional[int] = Field(None, alias='582', description='')
    ExDestination: Optional[str] = Field(None, alias='100', description='')
    QuoteStatus: Optional[int] = Field(None, alias='297', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    LegQuotStatGrp: Optional[LegQuotStatGrpComponent] = Field(None, description='')
    QuotQualGrp: Optional[QuotQualGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')

