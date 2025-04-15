"""
FIX CashDistribAgentAcctName field (tag 502).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashDistribAgentAcctNameField(FIXFieldBase):
    """"""
    tag: str = "502"
    name: str = "CashDistribAgentAcctName"
    type: str = "STRING"
    value: str
