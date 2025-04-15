"""
FIX TradingSessionStatus Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class TradingSessionStatusMessage(FIXMessageBase):
    """TradingSessionStatus Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["TradingSessionStatus"] = Field("TradingSessionStatus", alias="35", description="Message Type")

    TradSesReqID: Optional[str] = Field(None, alias="335", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    TradSesMethod: Optional[int] = Field(None, alias="338", description="")
    TradSesMode: Optional[int] = Field(None, alias="339", description="")
    UnsolicitedIndicator: Optional[bool] = Field(None, alias="325", description="")
    TradSesStatus: Optional[int] = Field(None, alias="340", description="")
    TradSesStatusRejReason: Optional[int] = Field(None, alias="567", description="")
    TradSesStartTime: Optional[datetime] = Field(None, alias="341", description="")
    TradSesOpenTime: Optional[datetime] = Field(None, alias="342", description="")
    TradSesPreCloseTime: Optional[datetime] = Field(None, alias="343", description="")
    TradSesCloseTime: Optional[datetime] = Field(None, alias="344", description="")
    TradSesEndTime: Optional[datetime] = Field(None, alias="345", description="")
    TotalVolumeTraded: Optional[float] = Field(None, alias="387", description="")
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
        if self.UnsolicitedIndicator is not None:
            fields.append(f"UnsolicitedIndicator={self.UnsolicitedIndicator}")
        if self.TradSesStatus is not None:
            fields.append(f"TradSesStatus={self.TradSesStatus}")
        if self.TradSesStatusRejReason is not None:
            fields.append(f"TradSesStatusRejReason={self.TradSesStatusRejReason}")
        if self.TradSesStartTime is not None:
            fields.append(f"TradSesStartTime={self.TradSesStartTime}")
        if self.TradSesOpenTime is not None:
            fields.append(f"TradSesOpenTime={self.TradSesOpenTime}")
        if self.TradSesPreCloseTime is not None:
            fields.append(f"TradSesPreCloseTime={self.TradSesPreCloseTime}")
        if self.TradSesCloseTime is not None:
            fields.append(f"TradSesCloseTime={self.TradSesCloseTime}")
        if self.TradSesEndTime is not None:
            fields.append(f"TradSesEndTime={self.TradSesEndTime}")
        if self.TotalVolumeTraded is not None:
            fields.append(f"TotalVolumeTraded={self.TotalVolumeTraded}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
TradingSessionStatusMessage.model_rebuild()
