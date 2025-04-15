"""
FIX IssueDate field (tag 225).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IssueDateField(FIXFieldBase):
    """"""
    tag: str = "225"
    name: str = "IssueDate"
    type: str = "LOCALMKTDATE"
    value: date
