"""
FIX 4.4 MDReqGrp Component

This module contains the Pydantic model for the MDReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoMDEntryTypesGroup(FIXComponentBase):
    """
    NoMDEntryTypes group fields
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
    
    MDEntryType: str = Field(..., description='', alias='269')


class MDReqGrpComponent(FIXComponentBase):
    """
    FIX 4.4 MDReqGrp Component
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
    
    NoMDEntryTypes: Optional[int] = Field(None, description='Number of NoMDEntryTypes entries', alias='')
    NoMDEntryTypes_items: List[NoMDEntryTypesGroup] = Field(default_factory=list)
