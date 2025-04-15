"""
FIX SettlInstRefID field (tag 214).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlInstRefIDField(FIXFieldBase):
    """"""
    tag: str = "214"
    name: str = "SettlInstRefID"
    type: str = "STRING"
    value: str
