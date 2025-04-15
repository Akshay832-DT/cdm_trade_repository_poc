"""
FIX Nested3PartyIDSource field (tag 950).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested3PartyIDSourceField(FIXFieldBase):
    """"""
    tag: str = "950"
    name: str = "Nested3PartyIDSource"
    type: str = "CHAR"
    value: str
