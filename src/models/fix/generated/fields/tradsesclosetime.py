"""
FIX TradSesCloseTime field (tag 344).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesCloseTimeField(FIXFieldBase):
    """"""
    tag: str = "344"
    name: str = "TradSesCloseTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
