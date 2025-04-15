"""
FIX Nested2PartySubID field (tag 760).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested2PartySubIDField(FIXFieldBase):
    """"""
    tag: str = "760"
    name: str = "Nested2PartySubID"
    type: str = "STRING"
    value: str
