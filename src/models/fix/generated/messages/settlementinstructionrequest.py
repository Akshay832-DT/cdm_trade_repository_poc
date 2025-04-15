"""
FIX SettlementInstructionRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.parties import PartiesComponent


# Forward references for components to avoid circular imports
PartiesComponent = ForwardRef('PartiesComponent')


class SettlementInstructionRequestMessage(FIXMessageBase):
    """SettlementInstructionRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["SettlementInstructionRequest"] = Field("SettlementInstructionRequest", alias="35", description="Message Type")

    SettlInstReqID: Optional[str] = Field(None, alias="791", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    AllocAccount: Optional[str] = Field(None, alias="79", description="")
    AllocAcctIDSource: Optional[int] = Field(None, alias="661", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    Product: Optional[int] = Field(None, alias="460", description="")
    SecurityType: Optional[str] = Field(None, alias="167", description="")
    CFICode: Optional[str] = Field(None, alias="461", description="")
    EffectiveTime: Optional[datetime] = Field(None, alias="168", description="")
    ExpireTime: Optional[datetime] = Field(None, alias="126", description="")
    LastUpdateTime: Optional[datetime] = Field(None, alias="779", description="")
    StandInstDbType: Optional[int] = Field(None, alias="169", description="")
    StandInstDbName: Optional[str] = Field(None, alias="170", description="")
    StandInstDbID: Optional[str] = Field(None, alias="171", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")

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
        if self.SettlInstReqID is not None:
            fields.append(f"SettlInstReqID={self.SettlInstReqID}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.AllocAccount is not None:
            fields.append(f"AllocAccount={self.AllocAccount}")
        if self.AllocAcctIDSource is not None:
            fields.append(f"AllocAcctIDSource={self.AllocAcctIDSource}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.Product is not None:
            fields.append(f"Product={self.Product}")
        if self.SecurityType is not None:
            fields.append(f"SecurityType={self.SecurityType}")
        if self.CFICode is not None:
            fields.append(f"CFICode={self.CFICode}")
        if self.EffectiveTime is not None:
            fields.append(f"EffectiveTime={self.EffectiveTime}")
        if self.ExpireTime is not None:
            fields.append(f"ExpireTime={self.ExpireTime}")
        if self.LastUpdateTime is not None:
            fields.append(f"LastUpdateTime={self.LastUpdateTime}")
        if self.StandInstDbType is not None:
            fields.append(f"StandInstDbType={self.StandInstDbType}")
        if self.StandInstDbName is not None:
            fields.append(f"StandInstDbName={self.StandInstDbName}")
        if self.StandInstDbID is not None:
            fields.append(f"StandInstDbID={self.StandInstDbID}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
SettlementInstructionRequestMessage.model_rebuild()
