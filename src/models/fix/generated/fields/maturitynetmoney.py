"""
FIX MaturityNetMoney field (tag 890).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MaturityNetMoneyField(FIXFieldBase):
    """"""
    tag: str = "890"
    name: str = "MaturityNetMoney"
    type: str = "AMT"
    value: float
