"""
FIX Pool field (tag 691).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PoolField(FIXFieldBase):
    """"""
    tag: str = "691"
    name: str = "Pool"
    type: str = "STRING"
    value: str
