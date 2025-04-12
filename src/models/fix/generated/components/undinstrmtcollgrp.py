"""
FIX 4.4 UndInstrmtCollGrp Component

This module contains the Pydantic model for the UndInstrmtCollGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class UndInstrmtCollGrp(TradeModel):
    """
    FIX 4.4 UndInstrmtCollGrp Component
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
    CollAction: Optional[int] = Field(None, description='', alias='944')
    UnderlyingInstrument: Optional[str] = Field(None)


class NoUnderlyings(TradeModel):
    """
    NoUnderlyings group fields
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
    CollAction: Optional[int] = Field(None, description='', alias='944')

    NoUnderlyingss: List[NoUnderlyings] = Field(default_factory=list)
