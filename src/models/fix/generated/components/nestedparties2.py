"""
FIX 4.4 NestedParties2 Component

This module contains the Pydantic model for the NestedParties2 component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoNested2PartyIDsGroup(FIXComponentBase):
    """
    NoNested2PartyIDs group fields
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
    
    Nested2PartyID: Optional[str] = Field(None, description='', alias='757')
    Nested2PartyIDSource: Optional[str] = Field(None, description='', alias='758')
    Nested2PartyRole: Optional[int] = Field(None, description='', alias='759')


class NestedParties2Component(FIXComponentBase):
    """
    FIX 4.4 NestedParties2 Component
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
    
    NstdPtys2SubGrp: Optional[NstdPtys2SubGrpComponent] = Field(None, description='NstdPtys2SubGrp component')
    NoNested2PartyIDs: Optional[int] = Field(None, description='Number of NoNested2PartyIDs entries', alias='')
    NoNested2PartyIDs_items: List[NoNested2PartyIDsGroup] = Field(default_factory=list)
