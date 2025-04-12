"""
FIX 4.4 TrdCapDtGrp Component

This module contains the Pydantic model for the TrdCapDtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class TrdCapDtGrp(TradeModel):
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
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')


class NoDates(TradeModel):
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
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')

    NoDatess: List[NoDates] = Field(default_factory=list)
