"""
FIX AvgParPx field (tag 860).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AvgParPxField(FIXFieldBase):
    """"""
    tag: str = "860"
    name: str = "AvgParPx"
    type: str = "PRICE"
    value: float
