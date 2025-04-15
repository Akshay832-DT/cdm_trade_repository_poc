"""
FIX TradeReportTransType field (tag 487).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeReportTransTypeField(FIXFieldBase):
    """"""
    tag: str = "487"
    name: str = "TradeReportTransType"
    type: str = "INT"
    value: int
