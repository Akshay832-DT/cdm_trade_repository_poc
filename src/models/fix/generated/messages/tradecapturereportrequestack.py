"""
FIX TradeCaptureReportRequestAck Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class TradeCaptureReportRequestAckMessage(FIXMessageBase):
    """TradeCaptureReportRequestAck Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["TradeCaptureReportRequestAck"] = Field("TradeCaptureReportRequestAck", alias="35", description="Message Type")

    TradeRequestID: Optional[str] = Field(None, alias="568", description="")
    TradeRequestType: Optional[int] = Field(None, alias="569", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    TotNumTradeReports: Optional[int] = Field(None, alias="748", description="")
    TradeRequestResult: Optional[int] = Field(None, alias="749", description="")
    TradeRequestStatus: Optional[int] = Field(None, alias="750", description="")
    MultiLegReportingType: Optional[str] = Field(None, alias="442", description="")
    ResponseTransportType: Optional[int] = Field(None, alias="725", description="")
    ResponseDestination: Optional[str] = Field(None, alias="726", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")

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
        if self.TotNumTradeReports is not None:
            fields.append(f"TotNumTradeReports={self.TotNumTradeReports}")
        if self.TradeRequestResult is not None:
            fields.append(f"TradeRequestResult={self.TradeRequestResult}")
        if self.TradeRequestStatus is not None:
            fields.append(f"TradeRequestStatus={self.TradeRequestStatus}")
        if self.MultiLegReportingType is not None:
            fields.append(f"MultiLegReportingType={self.MultiLegReportingType}")
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
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
TradeCaptureReportRequestAckMessage.model_rebuild()
