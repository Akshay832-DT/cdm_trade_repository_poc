"""
FIX TradeReportRefID field (tag 572).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeReportRefIDField(FIXFieldBase):
    """"""
    tag: str = "572"
    name: str = "TradeReportRefID"
    type: str = "STRING"
    value: str
