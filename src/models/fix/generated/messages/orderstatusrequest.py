"""
FIX OrderStatusRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrument import InstrumentComponent
    from ..components.parties import PartiesComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
PartiesComponent = ForwardRef('PartiesComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class OrderStatusRequestMessage(FIXMessageBase):
    """OrderStatusRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["OrderStatusRequest"] = Field("OrderStatusRequest", alias="35", description="Message Type")

    OrderID: Optional[str] = Field(None, alias="37", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    SecondaryClOrdID: Optional[str] = Field(None, alias="526", description="")
    ClOrdLinkID: Optional[str] = Field(None, alias="583", description="")
    OrdStatusReqID: Optional[str] = Field(None, alias="790", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")

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
        if self.OrderID is not None:
            fields.append(f"OrderID={self.OrderID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.SecondaryClOrdID is not None:
            fields.append(f"SecondaryClOrdID={self.SecondaryClOrdID}")
        if self.ClOrdLinkID is not None:
            fields.append(f"ClOrdLinkID={self.ClOrdLinkID}")
        if self.OrdStatusReqID is not None:
            fields.append(f"OrdStatusReqID={self.OrdStatusReqID}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.FinancingDetails is not None:
            fields.append(f"FinancingDetails={self.FinancingDetails}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
OrderStatusRequestMessage.model_rebuild()
