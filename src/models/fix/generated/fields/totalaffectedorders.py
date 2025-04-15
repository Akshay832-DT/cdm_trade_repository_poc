"""
FIX TotalAffectedOrders field (tag 533).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotalAffectedOrdersField(FIXFieldBase):
    """"""
    tag: str = "533"
    name: str = "TotalAffectedOrders"
    type: str = "INT"
    value: int
