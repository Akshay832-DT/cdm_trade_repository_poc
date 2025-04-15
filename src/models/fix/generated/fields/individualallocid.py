"""
FIX IndividualAllocID field (tag 467).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IndividualAllocIDField(FIXFieldBase):
    """"""
    tag: str = "467"
    name: str = "IndividualAllocID"
    type: str = "STRING"
    value: str
