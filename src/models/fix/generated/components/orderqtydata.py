"""
FIX 4.4 OrderQtyData Component

This module contains the Pydantic model for the OrderQtyData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class OrderQtyData(TradeModel):
    """
    FIX 4.4 OrderQtyData Component
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
    OrderQty: Optional[float] = Field(None, description='', alias='38')
    CashOrderQty: Optional[float] = Field(None, description='', alias='152')
    OrderPercent: Optional[float] = Field(None, description='', alias='516')
    RoundingDirection: Optional[str] = Field(None, description='', alias='468')
    RoundingModulus: Optional[float] = Field(None, description='', alias='469')
