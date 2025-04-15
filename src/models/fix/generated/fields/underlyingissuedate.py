"""
FIX UnderlyingIssueDate field (tag 242).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingIssueDateField(FIXFieldBase):
    """"""
    tag: str = "242"
    name: str = "UnderlyingIssueDate"
    type: str = "LOCALMKTDATE"
    value: date
