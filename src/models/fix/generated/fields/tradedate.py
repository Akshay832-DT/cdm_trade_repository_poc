"""
FIX TradeDate field (tag 75).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeDateField(FIXFieldBase):
    """"""
    tag: str = "75"
    name: str = "TradeDate"
    type: str = "LOCALMKTDATE"
    value: date
