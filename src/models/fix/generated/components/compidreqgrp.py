"""
FIX 4.4 CompIDReqGrp Component

This module contains the Pydantic model for the CompIDReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoCompIDs(FIXMessageBase):
    """
    NoCompIDs group fields
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
    
    refCompID: Optional[str] = Field(None, description='', alias='930')
    refSubID: Optional[str] = Field(None, description='', alias='931')
    locationID: Optional[str] = Field(None, description='', alias='283')
    deskID: Optional[str] = Field(None, description='', alias='284')


class CompIDReqGrp(FIXMessageBase):
    """
    FIX 4.4 CompIDReqGrp Component
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
    
    noCompIDs: Optional[int] = Field(None, description='Number of NoCompIDs entries', alias='936')
    noCompIDs_items: List[NoCompIDs] = Field(default_factory=list)
