"""
FIX AllocNetMoney field (tag 154).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocNetMoneyField(FIXFieldBase):
    """"""
    tag: str = "154"
    name: str = "AllocNetMoney"
    type: str = "AMT"
    value: float
