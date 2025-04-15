"""
FIX UnderlyingSecurityID field (tag 309).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecurityIDField(FIXFieldBase):
    """"""
    tag: str = "309"
    name: str = "UnderlyingSecurityID"
    type: str = "STRING"
    value: str
