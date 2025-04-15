"""
FIX EventPx field (tag 867).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EventPxField(FIXFieldBase):
    """"""
    tag: str = "867"
    name: str = "EventPx"
    type: str = "PRICE"
    value: float
