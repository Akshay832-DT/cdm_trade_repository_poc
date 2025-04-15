"""
FIX SettlPartyID field (tag 782).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlPartyIDField(FIXFieldBase):
    """"""
    tag: str = "782"
    name: str = "SettlPartyID"
    type: str = "STRING"
    value: str
