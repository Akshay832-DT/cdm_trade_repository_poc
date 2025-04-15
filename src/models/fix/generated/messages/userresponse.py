"""
FIX UserResponse Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class UserResponseMessage(FIXMessageBase):
    """UserResponse Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["UserResponse"] = Field("UserResponse", alias="35", description="Message Type")

    UserRequestID: Optional[str] = Field(None, alias="923", description="")
    Username: Optional[str] = Field(None, alias="553", description="")
    UserStatus: Optional[int] = Field(None, alias="926", description="")
    UserStatusText: Optional[str] = Field(None, alias="927", description="")

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
        if self.Username is not None:
            fields.append(f"Username={self.Username}")
        if self.UserStatus is not None:
            fields.append(f"UserStatus={self.UserStatus}")
        if self.UserStatusText is not None:
            fields.append(f"UserStatusText={self.UserStatusText}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
UserResponseMessage.model_rebuild()
