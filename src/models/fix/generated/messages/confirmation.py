"""
FIX Confirmation Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.commissiondata import CommissionDataComponent
    from ..components.cpctyconfgrp import CpctyConfGrpComponent
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.instrumentextension import InstrumentExtensionComponent
    from ..components.miscfeesgrp import MiscFeesGrpComponent
    from ..components.ordallocgrp import OrdAllocGrpComponent
    from ..components.parties import PartiesComponent
    from ..components.settlinstructionsdata import SettlInstructionsDataComponent
    from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
    from ..components.stipulations import StipulationsComponent
    from ..components.trdregtimestamps import TrdRegTimestampsComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent
    from ..components.yielddata import YieldDataComponent


# Forward references for components to avoid circular imports
CommissionDataComponent = ForwardRef('CommissionDataComponent')
CpctyConfGrpComponent = ForwardRef('CpctyConfGrpComponent')
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
InstrumentExtensionComponent = ForwardRef('InstrumentExtensionComponent')
MiscFeesGrpComponent = ForwardRef('MiscFeesGrpComponent')
OrdAllocGrpComponent = ForwardRef('OrdAllocGrpComponent')
PartiesComponent = ForwardRef('PartiesComponent')
SettlInstructionsDataComponent = ForwardRef('SettlInstructionsDataComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
TrdRegTimestampsComponent = ForwardRef('TrdRegTimestampsComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class ConfirmationMessage(FIXMessageBase):
    """Confirmation Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["Confirmation"] = Field("Confirmation", alias="35", description="Message Type")

    ConfirmID: Optional[str] = Field(None, alias="664", description="")
    ConfirmRefID: Optional[str] = Field(None, alias="772", description="")
    ConfirmReqID: Optional[str] = Field(None, alias="859", description="")
    ConfirmTransType: Optional[int] = Field(None, alias="666", description="")
    ConfirmType: Optional[int] = Field(None, alias="773", description="")
    CopyMsgIndicator: Optional[bool] = Field(None, alias="797", description="")
    LegalConfirm: Optional[bool] = Field(None, alias="650", description="")
    ConfirmStatus: Optional[int] = Field(None, alias="665", description="")
    AllocID: Optional[str] = Field(None, alias="70", description="")
    SecondaryAllocID: Optional[str] = Field(None, alias="793", description="")
    IndividualAllocID: Optional[str] = Field(None, alias="467", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    AllocQty: Optional[float] = Field(None, alias="80", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    LastMkt: Optional[str] = Field(None, alias="30", description="")
    AllocAccount: Optional[str] = Field(None, alias="79", description="")
    AllocAcctIDSource: Optional[int] = Field(None, alias="661", description="")
    AllocAccountType: Optional[int] = Field(None, alias="798", description="")
    AvgPx: Optional[float] = Field(None, alias="6", description="")
    AvgPxPrecision: Optional[int] = Field(None, alias="74", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    AvgParPx: Optional[float] = Field(None, alias="860", description="")
    ReportedPx: Optional[float] = Field(None, alias="861", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    ProcessCode: Optional[str] = Field(None, alias="81", description="")
    GrossTradeAmt: Optional[float] = Field(None, alias="381", description="")
    NumDaysInterest: Optional[int] = Field(None, alias="157", description="")
    ExDate: Optional[date] = Field(None, alias="230", description="")
    AccruedInterestRate: Optional[float] = Field(None, alias="158", description="")
    AccruedInterestAmt: Optional[float] = Field(None, alias="159", description="")
    InterestAtMaturity: Optional[float] = Field(None, alias="738", description="")
    EndAccruedInterestAmt: Optional[float] = Field(None, alias="920", description="")
    StartCash: Optional[float] = Field(None, alias="921", description="")
    EndCash: Optional[float] = Field(None, alias="922", description="")
    Concession: Optional[float] = Field(None, alias="238", description="")
    TotalTakedown: Optional[float] = Field(None, alias="237", description="")
    NetMoney: Optional[float] = Field(None, alias="118", description="")
    MaturityNetMoney: Optional[float] = Field(None, alias="890", description="")
    SettlCurrAmt: Optional[float] = Field(None, alias="119", description="")
    SettlCurrency: Optional[str] = Field(None, alias="120", description="")
    SettlCurrFxRate: Optional[float] = Field(None, alias="155", description="")
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias="156", description="")
    SettlType: Optional[str] = Field(None, alias="63", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    SharedCommission: Optional[float] = Field(None, alias="858", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    OrdAllocGrp: ForwardRef('OrdAllocGrpComponent') = Field(None, description="OrdAllocGrp Component")
    TrdRegTimestamps: ForwardRef('TrdRegTimestampsComponent') = Field(None, description="TrdRegTimestamps Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrumentExtension: ForwardRef('InstrumentExtensionComponent') = Field(None, description="InstrumentExtension Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    YieldData: ForwardRef('YieldDataComponent') = Field(None, description="YieldData Component")
    CpctyConfGrp: ForwardRef('CpctyConfGrpComponent') = Field(None, description="CpctyConfGrp Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    SettlInstructionsData: ForwardRef('SettlInstructionsDataComponent') = Field(None, description="SettlInstructionsData Component")
    CommissionData: ForwardRef('CommissionDataComponent') = Field(None, description="CommissionData Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")
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
        if self.ConfirmID is not None:
            fields.append(f"ConfirmID={self.ConfirmID}")
        if self.ConfirmRefID is not None:
            fields.append(f"ConfirmRefID={self.ConfirmRefID}")
        if self.ConfirmReqID is not None:
            fields.append(f"ConfirmReqID={self.ConfirmReqID}")
        if self.ConfirmTransType is not None:
            fields.append(f"ConfirmTransType={self.ConfirmTransType}")
        if self.ConfirmType is not None:
            fields.append(f"ConfirmType={self.ConfirmType}")
        if self.CopyMsgIndicator is not None:
            fields.append(f"CopyMsgIndicator={self.CopyMsgIndicator}")
        if self.LegalConfirm is not None:
            fields.append(f"LegalConfirm={self.LegalConfirm}")
        if self.ConfirmStatus is not None:
            fields.append(f"ConfirmStatus={self.ConfirmStatus}")
        if self.AllocID is not None:
            fields.append(f"AllocID={self.AllocID}")
        if self.SecondaryAllocID is not None:
            fields.append(f"SecondaryAllocID={self.SecondaryAllocID}")
        if self.IndividualAllocID is not None:
            fields.append(f"IndividualAllocID={self.IndividualAllocID}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.AllocQty is not None:
            fields.append(f"AllocQty={self.AllocQty}")
        if self.QtyType is not None:
            fields.append(f"QtyType={self.QtyType}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.LastMkt is not None:
            fields.append(f"LastMkt={self.LastMkt}")
        if self.AllocAccount is not None:
            fields.append(f"AllocAccount={self.AllocAccount}")
        if self.AllocAcctIDSource is not None:
            fields.append(f"AllocAcctIDSource={self.AllocAcctIDSource}")
        if self.AllocAccountType is not None:
            fields.append(f"AllocAccountType={self.AllocAccountType}")
        if self.AvgPx is not None:
            fields.append(f"AvgPx={self.AvgPx}")
        if self.AvgPxPrecision is not None:
            fields.append(f"AvgPxPrecision={self.AvgPxPrecision}")
        if self.PriceType is not None:
            fields.append(f"PriceType={self.PriceType}")
        if self.AvgParPx is not None:
            fields.append(f"AvgParPx={self.AvgParPx}")
        if self.ReportedPx is not None:
            fields.append(f"ReportedPx={self.ReportedPx}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.ProcessCode is not None:
            fields.append(f"ProcessCode={self.ProcessCode}")
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
        if self.Concession is not None:
            fields.append(f"Concession={self.Concession}")
        if self.TotalTakedown is not None:
            fields.append(f"TotalTakedown={self.TotalTakedown}")
        if self.NetMoney is not None:
            fields.append(f"NetMoney={self.NetMoney}")
        if self.MaturityNetMoney is not None:
            fields.append(f"MaturityNetMoney={self.MaturityNetMoney}")
        if self.SettlCurrAmt is not None:
            fields.append(f"SettlCurrAmt={self.SettlCurrAmt}")
        if self.SettlCurrency is not None:
            fields.append(f"SettlCurrency={self.SettlCurrency}")
        if self.SettlCurrFxRate is not None:
            fields.append(f"SettlCurrFxRate={self.SettlCurrFxRate}")
        if self.SettlCurrFxRateCalc is not None:
            fields.append(f"SettlCurrFxRateCalc={self.SettlCurrFxRateCalc}")
        if self.SettlType is not None:
            fields.append(f"SettlType={self.SettlType}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.SharedCommission is not None:
            fields.append(f"SharedCommission={self.SharedCommission}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.OrdAllocGrp is not None:
            fields.append(f"OrdAllocGrp={self.OrdAllocGrp}")
        if self.TrdRegTimestamps is not None:
            fields.append(f"TrdRegTimestamps={self.TrdRegTimestamps}")
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
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        if self.CpctyConfGrp is not None:
            fields.append(f"CpctyConfGrp={self.CpctyConfGrp}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.SettlInstructionsData is not None:
            fields.append(f"SettlInstructionsData={self.SettlInstructionsData}")
        if self.CommissionData is not None:
            fields.append(f"CommissionData={self.CommissionData}")
        if self.Stipulations is not None:
            fields.append(f"Stipulations={self.Stipulations}")
        if self.MiscFeesGrp is not None:
            fields.append(f"MiscFeesGrp={self.MiscFeesGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
ConfirmationMessage.model_rebuild()
