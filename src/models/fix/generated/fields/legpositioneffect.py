"""
FIX LegPositionEffect field (tag 564).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegPositionEffectField(FIXFieldBase):
    """"""
    tag: str = "564"
    name: str = "LegPositionEffect"
    type: str = "CHAR"
    value: str
