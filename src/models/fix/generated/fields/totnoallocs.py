"""
FIX TotNoAllocs field (tag 892).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNoAllocsField(FIXFieldBase):
    """"""
    tag: str = "892"
    name: str = "TotNoAllocs"
    type: str = "INT"
    value: int
