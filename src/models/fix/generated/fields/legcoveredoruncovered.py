"""
FIX LegCoveredOrUncovered field (tag 565).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegCoveredOrUncoveredField(FIXFieldBase):
    """"""
    tag: str = "565"
    name: str = "LegCoveredOrUncovered"
    type: str = "INT"
    value: int
