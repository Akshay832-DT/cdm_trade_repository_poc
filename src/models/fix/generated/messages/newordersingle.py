"""
FIX NewOrderSingle Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.commissiondata import CommissionDataComponent
    from ..components.discretioninstructions import DiscretionInstructionsComponent
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrument import InstrumentComponent
    from ..components.orderqtydata import OrderQtyDataComponent
    from ..components.parties import PartiesComponent
    from ..components.peginstructions import PegInstructionsComponent
    from ..components.preallocgrp import PreAllocGrpComponent
    from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
    from ..components.stipulations import StipulationsComponent
    from ..components.trdgsesgrp import TrdgSesGrpComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent
    from ..components.yielddata import YieldDataComponent


# Forward references for components to avoid circular imports
CommissionDataComponent = ForwardRef('CommissionDataComponent')
DiscretionInstructionsComponent = ForwardRef('DiscretionInstructionsComponent')
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
OrderQtyDataComponent = ForwardRef('OrderQtyDataComponent')
PartiesComponent = ForwardRef('PartiesComponent')
PegInstructionsComponent = ForwardRef('PegInstructionsComponent')
PreAllocGrpComponent = ForwardRef('PreAllocGrpComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
TrdgSesGrpComponent = ForwardRef('TrdgSesGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class NewOrderSingleMessage(FIXMessageBase):
    """NewOrderSingle Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["NewOrderSingle"] = Field("NewOrderSingle", alias="35", description="Message Type")

    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    SecondaryClOrdID: Optional[str] = Field(None, alias="526", description="")
    ClOrdLinkID: Optional[str] = Field(None, alias="583", description="")
    TradeOriginationDate: Optional[date] = Field(None, alias="229", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    DayBookingInst: Optional[str] = Field(None, alias="589", description="")
    BookingUnit: Optional[str] = Field(None, alias="590", description="")
    PreallocMethod: Optional[str] = Field(None, alias="591", description="")
    AllocID: Optional[str] = Field(None, alias="70", description="")
    SettlType: Optional[str] = Field(None, alias="63", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    CashMargin: Optional[str] = Field(None, alias="544", description="")
    ClearingFeeIndicator: Optional[str] = Field(None, alias="635", description="")
    HandlInst: Optional[str] = Field(None, alias="21", description="")
    ExecInst: Optional[List[str]] = Field(None, alias="18", description="")
    MinQty: Optional[float] = Field(None, alias="110", description="")
    MaxFloor: Optional[float] = Field(None, alias="111", description="")
    ExDestination: Optional[str] = Field(None, alias="100", description="")
    ProcessCode: Optional[str] = Field(None, alias="81", description="")
    PrevClosePx: Optional[float] = Field(None, alias="140", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    LocateReqd: Optional[bool] = Field(None, alias="114", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    OrdType: Optional[str] = Field(None, alias="40", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    Price: Optional[float] = Field(None, alias="44", description="")
    StopPx: Optional[float] = Field(None, alias="99", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    ComplianceID: Optional[str] = Field(None, alias="376", description="")
    SolicitedFlag: Optional[bool] = Field(None, alias="377", description="")
    IOIID: Optional[str] = Field(None, alias="23", description="")
    QuoteID: Optional[str] = Field(None, alias="117", description="")
    TimeInForce: Optional[str] = Field(None, alias="59", description="")
    EffectiveTime: Optional[datetime] = Field(None, alias="168", description="")
    ExpireDate: Optional[date] = Field(None, alias="432", description="")
    ExpireTime: Optional[datetime] = Field(None, alias="126", description="")
    GTBookingInst: Optional[int] = Field(None, alias="427", description="")
    OrderCapacity: Optional[str] = Field(None, alias="528", description="")
    OrderRestrictions: Optional[List[str]] = Field(None, alias="529", description="")
    CustOrderCapacity: Optional[int] = Field(None, alias="582", description="")
    ForexReq: Optional[bool] = Field(None, alias="121", description="")
    SettlCurrency: Optional[str] = Field(None, alias="120", description="")
    BookingType: Optional[int] = Field(None, alias="775", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    SettlDate2: Optional[date] = Field(None, alias="193", description="")
    OrderQty2: Optional[float] = Field(None, alias="192", description="")
    Price2: Optional[float] = Field(None, alias="640", description="")
    PositionEffect: Optional[str] = Field(None, alias="77", description="")
    CoveredOrUncovered: Optional[int] = Field(None, alias="203", description="")
    MaxShow: Optional[float] = Field(None, alias="210", description="")
    TargetStrategy: Optional[int] = Field(None, alias="847", description="")
    TargetStrategyParameters: Optional[str] = Field(None, alias="848", description="")
    ParticipationRate: Optional[float] = Field(None, alias="849", description="")
    CancellationRights: Optional[str] = Field(None, alias="480", description="")
    MoneyLaunderingStatus: Optional[str] = Field(None, alias="481", description="")
    RegistID: Optional[str] = Field(None, alias="513", description="")
    Designation: Optional[str] = Field(None, alias="494", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    PreAllocGrp: ForwardRef('PreAllocGrpComponent') = Field(None, description="PreAllocGrp Component")
    TrdgSesGrp: ForwardRef('TrdgSesGrpComponent') = Field(None, description="TrdgSesGrp Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")
    OrderQtyData: ForwardRef('OrderQtyDataComponent') = Field(None, description="OrderQtyData Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    YieldData: ForwardRef('YieldDataComponent') = Field(None, description="YieldData Component")
    CommissionData: ForwardRef('CommissionDataComponent') = Field(None, description="CommissionData Component")
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
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.SecondaryClOrdID is not None:
            fields.append(f"SecondaryClOrdID={self.SecondaryClOrdID}")
        if self.ClOrdLinkID is not None:
            fields.append(f"ClOrdLinkID={self.ClOrdLinkID}")
        if self.TradeOriginationDate is not None:
            fields.append(f"TradeOriginationDate={self.TradeOriginationDate}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.DayBookingInst is not None:
            fields.append(f"DayBookingInst={self.DayBookingInst}")
        if self.BookingUnit is not None:
            fields.append(f"BookingUnit={self.BookingUnit}")
        if self.PreallocMethod is not None:
            fields.append(f"PreallocMethod={self.PreallocMethod}")
        if self.AllocID is not None:
            fields.append(f"AllocID={self.AllocID}")
        if self.SettlType is not None:
            fields.append(f"SettlType={self.SettlType}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.CashMargin is not None:
            fields.append(f"CashMargin={self.CashMargin}")
        if self.ClearingFeeIndicator is not None:
            fields.append(f"ClearingFeeIndicator={self.ClearingFeeIndicator}")
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
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.LocateReqd is not None:
            fields.append(f"LocateReqd={self.LocateReqd}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.QtyType is not None:
            fields.append(f"QtyType={self.QtyType}")
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
        if self.SolicitedFlag is not None:
            fields.append(f"SolicitedFlag={self.SolicitedFlag}")
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
        if self.OrderCapacity is not None:
            fields.append(f"OrderCapacity={self.OrderCapacity}")
        if self.OrderRestrictions is not None:
            fields.append(f"OrderRestrictions={self.OrderRestrictions}")
        if self.CustOrderCapacity is not None:
            fields.append(f"CustOrderCapacity={self.CustOrderCapacity}")
        if self.ForexReq is not None:
            fields.append(f"ForexReq={self.ForexReq}")
        if self.SettlCurrency is not None:
            fields.append(f"SettlCurrency={self.SettlCurrency}")
        if self.BookingType is not None:
            fields.append(f"BookingType={self.BookingType}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.SettlDate2 is not None:
            fields.append(f"SettlDate2={self.SettlDate2}")
        if self.OrderQty2 is not None:
            fields.append(f"OrderQty2={self.OrderQty2}")
        if self.Price2 is not None:
            fields.append(f"Price2={self.Price2}")
        if self.PositionEffect is not None:
            fields.append(f"PositionEffect={self.PositionEffect}")
        if self.CoveredOrUncovered is not None:
            fields.append(f"CoveredOrUncovered={self.CoveredOrUncovered}")
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
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.PreAllocGrp is not None:
            fields.append(f"PreAllocGrp={self.PreAllocGrp}")
        if self.TrdgSesGrp is not None:
            fields.append(f"TrdgSesGrp={self.TrdgSesGrp}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.FinancingDetails is not None:
            fields.append(f"FinancingDetails={self.FinancingDetails}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.Stipulations is not None:
            fields.append(f"Stipulations={self.Stipulations}")
        if self.OrderQtyData is not None:
            fields.append(f"OrderQtyData={self.OrderQtyData}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        if self.CommissionData is not None:
            fields.append(f"CommissionData={self.CommissionData}")
        if self.PegInstructions is not None:
            fields.append(f"PegInstructions={self.PegInstructions}")
        if self.DiscretionInstructions is not None:
            fields.append(f"DiscretionInstructions={self.DiscretionInstructions}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
NewOrderSingleMessage.model_rebuild()
