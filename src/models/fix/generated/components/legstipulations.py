"""
FIX 4.4 LegStipulations Component

This module contains the Pydantic model for the LegStipulations component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


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
    
    legStipulationType: Optional[str] = Field(None, description='', alias='688')
    legStipulationValue: Optional[str] = Field(None, description='', alias='689')


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
    
    noLegStipulations: Optional[int] = Field(None, description='Number of NoLegStipulations entries', alias='683')
    noLegStipulations_items: List[NoLegStipulations] = Field(default_factory=list)
