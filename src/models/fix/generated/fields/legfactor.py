"""
FIX LegFactor field (tag 253).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegFactorField(FIXFieldBase):
    """"""
    tag: str = "253"
    name: str = "LegFactor"
    type: str = "FLOAT"
    value: float
