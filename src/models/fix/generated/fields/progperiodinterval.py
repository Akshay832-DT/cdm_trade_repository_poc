"""
FIX ProgPeriodInterval field (tag 415).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ProgPeriodIntervalField(FIXFieldBase):
    """"""
    tag: str = "415"
    name: str = "ProgPeriodInterval"
    type: str = "INT"
    value: int
