"""
FIX MidYield field (tag 633).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MidYieldField(FIXFieldBase):
    """"""
    tag: str = "633"
    name: str = "MidYield"
    type: str = "PERCENTAGE"
    value: float
