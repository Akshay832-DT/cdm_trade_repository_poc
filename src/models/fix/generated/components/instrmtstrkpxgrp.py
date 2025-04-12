"""
FIX 4.4 InstrmtStrkPxGrp Component

This module contains the Pydantic model for the InstrmtStrkPxGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class InstrmtStrkPxGrp(TradeModel):
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
    Instrument: str = Field(None)


class NoStrikes(TradeModel):
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

    NoStrikess: List[NoStrikes] = Field(default_factory=list)
