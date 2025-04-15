"""
FIX LastSpotRate field (tag 194).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastSpotRateField(FIXFieldBase):
    """"""
    tag: str = "194"
    name: str = "LastSpotRate"
    type: str = "PRICE"
    value: float
