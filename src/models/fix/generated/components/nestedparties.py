"""
FIX 4.4 NestedParties Component

This module contains the Pydantic model for the NestedParties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoNestedPartyIDsGroup(FIXComponentBase):
    """
    NoNestedPartyIDs group fields
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
    
    NestedPartyID: Optional[str] = Field(None, description='', alias='524')
    NestedPartyIDSource: Optional[str] = Field(None, description='', alias='525')
    NestedPartyRole: Optional[int] = Field(None, description='', alias='538')


class NestedPartiesComponent(FIXComponentBase):
    """
    FIX 4.4 NestedParties Component
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
    
    NstdPtysSubGrp: Optional[NstdPtysSubGrpComponent] = Field(None, description='NstdPtysSubGrp component')
    NoNestedPartyIDs: Optional[int] = Field(None, description='Number of NoNestedPartyIDs entries', alias='')
    NoNestedPartyIDs_items: List[NoNestedPartyIDsGroup] = Field(default_factory=list)
