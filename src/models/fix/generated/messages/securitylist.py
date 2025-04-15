"""
FIX SecurityList Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.seclistgrp import SecListGrpComponent


# Forward references for components to avoid circular imports
SecListGrpComponent = ForwardRef('SecListGrpComponent')


class SecurityListMessage(FIXMessageBase):
    """SecurityList Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["SecurityList"] = Field("SecurityList", alias="35", description="Message Type")

    SecurityReqID: Optional[str] = Field(None, alias="320", description="")
    SecurityResponseID: Optional[str] = Field(None, alias="322", description="")
    SecurityRequestResult: Optional[int] = Field(None, alias="560", description="")
    TotNoRelatedSym: Optional[int] = Field(None, alias="393", description="")
    LastFragment: Optional[bool] = Field(None, alias="893", description="")
    SecListGrp: ForwardRef('SecListGrpComponent') = Field(None, description="SecListGrp Component")

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
        if self.SecurityReqID is not None:
            fields.append(f"SecurityReqID={self.SecurityReqID}")
        if self.SecurityResponseID is not None:
            fields.append(f"SecurityResponseID={self.SecurityResponseID}")
        if self.SecurityRequestResult is not None:
            fields.append(f"SecurityRequestResult={self.SecurityRequestResult}")
        if self.TotNoRelatedSym is not None:
            fields.append(f"TotNoRelatedSym={self.TotNoRelatedSym}")
        if self.LastFragment is not None:
            fields.append(f"LastFragment={self.LastFragment}")
        if self.SecListGrp is not None:
            fields.append(f"SecListGrp={self.SecListGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
SecurityListMessage.model_rebuild()
