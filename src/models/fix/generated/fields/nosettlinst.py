"""
FIX NoSettlInst field (tag 778).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoSettlInstField(FIXFieldBase):
    """"""
    tag: str = "778"
    name: str = "NoSettlInst"
    type: str = "NUMINGROUP"
    value: int
