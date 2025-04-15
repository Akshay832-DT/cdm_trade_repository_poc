"""
FIX Nested2PartyID field (tag 757).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested2PartyIDField(FIXFieldBase):
    """"""
    tag: str = "757"
    name: str = "Nested2PartyID"
    type: str = "STRING"
    value: str
