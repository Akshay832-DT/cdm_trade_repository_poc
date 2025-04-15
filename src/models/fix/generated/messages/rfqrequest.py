"""
FIX RFQRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.rfqreqgrp import RFQReqGrpComponent


# Forward references for components to avoid circular imports
RFQReqGrpComponent = ForwardRef('RFQReqGrpComponent')


class RFQRequestMessage(FIXMessageBase):
    """RFQRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["RFQRequest"] = Field("RFQRequest", alias="35", description="Message Type")

    RFQReqID: Optional[str] = Field(None, alias="644", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    RFQReqGrp: ForwardRef('RFQReqGrpComponent') = Field(None, description="RFQReqGrp Component")

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
        if self.RFQReqID is not None:
            fields.append(f"RFQReqID={self.RFQReqID}")
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        if self.RFQReqGrp is not None:
            fields.append(f"RFQReqGrp={self.RFQReqGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
RFQRequestMessage.model_rebuild()
