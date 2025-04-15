"""
FIX MidPx field (tag 631).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MidPxField(FIXFieldBase):
    """"""
    tag: str = "631"
    name: str = "MidPx"
    type: str = "PRICE"
    value: float
