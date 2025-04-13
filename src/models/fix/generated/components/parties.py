"""
FIX 4.4 Parties Component

This module contains the Pydantic model for the Parties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoPartyIDsGroup(FIXComponentBase):
    """
    NoPartyIDs group fields
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
    
    PartyID: Optional[str] = Field(None, description='', alias='448')
    PartyIDSource: Optional[str] = Field(None, description='', alias='447')
    PartyRole: Optional[int] = Field(None, description='', alias='452')


class PartiesComponent(FIXComponentBase):
    """
    FIX 4.4 Parties Component
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
    
    PtysSubGrp: Optional[PtysSubGrpComponent] = Field(None, description='PtysSubGrp component')
    NoPartyIDs: Optional[int] = Field(None, description='Number of NoPartyIDs entries', alias='')
    NoPartyIDs_items: List[NoPartyIDsGroup] = Field(default_factory=list)
