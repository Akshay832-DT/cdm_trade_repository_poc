from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.quotqualgrp import QuotQualGrp
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.legquotgrp import LegQuotGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.yielddata import YieldData

class QuoteResponse(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    quoterespid: str = Field(..., description='', alias='693')
    quoteid: Optional[str] = Field(None, description='', alias='117')
    quoteresptype: int = Field(..., description='', alias='694')
    clordid: Optional[str] = Field(None, description='', alias='11')
    ordercapacity: Optional[str] = Field(None, description='', alias='528')
    ioiid: Optional[str] = Field(None, description='', alias='23')
    quotetype: Optional[int] = Field(None, description='', alias='537')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    side: Optional[str] = Field(None, description='', alias='54')
    settltype: Optional[str] = Field(None, description='', alias='63')
    settldate: Optional[date] = Field(None, description='', alias='64')
    settldate2: Optional[date] = Field(None, description='', alias='193')
    orderqty2: Optional[float] = Field(None, description='', alias='192')
    currency: Optional[str] = Field(None, description='', alias='15')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: Optional[int] = Field(None, description='', alias='581')
    bidpx: Optional[float] = Field(None, description='', alias='132')
    offerpx: Optional[float] = Field(None, description='', alias='133')
    mktbidpx: Optional[float] = Field(None, description='', alias='645')
    mktofferpx: Optional[float] = Field(None, description='', alias='646')
    minbidsize: Optional[float] = Field(None, description='', alias='647')
    bidsize: Optional[float] = Field(None, description='', alias='134')
    minoffersize: Optional[float] = Field(None, description='', alias='648')
    offersize: Optional[float] = Field(None, description='', alias='135')
    validuntiltime: Optional[datetime] = Field(None, description='', alias='62')
    bidspotrate: Optional[float] = Field(None, description='', alias='188')
    offerspotrate: Optional[float] = Field(None, description='', alias='190')
    bidforwardpoints: Optional[float] = Field(None, description='', alias='189')
    offerforwardpoints: Optional[float] = Field(None, description='', alias='191')
    midpx: Optional[float] = Field(None, description='', alias='631')
    bidyield: Optional[float] = Field(None, description='', alias='632')
    midyield: Optional[float] = Field(None, description='', alias='633')
    offeryield: Optional[float] = Field(None, description='', alias='634')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    ordtype: Optional[str] = Field(None, description='', alias='40')
    bidforwardpoints2: Optional[float] = Field(None, description='', alias='642')
    offerforwardpoints2: Optional[float] = Field(None, description='', alias='643')
    settlcurrbidfxrate: Optional[float] = Field(None, description='', alias='656')
    settlcurrofferfxrate: Optional[float] = Field(None, description='', alias='657')
    settlcurrfxratecalc: Optional[str] = Field(None, description='', alias='156')
    commission: Optional[float] = Field(None, description='', alias='12')
    commtype: Optional[str] = Field(None, description='', alias='13')
    custordercapacity: Optional[int] = Field(None, description='', alias='582')
    exdestination: Optional[str] = Field(None, description='', alias='100')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    price: Optional[float] = Field(None, description='', alias='44')
    pricetype: Optional[int] = Field(None, description='', alias='423')
    quotqualgrp: Optional[QuotQualGrp] = Field(None, description='QuotQualGrp component')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Instrument = Field(..., description='Instrument component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    orderqtydata: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    legquotgrp: Optional[LegQuotGrp] = Field(None, description='LegQuotGrp component')
    spreadorbenchmarkcurvedata: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yielddata: Optional[YieldData] = Field(None, description='YieldData component')

