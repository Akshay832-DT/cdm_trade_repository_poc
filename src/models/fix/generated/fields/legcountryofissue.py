"""
FIX LegCountryOfIssue field (tag 596).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegCountryOfIssueField(FIXFieldBase):
    """"""
    tag: str = "596"
    name: str = "LegCountryOfIssue"
    type: str = "COUNTRY"
    value: str
