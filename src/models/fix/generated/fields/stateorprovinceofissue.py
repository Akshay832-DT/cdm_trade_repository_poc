"""
FIX StateOrProvinceOfIssue field (tag 471).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StateOrProvinceOfIssueField(FIXFieldBase):
    """"""
    tag: str = "471"
    name: str = "StateOrProvinceOfIssue"
    type: str = "STRING"
    value: str
