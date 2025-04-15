"""
FIX TotalNumPosReports field (tag 727).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotalNumPosReportsField(FIXFieldBase):
    """"""
    tag: str = "727"
    name: str = "TotalNumPosReports"
    type: str = "INT"
    value: int
