"""
FIX SettlPartySubID field (tag 785).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlPartySubIDField(FIXFieldBase):
    """"""
    tag: str = "785"
    name: str = "SettlPartySubID"
    type: str = "STRING"
    value: str
