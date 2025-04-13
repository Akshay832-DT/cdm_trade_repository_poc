"""
FIX 4.4 MDReqGrp Component

This module contains the Pydantic model for the MDReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoMDEntryTypes(FIXMessageBase):
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
    
    mDEntryType: str = Field(..., description='', alias='269')


class MDReqGrp(FIXMessageBase):
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
    
    noMDEntryTypes: Optional[int] = Field(None, description='Number of NoMDEntryTypes entries', alias='267')
    noMDEntryTypes_items: List[NoMDEntryTypes] = Field(default_factory=list)
