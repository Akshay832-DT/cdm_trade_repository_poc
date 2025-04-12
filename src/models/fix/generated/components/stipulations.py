"""
FIX 4.4 Stipulations Component

This module contains the Pydantic model for the Stipulations component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class Stipulations(TradeModel):
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
    StipulationType: Optional[str] = Field(None, description='', alias='233')
    StipulationValue: Optional[str] = Field(None, description='', alias='234')


class NoStipulations(TradeModel):
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

    NoStipulationss: List[NoStipulations] = Field(default_factory=list)
