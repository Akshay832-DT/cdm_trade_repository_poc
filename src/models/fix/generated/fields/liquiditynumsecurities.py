"""
FIX LiquidityNumSecurities field (tag 441).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LiquidityNumSecuritiesField(FIXFieldBase):
    """"""
    tag: str = "441"
    name: str = "LiquidityNumSecurities"
    type: str = "INT"
    value: int
