"""
FIX EncodedTextLen field (tag 354).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedTextLenField(FIXFieldBase):
    """"""
    tag: str = "354"
    name: str = "EncodedTextLen"
    type: str = "LENGTH"
    value: int
