"""
FIX LegMaturityMonthYear field (tag 610).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegMaturityMonthYearField(FIXFieldBase):
    """"""
    tag: str = "610"
    name: str = "LegMaturityMonthYear"
    type: str = "MONTHYEAR"
    value: str
