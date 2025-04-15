"""
FIX OrderMassStatusRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrument import InstrumentComponent
    from ..components.parties import PartiesComponent
    from ..components.underlyinginstrument import UnderlyingInstrumentComponent


# Forward references for components to avoid circular imports
InstrumentComponent = ForwardRef('InstrumentComponent')
PartiesComponent = ForwardRef('PartiesComponent')
UnderlyingInstrumentComponent = ForwardRef('UnderlyingInstrumentComponent')


class OrderMassStatusRequestMessage(FIXMessageBase):
    """OrderMassStatusRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["OrderMassStatusRequest"] = Field("OrderMassStatusRequest", alias="35", description="Message Type")

    MassStatusReqID: Optional[str] = Field(None, alias="584", description="")
    MassStatusReqType: Optional[int] = Field(None, alias="585", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    UnderlyingInstrument: ForwardRef('UnderlyingInstrumentComponent') = Field(None, description="UnderlyingInstrument Component")

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
        if self.MassStatusReqID is not None:
            fields.append(f"MassStatusReqID={self.MassStatusReqID}")
        if self.MassStatusReqType is not None:
            fields.append(f"MassStatusReqType={self.MassStatusReqType}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.UnderlyingInstrument is not None:
            fields.append(f"UnderlyingInstrument={self.UnderlyingInstrument}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
OrderMassStatusRequestMessage.model_rebuild()
