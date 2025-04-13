"""
FIX 4.4 Stipulations Component

This module contains the Pydantic model for the Stipulations component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoStipulationsGroup(FIXComponentBase):
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
    
    StipulationType: Optional[str] = Field(None, description='', alias='233')
    StipulationValue: Optional[str] = Field(None, description='', alias='234')


class StipulationsComponent(FIXComponentBase):
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
    
    NoStipulations: Optional[int] = Field(None, description='Number of NoStipulations entries', alias='')
    NoStipulations_items: List[NoStipulationsGroup] = Field(default_factory=list)
