"""
FIX 4.4 InstrmtLegIOIGrp Component

This module contains the Pydantic model for the InstrmtLegIOIGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrumentleg import InstrumentLeg
from src.models.fix.generated.components.legstipulations import LegStipulations


class NoLegs(FIXMessageBase):
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
    
    legIOIQty: Optional[str] = Field(None, description='', alias='682')


class InstrmtLegIOIGrp(FIXMessageBase):
    """
    FIX 4.4 InstrmtLegIOIGrp Component
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
    
    instrumentLeg: Optional[InstrumentLeg] = Field(None, description='InstrumentLeg component')
    legStipulations: Optional[LegStipulations] = Field(None, description='LegStipulations component')
    noLegs: Optional[int] = Field(None, description='Number of NoLegs entries', alias='555')
    noLegs_items: List[NoLegs] = Field(default_factory=list)
