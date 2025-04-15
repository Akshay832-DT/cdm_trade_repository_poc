"""
FIX CashDistribAgentAcctNumber field (tag 500).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashDistribAgentAcctNumberField(FIXFieldBase):
    """"""
    tag: str = "500"
    name: str = "CashDistribAgentAcctNumber"
    type: str = "STRING"
    value: str
