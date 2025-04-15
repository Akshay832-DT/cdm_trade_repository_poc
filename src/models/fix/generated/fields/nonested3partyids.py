"""
FIX NoNested3PartyIDs field (tag 948).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoNested3PartyIDsField(FIXFieldBase):
    """"""
    tag: str = "948"
    name: str = "NoNested3PartyIDs"
    type: str = "NUMINGROUP"
    value: int
