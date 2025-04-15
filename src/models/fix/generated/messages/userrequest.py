"""
FIX UserRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class UserRequestMessage(FIXMessageBase):
    """UserRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["UserRequest"] = Field("UserRequest", alias="35", description="Message Type")

    UserRequestID: Optional[str] = Field(None, alias="923", description="")
    UserRequestType: Optional[int] = Field(None, alias="924", description="")
    Username: Optional[str] = Field(None, alias="553", description="")
    Password: Optional[str] = Field(None, alias="554", description="")
    NewPassword: Optional[str] = Field(None, alias="925", description="")
    RawDataLength: Optional[int] = Field(None, alias="95", description="")
    RawData: Optional[str] = Field(None, alias="96", description="")

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
        if self.UserRequestID is not None:
            fields.append(f"UserRequestID={self.UserRequestID}")
        if self.UserRequestType is not None:
            fields.append(f"UserRequestType={self.UserRequestType}")
        if self.Username is not None:
            fields.append(f"Username={self.Username}")
        if self.Password is not None:
            fields.append(f"Password={self.Password}")
        if self.NewPassword is not None:
            fields.append(f"NewPassword={self.NewPassword}")
        if self.RawDataLength is not None:
            fields.append(f"RawDataLength={self.RawDataLength}")
        if self.RawData is not None:
            fields.append(f"RawData={self.RawData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
UserRequestMessage.model_rebuild()
