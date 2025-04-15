"""
FIX NestedPartySubIDType field (tag 805).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NestedPartySubIDTypeField(FIXFieldBase):
    """"""
    tag: str = "805"
    name: str = "NestedPartySubIDType"
    type: str = "INT"
    value: int
