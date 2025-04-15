"""
FIX BidResponse Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.bidcomprspgrp import BidCompRspGrpComponent


# Forward references for components to avoid circular imports
BidCompRspGrpComponent = ForwardRef('BidCompRspGrpComponent')


class BidResponseMessage(FIXMessageBase):
    """BidResponse Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["BidResponse"] = Field("BidResponse", alias="35", description="Message Type")

    BidID: Optional[str] = Field(None, alias="390", description="")
    ClientBidID: Optional[str] = Field(None, alias="391", description="")
    BidCompRspGrp: ForwardRef('BidCompRspGrpComponent') = Field(None, description="BidCompRspGrp Component")

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
        if self.BidID is not None:
            fields.append(f"BidID={self.BidID}")
        if self.ClientBidID is not None:
            fields.append(f"ClientBidID={self.ClientBidID}")
        if self.BidCompRspGrp is not None:
            fields.append(f"BidCompRspGrp={self.BidCompRspGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
BidResponseMessage.model_rebuild()
