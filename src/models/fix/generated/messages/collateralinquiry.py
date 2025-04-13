from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.collinqqualgrp import CollInqQualGrp
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.execcollgrp import ExecCollGrp
from src.models.fix.generated.components.trdcollgrp import TrdCollGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsData

class CollateralInquiry(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    collinquiryid: Optional[str] = Field(None, description='', alias='909')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    responsetransporttype: Optional[int] = Field(None, description='', alias='725')
    responsedestination: Optional[str] = Field(None, description='', alias='726')
    account: Optional[str] = Field(None, description='', alias='1')
    accounttype: Optional[int] = Field(None, description='', alias='581')
    clordid: Optional[str] = Field(None, description='', alias='11')
    orderid: Optional[str] = Field(None, description='', alias='37')
    secondaryorderid: Optional[str] = Field(None, description='', alias='198')
    secondaryclordid: Optional[str] = Field(None, description='', alias='526')
    settldate: Optional[date] = Field(None, description='', alias='64')
    quantity: Optional[float] = Field(None, description='', alias='53')
    qtytype: Optional[int] = Field(None, description='', alias='854')
    currency: Optional[str] = Field(None, description='', alias='15')
    marginexcess: Optional[float] = Field(None, description='', alias='899')
    totalnetvalue: Optional[float] = Field(None, description='', alias='900')
    cashoutstanding: Optional[float] = Field(None, description='', alias='901')
    side: Optional[str] = Field(None, description='', alias='54')
    price: Optional[float] = Field(None, description='', alias='44')
    pricetype: Optional[int] = Field(None, description='', alias='423')
    accruedinterestamt: Optional[float] = Field(None, description='', alias='159')
    endaccruedinterestamt: Optional[float] = Field(None, description='', alias='920')
    startcash: Optional[float] = Field(None, description='', alias='921')
    endcash: Optional[float] = Field(None, description='', alias='922')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    settlsessid: Optional[str] = Field(None, description='', alias='716')
    settlsesssubid: Optional[str] = Field(None, description='', alias='717')
    clearingbusinessdate: Optional[date] = Field(None, description='', alias='715')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    collinqqualgrp: Optional[CollInqQualGrp] = Field(None, description='CollInqQualGrp component')
    parties: Optional[Parties] = Field(None, description='Parties component')
    execcollgrp: Optional[ExecCollGrp] = Field(None, description='ExecCollGrp component')
    trdcollgrp: Optional[TrdCollGrp] = Field(None, description='TrdCollGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    trdregtimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    spreadorbenchmarkcurvedata: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    settlinstructionsdata: Optional[SettlInstructionsData] = Field(None, description='SettlInstructionsData component')

