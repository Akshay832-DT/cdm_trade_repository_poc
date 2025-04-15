"""
FIX TotNumAssignmentReports field (tag 832).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNumAssignmentReportsField(FIXFieldBase):
    """"""
    tag: str = "832"
    name: str = "TotNumAssignmentReports"
    type: str = "INT"
    value: int
