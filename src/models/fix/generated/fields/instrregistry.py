"""
FIX InstrRegistry field (tag 543).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class InstrRegistryField(FIXFieldBase):
    """"""
    tag: str = "543"
    name: str = "InstrRegistry"
    type: str = "STRING"
    value: str
