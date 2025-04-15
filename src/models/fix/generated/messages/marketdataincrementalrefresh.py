"""
FIX MarketDataIncrementalRefresh Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.mdincgrp import MDIncGrpComponent


# Forward references for components to avoid circular imports
MDIncGrpComponent = ForwardRef('MDIncGrpComponent')


class MarketDataIncrementalRefreshMessage(FIXMessageBase):
    """MarketDataIncrementalRefresh Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["MarketDataIncrementalRefresh"] = Field("MarketDataIncrementalRefresh", alias="35", description="Message Type")

    MDReqID: Optional[str] = Field(None, alias="262", description="")
    ApplQueueDepth: Optional[int] = Field(None, alias="813", description="")
    ApplQueueResolution: Optional[int] = Field(None, alias="814", description="")
    MDIncGrp: ForwardRef('MDIncGrpComponent') = Field(None, description="MDIncGrp Component")

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
        if self.MDReqID is not None:
            fields.append(f"MDReqID={self.MDReqID}")
        if self.ApplQueueDepth is not None:
            fields.append(f"ApplQueueDepth={self.ApplQueueDepth}")
        if self.ApplQueueResolution is not None:
            fields.append(f"ApplQueueResolution={self.ApplQueueResolution}")
        if self.MDIncGrp is not None:
            fields.append(f"MDIncGrp={self.MDIncGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
MarketDataIncrementalRefreshMessage.model_rebuild()
