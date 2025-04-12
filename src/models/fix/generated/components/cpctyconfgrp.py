"""
FIX 4.4 CpctyConfGrp Component

This module contains the Pydantic model for the CpctyConfGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class CpctyConfGrp(FIXMessageBase):
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
    orderCapacity: str = Field(None, description='', alias='528')
    orderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    orderCapacityQty: float = Field(None, description='', alias='863')


class NoCapacities(FIXMessageBase):
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
    orderCapacity: int = Field(None, description='', alias='862')
    orderRestrictions: Optional[int] = Field(None, description='', alias='862')
    orderCapacityQty: int = Field(None, description='', alias='862')

    noCapacitiess: List[NoCapacities] = Field(default_factory=list)
