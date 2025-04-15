"""
FIX LegLocaleOfIssue field (tag 598).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegLocaleOfIssueField(FIXFieldBase):
    """"""
    tag: str = "598"
    name: str = "LegLocaleOfIssue"
    type: str = "STRING"
    value: str
