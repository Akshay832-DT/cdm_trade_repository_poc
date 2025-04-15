"""
FIX UnderlyingMaturityMonthYear field (tag 313).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingMaturityMonthYearField(FIXFieldBase):
    """"""
    tag: str = "313"
    name: str = "UnderlyingMaturityMonthYear"
    type: str = "MONTHYEAR"
    value: str
