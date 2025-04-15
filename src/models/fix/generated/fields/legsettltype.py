"""
FIX LegSettlType field (tag 587).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSettlTypeField(FIXFieldBase):
    """"""
    tag: str = "587"
    name: str = "LegSettlType"
    type: str = "CHAR"
    value: str
