"""
FIX UnderlyingLocaleOfIssue field (tag 594).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingLocaleOfIssueField(FIXFieldBase):
    """"""
    tag: str = "594"
    name: str = "UnderlyingLocaleOfIssue"
    type: str = "STRING"
    value: str
