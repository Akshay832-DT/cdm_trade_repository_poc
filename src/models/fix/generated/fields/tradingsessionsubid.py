"""
FIX TradingSessionSubID field (tag 625).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradingSessionSubIDField(FIXFieldBase):
    """"""
    tag: str = "625"
    name: str = "TradingSessionSubID"
    type: str = "STRING"
    value: str
