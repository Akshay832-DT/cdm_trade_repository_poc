"""
FIX Nested3PartySubID field (tag 953).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class Nested3PartySubIDField(FIXFieldBase):
    """"""
    tag: str = "953"
    name: str = "Nested3PartySubID"
    type: str = "STRING"
    value: str
