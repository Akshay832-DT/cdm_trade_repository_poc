"""
FIX NetMoney field (tag 118).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NetMoneyField(FIXFieldBase):
    """"""
    tag: str = "118"
    name: str = "NetMoney"
    type: str = "AMT"
    value: float
