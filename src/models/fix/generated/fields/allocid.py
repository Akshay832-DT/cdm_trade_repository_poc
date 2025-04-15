"""
FIX AllocID field (tag 70).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocIDField(FIXFieldBase):
    """"""
    tag: str = "70"
    name: str = "AllocID"
    type: str = "STRING"
    value: str
