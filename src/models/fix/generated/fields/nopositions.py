"""
FIX NoPositions field (tag 702).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoPositionsField(FIXFieldBase):
    """"""
    tag: str = "702"
    name: str = "NoPositions"
    type: str = "NUMINGROUP"
    value: int
