"""
FIX TargetCompID field (tag 56).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TargetCompIDField(FIXFieldBase):
    """"""
    tag: str = "56"
    name: str = "TargetCompID"
    type: str = "STRING"
    value: str
