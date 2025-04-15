"""
FIX UnderlyingStateOrProvinceOfIssue field (tag 593).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingStateOrProvinceOfIssueField(FIXFieldBase):
    """"""
    tag: str = "593"
    name: str = "UnderlyingStateOrProvinceOfIssue"
    type: str = "STRING"
    value: str
