"""
FIX SettlSessSubID field (tag 717).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlSessSubIDField(FIXFieldBase):
    """"""
    tag: str = "717"
    name: str = "SettlSessSubID"
    type: str = "STRING"
    value: str
