"""
FIX BodyLength field (tag 9).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BodyLengthField(FIXFieldBase):
    """"""
    tag: str = "9"
    name: str = "BodyLength"
    type: str = "LENGTH"
    value: int
