"""
FIX 4.4 AffectedOrdGrp Component

This module contains the Pydantic model for the AffectedOrdGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class AffectedOrdGrp(FIXMessageBase):
    """
    FIX 4.4 AffectedOrdGrp Component
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
    origClOrdID: Optional[str] = Field(None, description='', alias='41')
    affectedOrderID: Optional[str] = Field(None, description='', alias='535')
    affectedSecondaryOrderID: Optional[str] = Field(None, description='', alias='536')


class NoAffectedOrders(FIXMessageBase):
    """
    NoAffectedOrders group fields
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
    origClOrdID: Optional[int] = Field(None, description='', alias='534')
    affectedOrderID: Optional[int] = Field(None, description='', alias='534')
    affectedSecondaryOrderID: Optional[int] = Field(None, description='', alias='534')

    noAffectedOrderss: List[NoAffectedOrders] = Field(default_factory=list)
