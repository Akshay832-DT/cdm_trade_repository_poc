"""
FIX NestedPartyID field (tag 524).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NestedPartyIDField(FIXFieldBase):
    """"""
    tag: str = "524"
    name: str = "NestedPartyID"
    type: str = "STRING"
    value: str
