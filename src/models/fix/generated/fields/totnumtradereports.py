"""
FIX TotNumTradeReports field (tag 748).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNumTradeReportsField(FIXFieldBase):
    """"""
    tag: str = "748"
    name: str = "TotNumTradeReports"
    type: str = "INT"
    value: int
