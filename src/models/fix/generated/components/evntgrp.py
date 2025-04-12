"""
FIX 4.4 EvntGrp Component

This module contains the Pydantic model for the EvntGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class EvntGrp(TradeModel):
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
    EventType: Optional[int] = Field(None, description='', alias='865')
    EventDate: Optional[date] = Field(None, description='', alias='866')
    EventPx: Optional[float] = Field(None, description='', alias='867')
    EventText: Optional[str] = Field(None, description='', alias='868')


class NoEvents(TradeModel):
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

    NoEventss: List[NoEvents] = Field(default_factory=list)
