"""
FIX 4.4 YieldData Component

This module contains the Pydantic model for the YieldData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class YieldData(FIXMessageBase):
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
    
    yieldType: Optional[str] = Field(None, description='', alias='235')
    yieldValue: Optional[float] = Field(None, description='', alias='236')
    yieldCalcDate: Optional[date] = Field(None, description='', alias='701')
    yieldRedemptionDate: Optional[date] = Field(None, description='', alias='696')
    yieldRedemptionPrice: Optional[float] = Field(None, description='', alias='697')
    yieldRedemptionPriceType: Optional[int] = Field(None, description='', alias='698')
