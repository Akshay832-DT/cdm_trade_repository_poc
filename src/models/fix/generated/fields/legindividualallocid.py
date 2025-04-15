"""
FIX LegIndividualAllocID field (tag 672).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegIndividualAllocIDField(FIXFieldBase):
    """"""
    tag: str = "672"
    name: str = "LegIndividualAllocID"
    type: str = "STRING"
    value: str
