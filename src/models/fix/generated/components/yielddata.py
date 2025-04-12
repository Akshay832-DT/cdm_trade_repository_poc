"""
FIX 4.4 YieldData Component

This module contains the Pydantic model for the YieldData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class YieldData(TradeModel):
    """
    FIX 4.4 YieldData Component
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
    YieldType: Optional[str] = Field(None, description='', alias='235')
    Yield: Optional[float] = Field(None, description='', alias='236')
    YieldCalcDate: Optional[date] = Field(None, description='', alias='701')
    YieldRedemptionDate: Optional[date] = Field(None, description='', alias='696')
    YieldRedemptionPrice: Optional[float] = Field(None, description='', alias='697')
    YieldRedemptionPriceType: Optional[int] = Field(None, description='', alias='698')
