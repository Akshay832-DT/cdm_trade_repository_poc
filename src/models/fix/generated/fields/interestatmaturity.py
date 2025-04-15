"""
FIX InterestAtMaturity field (tag 738).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class InterestAtMaturityField(FIXFieldBase):
    """"""
    tag: str = "738"
    name: str = "InterestAtMaturity"
    type: str = "AMT"
    value: float
