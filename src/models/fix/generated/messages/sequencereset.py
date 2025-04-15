"""
FIX SequenceReset Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class SequenceResetMessage(FIXMessageBase):
    """SequenceReset Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["SequenceReset"] = Field("SequenceReset", alias="35", description="Message Type")

    GapFillFlag: Optional[bool] = Field(None, alias="123", description="")
    NewSeqNo: Optional[int] = Field(None, alias="36", description="")

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
        if self.GapFillFlag is not None:
            fields.append(f"GapFillFlag={self.GapFillFlag}")
        if self.NewSeqNo is not None:
            fields.append(f"NewSeqNo={self.NewSeqNo}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
SequenceResetMessage.model_rebuild()
