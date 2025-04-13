"""
FIX 4.4 PositionQty Component

This module contains the Pydantic model for the PositionQty component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nestedparties import NestedParties


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
    
    posType: Optional[str] = Field(None, description='', alias='703')
    longQty: Optional[float] = Field(None, description='', alias='704')
    shortQty: Optional[float] = Field(None, description='', alias='705')
    posQtyStatus: Optional[int] = Field(None, description='', alias='706')


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
    
    nestedParties: Optional[NestedParties] = Field(None, description='NestedParties component')
    noPositions: Optional[int] = Field(None, description='Number of NoPositions entries', alias='702')
    noPositions_items: List[NoPositions] = Field(default_factory=list)
