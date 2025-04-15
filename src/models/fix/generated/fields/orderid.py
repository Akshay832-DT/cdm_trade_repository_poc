"""
FIX OrderID field (tag 37).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderIDField(FIXFieldBase):
    """"""
    tag: str = "37"
    name: str = "OrderID"
    type: str = "STRING"
    value: str
