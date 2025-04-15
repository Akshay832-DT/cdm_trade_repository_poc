"""
FIX OrderAvgPx field (tag 799).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderAvgPxField(FIXFieldBase):
    """"""
    tag: str = "799"
    name: str = "OrderAvgPx"
    type: str = "PRICE"
    value: float
