"""
FIX DefBidSize field (tag 293).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DefBidSizeField(FIXFieldBase):
    """"""
    tag: str = "293"
    name: str = "DefBidSize"
    type: str = "QTY"
    value: float
