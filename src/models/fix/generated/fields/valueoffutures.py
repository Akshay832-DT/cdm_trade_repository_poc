"""
FIX ValueOfFutures field (tag 408).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ValueOfFuturesField(FIXFieldBase):
    """"""
    tag: str = "408"
    name: str = "ValueOfFutures"
    type: str = "AMT"
    value: float
