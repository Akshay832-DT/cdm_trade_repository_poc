"""
FIX NewOrderCross Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
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


# Forward references for components to avoid circular imports
DiscretionInstructionsComponent = ForwardRef('DiscretionInstructionsComponent')
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
PegInstructionsComponent = ForwardRef('PegInstructionsComponent')
SideCrossOrdModGrpComponent = ForwardRef('SideCrossOrdModGrpComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
TrdgSesGrpComponent = ForwardRef('TrdgSesGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class NewOrderCrossMessage(FIXMessageBase):
    """NewOrderCross Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["NewOrderCross"] = Field("NewOrderCross", alias="35", description="Message Type")

    CrossID: Optional[str] = Field(None, alias="548", description="")
    CrossType: Optional[int] = Field(None, alias="549", description="")
    CrossPrioritization: Optional[int] = Field(None, alias="550", description="")
    SettlType: Optional[str] = Field(None, alias="63", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    HandlInst: Optional[str] = Field(None, alias="21", description="")
    ExecInst: Optional[List[str]] = Field(None, alias="18", description="")
    MinQty: Optional[float] = Field(None, alias="110", description="")
    MaxFloor: Optional[float] = Field(None, alias="111", description="")
    ExDestination: Optional[str] = Field(None, alias="100", description="")
    ProcessCode: Optional[str] = Field(None, alias="81", description="")
    PrevClosePx: Optional[float] = Field(None, alias="140", description="")
    LocateReqd: Optional[bool] = Field(None, alias="114", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    OrdType: Optional[str] = Field(None, alias="40", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    Price: Optional[float] = Field(None, alias="44", description="")
    StopPx: Optional[float] = Field(None, alias="99", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    ComplianceID: Optional[str] = Field(None, alias="376", description="")
    IOIID: Optional[str] = Field(None, alias="23", description="")
    QuoteID: Optional[str] = Field(None, alias="117", description="")
    TimeInForce: Optional[str] = Field(None, alias="59", description="")
    EffectiveTime: Optional[datetime] = Field(None, alias="168", description="")
    ExpireDate: Optional[date] = Field(None, alias="432", description="")
    ExpireTime: Optional[datetime] = Field(None, alias="126", description="")
    GTBookingInst: Optional[int] = Field(None, alias="427", description="")
    MaxShow: Optional[float] = Field(None, alias="210", description="")
    TargetStrategy: Optional[int] = Field(None, alias="847", description="")
    TargetStrategyParameters: Optional[str] = Field(None, alias="848", description="")
    ParticipationRate: Optional[float] = Field(None, alias="849", description="")
    CancellationRights: Optional[str] = Field(None, alias="480", description="")
    MoneyLaunderingStatus: Optional[str] = Field(None, alias="481", description="")
    RegistID: Optional[str] = Field(None, alias="513", description="")
    Designation: Optional[str] = Field(None, alias="494", description="")
    SideCrossOrdModGrp: ForwardRef('SideCrossOrdModGrpComponent') = Field(None, description="SideCrossOrdModGrp Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    TrdgSesGrp: ForwardRef('TrdgSesGrpComponent') = Field(None, description="TrdgSesGrp Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    YieldData: ForwardRef('YieldDataComponent') = Field(None, description="YieldData Component")
    PegInstructions: ForwardRef('PegInstructionsComponent') = Field(None, description="PegInstructions Component")
    DiscretionInstructions: ForwardRef('DiscretionInstructionsComponent') = Field(None, description="DiscretionInstructions Component")

    @model_validator(mode='after')
    def resolve_forward_refs(self) -> 'FIXMessageBase':
        """Resolve forward references."""
        for field_name, field_value in self.model_fields.items():
            if isinstance(field_value.annotation, ForwardRef):
                field_value.annotation = eval(field_value.annotation.__forward_arg__)
        return self

    def __str__(self) -> str:
        fields = []
        if self.MsgType is not None:
            fields.append(f"MsgType={self.MsgType}")
        if self.CrossID is not None:
            fields.append(f"CrossID={self.CrossID}")
        if self.CrossType is not None:
            fields.append(f"CrossType={self.CrossType}")
        if self.CrossPrioritization is not None:
            fields.append(f"CrossPrioritization={self.CrossPrioritization}")
        if self.SettlType is not None:
            fields.append(f"SettlType={self.SettlType}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.HandlInst is not None:
            fields.append(f"HandlInst={self.HandlInst}")
        if self.ExecInst is not None:
            fields.append(f"ExecInst={self.ExecInst}")
        if self.MinQty is not None:
            fields.append(f"MinQty={self.MinQty}")
        if self.MaxFloor is not None:
            fields.append(f"MaxFloor={self.MaxFloor}")
        if self.ExDestination is not None:
            fields.append(f"ExDestination={self.ExDestination}")
        if self.ProcessCode is not None:
            fields.append(f"ProcessCode={self.ProcessCode}")
        if self.PrevClosePx is not None:
            fields.append(f"PrevClosePx={self.PrevClosePx}")
        if self.LocateReqd is not None:
            fields.append(f"LocateReqd={self.LocateReqd}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.OrdType is not None:
            fields.append(f"OrdType={self.OrdType}")
        if self.PriceType is not None:
            fields.append(f"PriceType={self.PriceType}")
        if self.Price is not None:
            fields.append(f"Price={self.Price}")
        if self.StopPx is not None:
            fields.append(f"StopPx={self.StopPx}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.ComplianceID is not None:
            fields.append(f"ComplianceID={self.ComplianceID}")
        if self.IOIID is not None:
            fields.append(f"IOIID={self.IOIID}")
        if self.QuoteID is not None:
            fields.append(f"QuoteID={self.QuoteID}")
        if self.TimeInForce is not None:
            fields.append(f"TimeInForce={self.TimeInForce}")
        if self.EffectiveTime is not None:
            fields.append(f"EffectiveTime={self.EffectiveTime}")
        if self.ExpireDate is not None:
            fields.append(f"ExpireDate={self.ExpireDate}")
        if self.ExpireTime is not None:
            fields.append(f"ExpireTime={self.ExpireTime}")
        if self.GTBookingInst is not None:
            fields.append(f"GTBookingInst={self.GTBookingInst}")
        if self.MaxShow is not None:
            fields.append(f"MaxShow={self.MaxShow}")
        if self.TargetStrategy is not None:
            fields.append(f"TargetStrategy={self.TargetStrategy}")
        if self.TargetStrategyParameters is not None:
            fields.append(f"TargetStrategyParameters={self.TargetStrategyParameters}")
        if self.ParticipationRate is not None:
            fields.append(f"ParticipationRate={self.ParticipationRate}")
        if self.CancellationRights is not None:
            fields.append(f"CancellationRights={self.CancellationRights}")
        if self.MoneyLaunderingStatus is not None:
            fields.append(f"MoneyLaunderingStatus={self.MoneyLaunderingStatus}")
        if self.RegistID is not None:
            fields.append(f"RegistID={self.RegistID}")
        if self.Designation is not None:
            fields.append(f"Designation={self.Designation}")
        if self.SideCrossOrdModGrp is not None:
            fields.append(f"SideCrossOrdModGrp={self.SideCrossOrdModGrp}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.TrdgSesGrp is not None:
            fields.append(f"TrdgSesGrp={self.TrdgSesGrp}")
        if self.Stipulations is not None:
            fields.append(f"Stipulations={self.Stipulations}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        if self.PegInstructions is not None:
            fields.append(f"PegInstructions={self.PegInstructions}")
        if self.DiscretionInstructions is not None:
            fields.append(f"DiscretionInstructions={self.DiscretionInstructions}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
NewOrderCrossMessage.model_rebuild()
