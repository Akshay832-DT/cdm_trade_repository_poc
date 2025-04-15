"""
FIX SideValue2 field (tag 397).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SideValue2Field(FIXFieldBase):
    """"""
    tag: str = "397"
    name: str = "SideValue2"
    type: str = "AMT"
    value: float
