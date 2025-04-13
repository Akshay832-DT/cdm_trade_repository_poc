"""
FIX 4.4 InstrmtStrkPxGrp Component

This module contains the Pydantic model for the InstrmtStrkPxGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoStrikesGroup(FIXComponentBase):
    """
    NoStrikes group fields
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
    


class InstrmtStrkPxGrpComponent(FIXComponentBase):
    """
    FIX 4.4 InstrmtStrkPxGrp Component
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
    
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    NoStrikes: Optional[int] = Field(None, description='Number of NoStrikes entries', alias='')
    NoStrikes_items: List[NoStrikesGroup] = Field(default_factory=list)
