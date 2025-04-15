"""
FIX NoPartyIDs field (tag 453).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoPartyIDsField(FIXFieldBase):
    """"""
    tag: str = "453"
    name: str = "NoPartyIDs"
    type: str = "NUMINGROUP"
    value: int
