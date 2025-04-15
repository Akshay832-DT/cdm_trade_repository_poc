"""
FIX NoLegs field (tag 555).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoLegsField(FIXFieldBase):
    """"""
    tag: str = "555"
    name: str = "NoLegs"
    type: str = "NUMINGROUP"
    value: int
