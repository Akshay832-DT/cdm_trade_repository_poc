"""
FIX TradeCaptureReportRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.instrumentextension import InstrumentExtensionComponent
    from ..components.parties import PartiesComponent
    from ..components.trdcapdtgrp import TrdCapDtGrpComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
InstrumentExtensionComponent = ForwardRef('InstrumentExtensionComponent')
PartiesComponent = ForwardRef('PartiesComponent')
TrdCapDtGrpComponent = ForwardRef('TrdCapDtGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class TradeCaptureReportRequestMessage(FIXMessageBase):
    """TradeCaptureReportRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["TradeCaptureReportRequest"] = Field("TradeCaptureReportRequest", alias="35", description="Message Type")

    TradeRequestID: Optional[str] = Field(None, alias="568", description="")
    TradeRequestType: Optional[int] = Field(None, alias="569", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    TradeReportID: Optional[str] = Field(None, alias="571", description="")
    SecondaryTradeReportID: Optional[str] = Field(None, alias="818", description="")
    ExecID: Optional[str] = Field(None, alias="17", description="")
    ExecType: Optional[str] = Field(None, alias="150", description="")
    OrderID: Optional[str] = Field(None, alias="37", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    MatchStatus: Optional[str] = Field(None, alias="573", description="")
    TrdType: Optional[int] = Field(None, alias="828", description="")
    TrdSubType: Optional[int] = Field(None, alias="829", description="")
    TransferReason: Optional[str] = Field(None, alias="830", description="")
    SecondaryTrdType: Optional[int] = Field(None, alias="855", description="")
    TradeLinkID: Optional[str] = Field(None, alias="820", description="")
    TrdMatchID: Optional[str] = Field(None, alias="880", description="")
    ClearingBusinessDate: Optional[date] = Field(None, alias="715", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    TimeBracket: Optional[str] = Field(None, alias="943", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    MultiLegReportingType: Optional[str] = Field(None, alias="442", description="")
    TradeInputSource: Optional[str] = Field(None, alias="578", description="")
    TradeInputDevice: Optional[str] = Field(None, alias="579", description="")
    ResponseTransportType: Optional[int] = Field(None, alias="725", description="")
    ResponseDestination: Optional[str] = Field(None, alias="726", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrumentExtension: ForwardRef('InstrumentExtensionComponent') = Field(None, description="InstrumentExtension Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    TrdCapDtGrp: ForwardRef('TrdCapDtGrpComponent') = Field(None, description="TrdCapDtGrp Component")

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
        if self.TradeRequestID is not None:
            fields.append(f"TradeRequestID={self.TradeRequestID}")
        if self.TradeRequestType is not None:
            fields.append(f"TradeRequestType={self.TradeRequestType}")
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        if self.TradeReportID is not None:
            fields.append(f"TradeReportID={self.TradeReportID}")
        if self.SecondaryTradeReportID is not None:
            fields.append(f"SecondaryTradeReportID={self.SecondaryTradeReportID}")
        if self.ExecID is not None:
            fields.append(f"ExecID={self.ExecID}")
        if self.ExecType is not None:
            fields.append(f"ExecType={self.ExecType}")
        if self.OrderID is not None:
            fields.append(f"OrderID={self.OrderID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.MatchStatus is not None:
            fields.append(f"MatchStatus={self.MatchStatus}")
        if self.TrdType is not None:
            fields.append(f"TrdType={self.TrdType}")
        if self.TrdSubType is not None:
            fields.append(f"TrdSubType={self.TrdSubType}")
        if self.TransferReason is not None:
            fields.append(f"TransferReason={self.TransferReason}")
        if self.SecondaryTrdType is not None:
            fields.append(f"SecondaryTrdType={self.SecondaryTrdType}")
        if self.TradeLinkID is not None:
            fields.append(f"TradeLinkID={self.TradeLinkID}")
        if self.TrdMatchID is not None:
            fields.append(f"TrdMatchID={self.TrdMatchID}")
        if self.ClearingBusinessDate is not None:
            fields.append(f"ClearingBusinessDate={self.ClearingBusinessDate}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.TimeBracket is not None:
            fields.append(f"TimeBracket={self.TimeBracket}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.MultiLegReportingType is not None:
            fields.append(f"MultiLegReportingType={self.MultiLegReportingType}")
        if self.TradeInputSource is not None:
            fields.append(f"TradeInputSource={self.TradeInputSource}")
        if self.TradeInputDevice is not None:
            fields.append(f"TradeInputDevice={self.TradeInputDevice}")
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
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
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
        if self.TrdCapDtGrp is not None:
            fields.append(f"TrdCapDtGrp={self.TrdCapDtGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
TradeCaptureReportRequestMessage.model_rebuild()
