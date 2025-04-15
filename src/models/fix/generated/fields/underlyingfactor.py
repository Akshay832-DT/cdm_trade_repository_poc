"""
FIX UnderlyingFactor field (tag 246).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingFactorField(FIXFieldBase):
    """"""
    tag: str = "246"
    name: str = "UnderlyingFactor"
    type: str = "FLOAT"
    value: float
