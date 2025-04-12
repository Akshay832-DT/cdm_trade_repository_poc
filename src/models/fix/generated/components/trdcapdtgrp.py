"""
FIX 4.4 TrdCapDtGrp Component

This module contains the Pydantic model for the TrdCapDtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class TrdCapDtGrp(FIXMessageBase):
    """
    FIX 4.4 TrdCapDtGrp Component
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
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')


class NoDates(FIXMessageBase):
    """
    NoDates group fields
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
    tradeDate: Optional[int] = Field(None, description='', alias='580')
    transactTime: Optional[int] = Field(None, description='', alias='580')

    noDatess: List[NoDates] = Field(default_factory=list)
