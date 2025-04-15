"""
FIX LegSide field (tag 624).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSideField(FIXFieldBase):
    """"""
    tag: str = "624"
    name: str = "LegSide"
    type: str = "CHAR"
    value: str
