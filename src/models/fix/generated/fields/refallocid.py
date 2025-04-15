"""
FIX RefAllocID field (tag 72).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RefAllocIDField(FIXFieldBase):
    """"""
    tag: str = "72"
    name: str = "RefAllocID"
    type: str = "STRING"
    value: str
