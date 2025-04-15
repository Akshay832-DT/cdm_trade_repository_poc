"""
FIX NoEvents field (tag 864).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoEventsField(FIXFieldBase):
    """"""
    tag: str = "864"
    name: str = "NoEvents"
    type: str = "NUMINGROUP"
    value: int
