"""
FIX OrderCancelReject Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

class OrderCancelRejectMessage(FIXMessageBase):
    """OrderCancelReject Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["OrderCancelReject"] = Field("OrderCancelReject", alias="35", description="Message Type")

    OrderID: Optional[str] = Field(None, alias="37", description="")
    SecondaryOrderID: Optional[str] = Field(None, alias="198", description="")
    SecondaryClOrdID: Optional[str] = Field(None, alias="526", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    ClOrdLinkID: Optional[str] = Field(None, alias="583", description="")
    OrigClOrdID: Optional[str] = Field(None, alias="41", description="")
    OrdStatus: Optional[str] = Field(None, alias="39", description="")
    WorkingIndicator: Optional[bool] = Field(None, alias="636", description="")
    OrigOrdModTime: Optional[datetime] = Field(None, alias="586", description="")
    ListID: Optional[str] = Field(None, alias="66", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    TradeOriginationDate: Optional[date] = Field(None, alias="229", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    CxlRejResponseTo: Optional[str] = Field(None, alias="434", description="")
    CxlRejReason: Optional[int] = Field(None, alias="102", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")

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
        if self.SecondaryOrderID is not None:
            fields.append(f"SecondaryOrderID={self.SecondaryOrderID}")
        if self.SecondaryClOrdID is not None:
            fields.append(f"SecondaryClOrdID={self.SecondaryClOrdID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.ClOrdLinkID is not None:
            fields.append(f"ClOrdLinkID={self.ClOrdLinkID}")
        if self.OrigClOrdID is not None:
            fields.append(f"OrigClOrdID={self.OrigClOrdID}")
        if self.OrdStatus is not None:
            fields.append(f"OrdStatus={self.OrdStatus}")
        if self.WorkingIndicator is not None:
            fields.append(f"WorkingIndicator={self.WorkingIndicator}")
        if self.OrigOrdModTime is not None:
            fields.append(f"OrigOrdModTime={self.OrigOrdModTime}")
        if self.ListID is not None:
            fields.append(f"ListID={self.ListID}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.TradeOriginationDate is not None:
            fields.append(f"TradeOriginationDate={self.TradeOriginationDate}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.CxlRejResponseTo is not None:
            fields.append(f"CxlRejResponseTo={self.CxlRejResponseTo}")
        if self.CxlRejReason is not None:
            fields.append(f"CxlRejReason={self.CxlRejReason}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
OrderCancelRejectMessage.model_rebuild()
