"""
FIX TradeLegRefID field (tag 824).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradeLegRefIDField(FIXFieldBase):
    """"""
    tag: str = "824"
    name: str = "TradeLegRefID"
    type: str = "STRING"
    value: str
