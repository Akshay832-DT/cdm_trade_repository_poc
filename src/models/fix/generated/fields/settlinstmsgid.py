"""
FIX SettlInstMsgID field (tag 777).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstMsgIDField(FIXFieldBase):
    """"""
    tag: str = "777"
    name: str = "SettlInstMsgID"
    type: str = "STRING"
    value: str
