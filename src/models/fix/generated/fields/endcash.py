"""
FIX EndCash field (tag 922).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EndCashField(FIXFieldBase):
    """"""
    tag: str = "922"
    name: str = "EndCash"
    type: str = "AMT"
    value: float
