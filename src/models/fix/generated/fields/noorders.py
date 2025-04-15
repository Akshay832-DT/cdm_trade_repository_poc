"""
FIX NoOrders field (tag 73).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoOrdersField(FIXFieldBase):
    """"""
    tag: str = "73"
    name: str = "NoOrders"
    type: str = "NUMINGROUP"
    value: int
