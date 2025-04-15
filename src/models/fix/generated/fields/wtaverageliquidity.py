"""
FIX WtAverageLiquidity field (tag 410).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class WtAverageLiquidityField(FIXFieldBase):
    """"""
    tag: str = "410"
    name: str = "WtAverageLiquidity"
    type: str = "PERCENTAGE"
    value: float
