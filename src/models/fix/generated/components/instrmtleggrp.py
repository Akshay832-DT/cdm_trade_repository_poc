"""
FIX 4.4 InstrmtLegGrp Component

This module contains the Pydantic model for the InstrmtLegGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoLegsGroup(FIXComponentBase):
    """
    NoLegs group fields
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
    


class InstrmtLegGrpComponent(FIXComponentBase):
    """
    FIX 4.4 InstrmtLegGrp Component
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
    
    InstrumentLeg: Optional[InstrumentLegComponent] = Field(None, description='InstrumentLeg component')
    NoLegs: Optional[int] = Field(None, description='Number of NoLegs entries', alias='')
    NoLegs_items: List[NoLegsGroup] = Field(default_factory=list)
