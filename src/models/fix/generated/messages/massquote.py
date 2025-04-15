"""
FIX MassQuote Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.parties import PartiesComponent
    from ..components.quotsetgrp import QuotSetGrpComponent


# Forward references for components to avoid circular imports
PartiesComponent = ForwardRef('PartiesComponent')
QuotSetGrpComponent = ForwardRef('QuotSetGrpComponent')


class MassQuoteMessage(FIXMessageBase):
    """MassQuote Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["MassQuote"] = Field("MassQuote", alias="35", description="Message Type")

    QuoteReqID: Optional[str] = Field(None, alias="131", description="")
    QuoteID: Optional[str] = Field(None, alias="117", description="")
    QuoteType: Optional[int] = Field(None, alias="537", description="")
    QuoteResponseLevel: Optional[int] = Field(None, alias="301", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    DefBidSize: Optional[float] = Field(None, alias="293", description="")
    DefOfferSize: Optional[float] = Field(None, alias="294", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    QuotSetGrp: ForwardRef('QuotSetGrpComponent') = Field(None, description="QuotSetGrp Component")

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
        if self.QuoteType is not None:
            fields.append(f"QuoteType={self.QuoteType}")
        if self.QuoteResponseLevel is not None:
            fields.append(f"QuoteResponseLevel={self.QuoteResponseLevel}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.DefBidSize is not None:
            fields.append(f"DefBidSize={self.DefBidSize}")
        if self.DefOfferSize is not None:
            fields.append(f"DefOfferSize={self.DefOfferSize}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.QuotSetGrp is not None:
            fields.append(f"QuotSetGrp={self.QuotSetGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
MassQuoteMessage.model_rebuild()
