"""
FIX OrderBookingQty field (tag 800).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderBookingQtyField(FIXFieldBase):
    """"""
    tag: str = "800"
    name: str = "OrderBookingQty"
    type: str = "QTY"
    value: float
