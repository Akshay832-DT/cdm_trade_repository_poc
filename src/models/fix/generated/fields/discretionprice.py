"""
FIX DiscretionPrice field (tag 845).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DiscretionPriceField(FIXFieldBase):
    """"""
    tag: str = "845"
    name: str = "DiscretionPrice"
    type: str = "PRICE"
    value: float
