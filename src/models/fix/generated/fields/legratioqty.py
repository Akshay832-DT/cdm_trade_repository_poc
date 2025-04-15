"""
FIX LegRatioQty field (tag 623).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegRatioQtyField(FIXFieldBase):
    """"""
    tag: str = "623"
    name: str = "LegRatioQty"
    type: str = "FLOAT"
    value: float
