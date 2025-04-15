"""
FIX Yield field (tag 236).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class YieldField(FIXFieldBase):
    """"""
    tag: str = "236"
    name: str = "Yield"
    type: str = "PERCENTAGE"
    value: float
