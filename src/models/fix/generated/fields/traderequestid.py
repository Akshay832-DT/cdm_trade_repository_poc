"""
FIX TradeRequestID field (tag 568).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeRequestIDField(FIXFieldBase):
    """"""
    tag: str = "568"
    name: str = "TradeRequestID"
    type: str = "STRING"
    value: str
