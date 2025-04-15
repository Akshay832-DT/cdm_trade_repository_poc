"""
FIX Component Model - YieldData
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class YieldDataComponent(FIXComponentBase):
    """FIX Component - YieldData"""
    YieldType: Optional[str] = Field(None, alias='235', description='')
    Yield: Optional[float] = Field(None, alias='236', description='')
    YieldCalcDate: Optional[date] = Field(None, alias='701', description='')
    YieldRedemptionDate: Optional[date] = Field(None, alias='696', description='')
    YieldRedemptionPrice: Optional[float] = Field(None, alias='697', description='')
    YieldRedemptionPriceType: Optional[int] = Field(None, alias='698', description='')

