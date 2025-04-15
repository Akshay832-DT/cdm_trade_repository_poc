"""
FIX CashOutstanding field (tag 901).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashOutstandingField(FIXFieldBase):
    """"""
    tag: str = "901"
    name: str = "CashOutstanding"
    type: str = "AMT"
    value: float
