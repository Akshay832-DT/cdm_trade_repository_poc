"""FIX message model for CrossOrderCancelReplaceRequest (t).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.discretioninstructions import DiscretionInstructionsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.peginstructions import PegInstructionsComponent
from ..components.sidecrossordmodgrp import SideCrossOrdModGrpComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.stipulations import StipulationsComponent
from ..components.trdgsesgrp import TrdgSesGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent
from ..components.yielddata import YieldDataComponent

class CrossOrderCancelReplaceRequestMessage(FIXMessageBase):
    """FIX message model for CrossOrderCancelReplaceRequest."""

    MsgType: str = Field("t", alias="35")

    OrderID: Optional[str] = Field(None, alias='37', description='')
    CrossID: str = Field(..., alias='548', description='')
    OrigCrossID: str = Field(..., alias='551', description='')
    CrossType: int = Field(..., alias='549', description='')
    CrossPrioritization: int = Field(..., alias='550', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    HandlInst: Optional[str] = Field(None, alias='21', description='')
    ExecInst: Optional[List[str]] = Field(None, alias='18', description='')
    MinQty: Optional[float] = Field(None, alias='110', description='')
    MaxFloor: Optional[float] = Field(None, alias='111', description='')
    ExDestination: Optional[str] = Field(None, alias='100', description='')
    ProcessCode: Optional[str] = Field(None, alias='81', description='')
    PrevClosePx: Optional[float] = Field(None, alias='140', description='')
    LocateReqd: Optional[bool] = Field(None, alias='114', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    OrdType: str = Field(..., alias='40', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    StopPx: Optional[float] = Field(None, alias='99', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    ComplianceID: Optional[str] = Field(None, alias='376', description='')
    IOIID: Optional[str] = Field(None, alias='23', description='')
    QuoteID: Optional[str] = Field(None, alias='117', description='')
    TimeInForce: Optional[str] = Field(None, alias='59', description='')
    EffectiveTime: Optional[datetime] = Field(None, alias='168', description='')
    ExpireDate: Optional[date] = Field(None, alias='432', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    GTBookingInst: Optional[int] = Field(None, alias='427', description='')
    MaxShow: Optional[float] = Field(None, alias='210', description='')
    TargetStrategy: Optional[int] = Field(None, alias='847', description='')
    TargetStrategyParameters: Optional[str] = Field(None, alias='848', description='')
    ParticipationRate: Optional[float] = Field(None, alias='849', description='')
    CancellationRights: Optional[str] = Field(None, alias='480', description='')
    MoneyLaunderingStatus: Optional[str] = Field(None, alias='481', description='')
    RegistID: Optional[str] = Field(None, alias='513', description='')
    Designation: Optional[str] = Field(None, alias='494', description='')
    SideCrossOrdModGrp: SideCrossOrdModGrpComponent = Field(..., description='')
    Instrument: InstrumentComponent = Field(..., description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')
    PegInstructions: Optional[PegInstructionsComponent] = Field(None, description='')
    DiscretionInstructions: Optional[DiscretionInstructionsComponent] = Field(None, description='')

