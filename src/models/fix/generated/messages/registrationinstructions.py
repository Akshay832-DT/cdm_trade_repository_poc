"""
FIX RegistrationInstructions Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.parties import PartiesComponent
    from ..components.rgstdistinstgrp import RgstDistInstGrpComponent
    from ..components.rgstdtlsgrp import RgstDtlsGrpComponent


# Forward references for components to avoid circular imports
PartiesComponent = ForwardRef('PartiesComponent')
RgstDistInstGrpComponent = ForwardRef('RgstDistInstGrpComponent')
RgstDtlsGrpComponent = ForwardRef('RgstDtlsGrpComponent')


class RegistrationInstructionsMessage(FIXMessageBase):
    """RegistrationInstructions Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["RegistrationInstructions"] = Field("RegistrationInstructions", alias="35", description="Message Type")

    RegistID: Optional[str] = Field(None, alias="513", description="")
    RegistTransType: Optional[str] = Field(None, alias="514", description="")
    RegistRefID: Optional[str] = Field(None, alias="508", description="")
    ClOrdID: Optional[str] = Field(None, alias="11", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    RegistAcctType: Optional[str] = Field(None, alias="493", description="")
    TaxAdvantageType: Optional[int] = Field(None, alias="495", description="")
    OwnershipType: Optional[str] = Field(None, alias="517", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    RgstDtlsGrp: ForwardRef('RgstDtlsGrpComponent') = Field(None, description="RgstDtlsGrp Component")
    RgstDistInstGrp: ForwardRef('RgstDistInstGrpComponent') = Field(None, description="RgstDistInstGrp Component")

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
        if self.RegistID is not None:
            fields.append(f"RegistID={self.RegistID}")
        if self.RegistTransType is not None:
            fields.append(f"RegistTransType={self.RegistTransType}")
        if self.RegistRefID is not None:
            fields.append(f"RegistRefID={self.RegistRefID}")
        if self.ClOrdID is not None:
            fields.append(f"ClOrdID={self.ClOrdID}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.RegistAcctType is not None:
            fields.append(f"RegistAcctType={self.RegistAcctType}")
        if self.TaxAdvantageType is not None:
            fields.append(f"TaxAdvantageType={self.TaxAdvantageType}")
        if self.OwnershipType is not None:
            fields.append(f"OwnershipType={self.OwnershipType}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.RgstDtlsGrp is not None:
            fields.append(f"RgstDtlsGrp={self.RgstDtlsGrp}")
        if self.RgstDistInstGrp is not None:
            fields.append(f"RgstDistInstGrp={self.RgstDistInstGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
RegistrationInstructionsMessage.model_rebuild()
