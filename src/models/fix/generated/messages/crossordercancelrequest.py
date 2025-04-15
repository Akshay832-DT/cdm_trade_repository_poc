"""
FIX CrossOrderCancelRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.sidecrossordcxlgrp import SideCrossOrdCxlGrpComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
SideCrossOrdCxlGrpComponent = ForwardRef('SideCrossOrdCxlGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class CrossOrderCancelRequestMessage(FIXMessageBase):
    """CrossOrderCancelRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["CrossOrderCancelRequest"] = Field("CrossOrderCancelRequest", alias="35", description="Message Type")

    OrderID: Optional[str] = Field(None, alias="37", description="")
    CrossID: Optional[str] = Field(None, alias="548", description="")
    OrigCrossID: Optional[str] = Field(None, alias="551", description="")
    CrossType: Optional[int] = Field(None, alias="549", description="")
    CrossPrioritization: Optional[int] = Field(None, alias="550", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    SideCrossOrdCxlGrp: ForwardRef('SideCrossOrdCxlGrpComponent') = Field(None, description="SideCrossOrdCxlGrp Component")
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
        if self.OrderID is not None:
            fields.append(f"OrderID={self.OrderID}")
        if self.CrossID is not None:
            fields.append(f"CrossID={self.CrossID}")
        if self.OrigCrossID is not None:
            fields.append(f"OrigCrossID={self.OrigCrossID}")
        if self.CrossType is not None:
            fields.append(f"CrossType={self.CrossType}")
        if self.CrossPrioritization is not None:
            fields.append(f"CrossPrioritization={self.CrossPrioritization}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.SideCrossOrdCxlGrp is not None:
            fields.append(f"SideCrossOrdCxlGrp={self.SideCrossOrdCxlGrp}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
CrossOrderCancelRequestMessage.model_rebuild()
