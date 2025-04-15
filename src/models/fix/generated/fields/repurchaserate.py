"""
FIX RepurchaseRate field (tag 227).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RepurchaseRateField(FIXFieldBase):
    """"""
    tag: str = "227"
    name: str = "RepurchaseRate"
    type: str = "PERCENTAGE"
    value: float
