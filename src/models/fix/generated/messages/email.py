"""
FIX Email Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtgrp import InstrmtGrpComponent
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.linesoftextgrp import LinesOfTextGrpComponent
    from ..components.routinggrp import RoutingGrpComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtGrpComponent = ForwardRef('InstrmtGrpComponent')
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
LinesOfTextGrpComponent = ForwardRef('LinesOfTextGrpComponent')
RoutingGrpComponent = ForwardRef('RoutingGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class EmailMessage(FIXMessageBase):
    """Email Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["Email"] = Field("Email", alias="35", description="Message Type")

    EmailThreadID: Optional[str] = Field(None, alias="164", description="")
    EmailType: Optional[str] = Field(None, alias="94", description="")
    OrigTime: Optional[datetime] = Field(None, alias="42", description="")
    Subject: Optional[str] = Field(None, alias="147", description="")
    EncodedSubjectLen: Optional[int] = Field(None, alias="356", description="")
    EncodedSubject: Optional[str] = Field(None, alias="357", description="")
    OrderID: Optional[str] = Field(None, alias="37", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    RawDataLength: Optional[int] = Field(None, alias="95", description="")
    RawData: Optional[str] = Field(None, alias="96", description="")
    RoutingGrp: ForwardRef('RoutingGrpComponent') = Field(None, description="RoutingGrp Component")
    InstrmtGrp: ForwardRef('InstrmtGrpComponent') = Field(None, description="InstrmtGrp Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    LinesOfTextGrp: ForwardRef('LinesOfTextGrpComponent') = Field(None, description="LinesOfTextGrp Component")

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
        if self.EmailThreadID is not None:
            fields.append(f"EmailThreadID={self.EmailThreadID}")
        if self.EmailType is not None:
            fields.append(f"EmailType={self.EmailType}")
        if self.OrigTime is not None:
            fields.append(f"OrigTime={self.OrigTime}")
        if self.Subject is not None:
            fields.append(f"Subject={self.Subject}")
        if self.EncodedSubjectLen is not None:
            fields.append(f"EncodedSubjectLen={self.EncodedSubjectLen}")
        if self.EncodedSubject is not None:
            fields.append(f"EncodedSubject={self.EncodedSubject}")
        if self.OrderID is not None:
            fields.append(f"OrderID={self.OrderID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.RawDataLength is not None:
            fields.append(f"RawDataLength={self.RawDataLength}")
        if self.RawData is not None:
            fields.append(f"RawData={self.RawData}")
        if self.RoutingGrp is not None:
            fields.append(f"RoutingGrp={self.RoutingGrp}")
        if self.InstrmtGrp is not None:
            fields.append(f"InstrmtGrp={self.InstrmtGrp}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.LinesOfTextGrp is not None:
            fields.append(f"LinesOfTextGrp={self.LinesOfTextGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
EmailMessage.model_rebuild()
