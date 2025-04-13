from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.sidecrossordmodgrp import SideCrossOrdModGrpComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrpComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.yielddata import YieldDataComponent
from src.models.fix.generated.components.peginstructions import PegInstructionsComponent
from src.models.fix.generated.components.discretioninstructions import DiscretionInstructionsComponent

class CrossOrderCancelReplaceRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    CrossID: str = Field(..., description='', alias='548')
    OrigCrossID: str = Field(..., description='', alias='551')
    CrossType: int = Field(..., description='', alias='549')
    CrossPrioritization: int = Field(..., description='', alias='550')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    HandlInst: Optional[str] = Field(None, description='', alias='21')
    ExecInst: Optional[List[str]] = Field(None, description='', alias='18')
    MinQty: Optional[float] = Field(None, description='', alias='110')
    MaxFloor: Optional[float] = Field(None, description='', alias='111')
    ExDestination: Optional[str] = Field(None, description='', alias='100')
    ProcessCode: Optional[str] = Field(None, description='', alias='81')
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    LocateReqd: Optional[bool] = Field(None, description='', alias='114')
    TransactTime: datetime = Field(..., description='', alias='60')
    OrdType: str = Field(..., description='', alias='40')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    StopPx: Optional[float] = Field(None, description='', alias='99')
    Currency: Optional[str] = Field(None, description='', alias='15')
    ComplianceID: Optional[str] = Field(None, description='', alias='376')
    IOIID: Optional[str] = Field(None, description='', alias='23')
    QuoteID: Optional[str] = Field(None, description='', alias='117')
    TimeInForce: Optional[str] = Field(None, description='', alias='59')
    EffectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    ExpireDate: Optional[date] = Field(None, description='', alias='432')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    GTBookingInst: Optional[int] = Field(None, description='', alias='427')
    MaxShow: Optional[float] = Field(None, description='', alias='210')
    TargetStrategy: Optional[int] = Field(None, description='', alias='847')
    TargetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    ParticipationRate: Optional[float] = Field(None, description='', alias='849')
    CancellationRights: Optional[str] = Field(None, description='', alias='480')
    MoneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    RegistID: Optional[str] = Field(None, description='', alias='513')
    Designation: Optional[str] = Field(None, description='', alias='494')
    SideCrossOrdModGrp: SideCrossOrdModGrpComponent = Field(..., description='SideCrossOrdModGrp component')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='TrdgSesGrp component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')
    PegInstructions: Optional[PegInstructionsComponent] = Field(None, description='PegInstructions component')
    DiscretionInstructions: Optional[DiscretionInstructionsComponent] = Field(None, description='DiscretionInstructions component')

