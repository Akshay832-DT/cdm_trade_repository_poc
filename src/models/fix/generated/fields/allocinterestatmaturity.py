"""
FIX AllocInterestAtMaturity field (tag 741).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocInterestAtMaturityField(FIXFieldBase):
    """"""
    tag: str = "741"
    name: str = "AllocInterestAtMaturity"
    type: str = "AMT"
    value: float
