"""
FIX EncodedSubjectLen field (tag 356).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedSubjectLenField(FIXFieldBase):
    """"""
    tag: str = "356"
    name: str = "EncodedSubjectLen"
    type: str = "LENGTH"
    value: int
