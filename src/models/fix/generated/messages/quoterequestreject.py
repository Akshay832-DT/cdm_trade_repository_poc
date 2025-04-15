"""
FIX QuoteRequestReject Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.quotreqrjctgrp import QuotReqRjctGrpComponent


# Forward references for components to avoid circular imports
QuotReqRjctGrpComponent = ForwardRef('QuotReqRjctGrpComponent')


class QuoteRequestRejectMessage(FIXMessageBase):
    """QuoteRequestReject Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["QuoteRequestReject"] = Field("QuoteRequestReject", alias="35", description="Message Type")

    QuoteReqID: Optional[str] = Field(None, alias="131", description="")
    RFQReqID: Optional[str] = Field(None, alias="644", description="")
    QuoteRequestRejectReason: Optional[int] = Field(None, alias="658", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    QuotReqRjctGrp: ForwardRef('QuotReqRjctGrpComponent') = Field(None, description="QuotReqRjctGrp Component")

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
        if self.QuoteReqID is not None:
            fields.append(f"QuoteReqID={self.QuoteReqID}")
        if self.RFQReqID is not None:
            fields.append(f"RFQReqID={self.RFQReqID}")
        if self.QuoteRequestRejectReason is not None:
            fields.append(f"QuoteRequestRejectReason={self.QuoteRequestRejectReason}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.QuotReqRjctGrp is not None:
            fields.append(f"QuotReqRjctGrp={self.QuotReqRjctGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
QuoteRequestRejectMessage.model_rebuild()
