"""
FIX NumberOfOrders field (tag 346).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NumberOfOrdersField(FIXFieldBase):
    """"""
    tag: str = "346"
    name: str = "NumberOfOrders"
    type: str = "INT"
    value: int
