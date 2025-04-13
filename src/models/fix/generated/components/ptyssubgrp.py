"""
FIX 4.4 PtysSubGrp Component

This module contains the Pydantic model for the PtysSubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoPartySubIDsGroup(FIXComponentBase):
    """
    NoPartySubIDs group fields
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
    
    PartySubID: Optional[str] = Field(None, description='', alias='523')
    PartySubIDType: Optional[int] = Field(None, description='', alias='803')


class PtysSubGrpComponent(FIXComponentBase):
    """
    FIX 4.4 PtysSubGrp Component
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
    
    NoPartySubIDs: Optional[int] = Field(None, description='Number of NoPartySubIDs entries', alias='')
    NoPartySubIDs_items: List[NoPartySubIDsGroup] = Field(default_factory=list)
