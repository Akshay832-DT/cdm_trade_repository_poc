"""
FIX LegPriceType field (tag 686).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegPriceTypeField(FIXFieldBase):
    """"""
    tag: str = "686"
    name: str = "LegPriceType"
    type: str = "INT"
    value: int
