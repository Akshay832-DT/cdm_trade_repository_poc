"""
FIX AllocPrice field (tag 366).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocPriceField(FIXFieldBase):
    """"""
    tag: str = "366"
    name: str = "AllocPrice"
    type: str = "PRICE"
    value: float
