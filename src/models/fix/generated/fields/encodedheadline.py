"""
FIX EncodedHeadline field (tag 359).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedHeadlineField(FIXFieldBase):
    """"""
    tag: str = "359"
    name: str = "EncodedHeadline"
    type: str = "DATA"
    value: str
