"""
FIX MaturityDate field (tag 541).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MaturityDateField(FIXFieldBase):
    """"""
    tag: str = "541"
    name: str = "MaturityDate"
    type: str = "LOCALMKTDATE"
    value: date
