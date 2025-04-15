"""
FIX RefTagID field (tag 371).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RefTagIDField(FIXFieldBase):
    """"""
    tag: str = "371"
    name: str = "RefTagID"
    type: str = "INT"
    value: int
