"""
FIX NoRoutingIDs field (tag 215).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoRoutingIDsField(FIXFieldBase):
    """"""
    tag: str = "215"
    name: str = "NoRoutingIDs"
    type: str = "NUMINGROUP"
    value: int
