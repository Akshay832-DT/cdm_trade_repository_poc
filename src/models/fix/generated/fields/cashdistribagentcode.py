"""
FIX CashDistribAgentCode field (tag 499).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashDistribAgentCodeField(FIXFieldBase):
    """"""
    tag: str = "499"
    name: str = "CashDistribAgentCode"
    type: str = "STRING"
    value: str
