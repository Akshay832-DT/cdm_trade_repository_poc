"""
FIX NestedPartySubID field (tag 545).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NestedPartySubIDField(FIXFieldBase):
    """"""
    tag: str = "545"
    name: str = "NestedPartySubID"
    type: str = "STRING"
    value: str
