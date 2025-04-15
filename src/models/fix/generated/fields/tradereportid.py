"""
FIX TradeReportID field (tag 571).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeReportIDField(FIXFieldBase):
    """"""
    tag: str = "571"
    name: str = "TradeReportID"
    type: str = "STRING"
    value: str
