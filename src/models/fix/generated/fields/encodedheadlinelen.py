"""
FIX EncodedHeadlineLen field (tag 358).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedHeadlineLenField(FIXFieldBase):
    """"""
    tag: str = "358"
    name: str = "EncodedHeadlineLen"
    type: str = "LENGTH"
    value: int
