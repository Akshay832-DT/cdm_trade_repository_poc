"""
FIX NoAffectedOrders field (tag 534).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoAffectedOrdersField(FIXFieldBase):
    """"""
    tag: str = "534"
    name: str = "NoAffectedOrders"
    type: str = "NUMINGROUP"
    value: int
