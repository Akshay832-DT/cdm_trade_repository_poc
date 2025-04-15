"""
FIX Nested2PartySubIDType field (tag 807).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested2PartySubIDTypeField(FIXFieldBase):
    """"""
    tag: str = "807"
    name: str = "Nested2PartySubIDType"
    type: str = "INT"
    value: int
