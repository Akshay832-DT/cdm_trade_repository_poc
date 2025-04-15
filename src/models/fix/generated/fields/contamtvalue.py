"""
FIX ContAmtValue field (tag 520).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContAmtValueField(FIXFieldBase):
    """"""
    tag: str = "520"
    name: str = "ContAmtValue"
    type: str = "FLOAT"
    value: float
