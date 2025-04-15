"""
FIX UnderlyingStartValue field (tag 884).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingStartValueField(FIXFieldBase):
    """"""
    tag: str = "884"
    name: str = "UnderlyingStartValue"
    type: str = "AMT"
    value: float
