"""
FIX ReportedPx field (tag 861).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ReportedPxField(FIXFieldBase):
    """"""
    tag: str = "861"
    name: str = "ReportedPx"
    type: str = "PRICE"
    value: float
