"""
FIX TradSesPreCloseTime field (tag 343).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesPreCloseTimeField(FIXFieldBase):
    """"""
    tag: str = "343"
    name: str = "TradSesPreCloseTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
