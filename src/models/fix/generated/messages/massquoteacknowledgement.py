"""
FIX MassQuoteAcknowledgement Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.parties import PartiesComponent
    from ..components.quotsetackgrp import QuotSetAckGrpComponent


# Forward references for components to avoid circular imports
PartiesComponent = ForwardRef('PartiesComponent')
QuotSetAckGrpComponent = ForwardRef('QuotSetAckGrpComponent')


class MassQuoteAcknowledgementMessage(FIXMessageBase):
    """MassQuoteAcknowledgement Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["MassQuoteAcknowledgement"] = Field("MassQuoteAcknowledgement", alias="35", description="Message Type")

    QuoteReqID: Optional[str] = Field(None, alias="131", description="")
    QuoteID: Optional[str] = Field(None, alias="117", description="")
    QuoteStatus: Optional[int] = Field(None, alias="297", description="")
    QuoteRejectReason: Optional[int] = Field(None, alias="300", description="")
    QuoteResponseLevel: Optional[int] = Field(None, alias="301", description="")
    QuoteType: Optional[int] = Field(None, alias="537", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    QuotSetAckGrp: ForwardRef('QuotSetAckGrpComponent') = Field(None, description="QuotSetAckGrp Component")

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
        if self.QuoteID is not None:
            fields.append(f"QuoteID={self.QuoteID}")
        if self.QuoteStatus is not None:
            fields.append(f"QuoteStatus={self.QuoteStatus}")
        if self.QuoteRejectReason is not None:
            fields.append(f"QuoteRejectReason={self.QuoteRejectReason}")
        if self.QuoteResponseLevel is not None:
            fields.append(f"QuoteResponseLevel={self.QuoteResponseLevel}")
        if self.QuoteType is not None:
            fields.append(f"QuoteType={self.QuoteType}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.QuotSetAckGrp is not None:
            fields.append(f"QuotSetAckGrp={self.QuotSetAckGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
MassQuoteAcknowledgementMessage.model_rebuild()
