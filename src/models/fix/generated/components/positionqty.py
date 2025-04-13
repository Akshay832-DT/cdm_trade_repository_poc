"""
FIX 4.4 PositionQty Component

This module contains the Pydantic model for the PositionQty component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoPositionsGroup(FIXComponentBase):
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
    
    PosType: Optional[str] = Field(None, description='', alias='703')
    LongQty: Optional[float] = Field(None, description='', alias='704')
    ShortQty: Optional[float] = Field(None, description='', alias='705')
    PosQtyStatus: Optional[int] = Field(None, description='', alias='706')


class PositionQtyComponent(FIXComponentBase):
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
    
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='NestedParties component')
    NoPositions: Optional[int] = Field(None, description='Number of NoPositions entries', alias='')
    NoPositions_items: List[NoPositionsGroup] = Field(default_factory=list)
