"""
FIX 4.4 NstdPtysSubGrp Component

This module contains the Pydantic model for the NstdPtysSubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoNestedPartySubIDsGroup(FIXComponentBase):
    """
    NoNestedPartySubIDs group fields
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
    
    NestedPartySubID: Optional[str] = Field(None, description='', alias='545')
    NestedPartySubIDType: Optional[int] = Field(None, description='', alias='805')


class NstdPtysSubGrpComponent(FIXComponentBase):
    """
    FIX 4.4 NstdPtysSubGrp Component
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
    
    NoNestedPartySubIDs: Optional[int] = Field(None, description='Number of NoNestedPartySubIDs entries', alias='')
    NoNestedPartySubIDs_items: List[NoNestedPartySubIDsGroup] = Field(default_factory=list)
