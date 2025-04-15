"""
FIX UnderlyingSymbolSfx field (tag 312).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSymbolSfxField(FIXFieldBase):
    """"""
    tag: str = "312"
    name: str = "UnderlyingSymbolSfx"
    type: str = "STRING"
    value: str
