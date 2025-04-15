"""
FIX UnderlyingCountryOfIssue field (tag 592).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingCountryOfIssueField(FIXFieldBase):
    """"""
    tag: str = "592"
    name: str = "UnderlyingCountryOfIssue"
    type: str = "COUNTRY"
    value: str
