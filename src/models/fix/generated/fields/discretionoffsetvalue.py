"""
FIX DiscretionOffsetValue field (tag 389).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DiscretionOffsetValueField(FIXFieldBase):
    """"""
    tag: str = "389"
    name: str = "DiscretionOffsetValue"
    type: str = "FLOAT"
    value: float
