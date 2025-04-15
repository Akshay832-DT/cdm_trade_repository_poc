"""
FIX TradSesOpenTime field (tag 342).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesOpenTimeField(FIXFieldBase):
    """"""
    tag: str = "342"
    name: str = "TradSesOpenTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
