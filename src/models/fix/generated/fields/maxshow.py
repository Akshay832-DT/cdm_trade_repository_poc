"""
FIX MaxShow field (tag 210).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MaxShowField(FIXFieldBase):
    """"""
    tag: str = "210"
    name: str = "MaxShow"
    type: str = "QTY"
    value: float
