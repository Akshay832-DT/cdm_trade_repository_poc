"""
FIX 4.4 LegQuotStatGrp Component

This module contains the Pydantic model for the LegQuotStatGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrumentleg import InstrumentLeg
from src.models.fix.generated.components.legstipulations import LegStipulations
from src.models.fix.generated.components.nestedparties import NestedParties


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
    
    legQty: Optional[float] = Field(None, description='', alias='687')
    legSwapType: Optional[int] = Field(None, description='', alias='690')
    legSettlType: Optional[str] = Field(None, description='', alias='587')
    legSettlDate: Optional[date] = Field(None, description='', alias='588')


class LegQuotStatGrp(FIXMessageBase):
    """
    FIX 4.4 LegQuotStatGrp Component
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
    nestedParties: Optional[NestedParties] = Field(None, description='NestedParties component')
    noLegs: Optional[int] = Field(None, description='Number of NoLegs entries', alias='555')
    noLegs_items: List[NoLegs] = Field(default_factory=list)
