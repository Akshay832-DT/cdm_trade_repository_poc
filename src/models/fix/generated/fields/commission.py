"""
FIX Commission field (tag 12).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CommissionField(FIXFieldBase):
    """"""
    tag: str = "12"
    name: str = "Commission"
    type: str = "AMT"
    value: float
