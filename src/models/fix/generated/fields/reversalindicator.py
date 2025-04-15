"""
FIX ReversalIndicator field (tag 700).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ReversalIndicatorField(FIXFieldBase):
    """"""
    tag: str = "700"
    name: str = "ReversalIndicator"
    type: str = "BOOLEAN"
    value: bool
