"""
FIX 4.4 MDRjctGrp Component

This module contains the Pydantic model for the MDRjctGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoAltMDSourceGroup(FIXComponentBase):
    """
    NoAltMDSource group fields
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
    
    AltMDSourceID: Optional[str] = Field(None, description='', alias='817')


class MDRjctGrpComponent(FIXComponentBase):
    """
    FIX 4.4 MDRjctGrp Component
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
    
    NoAltMDSource: Optional[int] = Field(None, description='Number of NoAltMDSource entries', alias='')
    NoAltMDSource_items: List[NoAltMDSourceGroup] = Field(default_factory=list)
