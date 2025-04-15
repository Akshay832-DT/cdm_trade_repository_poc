"""
FIX LegInstrRegistry field (tag 599).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegInstrRegistryField(FIXFieldBase):
    """"""
    tag: str = "599"
    name: str = "LegInstrRegistry"
    type: str = "STRING"
    value: str
