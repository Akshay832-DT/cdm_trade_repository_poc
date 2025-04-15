"""
FIX TradingSessionID field (tag 336).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradingSessionIDField(FIXFieldBase):
    """"""
    tag: str = "336"
    name: str = "TradingSessionID"
    type: str = "STRING"
    value: str
