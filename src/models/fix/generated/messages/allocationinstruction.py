"""
FIX AllocationInstruction Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.allocgrp import AllocGrpComponent
    from ..components.execallocgrp import ExecAllocGrpComponent
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.instrumentextension import InstrumentExtensionComponent
    from ..components.ordallocgrp import OrdAllocGrpComponent
    from ..components.parties import PartiesComponent
    from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
    from ..components.stipulations import StipulationsComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent
    from ..components.yielddata import YieldDataComponent


# Forward references for components to avoid circular imports
AllocGrpComponent = ForwardRef('AllocGrpComponent')
ExecAllocGrpComponent = ForwardRef('ExecAllocGrpComponent')
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
InstrumentExtensionComponent = ForwardRef('InstrumentExtensionComponent')
OrdAllocGrpComponent = ForwardRef('OrdAllocGrpComponent')
PartiesComponent = ForwardRef('PartiesComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class AllocationInstructionMessage(FIXMessageBase):
    """AllocationInstruction Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["AllocationInstruction"] = Field("AllocationInstruction", alias="35", description="Message Type")

    AllocID: Optional[str] = Field(None, alias="70", description="")
    AllocTransType: Optional[str] = Field(None, alias="71", description="")
    AllocType: Optional[int] = Field(None, alias="626", description="")
    SecondaryAllocID: Optional[str] = Field(None, alias="793", description="")
    RefAllocID: Optional[str] = Field(None, alias="72", description="")
    AllocCancReplaceReason: Optional[int] = Field(None, alias="796", description="")
    AllocIntermedReqType: Optional[int] = Field(None, alias="808", description="")
    AllocLinkID: Optional[str] = Field(None, alias="196", description="")
    AllocLinkType: Optional[int] = Field(None, alias="197", description="")
    BookingRefID: Optional[str] = Field(None, alias="466", description="")
    AllocNoOrdersType: Optional[int] = Field(None, alias="857", description="")
    PreviouslyReported: Optional[bool] = Field(None, alias="570", description="")
    ReversalIndicator: Optional[bool] = Field(None, alias="700", description="")
    MatchType: Optional[str] = Field(None, alias="574", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    Quantity: Optional[float] = Field(None, alias="53", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    LastMkt: Optional[str] = Field(None, alias="30", description="")
    TradeOriginationDate: Optional[date] = Field(None, alias="229", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    AvgPx: Optional[float] = Field(None, alias="6", description="")
    AvgParPx: Optional[float] = Field(None, alias="860", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    AvgPxPrecision: Optional[int] = Field(None, alias="74", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    SettlType: Optional[str] = Field(None, alias="63", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    BookingType: Optional[int] = Field(None, alias="775", description="")
    GrossTradeAmt: Optional[float] = Field(None, alias="381", description="")
    Concession: Optional[float] = Field(None, alias="238", description="")
    TotalTakedown: Optional[float] = Field(None, alias="237", description="")
    NetMoney: Optional[float] = Field(None, alias="118", description="")
    PositionEffect: Optional[str] = Field(None, alias="77", description="")
    AutoAcceptIndicator: Optional[bool] = Field(None, alias="754", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    NumDaysInterest: Optional[int] = Field(None, alias="157", description="")
    AccruedInterestRate: Optional[float] = Field(None, alias="158", description="")
    AccruedInterestAmt: Optional[float] = Field(None, alias="159", description="")
    TotalAccruedInterestAmt: Optional[float] = Field(None, alias="540", description="")
    InterestAtMaturity: Optional[float] = Field(None, alias="738", description="")
    EndAccruedInterestAmt: Optional[float] = Field(None, alias="920", description="")
    StartCash: Optional[float] = Field(None, alias="921", description="")
    EndCash: Optional[float] = Field(None, alias="922", description="")
    LegalConfirm: Optional[bool] = Field(None, alias="650", description="")
    TotNoAllocs: Optional[int] = Field(None, alias="892", description="")
    LastFragment: Optional[bool] = Field(None, alias="893", description="")
    OrdAllocGrp: ForwardRef('OrdAllocGrpComponent') = Field(None, description="OrdAllocGrp Component")
    ExecAllocGrp: ForwardRef('ExecAllocGrpComponent') = Field(None, description="ExecAllocGrp Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrumentExtension: ForwardRef('InstrumentExtensionComponent') = Field(None, description="InstrumentExtension Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")
    YieldData: ForwardRef('YieldDataComponent') = Field(None, description="YieldData Component")
    AllocGrp: ForwardRef('AllocGrpComponent') = Field(None, description="AllocGrp Component")

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
        if self.AllocID is not None:
            fields.append(f"AllocID={self.AllocID}")
        if self.AllocTransType is not None:
            fields.append(f"AllocTransType={self.AllocTransType}")
        if self.AllocType is not None:
            fields.append(f"AllocType={self.AllocType}")
        if self.SecondaryAllocID is not None:
            fields.append(f"SecondaryAllocID={self.SecondaryAllocID}")
        if self.RefAllocID is not None:
            fields.append(f"RefAllocID={self.RefAllocID}")
        if self.AllocCancReplaceReason is not None:
            fields.append(f"AllocCancReplaceReason={self.AllocCancReplaceReason}")
        if self.AllocIntermedReqType is not None:
            fields.append(f"AllocIntermedReqType={self.AllocIntermedReqType}")
        if self.AllocLinkID is not None:
            fields.append(f"AllocLinkID={self.AllocLinkID}")
        if self.AllocLinkType is not None:
            fields.append(f"AllocLinkType={self.AllocLinkType}")
        if self.BookingRefID is not None:
            fields.append(f"BookingRefID={self.BookingRefID}")
        if self.AllocNoOrdersType is not None:
            fields.append(f"AllocNoOrdersType={self.AllocNoOrdersType}")
        if self.PreviouslyReported is not None:
            fields.append(f"PreviouslyReported={self.PreviouslyReported}")
        if self.ReversalIndicator is not None:
            fields.append(f"ReversalIndicator={self.ReversalIndicator}")
        if self.MatchType is not None:
            fields.append(f"MatchType={self.MatchType}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.Quantity is not None:
            fields.append(f"Quantity={self.Quantity}")
        if self.QtyType is not None:
            fields.append(f"QtyType={self.QtyType}")
        if self.LastMkt is not None:
            fields.append(f"LastMkt={self.LastMkt}")
        if self.TradeOriginationDate is not None:
            fields.append(f"TradeOriginationDate={self.TradeOriginationDate}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.PriceType is not None:
            fields.append(f"PriceType={self.PriceType}")
        if self.AvgPx is not None:
            fields.append(f"AvgPx={self.AvgPx}")
        if self.AvgParPx is not None:
            fields.append(f"AvgParPx={self.AvgParPx}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.AvgPxPrecision is not None:
            fields.append(f"AvgPxPrecision={self.AvgPxPrecision}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.SettlType is not None:
            fields.append(f"SettlType={self.SettlType}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.BookingType is not None:
            fields.append(f"BookingType={self.BookingType}")
        if self.GrossTradeAmt is not None:
            fields.append(f"GrossTradeAmt={self.GrossTradeAmt}")
        if self.Concession is not None:
            fields.append(f"Concession={self.Concession}")
        if self.TotalTakedown is not None:
            fields.append(f"TotalTakedown={self.TotalTakedown}")
        if self.NetMoney is not None:
            fields.append(f"NetMoney={self.NetMoney}")
        if self.PositionEffect is not None:
            fields.append(f"PositionEffect={self.PositionEffect}")
        if self.AutoAcceptIndicator is not None:
            fields.append(f"AutoAcceptIndicator={self.AutoAcceptIndicator}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.NumDaysInterest is not None:
            fields.append(f"NumDaysInterest={self.NumDaysInterest}")
        if self.AccruedInterestRate is not None:
            fields.append(f"AccruedInterestRate={self.AccruedInterestRate}")
        if self.AccruedInterestAmt is not None:
            fields.append(f"AccruedInterestAmt={self.AccruedInterestAmt}")
        if self.TotalAccruedInterestAmt is not None:
            fields.append(f"TotalAccruedInterestAmt={self.TotalAccruedInterestAmt}")
        if self.InterestAtMaturity is not None:
            fields.append(f"InterestAtMaturity={self.InterestAtMaturity}")
        if self.EndAccruedInterestAmt is not None:
            fields.append(f"EndAccruedInterestAmt={self.EndAccruedInterestAmt}")
        if self.StartCash is not None:
            fields.append(f"StartCash={self.StartCash}")
        if self.EndCash is not None:
            fields.append(f"EndCash={self.EndCash}")
        if self.LegalConfirm is not None:
            fields.append(f"LegalConfirm={self.LegalConfirm}")
        if self.TotNoAllocs is not None:
            fields.append(f"TotNoAllocs={self.TotNoAllocs}")
        if self.LastFragment is not None:
            fields.append(f"LastFragment={self.LastFragment}")
        if self.OrdAllocGrp is not None:
            fields.append(f"OrdAllocGrp={self.OrdAllocGrp}")
        if self.ExecAllocGrp is not None:
            fields.append(f"ExecAllocGrp={self.ExecAllocGrp}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.InstrumentExtension is not None:
            fields.append(f"InstrumentExtension={self.InstrumentExtension}")
        if self.FinancingDetails is not None:
            fields.append(f"FinancingDetails={self.FinancingDetails}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.Stipulations is not None:
            fields.append(f"Stipulations={self.Stipulations}")
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        if self.AllocGrp is not None:
            fields.append(f"AllocGrp={self.AllocGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
AllocationInstructionMessage.model_rebuild()
