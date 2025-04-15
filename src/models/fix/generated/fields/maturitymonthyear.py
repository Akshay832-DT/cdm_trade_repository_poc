"""
FIX MaturityMonthYear field (tag 200).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MaturityMonthYearField(FIXFieldBase):
    """"""
    tag: str = "200"
    name: str = "MaturityMonthYear"
    type: str = "MONTHYEAR"
    value: str
