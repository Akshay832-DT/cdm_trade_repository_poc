"""
FIX CollateralInquiryAck Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.collinqqualgrp import CollInqQualGrpComponent
    from ..components.execcollgrp import ExecCollGrpComponent
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.parties import PartiesComponent
    from ..components.trdcollgrp import TrdCollGrpComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
CollInqQualGrpComponent = ForwardRef('CollInqQualGrpComponent')
ExecCollGrpComponent = ForwardRef('ExecCollGrpComponent')
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
PartiesComponent = ForwardRef('PartiesComponent')
TrdCollGrpComponent = ForwardRef('TrdCollGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class CollateralInquiryAckMessage(FIXMessageBase):
    """CollateralInquiryAck Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["CollateralInquiryAck"] = Field("CollateralInquiryAck", alias="35", description="Message Type")

    CollInquiryID: Optional[str] = Field(None, alias="909", description="")
    CollInquiryStatus: Optional[int] = Field(None, alias="945", description="")
    CollInquiryResult: Optional[int] = Field(None, alias="946", description="")
    TotNumReports: Optional[int] = Field(None, alias="911", description="")
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
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    SettlSessID: Optional[str] = Field(None, alias="716", description="")
    SettlSessSubID: Optional[str] = Field(None, alias="717", description="")
    ClearingBusinessDate: Optional[date] = Field(None, alias="715", description="")
    ResponseTransportType: Optional[int] = Field(None, alias="725", description="")
    ResponseDestination: Optional[str] = Field(None, alias="726", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    CollInqQualGrp: ForwardRef('CollInqQualGrpComponent') = Field(None, description="CollInqQualGrp Component")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    ExecCollGrp: ForwardRef('ExecCollGrpComponent') = Field(None, description="ExecCollGrp Component")
    TrdCollGrp: ForwardRef('TrdCollGrpComponent') = Field(None, description="TrdCollGrp Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")

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
        if self.CollInquiryID is not None:
            fields.append(f"CollInquiryID={self.CollInquiryID}")
        if self.CollInquiryStatus is not None:
            fields.append(f"CollInquiryStatus={self.CollInquiryStatus}")
        if self.CollInquiryResult is not None:
            fields.append(f"CollInquiryResult={self.CollInquiryResult}")
        if self.TotNumReports is not None:
            fields.append(f"TotNumReports={self.TotNumReports}")
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
        if self.ResponseTransportType is not None:
            fields.append(f"ResponseTransportType={self.ResponseTransportType}")
        if self.ResponseDestination is not None:
            fields.append(f"ResponseDestination={self.ResponseDestination}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.CollInqQualGrp is not None:
            fields.append(f"CollInqQualGrp={self.CollInqQualGrp}")
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
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
CollateralInquiryAckMessage.model_rebuild()
