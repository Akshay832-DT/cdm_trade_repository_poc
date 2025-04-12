"""
FIX 4.4 UndInstrmtCollGrp Component

This module contains the Pydantic model for the UndInstrmtCollGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class UndInstrmtCollGrp(FIXMessageBase):
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
    collAction: Optional[int] = Field(None, description='', alias='944')
    underlyingInstrument: Optional[str] = Field(None)


class NoUnderlyings(FIXMessageBase):
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
    collAction: Optional[int] = Field(None, description='', alias='711')

    noUnderlyingss: List[NoUnderlyings] = Field(default_factory=list)
