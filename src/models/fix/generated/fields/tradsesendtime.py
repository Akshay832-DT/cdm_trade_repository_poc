"""
FIX TradSesEndTime field (tag 345).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesEndTimeField(FIXFieldBase):
    """"""
    tag: str = "345"
    name: str = "TradSesEndTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
