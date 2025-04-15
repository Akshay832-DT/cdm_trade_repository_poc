"""
FIX TradeInputSource field (tag 578).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeInputSourceField(FIXFieldBase):
    """"""
    tag: str = "578"
    name: str = "TradeInputSource"
    type: str = "STRING"
    value: str
