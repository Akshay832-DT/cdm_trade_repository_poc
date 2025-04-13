"""
FIX 4.4 NestedParties3 Component

This module contains the Pydantic model for the NestedParties3 component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoNested3PartyIDsGroup(FIXComponentBase):
    """
    NoNested3PartyIDs group fields
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
    
    Nested3PartyID: Optional[str] = Field(None, description='', alias='949')
    Nested3PartyIDSource: Optional[str] = Field(None, description='', alias='950')
    Nested3PartyRole: Optional[int] = Field(None, description='', alias='951')


class NestedParties3Component(FIXComponentBase):
    """
    FIX 4.4 NestedParties3 Component
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
    
    NstdPtys3SubGrp: Optional[NstdPtys3SubGrpComponent] = Field(None, description='NstdPtys3SubGrp component')
    NoNested3PartyIDs: Optional[int] = Field(None, description='Number of NoNested3PartyIDs entries', alias='')
    NoNested3PartyIDs_items: List[NoNested3PartyIDsGroup] = Field(default_factory=list)
