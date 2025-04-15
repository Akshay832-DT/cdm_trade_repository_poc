"""FIX message model for QuoteResponse (AJ).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrument import InstrumentComponent
from ..components.legquotgrp import LegQuotGrpComponent
from ..components.orderqtydata import OrderQtyDataComponent
from ..components.parties import PartiesComponent
from ..components.quotqualgrp import QuotQualGrpComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.stipulations import StipulationsComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent
from ..components.yielddata import YieldDataComponent

class QuoteResponseMessage(FIXMessageBase):
    """FIX message model for QuoteResponse."""

    MsgType: str = Field("AJ", alias="35")

    QuoteRespID: str = Field(..., alias='693', description='')
    QuoteID: Optional[str] = Field(None, alias='117', description='')
    QuoteRespType: int = Field(..., alias='694', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    OrderCapacity: Optional[str] = Field(None, alias='528', description='')
    IOIID: Optional[str] = Field(None, alias='23', description='')
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
    Commission: Optional[float] = Field(None, alias='12', description='')
    CommType: Optional[str] = Field(None, alias='13', description='')
    CustOrderCapacity: Optional[int] = Field(None, alias='582', description='')
    ExDestination: Optional[str] = Field(None, alias='100', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    QuotQualGrp: Optional[QuotQualGrpComponent] = Field(None, description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    LegQuotGrp: Optional[LegQuotGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')

