"""
FIX EncodedAllocTextLen field (tag 360).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedAllocTextLenField(FIXFieldBase):
    """"""
    tag: str = "360"
    name: str = "EncodedAllocTextLen"
    type: str = "LENGTH"
    value: int
