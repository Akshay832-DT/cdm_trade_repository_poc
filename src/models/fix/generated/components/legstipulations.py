"""
FIX 4.4 LegStipulations Component

This module contains the Pydantic model for the LegStipulations component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class LegStipulations(FIXMessageBase):
    """
    FIX 4.4 LegStipulations Component
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
    legStipulationType: Optional[str] = Field(None, description='', alias='688')
    legStipulationValue: Optional[str] = Field(None, description='', alias='689')


class NoLegStipulations(FIXMessageBase):
    """
    NoLegStipulations group fields
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
    legStipulationType: Optional[int] = Field(None, description='', alias='683')
    legStipulationValue: Optional[int] = Field(None, description='', alias='683')

    noLegStipulationss: List[NoLegStipulations] = Field(default_factory=list)
