"""
FIX Nested3PartyID field (tag 949).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested3PartyIDField(FIXFieldBase):
    """"""
    tag: str = "949"
    name: str = "Nested3PartyID"
    type: str = "STRING"
    value: str
