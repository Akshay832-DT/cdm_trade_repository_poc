"""
FIX LegIssueDate field (tag 249).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegIssueDateField(FIXFieldBase):
    """"""
    tag: str = "249"
    name: str = "LegIssueDate"
    type: str = "LOCALMKTDATE"
    value: date
