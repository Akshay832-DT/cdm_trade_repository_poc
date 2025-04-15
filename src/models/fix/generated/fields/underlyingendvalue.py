"""
FIX UnderlyingEndValue field (tag 886).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingEndValueField(FIXFieldBase):
    """"""
    tag: str = "886"
    name: str = "UnderlyingEndValue"
    type: str = "AMT"
    value: float
