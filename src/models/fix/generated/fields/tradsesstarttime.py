"""
FIX TradSesStartTime field (tag 341).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesStartTimeField(FIXFieldBase):
    """"""
    tag: str = "341"
    name: str = "TradSesStartTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
