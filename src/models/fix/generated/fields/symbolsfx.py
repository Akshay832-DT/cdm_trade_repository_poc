"""
FIX SymbolSfx field (tag 65).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SymbolSfxField(FIXFieldBase):
    """"""
    tag: str = "65"
    name: str = "SymbolSfx"
    type: str = "STRING"
    value: str
