"""
FIX MarginExcess field (tag 899).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MarginExcessField(FIXFieldBase):
    """"""
    tag: str = "899"
    name: str = "MarginExcess"
    type: str = "AMT"
    value: float
