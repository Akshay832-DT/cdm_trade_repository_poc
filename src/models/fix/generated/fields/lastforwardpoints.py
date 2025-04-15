"""
FIX LastForwardPoints field (tag 195).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastForwardPointsField(FIXFieldBase):
    """"""
    tag: str = "195"
    name: str = "LastForwardPoints"
    type: str = "PRICEOFFSET"
    value: float
