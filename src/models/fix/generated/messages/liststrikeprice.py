"""
FIX ListStrikePrice Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtstrkpxgrp import InstrmtStrkPxGrpComponent
    from ..components.undinstrmtstrkpxgrp import UndInstrmtStrkPxGrpComponent


# Forward references for components to avoid circular imports
InstrmtStrkPxGrpComponent = ForwardRef('InstrmtStrkPxGrpComponent')
UndInstrmtStrkPxGrpComponent = ForwardRef('UndInstrmtStrkPxGrpComponent')


class ListStrikePriceMessage(FIXMessageBase):
    """ListStrikePrice Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["ListStrikePrice"] = Field("ListStrikePrice", alias="35", description="Message Type")

    ListID: Optional[str] = Field(None, alias="66", description="")
    TotNoStrikes: Optional[int] = Field(None, alias="422", description="")
    LastFragment: Optional[bool] = Field(None, alias="893", description="")
    InstrmtStrkPxGrp: ForwardRef('InstrmtStrkPxGrpComponent') = Field(None, description="InstrmtStrkPxGrp Component")
    UndInstrmtStrkPxGrp: ForwardRef('UndInstrmtStrkPxGrpComponent') = Field(None, description="UndInstrmtStrkPxGrp Component")

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
        if self.ListID is not None:
            fields.append(f"ListID={self.ListID}")
        if self.TotNoStrikes is not None:
            fields.append(f"TotNoStrikes={self.TotNoStrikes}")
        if self.LastFragment is not None:
            fields.append(f"LastFragment={self.LastFragment}")
        if self.InstrmtStrkPxGrp is not None:
            fields.append(f"InstrmtStrkPxGrp={self.InstrmtStrkPxGrp}")
        if self.UndInstrmtStrkPxGrp is not None:
            fields.append(f"UndInstrmtStrkPxGrp={self.UndInstrmtStrkPxGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
ListStrikePriceMessage.model_rebuild()
