"""
FIX NoTrades field (tag 897).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoTradesField(FIXFieldBase):
    """"""
    tag: str = "897"
    name: str = "NoTrades"
    type: str = "NUMINGROUP"
    value: int
