"""
FIX Nested2PartyRole field (tag 759).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested2PartyRoleField(FIXFieldBase):
    """"""
    tag: str = "759"
    name: str = "Nested2PartyRole"
    type: str = "INT"
    value: int
