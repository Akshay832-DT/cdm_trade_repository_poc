"""
FIX Nested3PartyRole field (tag 951).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested3PartyRoleField(FIXFieldBase):
    """"""
    tag: str = "951"
    name: str = "Nested3PartyRole"
    type: str = "INT"
    value: int
