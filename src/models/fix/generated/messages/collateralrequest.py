"""
FIX CollateralRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.execcollgrp import ExecCollGrpComponent
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.miscfeesgrp import MiscFeesGrpComponent
    from ..components.parties import PartiesComponent
    from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
    from ..components.stipulations import StipulationsComponent
    from ..components.trdcollgrp import TrdCollGrpComponent
    from ..components.trdregtimestamps import TrdRegTimestampsComponent
    from ..components.undinstrmtcollgrp import UndInstrmtCollGrpComponent


# Forward references for components to avoid circular imports
ExecCollGrpComponent = ForwardRef('ExecCollGrpComponent')
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
MiscFeesGrpComponent = ForwardRef('MiscFeesGrpComponent')
PartiesComponent = ForwardRef('PartiesComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
TrdCollGrpComponent = ForwardRef('TrdCollGrpComponent')
TrdRegTimestampsComponent = ForwardRef('TrdRegTimestampsComponent')
UndInstrmtCollGrpComponent = ForwardRef('UndInstrmtCollGrpComponent')


class CollateralRequestMessage(FIXMessageBase):
    """CollateralRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["CollateralRequest"] = Field("CollateralRequest", alias="35", description="Message Type")

    CollReqID: Optional[str] = Field(None, alias="894", description="")
    CollAsgnReason: Optional[int] = Field(None, alias="895", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    ExpireTime: Optional[datetime] = Field(None, alias="126", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    OrderID: Optional[str] = Field(None, alias="37", description="")
    SecondaryOrderID: Optional[str] = Field(None, alias="198", description="")
    SecondaryClOrdID: Optional[str] = Field(None, alias="526", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    Quantity: Optional[float] = Field(None, alias="53", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    MarginExcess: Optional[float] = Field(None, alias="899", description="")
    TotalNetValue: Optional[float] = Field(None, alias="900", description="")
    CashOutstanding: Optional[float] = Field(None, alias="901", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    Price: Optional[float] = Field(None, alias="44", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    AccruedInterestAmt: Optional[float] = Field(None, alias="159", description="")
    EndAccruedInterestAmt: Optional[float] = Field(None, alias="920", description="")
    StartCash: Optional[float] = Field(None, alias="921", description="")
    EndCash: Optional[float] = Field(None, alias="922", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    SettlSessID: Optional[str] = Field(None, alias="716", description="")
    SettlSessSubID: Optional[str] = Field(None, alias="717", description="")
    ClearingBusinessDate: Optional[date] = Field(None, alias="715", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    ExecCollGrp: ForwardRef('ExecCollGrpComponent') = Field(None, description="ExecCollGrp Component")
    TrdCollGrp: ForwardRef('TrdCollGrpComponent') = Field(None, description="TrdCollGrp Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    UndInstrmtCollGrp: ForwardRef('UndInstrmtCollGrpComponent') = Field(None, description="UndInstrmtCollGrp Component")
    TrdRegTimestamps: ForwardRef('TrdRegTimestampsComponent') = Field(None, description="TrdRegTimestamps Component")
    MiscFeesGrp: ForwardRef('MiscFeesGrpComponent') = Field(None, description="MiscFeesGrp Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")

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
        if self.CollReqID is not None:
            fields.append(f"CollReqID={self.CollReqID}")
        if self.CollAsgnReason is not None:
            fields.append(f"CollAsgnReason={self.CollAsgnReason}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.ExpireTime is not None:
            fields.append(f"ExpireTime={self.ExpireTime}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.OrderID is not None:
            fields.append(f"OrderID={self.OrderID}")
        if self.SecondaryOrderID is not None:
            fields.append(f"SecondaryOrderID={self.SecondaryOrderID}")
        if self.SecondaryClOrdID is not None:
            fields.append(f"SecondaryClOrdID={self.SecondaryClOrdID}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.Quantity is not None:
            fields.append(f"Quantity={self.Quantity}")
        if self.QtyType is not None:
            fields.append(f"QtyType={self.QtyType}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.MarginExcess is not None:
            fields.append(f"MarginExcess={self.MarginExcess}")
        if self.TotalNetValue is not None:
            fields.append(f"TotalNetValue={self.TotalNetValue}")
        if self.CashOutstanding is not None:
            fields.append(f"CashOutstanding={self.CashOutstanding}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.Price is not None:
            fields.append(f"Price={self.Price}")
        if self.PriceType is not None:
            fields.append(f"PriceType={self.PriceType}")
        if self.AccruedInterestAmt is not None:
            fields.append(f"AccruedInterestAmt={self.AccruedInterestAmt}")
        if self.EndAccruedInterestAmt is not None:
            fields.append(f"EndAccruedInterestAmt={self.EndAccruedInterestAmt}")
        if self.StartCash is not None:
            fields.append(f"StartCash={self.StartCash}")
        if self.EndCash is not None:
            fields.append(f"EndCash={self.EndCash}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.SettlSessID is not None:
            fields.append(f"SettlSessID={self.SettlSessID}")
        if self.SettlSessSubID is not None:
            fields.append(f"SettlSessSubID={self.SettlSessSubID}")
        if self.ClearingBusinessDate is not None:
            fields.append(f"ClearingBusinessDate={self.ClearingBusinessDate}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.ExecCollGrp is not None:
            fields.append(f"ExecCollGrp={self.ExecCollGrp}")
        if self.TrdCollGrp is not None:
            fields.append(f"TrdCollGrp={self.TrdCollGrp}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.FinancingDetails is not None:
            fields.append(f"FinancingDetails={self.FinancingDetails}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.UndInstrmtCollGrp is not None:
            fields.append(f"UndInstrmtCollGrp={self.UndInstrmtCollGrp}")
        if self.TrdRegTimestamps is not None:
            fields.append(f"TrdRegTimestamps={self.TrdRegTimestamps}")
        if self.MiscFeesGrp is not None:
            fields.append(f"MiscFeesGrp={self.MiscFeesGrp}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.Stipulations is not None:
            fields.append(f"Stipulations={self.Stipulations}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
CollateralRequestMessage.model_rebuild()
