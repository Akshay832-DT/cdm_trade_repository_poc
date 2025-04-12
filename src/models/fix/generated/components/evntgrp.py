"""
FIX 4.4 EvntGrp Component

This module contains the Pydantic model for the EvntGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class EvntGrp(FIXMessageBase):
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
    eventType: Optional[int] = Field(None, description='', alias='865')
    eventDate: Optional[date] = Field(None, description='', alias='866')
    eventPx: Optional[float] = Field(None, description='', alias='867')
    eventText: Optional[str] = Field(None, description='', alias='868')


class NoEvents(FIXMessageBase):
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
    eventType: Optional[int] = Field(None, description='', alias='864')
    eventDate: Optional[int] = Field(None, description='', alias='864')
    eventPx: Optional[int] = Field(None, description='', alias='864')
    eventText: Optional[int] = Field(None, description='', alias='864')

    noEventss: List[NoEvents] = Field(default_factory=list)
