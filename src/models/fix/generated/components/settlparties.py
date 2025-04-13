"""
FIX 4.4 SettlParties Component

This module contains the Pydantic model for the SettlParties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoSettlPartyIDsGroup(FIXComponentBase):
    """
    NoSettlPartyIDs group fields
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
    
    SettlPartyID: Optional[str] = Field(None, description='', alias='782')
    SettlPartyIDSource: Optional[str] = Field(None, description='', alias='783')
    SettlPartyRole: Optional[int] = Field(None, description='', alias='784')


class SettlPartiesComponent(FIXComponentBase):
    """
    FIX 4.4 SettlParties Component
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
    
    SettlPtysSubGrp: Optional[SettlPtysSubGrpComponent] = Field(None, description='SettlPtysSubGrp component')
    NoSettlPartyIDs: Optional[int] = Field(None, description='Number of NoSettlPartyIDs entries', alias='')
    NoSettlPartyIDs_items: List[NoSettlPartyIDsGroup] = Field(default_factory=list)
