"""
FIX SettlInstID field (tag 162).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstIDField(FIXFieldBase):
    """"""
    tag: str = "162"
    name: str = "SettlInstID"
    type: str = "STRING"
    value: str
