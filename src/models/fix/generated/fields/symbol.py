"""
FIX Symbol field (tag 55).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SymbolField(FIXFieldBase):
    """"""
    tag: str = "55"
    name: str = "Symbol"
    type: str = "STRING"
    value: str
