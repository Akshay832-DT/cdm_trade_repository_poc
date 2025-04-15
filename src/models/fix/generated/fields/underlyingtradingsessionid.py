"""
FIX UnderlyingTradingSessionID field (tag 822).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingTradingSessionIDField(FIXFieldBase):
    """"""
    tag: str = "822"
    name: str = "UnderlyingTradingSessionID"
    type: str = "STRING"
    value: str
