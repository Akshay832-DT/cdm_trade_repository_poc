"""
FIX AllocationReportAck Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.allocackgrp import AllocAckGrpComponent
    from ..components.parties import PartiesComponent


# Forward references for components to avoid circular imports
AllocAckGrpComponent = ForwardRef('AllocAckGrpComponent')
PartiesComponent = ForwardRef('PartiesComponent')


class AllocationReportAckMessage(FIXMessageBase):
    """AllocationReportAck Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["AllocationReportAck"] = Field("AllocationReportAck", alias="35", description="Message Type")

    AllocReportID: Optional[str] = Field(None, alias="755", description="")
    AllocID: Optional[str] = Field(None, alias="70", description="")
    SecondaryAllocID: Optional[str] = Field(None, alias="793", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    AllocStatus: Optional[int] = Field(None, alias="87", description="")
    AllocRejCode: Optional[int] = Field(None, alias="88", description="")
    AllocReportType: Optional[int] = Field(None, alias="794", description="")
    AllocIntermedReqType: Optional[int] = Field(None, alias="808", description="")
    MatchStatus: Optional[str] = Field(None, alias="573", description="")
    Product: Optional[int] = Field(None, alias="460", description="")
    SecurityType: Optional[str] = Field(None, alias="167", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    AllocAckGrp: ForwardRef('AllocAckGrpComponent') = Field(None, description="AllocAckGrp Component")

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
        if self.AllocReportID is not None:
            fields.append(f"AllocReportID={self.AllocReportID}")
        if self.AllocID is not None:
            fields.append(f"AllocID={self.AllocID}")
        if self.SecondaryAllocID is not None:
            fields.append(f"SecondaryAllocID={self.SecondaryAllocID}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.AllocStatus is not None:
            fields.append(f"AllocStatus={self.AllocStatus}")
        if self.AllocRejCode is not None:
            fields.append(f"AllocRejCode={self.AllocRejCode}")
        if self.AllocReportType is not None:
            fields.append(f"AllocReportType={self.AllocReportType}")
        if self.AllocIntermedReqType is not None:
            fields.append(f"AllocIntermedReqType={self.AllocIntermedReqType}")
        if self.MatchStatus is not None:
            fields.append(f"MatchStatus={self.MatchStatus}")
        if self.Product is not None:
            fields.append(f"Product={self.Product}")
        if self.SecurityType is not None:
            fields.append(f"SecurityType={self.SecurityType}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.AllocAckGrp is not None:
            fields.append(f"AllocAckGrp={self.AllocAckGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
AllocationReportAckMessage.model_rebuild()
