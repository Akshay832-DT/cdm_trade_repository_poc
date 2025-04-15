"""
FIX Nested3PartySubIDType field (tag 954).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested3PartySubIDTypeField(FIXFieldBase):
    """"""
    tag: str = "954"
    name: str = "Nested3PartySubIDType"
    type: str = "INT"
    value: int
