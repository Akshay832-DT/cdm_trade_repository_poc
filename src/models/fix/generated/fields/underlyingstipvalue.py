"""
FIX UnderlyingStipValue field (tag 889).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingStipValueField(FIXFieldBase):
    """"""
    tag: str = "889"
    name: str = "UnderlyingStipValue"
    type: str = "STRING"
    value: str
