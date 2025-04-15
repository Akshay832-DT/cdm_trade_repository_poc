"""
FIX TradeCaptureReportAck Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrument import InstrumentComponent
    from ..components.trdallocgrp import TrdAllocGrpComponent
    from ..components.trdinstrmtleggrp import TrdInstrmtLegGrpComponent
    from ..components.trdregtimestamps import TrdRegTimestampsComponent


# Forward references for components to avoid circular imports
InstrumentComponent = ForwardRef('InstrumentComponent')
TrdAllocGrpComponent = ForwardRef('TrdAllocGrpComponent')
TrdInstrmtLegGrpComponent = ForwardRef('TrdInstrmtLegGrpComponent')
TrdRegTimestampsComponent = ForwardRef('TrdRegTimestampsComponent')


class TradeCaptureReportAckMessage(FIXMessageBase):
    """TradeCaptureReportAck Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["TradeCaptureReportAck"] = Field("TradeCaptureReportAck", alias="35", description="Message Type")

    TradeReportID: Optional[str] = Field(None, alias="571", description="")
    TradeReportTransType: Optional[int] = Field(None, alias="487", description="")
    TradeReportType: Optional[int] = Field(None, alias="856", description="")
    TrdType: Optional[int] = Field(None, alias="828", description="")
    TrdSubType: Optional[int] = Field(None, alias="829", description="")
    SecondaryTrdType: Optional[int] = Field(None, alias="855", description="")
    TransferReason: Optional[str] = Field(None, alias="830", description="")
    ExecType: Optional[str] = Field(None, alias="150", description="")
    TradeReportRefID: Optional[str] = Field(None, alias="572", description="")
    SecondaryTradeReportRefID: Optional[str] = Field(None, alias="881", description="")
    TrdRptStatus: Optional[int] = Field(None, alias="939", description="")
    TradeReportRejectReason: Optional[int] = Field(None, alias="751", description="")
    SecondaryTradeReportID: Optional[str] = Field(None, alias="818", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    TradeLinkID: Optional[str] = Field(None, alias="820", description="")
    TrdMatchID: Optional[str] = Field(None, alias="880", description="")
    ExecID: Optional[str] = Field(None, alias="17", description="")
    SecondaryExecID: Optional[str] = Field(None, alias="527", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    ResponseTransportType: Optional[int] = Field(None, alias="725", description="")
    ResponseDestination: Optional[str] = Field(None, alias="726", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    ClearingFeeIndicator: Optional[str] = Field(None, alias="635", description="")
    OrderCapacity: Optional[str] = Field(None, alias="528", description="")
    OrderRestrictions: Optional[List[str]] = Field(None, alias="529", description="")
    CustOrderCapacity: Optional[int] = Field(None, alias="582", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    PositionEffect: Optional[str] = Field(None, alias="77", description="")
    PreallocMethod: Optional[str] = Field(None, alias="591", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    TrdRegTimestamps: ForwardRef('TrdRegTimestampsComponent') = Field(None, description="TrdRegTimestamps Component")
    TrdInstrmtLegGrp: ForwardRef('TrdInstrmtLegGrpComponent') = Field(None, description="TrdInstrmtLegGrp Component")
    TrdAllocGrp: ForwardRef('TrdAllocGrpComponent') = Field(None, description="TrdAllocGrp Component")

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
        if self.TradeReportID is not None:
            fields.append(f"TradeReportID={self.TradeReportID}")
        if self.TradeReportTransType is not None:
            fields.append(f"TradeReportTransType={self.TradeReportTransType}")
        if self.TradeReportType is not None:
            fields.append(f"TradeReportType={self.TradeReportType}")
        if self.TrdType is not None:
            fields.append(f"TrdType={self.TrdType}")
        if self.TrdSubType is not None:
            fields.append(f"TrdSubType={self.TrdSubType}")
        if self.SecondaryTrdType is not None:
            fields.append(f"SecondaryTrdType={self.SecondaryTrdType}")
        if self.TransferReason is not None:
            fields.append(f"TransferReason={self.TransferReason}")
        if self.ExecType is not None:
            fields.append(f"ExecType={self.ExecType}")
        if self.TradeReportRefID is not None:
            fields.append(f"TradeReportRefID={self.TradeReportRefID}")
        if self.SecondaryTradeReportRefID is not None:
            fields.append(f"SecondaryTradeReportRefID={self.SecondaryTradeReportRefID}")
        if self.TrdRptStatus is not None:
            fields.append(f"TrdRptStatus={self.TrdRptStatus}")
        if self.TradeReportRejectReason is not None:
            fields.append(f"TradeReportRejectReason={self.TradeReportRejectReason}")
        if self.SecondaryTradeReportID is not None:
            fields.append(f"SecondaryTradeReportID={self.SecondaryTradeReportID}")
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        if self.TradeLinkID is not None:
            fields.append(f"TradeLinkID={self.TradeLinkID}")
        if self.TrdMatchID is not None:
            fields.append(f"TrdMatchID={self.TrdMatchID}")
        if self.ExecID is not None:
            fields.append(f"ExecID={self.ExecID}")
        if self.SecondaryExecID is not None:
            fields.append(f"SecondaryExecID={self.SecondaryExecID}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
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
        if self.ClearingFeeIndicator is not None:
            fields.append(f"ClearingFeeIndicator={self.ClearingFeeIndicator}")
        if self.OrderCapacity is not None:
            fields.append(f"OrderCapacity={self.OrderCapacity}")
        if self.OrderRestrictions is not None:
            fields.append(f"OrderRestrictions={self.OrderRestrictions}")
        if self.CustOrderCapacity is not None:
            fields.append(f"CustOrderCapacity={self.CustOrderCapacity}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.PositionEffect is not None:
            fields.append(f"PositionEffect={self.PositionEffect}")
        if self.PreallocMethod is not None:
            fields.append(f"PreallocMethod={self.PreallocMethod}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.TrdRegTimestamps is not None:
            fields.append(f"TrdRegTimestamps={self.TrdRegTimestamps}")
        if self.TrdInstrmtLegGrp is not None:
            fields.append(f"TrdInstrmtLegGrp={self.TrdInstrmtLegGrp}")
        if self.TrdAllocGrp is not None:
            fields.append(f"TrdAllocGrp={self.TrdAllocGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
TradeCaptureReportAckMessage.model_rebuild()
