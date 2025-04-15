"""
FIX LegSymbol field (tag 600).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSymbolField(FIXFieldBase):
    """"""
    tag: str = "600"
    name: str = "LegSymbol"
    type: str = "STRING"
    value: str
