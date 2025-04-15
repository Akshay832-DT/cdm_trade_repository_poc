"""
FIX SettlPartyIDSource field (tag 783).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlPartyIDSourceField(FIXFieldBase):
    """"""
    tag: str = "783"
    name: str = "SettlPartyIDSource"
    type: str = "CHAR"
    value: str
