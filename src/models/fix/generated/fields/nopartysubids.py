"""
FIX NoPartySubIDs field (tag 802).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoPartySubIDsField(FIXFieldBase):
    """"""
    tag: str = "802"
    name: str = "NoPartySubIDs"
    type: str = "NUMINGROUP"
    value: int
