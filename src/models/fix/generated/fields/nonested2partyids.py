"""
FIX NoNested2PartyIDs field (tag 756).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoNested2PartyIDsField(FIXFieldBase):
    """"""
    tag: str = "756"
    name: str = "NoNested2PartyIDs"
    type: str = "NUMINGROUP"
    value: int
