"""
FIX UnderlyingSecurityType field (tag 310).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecurityTypeField(FIXFieldBase):
    """"""
    tag: str = "310"
    name: str = "UnderlyingSecurityType"
    type: str = "STRING"
    value: str
