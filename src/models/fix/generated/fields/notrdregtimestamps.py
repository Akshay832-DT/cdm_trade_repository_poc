"""
FIX NoTrdRegTimestamps field (tag 768).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoTrdRegTimestampsField(FIXFieldBase):
    """"""
    tag: str = "768"
    name: str = "NoTrdRegTimestamps"
    type: str = "NUMINGROUP"
    value: int
