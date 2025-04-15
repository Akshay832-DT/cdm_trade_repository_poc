"""
FIX SharedCommission field (tag 858).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SharedCommissionField(FIXFieldBase):
    """"""
    tag: str = "858"
    name: str = "SharedCommission"
    type: str = "AMT"
    value: float
