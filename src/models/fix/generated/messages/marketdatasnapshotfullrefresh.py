"""
FIX MarketDataSnapshotFullRefresh Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.mdfullgrp import MDFullGrpComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
MDFullGrpComponent = ForwardRef('MDFullGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class MarketDataSnapshotFullRefreshMessage(FIXMessageBase):
    """MarketDataSnapshotFullRefresh Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["MarketDataSnapshotFullRefresh"] = Field("MarketDataSnapshotFullRefresh", alias="35", description="Message Type")

    MDReqID: Optional[str] = Field(None, alias="262", description="")
    FinancialStatus: Optional[List[str]] = Field(None, alias="291", description="")
    CorporateAction: Optional[List[str]] = Field(None, alias="292", description="")
    NetChgPrevDay: Optional[float] = Field(None, alias="451", description="")
    ApplQueueDepth: Optional[int] = Field(None, alias="813", description="")
    ApplQueueResolution: Optional[int] = Field(None, alias="814", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    MDFullGrp: ForwardRef('MDFullGrpComponent') = Field(None, description="MDFullGrp Component")

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
        if self.FinancialStatus is not None:
            fields.append(f"FinancialStatus={self.FinancialStatus}")
        if self.CorporateAction is not None:
            fields.append(f"CorporateAction={self.CorporateAction}")
        if self.NetChgPrevDay is not None:
            fields.append(f"NetChgPrevDay={self.NetChgPrevDay}")
        if self.ApplQueueDepth is not None:
            fields.append(f"ApplQueueDepth={self.ApplQueueDepth}")
        if self.ApplQueueResolution is not None:
            fields.append(f"ApplQueueResolution={self.ApplQueueResolution}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.MDFullGrp is not None:
            fields.append(f"MDFullGrp={self.MDFullGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
MarketDataSnapshotFullRefreshMessage.model_rebuild()
