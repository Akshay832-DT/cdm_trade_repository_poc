"""
FIX Component Model - OrderQtyData
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class OrderQtyDataComponent(FIXComponentBase):
    """FIX Component - OrderQtyData"""
    OrderQty: Optional[float] = Field(None, alias='38', description='')
    CashOrderQty: Optional[float] = Field(None, alias='152', description='')
    OrderPercent: Optional[float] = Field(None, alias='516', description='')
    RoundingDirection: Optional[str] = Field(None, alias='468', description='')
    RoundingModulus: Optional[float] = Field(None, alias='469', description='')

