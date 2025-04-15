"""
FIX Logon Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class LogonMessage(FIXMessageBase):
    """Logon Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["Logon"] = Field("Logon", alias="35", description="Message Type")

    EncryptMethod: Optional[int] = Field(None, alias="98", description="")
    HeartBtInt: Optional[int] = Field(None, alias="108", description="")
    RawDataLength: Optional[int] = Field(None, alias="95", description="")
    RawData: Optional[str] = Field(None, alias="96", description="")
    ResetSeqNumFlag: Optional[bool] = Field(None, alias="141", description="")
    NextExpectedMsgSeqNum: Optional[int] = Field(None, alias="789", description="")
    MaxMessageSize: Optional[int] = Field(None, alias="383", description="")
    TestMessageIndicator: Optional[bool] = Field(None, alias="464", description="")
    Username: Optional[str] = Field(None, alias="553", description="")
    Password: Optional[str] = Field(None, alias="554", description="")

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
        if self.EncryptMethod is not None:
            fields.append(f"EncryptMethod={self.EncryptMethod}")
        if self.HeartBtInt is not None:
            fields.append(f"HeartBtInt={self.HeartBtInt}")
        if self.RawDataLength is not None:
            fields.append(f"RawDataLength={self.RawDataLength}")
        if self.RawData is not None:
            fields.append(f"RawData={self.RawData}")
        if self.ResetSeqNumFlag is not None:
            fields.append(f"ResetSeqNumFlag={self.ResetSeqNumFlag}")
        if self.NextExpectedMsgSeqNum is not None:
            fields.append(f"NextExpectedMsgSeqNum={self.NextExpectedMsgSeqNum}")
        if self.MaxMessageSize is not None:
            fields.append(f"MaxMessageSize={self.MaxMessageSize}")
        if self.TestMessageIndicator is not None:
            fields.append(f"TestMessageIndicator={self.TestMessageIndicator}")
        if self.Username is not None:
            fields.append(f"Username={self.Username}")
        if self.Password is not None:
            fields.append(f"Password={self.Password}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
LogonMessage.model_rebuild()
