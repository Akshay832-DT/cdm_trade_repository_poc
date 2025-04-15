"""
FIX TotalNetValue field (tag 900).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotalNetValueField(FIXFieldBase):
    """"""
    tag: str = "900"
    name: str = "TotalNetValue"
    type: str = "AMT"
    value: float
