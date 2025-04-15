"""
FIX OrderCancelRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrument import InstrumentComponent
    from ..components.orderqtydata import OrderQtyDataComponent
    from ..components.parties import PartiesComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
OrderQtyDataComponent = ForwardRef('OrderQtyDataComponent')
PartiesComponent = ForwardRef('PartiesComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class OrderCancelRequestMessage(FIXMessageBase):
    """OrderCancelRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["OrderCancelRequest"] = Field("OrderCancelRequest", alias="35", description="Message Type")

    OrigClOrdID: Optional[str] = Field(None, alias="41", description="")
    OrderID: Optional[str] = Field(None, alias="37", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    SecondaryClOrdID: Optional[str] = Field(None, alias="526", description="")
    ClOrdLinkID: Optional[str] = Field(None, alias="583", description="")
    ListID: Optional[str] = Field(None, alias="66", description="")
    OrigOrdModTime: Optional[datetime] = Field(None, alias="586", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    ComplianceID: Optional[str] = Field(None, alias="376", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    OrderQtyData: ForwardRef('OrderQtyDataComponent') = Field(None, description="OrderQtyData Component")

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
        if self.OrigClOrdID is not None:
            fields.append(f"OrigClOrdID={self.OrigClOrdID}")
        if self.OrderID is not None:
            fields.append(f"OrderID={self.OrderID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.SecondaryClOrdID is not None:
            fields.append(f"SecondaryClOrdID={self.SecondaryClOrdID}")
        if self.ClOrdLinkID is not None:
            fields.append(f"ClOrdLinkID={self.ClOrdLinkID}")
        if self.ListID is not None:
            fields.append(f"ListID={self.ListID}")
        if self.OrigOrdModTime is not None:
            fields.append(f"OrigOrdModTime={self.OrigOrdModTime}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.ComplianceID is not None:
            fields.append(f"ComplianceID={self.ComplianceID}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.FinancingDetails is not None:
            fields.append(f"FinancingDetails={self.FinancingDetails}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.OrderQtyData is not None:
            fields.append(f"OrderQtyData={self.OrderQtyData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
OrderCancelRequestMessage.model_rebuild()
