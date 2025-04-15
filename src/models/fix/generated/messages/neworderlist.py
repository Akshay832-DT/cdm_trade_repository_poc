"""
FIX NewOrderList Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.listordgrp import ListOrdGrpComponent


# Forward references for components to avoid circular imports
ListOrdGrpComponent = ForwardRef('ListOrdGrpComponent')


class NewOrderListMessage(FIXMessageBase):
    """NewOrderList Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["NewOrderList"] = Field("NewOrderList", alias="35", description="Message Type")

    ListID: Optional[str] = Field(None, alias="66", description="")
    BidID: Optional[str] = Field(None, alias="390", description="")
    ClientBidID: Optional[str] = Field(None, alias="391", description="")
    ProgRptReqs: Optional[int] = Field(None, alias="414", description="")
    BidType: Optional[int] = Field(None, alias="394", description="")
    ProgPeriodInterval: Optional[int] = Field(None, alias="415", description="")
    CancellationRights: Optional[str] = Field(None, alias="480", description="")
    MoneyLaunderingStatus: Optional[str] = Field(None, alias="481", description="")
    RegistID: Optional[str] = Field(None, alias="513", description="")
    ListExecInstType: Optional[str] = Field(None, alias="433", description="")
    ListExecInst: Optional[str] = Field(None, alias="69", description="")
    EncodedListExecInstLen: Optional[int] = Field(None, alias="352", description="")
    EncodedListExecInst: Optional[str] = Field(None, alias="353", description="")
    AllowableOneSidednessPct: Optional[float] = Field(None, alias="765", description="")
    AllowableOneSidednessValue: Optional[float] = Field(None, alias="766", description="")
    AllowableOneSidednessCurr: Optional[str] = Field(None, alias="767", description="")
    TotNoOrders: Optional[int] = Field(None, alias="68", description="")
    LastFragment: Optional[bool] = Field(None, alias="893", description="")
    ListOrdGrp: ForwardRef('ListOrdGrpComponent') = Field(None, description="ListOrdGrp Component")

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
        if self.BidID is not None:
            fields.append(f"BidID={self.BidID}")
        if self.ClientBidID is not None:
            fields.append(f"ClientBidID={self.ClientBidID}")
        if self.ProgRptReqs is not None:
            fields.append(f"ProgRptReqs={self.ProgRptReqs}")
        if self.BidType is not None:
            fields.append(f"BidType={self.BidType}")
        if self.ProgPeriodInterval is not None:
            fields.append(f"ProgPeriodInterval={self.ProgPeriodInterval}")
        if self.CancellationRights is not None:
            fields.append(f"CancellationRights={self.CancellationRights}")
        if self.MoneyLaunderingStatus is not None:
            fields.append(f"MoneyLaunderingStatus={self.MoneyLaunderingStatus}")
        if self.RegistID is not None:
            fields.append(f"RegistID={self.RegistID}")
        if self.ListExecInstType is not None:
            fields.append(f"ListExecInstType={self.ListExecInstType}")
        if self.ListExecInst is not None:
            fields.append(f"ListExecInst={self.ListExecInst}")
        if self.EncodedListExecInstLen is not None:
            fields.append(f"EncodedListExecInstLen={self.EncodedListExecInstLen}")
        if self.EncodedListExecInst is not None:
            fields.append(f"EncodedListExecInst={self.EncodedListExecInst}")
        if self.AllowableOneSidednessPct is not None:
            fields.append(f"AllowableOneSidednessPct={self.AllowableOneSidednessPct}")
        if self.AllowableOneSidednessValue is not None:
            fields.append(f"AllowableOneSidednessValue={self.AllowableOneSidednessValue}")
        if self.AllowableOneSidednessCurr is not None:
            fields.append(f"AllowableOneSidednessCurr={self.AllowableOneSidednessCurr}")
        if self.TotNoOrders is not None:
            fields.append(f"TotNoOrders={self.TotNoOrders}")
        if self.LastFragment is not None:
            fields.append(f"LastFragment={self.LastFragment}")
        if self.ListOrdGrp is not None:
            fields.append(f"ListOrdGrp={self.ListOrdGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
NewOrderListMessage.model_rebuild()
