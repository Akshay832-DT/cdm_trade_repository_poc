from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.sidecrossordmodgrp import SideCrossOrdModGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrp
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.yielddata import YieldData
from src.models.fix.generated.components.peginstructions import PegInstructions
from src.models.fix.generated.components.discretioninstructions import DiscretionInstructions

class NewOrderCross(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    crossid: str = Field(..., description='', alias='548')
    crosstype: int = Field(..., description='', alias='549')
    crossprioritization: int = Field(..., description='', alias='550')
    settltype: Optional[str] = Field(None, description='', alias='63')
    settldate: Optional[date] = Field(None, description='', alias='64')
    handlinst: Optional[str] = Field(None, description='', alias='21')
    execinst: Optional[List[str]] = Field(None, description='', alias='18')
    minqty: Optional[float] = Field(None, description='', alias='110')
    maxfloor: Optional[float] = Field(None, description='', alias='111')
    exdestination: Optional[str] = Field(None, description='', alias='100')
    processcode: Optional[str] = Field(None, description='', alias='81')
    prevclosepx: Optional[float] = Field(None, description='', alias='140')
    locatereqd: Optional[bool] = Field(None, description='', alias='114')
    transacttime: datetime = Field(..., description='', alias='60')
    ordtype: str = Field(..., description='', alias='40')
    pricetype: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    stoppx: Optional[float] = Field(None, description='', alias='99')
    currency: Optional[str] = Field(None, description='', alias='15')
    complianceid: Optional[str] = Field(None, description='', alias='376')
    ioiid: Optional[str] = Field(None, description='', alias='23')
    quoteid: Optional[str] = Field(None, description='', alias='117')
    timeinforce: Optional[str] = Field(None, description='', alias='59')
    effectivetime: Optional[datetime] = Field(None, description='', alias='168')
    expiredate: Optional[date] = Field(None, description='', alias='432')
    expiretime: Optional[datetime] = Field(None, description='', alias='126')
    gtbookinginst: Optional[int] = Field(None, description='', alias='427')
    maxshow: Optional[float] = Field(None, description='', alias='210')
    targetstrategy: Optional[int] = Field(None, description='', alias='847')
    targetstrategyparameters: Optional[str] = Field(None, description='', alias='848')
    participationrate: Optional[float] = Field(None, description='', alias='849')
    cancellationrights: Optional[str] = Field(None, description='', alias='480')
    moneylaunderingstatus: Optional[str] = Field(None, description='', alias='481')
    registid: Optional[str] = Field(None, description='', alias='513')
    designation: Optional[str] = Field(None, description='', alias='494')
    sidecrossordmodgrp: SideCrossOrdModGrp = Field(..., description='SideCrossOrdModGrp component')
    instrument: Instrument = Field(..., description='Instrument component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    trdgsesgrp: Optional[TrdgSesGrp] = Field(None, description='TrdgSesGrp component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    spreadorbenchmarkcurvedata: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yielddata: Optional[YieldData] = Field(None, description='YieldData component')
    peginstructions: Optional[PegInstructions] = Field(None, description='PegInstructions component')
    discretioninstructions: Optional[DiscretionInstructions] = Field(None, description='DiscretionInstructions component')

