"""
FIX DontKnowTrade Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.orderqtydata import OrderQtyDataComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
OrderQtyDataComponent = ForwardRef('OrderQtyDataComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class DontKnowTradeMessage(FIXMessageBase):
    """DontKnowTrade Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["DontKnowTrade"] = Field("DontKnowTrade", alias="35", description="Message Type")

    OrderID: Optional[str] = Field(None, alias="37", description="")
    SecondaryOrderID: Optional[str] = Field(None, alias="198", description="")
    ExecID: Optional[str] = Field(None, alias="17", description="")
    DKReason: Optional[str] = Field(None, alias="127", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    LastQty: Optional[float] = Field(None, alias="32", description="")
    LastPx: Optional[float] = Field(None, alias="31", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    OrderQtyData: ForwardRef('OrderQtyDataComponent') = Field(None, description="OrderQtyData Component")

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
        if self.ExecID is not None:
            fields.append(f"ExecID={self.ExecID}")
        if self.DKReason is not None:
            fields.append(f"DKReason={self.DKReason}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.LastQty is not None:
            fields.append(f"LastQty={self.LastQty}")
        if self.LastPx is not None:
            fields.append(f"LastPx={self.LastPx}")
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
        if self.OrderQtyData is not None:
            fields.append(f"OrderQtyData={self.OrderQtyData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
DontKnowTradeMessage.model_rebuild()
