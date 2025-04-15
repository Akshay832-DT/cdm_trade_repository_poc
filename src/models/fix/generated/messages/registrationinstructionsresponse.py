"""
FIX RegistrationInstructionsResponse Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.parties import PartiesComponent


# Forward references for components to avoid circular imports
PartiesComponent = ForwardRef('PartiesComponent')


class RegistrationInstructionsResponseMessage(FIXMessageBase):
    """RegistrationInstructionsResponse Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["RegistrationInstructionsResponse"] = Field("RegistrationInstructionsResponse", alias="35", description="Message Type")

    RegistID: Optional[str] = Field(None, alias="513", description="")
    RegistTransType: Optional[str] = Field(None, alias="514", description="")
    RegistRefID: Optional[str] = Field(None, alias="508", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    RegistStatus: Optional[str] = Field(None, alias="506", description="")
    RegistRejReasonCode: Optional[int] = Field(None, alias="507", description="")
    RegistRejReasonText: Optional[str] = Field(None, alias="496", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")

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
        if self.RegistID is not None:
            fields.append(f"RegistID={self.RegistID}")
        if self.RegistTransType is not None:
            fields.append(f"RegistTransType={self.RegistTransType}")
        if self.RegistRefID is not None:
            fields.append(f"RegistRefID={self.RegistRefID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.RegistStatus is not None:
            fields.append(f"RegistStatus={self.RegistStatus}")
        if self.RegistRejReasonCode is not None:
            fields.append(f"RegistRejReasonCode={self.RegistRejReasonCode}")
        if self.RegistRejReasonText is not None:
            fields.append(f"RegistRejReasonText={self.RegistRejReasonText}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
RegistrationInstructionsResponseMessage.model_rebuild()
