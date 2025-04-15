"""
FIX Nested2PartyIDSource field (tag 758).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested2PartyIDSourceField(FIXFieldBase):
    """"""
    tag: str = "758"
    name: str = "Nested2PartyIDSource"
    type: str = "CHAR"
    value: str
