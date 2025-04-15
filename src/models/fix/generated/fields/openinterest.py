"""
FIX OpenInterest field (tag 746).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OpenInterestField(FIXFieldBase):
    """"""
    tag: str = "746"
    name: str = "OpenInterest"
    type: str = "AMT"
    value: float
