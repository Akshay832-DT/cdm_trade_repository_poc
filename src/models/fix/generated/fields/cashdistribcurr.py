"""
FIX CashDistribCurr field (tag 478).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashDistribCurrField(FIXFieldBase):
    """"""
    tag: str = "478"
    name: str = "CashDistribCurr"
    type: str = "CURRENCY"
    value: str
