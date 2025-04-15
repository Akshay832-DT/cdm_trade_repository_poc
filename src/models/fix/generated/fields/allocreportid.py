"""
FIX AllocReportID field (tag 755).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocReportIDField(FIXFieldBase):
    """"""
    tag: str = "755"
    name: str = "AllocReportID"
    type: str = "STRING"
    value: str
