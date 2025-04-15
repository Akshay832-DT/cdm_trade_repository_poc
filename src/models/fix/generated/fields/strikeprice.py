"""
FIX StrikePrice field (tag 202).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StrikePriceField(FIXFieldBase):
    """"""
    tag: str = "202"
    name: str = "StrikePrice"
    type: str = "PRICE"
    value: float
