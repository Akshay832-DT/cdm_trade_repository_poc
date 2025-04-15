"""
FIX NoSettlPartyIDs field (tag 781).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoSettlPartyIDsField(FIXFieldBase):
    """"""
    tag: str = "781"
    name: str = "NoSettlPartyIDs"
    type: str = "NUMINGROUP"
    value: int
