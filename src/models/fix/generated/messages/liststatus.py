"""
FIX ListStatus Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.ordliststatgrp import OrdListStatGrpComponent


# Forward references for components to avoid circular imports
OrdListStatGrpComponent = ForwardRef('OrdListStatGrpComponent')


class ListStatusMessage(FIXMessageBase):
    """ListStatus Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["ListStatus"] = Field("ListStatus", alias="35", description="Message Type")

    ListID: Optional[str] = Field(None, alias="66", description="")
    ListStatusType: Optional[int] = Field(None, alias="429", description="")
    NoRpts: Optional[int] = Field(None, alias="82", description="")
    ListOrderStatus: Optional[int] = Field(None, alias="431", description="")
    RptSeq: Optional[int] = Field(None, alias="83", description="")
    ListStatusText: Optional[str] = Field(None, alias="444", description="")
    EncodedListStatusTextLen: Optional[int] = Field(None, alias="445", description="")
    EncodedListStatusText: Optional[str] = Field(None, alias="446", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    TotNoOrders: Optional[int] = Field(None, alias="68", description="")
    LastFragment: Optional[bool] = Field(None, alias="893", description="")
    OrdListStatGrp: ForwardRef('OrdListStatGrpComponent') = Field(None, description="OrdListStatGrp Component")

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
        if self.ListID is not None:
            fields.append(f"ListID={self.ListID}")
        if self.ListStatusType is not None:
            fields.append(f"ListStatusType={self.ListStatusType}")
        if self.NoRpts is not None:
            fields.append(f"NoRpts={self.NoRpts}")
        if self.ListOrderStatus is not None:
            fields.append(f"ListOrderStatus={self.ListOrderStatus}")
        if self.RptSeq is not None:
            fields.append(f"RptSeq={self.RptSeq}")
        if self.ListStatusText is not None:
            fields.append(f"ListStatusText={self.ListStatusText}")
        if self.EncodedListStatusTextLen is not None:
            fields.append(f"EncodedListStatusTextLen={self.EncodedListStatusTextLen}")
        if self.EncodedListStatusText is not None:
            fields.append(f"EncodedListStatusText={self.EncodedListStatusText}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.TotNoOrders is not None:
            fields.append(f"TotNoOrders={self.TotNoOrders}")
        if self.LastFragment is not None:
            fields.append(f"LastFragment={self.LastFragment}")
        if self.OrdListStatGrp is not None:
            fields.append(f"OrdListStatGrp={self.OrdListStatGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
ListStatusMessage.model_rebuild()
