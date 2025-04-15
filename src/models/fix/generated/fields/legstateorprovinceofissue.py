"""
FIX LegStateOrProvinceOfIssue field (tag 597).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegStateOrProvinceOfIssueField(FIXFieldBase):
    """"""
    tag: str = "597"
    name: str = "LegStateOrProvinceOfIssue"
    type: str = "STRING"
    value: str
