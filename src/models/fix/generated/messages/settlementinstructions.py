"""
FIX SettlementInstructions Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.settlinstgrp import SettlInstGrpComponent


# Forward references for components to avoid circular imports
SettlInstGrpComponent = ForwardRef('SettlInstGrpComponent')


class SettlementInstructionsMessage(FIXMessageBase):
    """SettlementInstructions Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["SettlementInstructions"] = Field("SettlementInstructions", alias="35", description="Message Type")

    SettlInstMsgID: Optional[str] = Field(None, alias="777", description="")
    SettlInstReqID: Optional[str] = Field(None, alias="791", description="")
    SettlInstMode: Optional[str] = Field(None, alias="160", description="")
    SettlInstReqRejCode: Optional[int] = Field(None, alias="792", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    SettlInstGrp: ForwardRef('SettlInstGrpComponent') = Field(None, description="SettlInstGrp Component")

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
        if self.SettlInstMsgID is not None:
            fields.append(f"SettlInstMsgID={self.SettlInstMsgID}")
        if self.SettlInstReqID is not None:
            fields.append(f"SettlInstReqID={self.SettlInstReqID}")
        if self.SettlInstMode is not None:
            fields.append(f"SettlInstMode={self.SettlInstMode}")
        if self.SettlInstReqRejCode is not None:
            fields.append(f"SettlInstReqRejCode={self.SettlInstReqRejCode}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.SettlInstGrp is not None:
            fields.append(f"SettlInstGrp={self.SettlInstGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
SettlementInstructionsMessage.model_rebuild()
