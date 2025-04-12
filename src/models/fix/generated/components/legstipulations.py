"""
FIX 4.4 LegStipulations Component

This module contains the Pydantic model for the LegStipulations component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class LegStipulations(TradeModel):
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
    LegStipulationType: Optional[str] = Field(None, description='', alias='688')
    LegStipulationValue: Optional[str] = Field(None, description='', alias='689')


class NoLegStipulations(TradeModel):
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
    LegStipulationType: Optional[str] = Field(None, description='', alias='688')
    LegStipulationValue: Optional[str] = Field(None, description='', alias='689')

    NoLegStipulationss: List[NoLegStipulations] = Field(default_factory=list)
