"""
FIX NestedPartyIDSource field (tag 525).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NestedPartyIDSourceField(FIXFieldBase):
    """"""
    tag: str = "525"
    name: str = "NestedPartyIDSource"
    type: str = "CHAR"
    value: str
