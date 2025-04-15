"""
FIX UnderlyingInstrRegistry field (tag 595).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingInstrRegistryField(FIXFieldBase):
    """"""
    tag: str = "595"
    name: str = "UnderlyingInstrRegistry"
    type: str = "STRING"
    value: str
