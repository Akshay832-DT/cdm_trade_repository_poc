from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrp
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.yielddata import YieldData
from src.models.fix.generated.components.cpctyconfgrp import CpctyConfGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsData
from src.models.fix.generated.components.commissiondata import CommissionData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.miscfeesgrp import MiscFeesGrp

class Confirmation(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    confirmid: str = Field(..., description='', alias='664')
    confirmrefid: Optional[str] = Field(None, description='', alias='772')
    confirmreqid: Optional[str] = Field(None, description='', alias='859')
    confirmtranstype: int = Field(..., description='', alias='666')
    confirmtype: int = Field(..., description='', alias='773')
    copymsgindicator: Optional[bool] = Field(None, description='', alias='797')
    legalconfirm: Optional[bool] = Field(None, description='', alias='650')
    confirmstatus: int = Field(..., description='', alias='665')
    allocid: Optional[str] = Field(None, description='', alias='70')
    secondaryallocid: Optional[str] = Field(None, description='', alias='793')
    individualallocid: Optional[str] = Field(None, description='', alias='467')
    transacttime: datetime = Field(..., description='', alias='60')
    tradedate: date = Field(..., description='', alias='75')
    allocqty: float = Field(..., description='', alias='80')
    qtytype: Optional[int] = Field(None, description='', alias='854')
    side: str = Field(..., description='', alias='54')
    currency: Optional[str] = Field(None, description='', alias='15')
    lastmkt: Optional[str] = Field(None, description='', alias='30')
    allocaccount: str = Field(..., description='', alias='79')
    allocacctidsource: Optional[int] = Field(None, description='', alias='661')
    allocaccounttype: Optional[int] = Field(None, description='', alias='798')
    avgpx: float = Field(..., description='', alias='6')
    avgpxprecision: Optional[int] = Field(None, description='', alias='74')
    pricetype: Optional[int] = Field(None, description='', alias='423')
    avgparpx: Optional[float] = Field(None, description='', alias='860')
    reportedpx: Optional[float] = Field(None, description='', alias='861')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    processcode: Optional[str] = Field(None, description='', alias='81')
    grosstradeamt: float = Field(..., description='', alias='381')
    numdaysinterest: Optional[int] = Field(None, description='', alias='157')
    exdate: Optional[date] = Field(None, description='', alias='230')
    accruedinterestrate: Optional[float] = Field(None, description='', alias='158')
    accruedinterestamt: Optional[float] = Field(None, description='', alias='159')
    interestatmaturity: Optional[float] = Field(None, description='', alias='738')
    endaccruedinterestamt: Optional[float] = Field(None, description='', alias='920')
    startcash: Optional[float] = Field(None, description='', alias='921')
    endcash: Optional[float] = Field(None, description='', alias='922')
    concession: Optional[float] = Field(None, description='', alias='238')
    totaltakedown: Optional[float] = Field(None, description='', alias='237')
    netmoney: float = Field(..., description='', alias='118')
    maturitynetmoney: Optional[float] = Field(None, description='', alias='890')
    settlcurramt: Optional[float] = Field(None, description='', alias='119')
    settlcurrency: Optional[str] = Field(None, description='', alias='120')
    settlcurrfxrate: Optional[float] = Field(None, description='', alias='155')
    settlcurrfxratecalc: Optional[str] = Field(None, description='', alias='156')
    settltype: Optional[str] = Field(None, description='', alias='63')
    settldate: Optional[date] = Field(None, description='', alias='64')
    sharedcommission: Optional[float] = Field(None, description='', alias='858')
    parties: Optional[Parties] = Field(None, description='Parties component')
    ordallocgrp: Optional[OrdAllocGrp] = Field(None, description='OrdAllocGrp component')
    trdregtimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    instrument: Instrument = Field(..., description='Instrument component')
    instrumentextension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undinstrmtgrp: UndInstrmtGrp = Field(..., description='UndInstrmtGrp component')
    instrmtleggrp: InstrmtLegGrp = Field(..., description='InstrmtLegGrp component')
    yielddata: Optional[YieldData] = Field(None, description='YieldData component')
    cpctyconfgrp: CpctyConfGrp = Field(..., description='CpctyConfGrp component')
    spreadorbenchmarkcurvedata: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    settlinstructionsdata: Optional[SettlInstructionsData] = Field(None, description='SettlInstructionsData component')
    commissiondata: Optional[CommissionData] = Field(None, description='CommissionData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    miscfeesgrp: Optional[MiscFeesGrp] = Field(None, description='MiscFeesGrp component')

