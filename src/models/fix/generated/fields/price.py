"""
FIX Price field (tag 44).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PriceField(FIXFieldBase):
    """"""
    tag: str = "44"
    name: str = "Price"
    type: str = "PRICE"
    value: float
