"""
FIX UnderlyingSymbol field (tag 311).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSymbolField(FIXFieldBase):
    """"""
    tag: str = "311"
    name: str = "UnderlyingSymbol"
    type: str = "STRING"
    value: str
