"""
FIX SecondaryTradeReportID field (tag 818).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecondaryTradeReportIDField(FIXFieldBase):
    """"""
    tag: str = "818"
    name: str = "SecondaryTradeReportID"
    type: str = "STRING"
    value: str
