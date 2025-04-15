"""
FIX CashDistribPayRef field (tag 501).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashDistribPayRefField(FIXFieldBase):
    """"""
    tag: str = "501"
    name: str = "CashDistribPayRef"
    type: str = "STRING"
    value: str
