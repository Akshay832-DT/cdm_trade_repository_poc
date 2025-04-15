"""
FIX TotNumReports field (tag 911).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNumReportsField(FIXFieldBase):
    """"""
    tag: str = "911"
    name: str = "TotNumReports"
    type: str = "INT"
    value: int
