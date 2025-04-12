"""
FIX 4.4 Stipulations Component

This module contains the Pydantic model for the Stipulations component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class Stipulations(FIXMessageBase):
    """
    FIX 4.4 Stipulations Component
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
    stipulationType: Optional[str] = Field(None, description='', alias='233')
    stipulationValue: Optional[str] = Field(None, description='', alias='234')


class NoStipulations(FIXMessageBase):
    """
    NoStipulations group fields
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
    stipulationType: Optional[int] = Field(None, description='', alias='232')
    stipulationValue: Optional[int] = Field(None, description='', alias='232')

    noStipulationss: List[NoStipulations] = Field(default_factory=list)
