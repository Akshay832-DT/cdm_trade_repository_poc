"""
FIX AllocReportRefID field (tag 795).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocReportRefIDField(FIXFieldBase):
    """"""
    tag: str = "795"
    name: str = "AllocReportRefID"
    type: str = "STRING"
    value: str
