"""
FIX LegBidPx field (tag 681).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegBidPxField(FIXFieldBase):
    """"""
    tag: str = "681"
    name: str = "LegBidPx"
    type: str = "PRICE"
    value: float
