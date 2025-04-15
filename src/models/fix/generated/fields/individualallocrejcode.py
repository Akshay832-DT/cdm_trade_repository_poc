"""
FIX IndividualAllocRejCode field (tag 776).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IndividualAllocRejCodeField(FIXFieldBase):
    """"""
    tag: str = "776"
    name: str = "IndividualAllocRejCode"
    type: str = "INT"
    value: int
