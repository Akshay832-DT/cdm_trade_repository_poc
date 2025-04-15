"""
FIX NoContAmts field (tag 518).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoContAmtsField(FIXFieldBase):
    """"""
    tag: str = "518"
    name: str = "NoContAmts"
    type: str = "NUMINGROUP"
    value: int
