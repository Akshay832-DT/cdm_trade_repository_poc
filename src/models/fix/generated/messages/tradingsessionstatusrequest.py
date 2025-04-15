"""
FIX TradingSessionStatusRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class TradingSessionStatusRequestMessage(FIXMessageBase):
    """TradingSessionStatusRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["TradingSessionStatusRequest"] = Field("TradingSessionStatusRequest", alias="35", description="Message Type")

    TradSesReqID: Optional[str] = Field(None, alias="335", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    TradSesMethod: Optional[int] = Field(None, alias="338", description="")
    TradSesMode: Optional[int] = Field(None, alias="339", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")

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
        if self.TradSesReqID is not None:
            fields.append(f"TradSesReqID={self.TradSesReqID}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.TradSesMethod is not None:
            fields.append(f"TradSesMethod={self.TradSesMethod}")
        if self.TradSesMode is not None:
            fields.append(f"TradSesMode={self.TradSesMode}")
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
TradingSessionStatusRequestMessage.model_rebuild()
