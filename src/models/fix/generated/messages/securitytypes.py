"""
FIX SecurityTypes Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.sectypesgrp import SecTypesGrpComponent


# Forward references for components to avoid circular imports
SecTypesGrpComponent = ForwardRef('SecTypesGrpComponent')


class SecurityTypesMessage(FIXMessageBase):
    """SecurityTypes Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["SecurityTypes"] = Field("SecurityTypes", alias="35", description="Message Type")

    SecurityReqID: Optional[str] = Field(None, alias="320", description="")
    SecurityResponseID: Optional[str] = Field(None, alias="322", description="")
    SecurityResponseType: Optional[int] = Field(None, alias="323", description="")
    TotNoSecurityTypes: Optional[int] = Field(None, alias="557", description="")
    LastFragment: Optional[bool] = Field(None, alias="893", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    SecTypesGrp: ForwardRef('SecTypesGrpComponent') = Field(None, description="SecTypesGrp Component")

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
        if self.SecurityReqID is not None:
            fields.append(f"SecurityReqID={self.SecurityReqID}")
        if self.SecurityResponseID is not None:
            fields.append(f"SecurityResponseID={self.SecurityResponseID}")
        if self.SecurityResponseType is not None:
            fields.append(f"SecurityResponseType={self.SecurityResponseType}")
        if self.TotNoSecurityTypes is not None:
            fields.append(f"TotNoSecurityTypes={self.TotNoSecurityTypes}")
        if self.LastFragment is not None:
            fields.append(f"LastFragment={self.LastFragment}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        if self.SecTypesGrp is not None:
            fields.append(f"SecTypesGrp={self.SecTypesGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
SecurityTypesMessage.model_rebuild()
