"""
FIX NoUnderlyings field (tag 711).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoUnderlyingsField(FIXFieldBase):
    """"""
    tag: str = "711"
    name: str = "NoUnderlyings"
    type: str = "NUMINGROUP"
    value: int
