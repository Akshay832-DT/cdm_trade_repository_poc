"""
FIX 4.4 InstrmtLegIOIGrp Component

This module contains the Pydantic model for the InstrmtLegIOIGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class InstrmtLegIOIGrp(TradeModel):
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
    LegIOIQty: Optional[str] = Field(None, description='', alias='682')
    InstrumentLeg: Optional[str] = Field(None)
    LegStipulations: Optional[str] = Field(None)


class NoLegs(TradeModel):
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
    LegIOIQty: Optional[str] = Field(None, description='', alias='682')

    NoLegss: List[NoLegs] = Field(default_factory=list)
