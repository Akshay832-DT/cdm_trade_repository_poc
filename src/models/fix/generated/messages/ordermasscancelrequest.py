"""
FIX OrderMassCancelRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrument import InstrumentComponent
    from ..components.underlyinginstrument import UnderlyingInstrumentComponent


# Forward references for components to avoid circular imports
InstrumentComponent = ForwardRef('InstrumentComponent')
UnderlyingInstrumentComponent = ForwardRef('UnderlyingInstrumentComponent')


class OrderMassCancelRequestMessage(FIXMessageBase):
    """OrderMassCancelRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["OrderMassCancelRequest"] = Field("OrderMassCancelRequest", alias="35", description="Message Type")

    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    SecondaryClOrdID: Optional[str] = Field(None, alias="526", description="")
    MassCancelRequestType: Optional[str] = Field(None, alias="530", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    UnderlyingInstrument: ForwardRef('UnderlyingInstrumentComponent') = Field(None, description="UnderlyingInstrument Component")

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
        if self.MassCancelRequestType is not None:
            fields.append(f"MassCancelRequestType={self.MassCancelRequestType}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.UnderlyingInstrument is not None:
            fields.append(f"UnderlyingInstrument={self.UnderlyingInstrument}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
OrderMassCancelRequestMessage.model_rebuild()
