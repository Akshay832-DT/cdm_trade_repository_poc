"""
FIX LegPool field (tag 740).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegPoolField(FIXFieldBase):
    """"""
    tag: str = "740"
    name: str = "LegPool"
    type: str = "STRING"
    value: str
