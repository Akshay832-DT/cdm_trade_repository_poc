"""
FIX SettlInstReqID field (tag 791).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstReqIDField(FIXFieldBase):
    """"""
    tag: str = "791"
    name: str = "SettlInstReqID"
    type: str = "STRING"
    value: str
