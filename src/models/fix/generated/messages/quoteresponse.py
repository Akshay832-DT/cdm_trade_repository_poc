from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.quotqualgrp import QuotQualGrpComponent
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.legquotgrp import LegQuotGrpComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.yielddata import YieldDataComponent

class QuoteResponse(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    QuoteRespID: str = Field(..., description='', alias='693')
    QuoteID: Optional[str] = Field(None, description='', alias='117')
    QuoteRespType: int = Field(..., description='', alias='694')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    IOIID: Optional[str] = Field(None, description='', alias='23')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Side: Optional[str] = Field(None, description='', alias='54')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    Currency: Optional[str] = Field(None, description='', alias='15')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    BidPx: Optional[float] = Field(None, description='', alias='132')
    OfferPx: Optional[float] = Field(None, description='', alias='133')
    MktBidPx: Optional[float] = Field(None, description='', alias='645')
    MktOfferPx: Optional[float] = Field(None, description='', alias='646')
    MinBidSize: Optional[float] = Field(None, description='', alias='647')
    BidSize: Optional[float] = Field(None, description='', alias='134')
    MinOfferSize: Optional[float] = Field(None, description='', alias='648')
    OfferSize: Optional[float] = Field(None, description='', alias='135')
    ValidUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    BidSpotRate: Optional[float] = Field(None, description='', alias='188')
    OfferSpotRate: Optional[float] = Field(None, description='', alias='190')
    BidForwardPoints: Optional[float] = Field(None, description='', alias='189')
    OfferForwardPoints: Optional[float] = Field(None, description='', alias='191')
    MidPx: Optional[float] = Field(None, description='', alias='631')
    BidYield: Optional[float] = Field(None, description='', alias='632')
    MidYield: Optional[float] = Field(None, description='', alias='633')
    OfferYield: Optional[float] = Field(None, description='', alias='634')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    BidForwardPoints2: Optional[float] = Field(None, description='', alias='642')
    OfferForwardPoints2: Optional[float] = Field(None, description='', alias='643')
    SettlCurrBidFxRate: Optional[float] = Field(None, description='', alias='656')
    SettlCurrOfferFxRate: Optional[float] = Field(None, description='', alias='657')
    SettlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    Commission: Optional[float] = Field(None, description='', alias='12')
    CommType: Optional[str] = Field(None, description='', alias='13')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    ExDestination: Optional[str] = Field(None, description='', alias='100')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Price: Optional[float] = Field(None, description='', alias='44')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    QuotQualGrp: Optional[QuotQualGrpComponent] = Field(None, description='QuotQualGrp component')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='OrderQtyData component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    LegQuotGrp: Optional[LegQuotGrpComponent] = Field(None, description='LegQuotGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')

