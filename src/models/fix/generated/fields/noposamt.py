"""
FIX NoPosAmt field (tag 753).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoPosAmtField(FIXFieldBase):
    """"""
    tag: str = "753"
    name: str = "NoPosAmt"
    type: str = "NUMINGROUP"
    value: int
