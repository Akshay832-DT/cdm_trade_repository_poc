"""
FIX 4.4 SettlPtysSubGrp Component

This module contains the Pydantic model for the SettlPtysSubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoSettlPartySubIDsGroup(FIXComponentBase):
    """
    NoSettlPartySubIDs group fields
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
    
    SettlPartySubID: Optional[str] = Field(None, description='', alias='785')
    SettlPartySubIDType: Optional[int] = Field(None, description='', alias='786')


class SettlPtysSubGrpComponent(FIXComponentBase):
    """
    FIX 4.4 SettlPtysSubGrp Component
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
    
    NoSettlPartySubIDs: Optional[int] = Field(None, description='Number of NoSettlPartySubIDs entries', alias='')
    NoSettlPartySubIDs_items: List[NoSettlPartySubIDsGroup] = Field(default_factory=list)
