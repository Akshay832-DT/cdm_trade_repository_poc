"""
FIX UnderlyingTradingSessionSubID field (tag 823).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingTradingSessionSubIDField(FIXFieldBase):
    """"""
    tag: str = "823"
    name: str = "UnderlyingTradingSessionSubID"
    type: str = "STRING"
    value: str
