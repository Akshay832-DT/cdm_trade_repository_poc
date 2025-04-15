"""
FIX MktBidPx field (tag 645).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MktBidPxField(FIXFieldBase):
    """"""
    tag: str = "645"
    name: str = "MktBidPx"
    type: str = "PRICE"
    value: float
