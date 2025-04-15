"""
FIX PriceDelta field (tag 811).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PriceDeltaField(FIXFieldBase):
    """"""
    tag: str = "811"
    name: str = "PriceDelta"
    type: str = "FLOAT"
    value: float
