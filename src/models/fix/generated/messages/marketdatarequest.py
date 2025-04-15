"""
FIX MarketDataRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtmdreqgrp import InstrmtMDReqGrpComponent
    from ..components.mdreqgrp import MDReqGrpComponent
    from ..components.trdgsesgrp import TrdgSesGrpComponent


# Forward references for components to avoid circular imports
InstrmtMDReqGrpComponent = ForwardRef('InstrmtMDReqGrpComponent')
MDReqGrpComponent = ForwardRef('MDReqGrpComponent')
TrdgSesGrpComponent = ForwardRef('TrdgSesGrpComponent')


class MarketDataRequestMessage(FIXMessageBase):
    """MarketDataRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["MarketDataRequest"] = Field("MarketDataRequest", alias="35", description="Message Type")

    MDReqID: Optional[str] = Field(None, alias="262", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    MarketDepth: Optional[int] = Field(None, alias="264", description="")
    MDUpdateType: Optional[int] = Field(None, alias="265", description="")
    AggregatedBook: Optional[bool] = Field(None, alias="266", description="")
    OpenCloseSettlFlag: Optional[List[str]] = Field(None, alias="286", description="")
    Scope: Optional[List[str]] = Field(None, alias="546", description="")
    MDImplicitDelete: Optional[bool] = Field(None, alias="547", description="")
    ApplQueueAction: Optional[int] = Field(None, alias="815", description="")
    ApplQueueMax: Optional[int] = Field(None, alias="812", description="")
    MDReqGrp: ForwardRef('MDReqGrpComponent') = Field(None, description="MDReqGrp Component")
    InstrmtMDReqGrp: ForwardRef('InstrmtMDReqGrpComponent') = Field(None, description="InstrmtMDReqGrp Component")
    TrdgSesGrp: ForwardRef('TrdgSesGrpComponent') = Field(None, description="TrdgSesGrp Component")

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
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        if self.MarketDepth is not None:
            fields.append(f"MarketDepth={self.MarketDepth}")
        if self.MDUpdateType is not None:
            fields.append(f"MDUpdateType={self.MDUpdateType}")
        if self.AggregatedBook is not None:
            fields.append(f"AggregatedBook={self.AggregatedBook}")
        if self.OpenCloseSettlFlag is not None:
            fields.append(f"OpenCloseSettlFlag={self.OpenCloseSettlFlag}")
        if self.Scope is not None:
            fields.append(f"Scope={self.Scope}")
        if self.MDImplicitDelete is not None:
            fields.append(f"MDImplicitDelete={self.MDImplicitDelete}")
        if self.ApplQueueAction is not None:
            fields.append(f"ApplQueueAction={self.ApplQueueAction}")
        if self.ApplQueueMax is not None:
            fields.append(f"ApplQueueMax={self.ApplQueueMax}")
        if self.MDReqGrp is not None:
            fields.append(f"MDReqGrp={self.MDReqGrp}")
        if self.InstrmtMDReqGrp is not None:
            fields.append(f"InstrmtMDReqGrp={self.InstrmtMDReqGrp}")
        if self.TrdgSesGrp is not None:
            fields.append(f"TrdgSesGrp={self.TrdgSesGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
MarketDataRequestMessage.model_rebuild()
