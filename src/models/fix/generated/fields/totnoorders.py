"""
FIX TotNoOrders field (tag 68).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNoOrdersField(FIXFieldBase):
    """"""
    tag: str = "68"
    name: str = "TotNoOrders"
    type: str = "INT"
    value: int
