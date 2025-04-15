"""
FIX NoNested3PartySubIDs field (tag 952).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoNested3PartySubIDsField(FIXFieldBase):
    """"""
    tag: str = "952"
    name: str = "NoNested3PartySubIDs"
    type: str = "NUMINGROUP"
    value: int
