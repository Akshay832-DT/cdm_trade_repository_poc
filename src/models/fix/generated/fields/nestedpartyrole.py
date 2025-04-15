"""
FIX NestedPartyRole field (tag 538).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NestedPartyRoleField(FIXFieldBase):
    """"""
    tag: str = "538"
    name: str = "NestedPartyRole"
    type: str = "INT"
    value: int
