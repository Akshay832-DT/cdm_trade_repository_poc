"""
FIX OutsideIndexPct field (tag 407).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OutsideIndexPctField(FIXFieldBase):
    """"""
    tag: str = "407"
    name: str = "OutsideIndexPct"
    type: str = "PERCENTAGE"
    value: float
