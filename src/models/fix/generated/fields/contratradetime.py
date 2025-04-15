"""
FIX ContraTradeTime field (tag 438).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContraTradeTimeField(FIXFieldBase):
    """"""
    tag: str = "438"
    name: str = "ContraTradeTime"
    type: str = "UTCTIMESTAMP"
    value: datetime
