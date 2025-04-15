"""
FIX ConfirmationRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.ordallocgrp import OrdAllocGrpComponent


# Forward references for components to avoid circular imports
OrdAllocGrpComponent = ForwardRef('OrdAllocGrpComponent')


class ConfirmationRequestMessage(FIXMessageBase):
    """ConfirmationRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["ConfirmationRequest"] = Field("ConfirmationRequest", alias="35", description="Message Type")

    ConfirmReqID: Optional[str] = Field(None, alias="859", description="")
    ConfirmType: Optional[int] = Field(None, alias="773", description="")
    AllocID: Optional[str] = Field(None, alias="70", description="")
    SecondaryAllocID: Optional[str] = Field(None, alias="793", description="")
    IndividualAllocID: Optional[str] = Field(None, alias="467", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    AllocAccount: Optional[str] = Field(None, alias="79", description="")
    AllocAcctIDSource: Optional[int] = Field(None, alias="661", description="")
    AllocAccountType: Optional[int] = Field(None, alias="798", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    OrdAllocGrp: ForwardRef('OrdAllocGrpComponent') = Field(None, description="OrdAllocGrp Component")

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
        if self.ConfirmReqID is not None:
            fields.append(f"ConfirmReqID={self.ConfirmReqID}")
        if self.ConfirmType is not None:
            fields.append(f"ConfirmType={self.ConfirmType}")
        if self.AllocID is not None:
            fields.append(f"AllocID={self.AllocID}")
        if self.SecondaryAllocID is not None:
            fields.append(f"SecondaryAllocID={self.SecondaryAllocID}")
        if self.IndividualAllocID is not None:
            fields.append(f"IndividualAllocID={self.IndividualAllocID}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.AllocAccount is not None:
            fields.append(f"AllocAccount={self.AllocAccount}")
        if self.AllocAcctIDSource is not None:
            fields.append(f"AllocAcctIDSource={self.AllocAcctIDSource}")
        if self.AllocAccountType is not None:
            fields.append(f"AllocAccountType={self.AllocAccountType}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.OrdAllocGrp is not None:
            fields.append(f"OrdAllocGrp={self.OrdAllocGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
ConfirmationRequestMessage.model_rebuild()
