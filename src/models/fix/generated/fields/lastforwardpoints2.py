"""
FIX LastForwardPoints2 field (tag 641).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastForwardPoints2Field(FIXFieldBase):
    """"""
    tag: str = "641"
    name: str = "LastForwardPoints2"
    type: str = "PRICEOFFSET"
    value: float
