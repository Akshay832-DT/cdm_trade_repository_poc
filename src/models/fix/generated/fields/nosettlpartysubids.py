"""
FIX NoSettlPartySubIDs field (tag 801).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoSettlPartySubIDsField(FIXFieldBase):
    """"""
    tag: str = "801"
    name: str = "NoSettlPartySubIDs"
    type: str = "NUMINGROUP"
    value: int
