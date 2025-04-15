"""
FIX SideValue1 field (tag 396).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SideValue1Field(FIXFieldBase):
    """"""
    tag: str = "396"
    name: str = "SideValue1"
    type: str = "AMT"
    value: float
