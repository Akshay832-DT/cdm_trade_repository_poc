"""
FIX TotalTakedown field (tag 237).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotalTakedownField(FIXFieldBase):
    """"""
    tag: str = "237"
    name: str = "TotalTakedown"
    type: str = "AMT"
    value: float
