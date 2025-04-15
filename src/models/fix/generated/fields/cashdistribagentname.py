"""
FIX CashDistribAgentName field (tag 498).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CashDistribAgentNameField(FIXFieldBase):
    """"""
    tag: str = "498"
    name: str = "CashDistribAgentName"
    type: str = "STRING"
    value: str
