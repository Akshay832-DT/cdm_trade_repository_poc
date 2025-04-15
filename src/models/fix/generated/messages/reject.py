"""
FIX Reject Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class RejectMessage(FIXMessageBase):
    """Reject Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["Reject"] = Field("Reject", alias="35", description="Message Type")

    RefSeqNum: Optional[int] = Field(None, alias="45", description="")
    RefTagID: Optional[int] = Field(None, alias="371", description="")
    RefMsgType: Optional[str] = Field(None, alias="372", description="")
    SessionRejectReason: Optional[int] = Field(None, alias="373", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")

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
        if self.RefSeqNum is not None:
            fields.append(f"RefSeqNum={self.RefSeqNum}")
        if self.RefTagID is not None:
            fields.append(f"RefTagID={self.RefTagID}")
        if self.RefMsgType is not None:
            fields.append(f"RefMsgType={self.RefMsgType}")
        if self.SessionRejectReason is not None:
            fields.append(f"SessionRejectReason={self.SessionRejectReason}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
RejectMessage.model_rebuild()
