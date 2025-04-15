"""
FIX MarketDepth field (tag 264).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MarketDepthField(FIXFieldBase):
    """"""
    tag: str = "264"
    name: str = "MarketDepth"
    type: str = "INT"
    value: int
