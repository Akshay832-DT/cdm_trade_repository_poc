"""
FIX NoNestedPartySubIDs field (tag 804).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoNestedPartySubIDsField(FIXFieldBase):
    """"""
    tag: str = "804"
    name: str = "NoNestedPartySubIDs"
    type: str = "NUMINGROUP"
    value: int
