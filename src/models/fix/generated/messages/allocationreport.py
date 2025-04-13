from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrp
from src.models.fix.generated.components.execallocgrp import ExecAllocGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.yielddata import YieldData
from src.models.fix.generated.components.allocgrp import AllocGrp

class AllocationReport(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    allocreportid: str = Field(..., description='', alias='755')
    allocid: Optional[str] = Field(None, description='', alias='70')
    alloctranstype: str = Field(..., description='', alias='71')
    allocreportrefid: Optional[str] = Field(None, description='', alias='795')
    alloccancreplacereason: Optional[int] = Field(None, description='', alias='796')
    secondaryallocid: Optional[str] = Field(None, description='', alias='793')
    allocreporttype: int = Field(..., description='', alias='794')
    allocstatus: int = Field(..., description='', alias='87')
    allocrejcode: Optional[int] = Field(None, description='', alias='88')
    refallocid: Optional[str] = Field(None, description='', alias='72')
    allocintermedreqtype: Optional[int] = Field(None, description='', alias='808')
    alloclinkid: Optional[str] = Field(None, description='', alias='196')
    alloclinktype: Optional[int] = Field(None, description='', alias='197')
    bookingrefid: Optional[str] = Field(None, description='', alias='466')
    allocnoorderstype: int = Field(..., description='', alias='857')
    previouslyreported: Optional[bool] = Field(None, description='', alias='570')
    reversalindicator: Optional[bool] = Field(None, description='', alias='700')
    matchtype: Optional[str] = Field(None, description='', alias='574')
    side: str = Field(..., description='', alias='54')
    quantity: float = Field(..., description='', alias='53')
    qtytype: Optional[int] = Field(None, description='', alias='854')
    lastmkt: Optional[str] = Field(None, description='', alias='30')
    tradeoriginationdate: Optional[date] = Field(None, description='', alias='229')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    pricetype: Optional[int] = Field(None, description='', alias='423')
    avgpx: float = Field(..., description='', alias='6')
    avgparpx: Optional[float] = Field(None, description='', alias='860')
    currency: Optional[str] = Field(None, description='', alias='15')
    avgpxprecision: Optional[int] = Field(None, description='', alias='74')
    tradedate: date = Field(..., description='', alias='75')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    settltype: Optional[str] = Field(None, description='', alias='63')
    settldate: Optional[date] = Field(None, description='', alias='64')
    bookingtype: Optional[int] = Field(None, description='', alias='775')
    grosstradeamt: Optional[float] = Field(None, description='', alias='381')
    concession: Optional[float] = Field(None, description='', alias='238')
    totaltakedown: Optional[float] = Field(None, description='', alias='237')
    netmoney: Optional[float] = Field(None, description='', alias='118')
    positioneffect: Optional[str] = Field(None, description='', alias='77')
    autoacceptindicator: Optional[bool] = Field(None, description='', alias='754')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    numdaysinterest: Optional[int] = Field(None, description='', alias='157')
    accruedinterestrate: Optional[float] = Field(None, description='', alias='158')
    accruedinterestamt: Optional[float] = Field(None, description='', alias='159')
    totalaccruedinterestamt: Optional[float] = Field(None, description='', alias='540')
    interestatmaturity: Optional[float] = Field(None, description='', alias='738')
    endaccruedinterestamt: Optional[float] = Field(None, description='', alias='920')
    startcash: Optional[float] = Field(None, description='', alias='921')
    endcash: Optional[float] = Field(None, description='', alias='922')
    legalconfirm: Optional[bool] = Field(None, description='', alias='650')
    totnoallocs: Optional[int] = Field(None, description='', alias='892')
    lastfragment: Optional[bool] = Field(None, description='', alias='893')
    ordallocgrp: Optional[OrdAllocGrp] = Field(None, description='OrdAllocGrp component')
    execallocgrp: Optional[ExecAllocGrp] = Field(None, description='ExecAllocGrp component')
    instrument: Instrument = Field(..., description='Instrument component')
    instrumentextension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    spreadorbenchmarkcurvedata: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    parties: Optional[Parties] = Field(None, description='Parties component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    yielddata: Optional[YieldData] = Field(None, description='YieldData component')
    allocgrp: Optional[AllocGrp] = Field(None, description='AllocGrp component')

