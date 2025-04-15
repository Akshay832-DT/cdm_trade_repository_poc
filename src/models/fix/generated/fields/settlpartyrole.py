"""
FIX SettlPartyRole field (tag 784).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlPartyRoleField(FIXFieldBase):
    """"""
    tag: str = "784"
    name: str = "SettlPartyRole"
    type: str = "INT"
    value: int
