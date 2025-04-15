"""
FIX LegAllocAccount field (tag 671).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegAllocAccountField(FIXFieldBase):
    """"""
    tag: str = "671"
    name: str = "LegAllocAccount"
    type: str = "STRING"
    value: str
