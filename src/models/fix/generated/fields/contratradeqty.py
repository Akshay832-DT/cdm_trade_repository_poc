"""
FIX ContraTradeQty field (tag 437).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContraTradeQtyField(FIXFieldBase):
    """"""
    tag: str = "437"
    name: str = "ContraTradeQty"
    type: str = "QTY"
    value: float
