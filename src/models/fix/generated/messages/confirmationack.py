"""
FIX ConfirmationAck Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class ConfirmationAckMessage(FIXMessageBase):
    """ConfirmationAck Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["ConfirmationAck"] = Field("ConfirmationAck", alias="35", description="Message Type")

    ConfirmID: Optional[str] = Field(None, alias="664", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    AffirmStatus: Optional[int] = Field(None, alias="940", description="")
    ConfirmRejReason: Optional[int] = Field(None, alias="774", description="")
    MatchStatus: Optional[str] = Field(None, alias="573", description="")
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
        if self.ConfirmID is not None:
            fields.append(f"ConfirmID={self.ConfirmID}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.AffirmStatus is not None:
            fields.append(f"AffirmStatus={self.AffirmStatus}")
        if self.ConfirmRejReason is not None:
            fields.append(f"ConfirmRejReason={self.ConfirmRejReason}")
        if self.MatchStatus is not None:
            fields.append(f"MatchStatus={self.MatchStatus}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
ConfirmationAckMessage.model_rebuild()
