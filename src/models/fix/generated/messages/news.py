"""
FIX News Message
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


class NewsMessage(FIXMessageBase):
    """News Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["News"] = Field("News", alias="35", description="Message Type")

    OrigTime: Optional[datetime] = Field(None, alias="42", description="")
    Urgency: Optional[str] = Field(None, alias="61", description="")
    Headline: Optional[str] = Field(None, alias="148", description="")
    EncodedHeadlineLen: Optional[int] = Field(None, alias="358", description="")
    EncodedHeadline: Optional[str] = Field(None, alias="359", description="")
    URLLink: Optional[str] = Field(None, alias="149", description="")
    RawDataLength: Optional[int] = Field(None, alias="95", description="")
    RawData: Optional[str] = Field(None, alias="96", description="")
    RoutingGrp: ForwardRef('RoutingGrpComponent') = Field(None, description="RoutingGrp Component")
    InstrmtGrp: ForwardRef('InstrmtGrpComponent') = Field(None, description="InstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
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
        if self.OrigTime is not None:
            fields.append(f"OrigTime={self.OrigTime}")
        if self.Urgency is not None:
            fields.append(f"Urgency={self.Urgency}")
        if self.Headline is not None:
            fields.append(f"Headline={self.Headline}")
        if self.EncodedHeadlineLen is not None:
            fields.append(f"EncodedHeadlineLen={self.EncodedHeadlineLen}")
        if self.EncodedHeadline is not None:
            fields.append(f"EncodedHeadline={self.EncodedHeadline}")
        if self.URLLink is not None:
            fields.append(f"URLLink={self.URLLink}")
        if self.RawDataLength is not None:
            fields.append(f"RawDataLength={self.RawDataLength}")
        if self.RawData is not None:
            fields.append(f"RawData={self.RawData}")
        if self.RoutingGrp is not None:
            fields.append(f"RoutingGrp={self.RoutingGrp}")
        if self.InstrmtGrp is not None:
            fields.append(f"InstrmtGrp={self.InstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.LinesOfTextGrp is not None:
            fields.append(f"LinesOfTextGrp={self.LinesOfTextGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
NewsMessage.model_rebuild()
