"""
FIX UnderlyingCurrentValue field (tag 885).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCurrentValueField(FIXFieldBase):
    """"""
    tag: str = "885"
    name: str = "UnderlyingCurrentValue"
    type: str = "AMT"
    value: float
