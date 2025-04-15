"""
FIX ExecutionReport Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.commissiondata import CommissionDataComponent
    from ..components.contamtgrp import ContAmtGrpComponent
    from ..components.contragrp import ContraGrpComponent
    from ..components.discretioninstructions import DiscretionInstructionsComponent
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrmtlegexecgrp import InstrmtLegExecGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.miscfeesgrp import MiscFeesGrpComponent
    from ..components.orderqtydata import OrderQtyDataComponent
    from ..components.parties import PartiesComponent
    from ..components.peginstructions import PegInstructionsComponent
    from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
    from ..components.stipulations import StipulationsComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent
    from ..components.yielddata import YieldDataComponent


# Forward references for components to avoid circular imports
CommissionDataComponent = ForwardRef('CommissionDataComponent')
ContAmtGrpComponent = ForwardRef('ContAmtGrpComponent')
ContraGrpComponent = ForwardRef('ContraGrpComponent')
DiscretionInstructionsComponent = ForwardRef('DiscretionInstructionsComponent')
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrmtLegExecGrpComponent = ForwardRef('InstrmtLegExecGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
MiscFeesGrpComponent = ForwardRef('MiscFeesGrpComponent')
OrderQtyDataComponent = ForwardRef('OrderQtyDataComponent')
PartiesComponent = ForwardRef('PartiesComponent')
PegInstructionsComponent = ForwardRef('PegInstructionsComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class ExecutionReportMessage(FIXMessageBase):
    """ExecutionReport Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["ExecutionReport"] = Field("ExecutionReport", alias="35", description="Message Type")

    OrderID: Optional[str] = Field(None, alias="37", description="")
    SecondaryOrderID: Optional[str] = Field(None, alias="198", description="")
    SecondaryClOrdID: Optional[str] = Field(None, alias="526", description="")
    SecondaryExecID: Optional[str] = Field(None, alias="527", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    OrigClOrdID: Optional[str] = Field(None, alias="41", description="")
    ClOrdLinkID: Optional[str] = Field(None, alias="583", description="")
    QuoteRespID: Optional[str] = Field(None, alias="693", description="")
    OrdStatusReqID: Optional[str] = Field(None, alias="790", description="")
    MassStatusReqID: Optional[str] = Field(None, alias="584", description="")
    TotNumReports: Optional[int] = Field(None, alias="911", description="")
    LastRptRequested: Optional[bool] = Field(None, alias="912", description="")
    TradeOriginationDate: Optional[date] = Field(None, alias="229", description="")
    ListID: Optional[str] = Field(None, alias="66", description="")
    CrossID: Optional[str] = Field(None, alias="548", description="")
    OrigCrossID: Optional[str] = Field(None, alias="551", description="")
    CrossType: Optional[int] = Field(None, alias="549", description="")
    ExecID: Optional[str] = Field(None, alias="17", description="")
    ExecRefID: Optional[str] = Field(None, alias="19", description="")
    ExecType: Optional[str] = Field(None, alias="150", description="")
    OrdStatus: Optional[str] = Field(None, alias="39", description="")
    WorkingIndicator: Optional[bool] = Field(None, alias="636", description="")
    OrdRejReason: Optional[int] = Field(None, alias="103", description="")
    ExecRestatementReason: Optional[int] = Field(None, alias="378", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    DayBookingInst: Optional[str] = Field(None, alias="589", description="")
    BookingUnit: Optional[str] = Field(None, alias="590", description="")
    PreallocMethod: Optional[str] = Field(None, alias="591", description="")
    SettlType: Optional[str] = Field(None, alias="63", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    CashMargin: Optional[str] = Field(None, alias="544", description="")
    ClearingFeeIndicator: Optional[str] = Field(None, alias="635", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    OrdType: Optional[str] = Field(None, alias="40", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    Price: Optional[float] = Field(None, alias="44", description="")
    StopPx: Optional[float] = Field(None, alias="99", description="")
    PeggedPrice: Optional[float] = Field(None, alias="839", description="")
    DiscretionPrice: Optional[float] = Field(None, alias="845", description="")
    TargetStrategy: Optional[int] = Field(None, alias="847", description="")
    TargetStrategyParameters: Optional[str] = Field(None, alias="848", description="")
    ParticipationRate: Optional[float] = Field(None, alias="849", description="")
    TargetStrategyPerformance: Optional[float] = Field(None, alias="850", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    ComplianceID: Optional[str] = Field(None, alias="376", description="")
    SolicitedFlag: Optional[bool] = Field(None, alias="377", description="")
    TimeInForce: Optional[str] = Field(None, alias="59", description="")
    EffectiveTime: Optional[datetime] = Field(None, alias="168", description="")
    ExpireDate: Optional[date] = Field(None, alias="432", description="")
    ExpireTime: Optional[datetime] = Field(None, alias="126", description="")
    ExecInst: Optional[List[str]] = Field(None, alias="18", description="")
    OrderCapacity: Optional[str] = Field(None, alias="528", description="")
    OrderRestrictions: Optional[List[str]] = Field(None, alias="529", description="")
    CustOrderCapacity: Optional[int] = Field(None, alias="582", description="")
    LastQty: Optional[float] = Field(None, alias="32", description="")
    UnderlyingLastQty: Optional[float] = Field(None, alias="652", description="")
    LastPx: Optional[float] = Field(None, alias="31", description="")
    UnderlyingLastPx: Optional[float] = Field(None, alias="651", description="")
    LastParPx: Optional[float] = Field(None, alias="669", description="")
    LastSpotRate: Optional[float] = Field(None, alias="194", description="")
    LastForwardPoints: Optional[float] = Field(None, alias="195", description="")
    LastMkt: Optional[str] = Field(None, alias="30", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    TimeBracket: Optional[str] = Field(None, alias="943", description="")
    LastCapacity: Optional[str] = Field(None, alias="29", description="")
    LeavesQty: Optional[float] = Field(None, alias="151", description="")
    CumQty: Optional[float] = Field(None, alias="14", description="")
    AvgPx: Optional[float] = Field(None, alias="6", description="")
    DayOrderQty: Optional[float] = Field(None, alias="424", description="")
    DayCumQty: Optional[float] = Field(None, alias="425", description="")
    DayAvgPx: Optional[float] = Field(None, alias="426", description="")
    GTBookingInst: Optional[int] = Field(None, alias="427", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    ReportToExch: Optional[bool] = Field(None, alias="113", description="")
    GrossTradeAmt: Optional[float] = Field(None, alias="381", description="")
    NumDaysInterest: Optional[int] = Field(None, alias="157", description="")
    ExDate: Optional[date] = Field(None, alias="230", description="")
    AccruedInterestRate: Optional[float] = Field(None, alias="158", description="")
    AccruedInterestAmt: Optional[float] = Field(None, alias="159", description="")
    InterestAtMaturity: Optional[float] = Field(None, alias="738", description="")
    EndAccruedInterestAmt: Optional[float] = Field(None, alias="920", description="")
    StartCash: Optional[float] = Field(None, alias="921", description="")
    EndCash: Optional[float] = Field(None, alias="922", description="")
    TradedFlatSwitch: Optional[bool] = Field(None, alias="258", description="")
    BasisFeatureDate: Optional[date] = Field(None, alias="259", description="")
    BasisFeaturePrice: Optional[float] = Field(None, alias="260", description="")
    Concession: Optional[float] = Field(None, alias="238", description="")
    TotalTakedown: Optional[float] = Field(None, alias="237", description="")
    NetMoney: Optional[float] = Field(None, alias="118", description="")
    SettlCurrAmt: Optional[float] = Field(None, alias="119", description="")
    SettlCurrency: Optional[str] = Field(None, alias="120", description="")
    SettlCurrFxRate: Optional[float] = Field(None, alias="155", description="")
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias="156", description="")
    HandlInst: Optional[str] = Field(None, alias="21", description="")
    MinQty: Optional[float] = Field(None, alias="110", description="")
    MaxFloor: Optional[float] = Field(None, alias="111", description="")
    PositionEffect: Optional[str] = Field(None, alias="77", description="")
    MaxShow: Optional[float] = Field(None, alias="210", description="")
    BookingType: Optional[int] = Field(None, alias="775", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    SettlDate2: Optional[date] = Field(None, alias="193", description="")
    OrderQty2: Optional[float] = Field(None, alias="192", description="")
    LastForwardPoints2: Optional[float] = Field(None, alias="641", description="")
    MultiLegReportingType: Optional[str] = Field(None, alias="442", description="")
    CancellationRights: Optional[str] = Field(None, alias="480", description="")
    MoneyLaunderingStatus: Optional[str] = Field(None, alias="481", description="")
    RegistID: Optional[str] = Field(None, alias="513", description="")
    Designation: Optional[str] = Field(None, alias="494", description="")
    TransBkdTime: Optional[datetime] = Field(None, alias="483", description="")
    ExecValuationPoint: Optional[datetime] = Field(None, alias="515", description="")
    ExecPriceType: Optional[str] = Field(None, alias="484", description="")
    ExecPriceAdjustment: Optional[float] = Field(None, alias="485", description="")
    PriorityIndicator: Optional[int] = Field(None, alias="638", description="")
    PriceImprovement: Optional[float] = Field(None, alias="639", description="")
    LastLiquidityInd: Optional[int] = Field(None, alias="851", description="")
    CopyMsgIndicator: Optional[bool] = Field(None, alias="797", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    ContraGrp: ForwardRef('ContraGrpComponent') = Field(None, description="ContraGrp Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")
    OrderQtyData: ForwardRef('OrderQtyDataComponent') = Field(None, description="OrderQtyData Component")
    PegInstructions: ForwardRef('PegInstructionsComponent') = Field(None, description="PegInstructions Component")
    DiscretionInstructions: ForwardRef('DiscretionInstructionsComponent') = Field(None, description="DiscretionInstructions Component")
    CommissionData: ForwardRef('CommissionDataComponent') = Field(None, description="CommissionData Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    YieldData: ForwardRef('YieldDataComponent') = Field(None, description="YieldData Component")
    ContAmtGrp: ForwardRef('ContAmtGrpComponent') = Field(None, description="ContAmtGrp Component")
    InstrmtLegExecGrp: ForwardRef('InstrmtLegExecGrpComponent') = Field(None, description="InstrmtLegExecGrp Component")
    MiscFeesGrp: ForwardRef('MiscFeesGrpComponent') = Field(None, description="MiscFeesGrp Component")

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
        if self.OrderID is not None:
            fields.append(f"OrderID={self.OrderID}")
        if self.SecondaryOrderID is not None:
            fields.append(f"SecondaryOrderID={self.SecondaryOrderID}")
        if self.SecondaryClOrdID is not None:
            fields.append(f"SecondaryClOrdID={self.SecondaryClOrdID}")
        if self.SecondaryExecID is not None:
            fields.append(f"SecondaryExecID={self.SecondaryExecID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.OrigClOrdID is not None:
            fields.append(f"OrigClOrdID={self.OrigClOrdID}")
        if self.ClOrdLinkID is not None:
            fields.append(f"ClOrdLinkID={self.ClOrdLinkID}")
        if self.QuoteRespID is not None:
            fields.append(f"QuoteRespID={self.QuoteRespID}")
        if self.OrdStatusReqID is not None:
            fields.append(f"OrdStatusReqID={self.OrdStatusReqID}")
        if self.MassStatusReqID is not None:
            fields.append(f"MassStatusReqID={self.MassStatusReqID}")
        if self.TotNumReports is not None:
            fields.append(f"TotNumReports={self.TotNumReports}")
        if self.LastRptRequested is not None:
            fields.append(f"LastRptRequested={self.LastRptRequested}")
        if self.TradeOriginationDate is not None:
            fields.append(f"TradeOriginationDate={self.TradeOriginationDate}")
        if self.ListID is not None:
            fields.append(f"ListID={self.ListID}")
        if self.CrossID is not None:
            fields.append(f"CrossID={self.CrossID}")
        if self.OrigCrossID is not None:
            fields.append(f"OrigCrossID={self.OrigCrossID}")
        if self.CrossType is not None:
            fields.append(f"CrossType={self.CrossType}")
        if self.ExecID is not None:
            fields.append(f"ExecID={self.ExecID}")
        if self.ExecRefID is not None:
            fields.append(f"ExecRefID={self.ExecRefID}")
        if self.ExecType is not None:
            fields.append(f"ExecType={self.ExecType}")
        if self.OrdStatus is not None:
            fields.append(f"OrdStatus={self.OrdStatus}")
        if self.WorkingIndicator is not None:
            fields.append(f"WorkingIndicator={self.WorkingIndicator}")
        if self.OrdRejReason is not None:
            fields.append(f"OrdRejReason={self.OrdRejReason}")
        if self.ExecRestatementReason is not None:
            fields.append(f"ExecRestatementReason={self.ExecRestatementReason}")
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
        if self.SettlType is not None:
            fields.append(f"SettlType={self.SettlType}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.CashMargin is not None:
            fields.append(f"CashMargin={self.CashMargin}")
        if self.ClearingFeeIndicator is not None:
            fields.append(f"ClearingFeeIndicator={self.ClearingFeeIndicator}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
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
        if self.PeggedPrice is not None:
            fields.append(f"PeggedPrice={self.PeggedPrice}")
        if self.DiscretionPrice is not None:
            fields.append(f"DiscretionPrice={self.DiscretionPrice}")
        if self.TargetStrategy is not None:
            fields.append(f"TargetStrategy={self.TargetStrategy}")
        if self.TargetStrategyParameters is not None:
            fields.append(f"TargetStrategyParameters={self.TargetStrategyParameters}")
        if self.ParticipationRate is not None:
            fields.append(f"ParticipationRate={self.ParticipationRate}")
        if self.TargetStrategyPerformance is not None:
            fields.append(f"TargetStrategyPerformance={self.TargetStrategyPerformance}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.ComplianceID is not None:
            fields.append(f"ComplianceID={self.ComplianceID}")
        if self.SolicitedFlag is not None:
            fields.append(f"SolicitedFlag={self.SolicitedFlag}")
        if self.TimeInForce is not None:
            fields.append(f"TimeInForce={self.TimeInForce}")
        if self.EffectiveTime is not None:
            fields.append(f"EffectiveTime={self.EffectiveTime}")
        if self.ExpireDate is not None:
            fields.append(f"ExpireDate={self.ExpireDate}")
        if self.ExpireTime is not None:
            fields.append(f"ExpireTime={self.ExpireTime}")
        if self.ExecInst is not None:
            fields.append(f"ExecInst={self.ExecInst}")
        if self.OrderCapacity is not None:
            fields.append(f"OrderCapacity={self.OrderCapacity}")
        if self.OrderRestrictions is not None:
            fields.append(f"OrderRestrictions={self.OrderRestrictions}")
        if self.CustOrderCapacity is not None:
            fields.append(f"CustOrderCapacity={self.CustOrderCapacity}")
        if self.LastQty is not None:
            fields.append(f"LastQty={self.LastQty}")
        if self.UnderlyingLastQty is not None:
            fields.append(f"UnderlyingLastQty={self.UnderlyingLastQty}")
        if self.LastPx is not None:
            fields.append(f"LastPx={self.LastPx}")
        if self.UnderlyingLastPx is not None:
            fields.append(f"UnderlyingLastPx={self.UnderlyingLastPx}")
        if self.LastParPx is not None:
            fields.append(f"LastParPx={self.LastParPx}")
        if self.LastSpotRate is not None:
            fields.append(f"LastSpotRate={self.LastSpotRate}")
        if self.LastForwardPoints is not None:
            fields.append(f"LastForwardPoints={self.LastForwardPoints}")
        if self.LastMkt is not None:
            fields.append(f"LastMkt={self.LastMkt}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.TimeBracket is not None:
            fields.append(f"TimeBracket={self.TimeBracket}")
        if self.LastCapacity is not None:
            fields.append(f"LastCapacity={self.LastCapacity}")
        if self.LeavesQty is not None:
            fields.append(f"LeavesQty={self.LeavesQty}")
        if self.CumQty is not None:
            fields.append(f"CumQty={self.CumQty}")
        if self.AvgPx is not None:
            fields.append(f"AvgPx={self.AvgPx}")
        if self.DayOrderQty is not None:
            fields.append(f"DayOrderQty={self.DayOrderQty}")
        if self.DayCumQty is not None:
            fields.append(f"DayCumQty={self.DayCumQty}")
        if self.DayAvgPx is not None:
            fields.append(f"DayAvgPx={self.DayAvgPx}")
        if self.GTBookingInst is not None:
            fields.append(f"GTBookingInst={self.GTBookingInst}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.ReportToExch is not None:
            fields.append(f"ReportToExch={self.ReportToExch}")
        if self.GrossTradeAmt is not None:
            fields.append(f"GrossTradeAmt={self.GrossTradeAmt}")
        if self.NumDaysInterest is not None:
            fields.append(f"NumDaysInterest={self.NumDaysInterest}")
        if self.ExDate is not None:
            fields.append(f"ExDate={self.ExDate}")
        if self.AccruedInterestRate is not None:
            fields.append(f"AccruedInterestRate={self.AccruedInterestRate}")
        if self.AccruedInterestAmt is not None:
            fields.append(f"AccruedInterestAmt={self.AccruedInterestAmt}")
        if self.InterestAtMaturity is not None:
            fields.append(f"InterestAtMaturity={self.InterestAtMaturity}")
        if self.EndAccruedInterestAmt is not None:
            fields.append(f"EndAccruedInterestAmt={self.EndAccruedInterestAmt}")
        if self.StartCash is not None:
            fields.append(f"StartCash={self.StartCash}")
        if self.EndCash is not None:
            fields.append(f"EndCash={self.EndCash}")
        if self.TradedFlatSwitch is not None:
            fields.append(f"TradedFlatSwitch={self.TradedFlatSwitch}")
        if self.BasisFeatureDate is not None:
            fields.append(f"BasisFeatureDate={self.BasisFeatureDate}")
        if self.BasisFeaturePrice is not None:
            fields.append(f"BasisFeaturePrice={self.BasisFeaturePrice}")
        if self.Concession is not None:
            fields.append(f"Concession={self.Concession}")
        if self.TotalTakedown is not None:
            fields.append(f"TotalTakedown={self.TotalTakedown}")
        if self.NetMoney is not None:
            fields.append(f"NetMoney={self.NetMoney}")
        if self.SettlCurrAmt is not None:
            fields.append(f"SettlCurrAmt={self.SettlCurrAmt}")
        if self.SettlCurrency is not None:
            fields.append(f"SettlCurrency={self.SettlCurrency}")
        if self.SettlCurrFxRate is not None:
            fields.append(f"SettlCurrFxRate={self.SettlCurrFxRate}")
        if self.SettlCurrFxRateCalc is not None:
            fields.append(f"SettlCurrFxRateCalc={self.SettlCurrFxRateCalc}")
        if self.HandlInst is not None:
            fields.append(f"HandlInst={self.HandlInst}")
        if self.MinQty is not None:
            fields.append(f"MinQty={self.MinQty}")
        if self.MaxFloor is not None:
            fields.append(f"MaxFloor={self.MaxFloor}")
        if self.PositionEffect is not None:
            fields.append(f"PositionEffect={self.PositionEffect}")
        if self.MaxShow is not None:
            fields.append(f"MaxShow={self.MaxShow}")
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
        if self.LastForwardPoints2 is not None:
            fields.append(f"LastForwardPoints2={self.LastForwardPoints2}")
        if self.MultiLegReportingType is not None:
            fields.append(f"MultiLegReportingType={self.MultiLegReportingType}")
        if self.CancellationRights is not None:
            fields.append(f"CancellationRights={self.CancellationRights}")
        if self.MoneyLaunderingStatus is not None:
            fields.append(f"MoneyLaunderingStatus={self.MoneyLaunderingStatus}")
        if self.RegistID is not None:
            fields.append(f"RegistID={self.RegistID}")
        if self.Designation is not None:
            fields.append(f"Designation={self.Designation}")
        if self.TransBkdTime is not None:
            fields.append(f"TransBkdTime={self.TransBkdTime}")
        if self.ExecValuationPoint is not None:
            fields.append(f"ExecValuationPoint={self.ExecValuationPoint}")
        if self.ExecPriceType is not None:
            fields.append(f"ExecPriceType={self.ExecPriceType}")
        if self.ExecPriceAdjustment is not None:
            fields.append(f"ExecPriceAdjustment={self.ExecPriceAdjustment}")
        if self.PriorityIndicator is not None:
            fields.append(f"PriorityIndicator={self.PriorityIndicator}")
        if self.PriceImprovement is not None:
            fields.append(f"PriceImprovement={self.PriceImprovement}")
        if self.LastLiquidityInd is not None:
            fields.append(f"LastLiquidityInd={self.LastLiquidityInd}")
        if self.CopyMsgIndicator is not None:
            fields.append(f"CopyMsgIndicator={self.CopyMsgIndicator}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.ContraGrp is not None:
            fields.append(f"ContraGrp={self.ContraGrp}")
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
        if self.PegInstructions is not None:
            fields.append(f"PegInstructions={self.PegInstructions}")
        if self.DiscretionInstructions is not None:
            fields.append(f"DiscretionInstructions={self.DiscretionInstructions}")
        if self.CommissionData is not None:
            fields.append(f"CommissionData={self.CommissionData}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        if self.ContAmtGrp is not None:
            fields.append(f"ContAmtGrp={self.ContAmtGrp}")
        if self.InstrmtLegExecGrp is not None:
            fields.append(f"InstrmtLegExecGrp={self.InstrmtLegExecGrp}")
        if self.MiscFeesGrp is not None:
            fields.append(f"MiscFeesGrp={self.MiscFeesGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
ExecutionReportMessage.model_rebuild()
