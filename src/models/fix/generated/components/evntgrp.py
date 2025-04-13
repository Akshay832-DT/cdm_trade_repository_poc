"""
FIX 4.4 EvntGrp Component

This module contains the Pydantic model for the EvntGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoEventsGroup(FIXComponentBase):
    """
    NoEvents group fields
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
    
    EventType: Optional[int] = Field(None, description='', alias='865')
    EventDate: Optional[date] = Field(None, description='', alias='866')
    EventPx: Optional[float] = Field(None, description='', alias='867')
    EventText: Optional[str] = Field(None, description='', alias='868')


class EvntGrpComponent(FIXComponentBase):
    """
    FIX 4.4 EvntGrp Component
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
    
    NoEvents: Optional[int] = Field(None, description='Number of NoEvents entries', alias='')
    NoEvents_items: List[NoEventsGroup] = Field(default_factory=list)
