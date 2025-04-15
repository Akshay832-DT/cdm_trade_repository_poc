"""
FIX ResendRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class ResendRequestMessage(FIXMessageBase):
    """ResendRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["ResendRequest"] = Field("ResendRequest", alias="35", description="Message Type")

    BeginSeqNo: Optional[int] = Field(None, alias="7", description="")
    EndSeqNo: Optional[int] = Field(None, alias="16", description="")

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
        if self.BeginSeqNo is not None:
            fields.append(f"BeginSeqNo={self.BeginSeqNo}")
        if self.EndSeqNo is not None:
            fields.append(f"EndSeqNo={self.EndSeqNo}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
ResendRequestMessage.model_rebuild()
