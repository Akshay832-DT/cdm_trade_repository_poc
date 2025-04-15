"""
FIX NetworkCounterpartySystemStatusResponse Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.compidstatgrp import CompIDStatGrpComponent


# Forward references for components to avoid circular imports
CompIDStatGrpComponent = ForwardRef('CompIDStatGrpComponent')


class NetworkCounterpartySystemStatusResponseMessage(FIXMessageBase):
    """NetworkCounterpartySystemStatusResponse Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["NetworkCounterpartySystemStatusResponse"] = Field("NetworkCounterpartySystemStatusResponse", alias="35", description="Message Type")

    NetworkStatusResponseType: Optional[int] = Field(None, alias="937", description="")
    NetworkRequestID: Optional[str] = Field(None, alias="933", description="")
    NetworkResponseID: Optional[str] = Field(None, alias="932", description="")
    LastNetworkResponseID: Optional[str] = Field(None, alias="934", description="")
    CompIDStatGrp: ForwardRef('CompIDStatGrpComponent') = Field(None, description="CompIDStatGrp Component")

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
        if self.NetworkStatusResponseType is not None:
            fields.append(f"NetworkStatusResponseType={self.NetworkStatusResponseType}")
        if self.NetworkRequestID is not None:
            fields.append(f"NetworkRequestID={self.NetworkRequestID}")
        if self.NetworkResponseID is not None:
            fields.append(f"NetworkResponseID={self.NetworkResponseID}")
        if self.LastNetworkResponseID is not None:
            fields.append(f"LastNetworkResponseID={self.LastNetworkResponseID}")
        if self.CompIDStatGrp is not None:
            fields.append(f"CompIDStatGrp={self.CompIDStatGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
NetworkCounterpartySystemStatusResponseMessage.model_rebuild()
