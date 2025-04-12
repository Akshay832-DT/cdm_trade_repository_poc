"""
FIX 4.4 PositionQty Component

This module contains the Pydantic model for the PositionQty component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class PositionQty(FIXMessageBase):
    """
    FIX 4.4 PositionQty Component
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
    posType: Optional[str] = Field(None, description='', alias='703')
    longQty: Optional[float] = Field(None, description='', alias='704')
    shortQty: Optional[float] = Field(None, description='', alias='705')
    posQtyStatus: Optional[int] = Field(None, description='', alias='706')
    nestedParties: Optional[str] = Field(None)


class NoPositions(FIXMessageBase):
    """
    NoPositions group fields
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
    posType: Optional[int] = Field(None, description='', alias='702')
    longQty: Optional[int] = Field(None, description='', alias='702')
    shortQty: Optional[int] = Field(None, description='', alias='702')
    posQtyStatus: Optional[int] = Field(None, description='', alias='702')

    noPositionss: List[NoPositions] = Field(default_factory=list)
