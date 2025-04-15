"""
FIX NoNested2PartySubIDs field (tag 806).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoNested2PartySubIDsField(FIXFieldBase):
    """"""
    tag: str = "806"
    name: str = "NoNested2PartySubIDs"
    type: str = "NUMINGROUP"
    value: int
