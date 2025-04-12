"""
FIX 4.4 CpctyConfGrp Component

This module contains the Pydantic model for the CpctyConfGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class CpctyConfGrp(TradeModel):
    """
    FIX 4.4 CpctyConfGrp Component
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
    OrderCapacity: str = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    OrderCapacityQty: float = Field(None, description='', alias='863')


class NoCapacities(TradeModel):
    """
    NoCapacities group fields
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
    OrderCapacity: str = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    OrderCapacityQty: float = Field(None, description='', alias='863')

    NoCapacitiess: List[NoCapacities] = Field(default_factory=list)
