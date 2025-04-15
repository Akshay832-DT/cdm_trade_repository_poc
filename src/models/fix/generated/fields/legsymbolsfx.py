"""
FIX LegSymbolSfx field (tag 601).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSymbolSfxField(FIXFieldBase):
    """"""
    tag: str = "601"
    name: str = "LegSymbolSfx"
    type: str = "STRING"
    value: str
