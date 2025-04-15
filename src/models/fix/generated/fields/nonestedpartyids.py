"""
FIX NoNestedPartyIDs field (tag 539).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoNestedPartyIDsField(FIXFieldBase):
    """"""
    tag: str = "539"
    name: str = "NoNestedPartyIDs"
    type: str = "NUMINGROUP"
    value: int
