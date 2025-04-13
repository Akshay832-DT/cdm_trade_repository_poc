"""
FIX 4.4 NstdPtys2SubGrp Component

This module contains the Pydantic model for the NstdPtys2SubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoNested2PartySubIDsGroup(FIXComponentBase):
    """
    NoNested2PartySubIDs group fields
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    Nested2PartySubID: Optional[str] = Field(None, description='', alias='760')
    Nested2PartySubIDType: Optional[int] = Field(None, description='', alias='807')


class NstdPtys2SubGrpComponent(FIXComponentBase):
    """
    FIX 4.4 NstdPtys2SubGrp Component
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    NoNested2PartySubIDs: Optional[int] = Field(None, description='Number of NoNested2PartySubIDs entries', alias='')
    NoNested2PartySubIDs_items: List[NoNested2PartySubIDsGroup] = Field(default_factory=list)
