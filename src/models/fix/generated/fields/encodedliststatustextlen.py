"""
FIX EncodedListStatusTextLen field (tag 445).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedListStatusTextLenField(FIXFieldBase):
    """"""
    tag: str = "445"
    name: str = "EncodedListStatusTextLen"
    type: str = "LENGTH"
    value: int
