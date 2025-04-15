"""
FIX UnderlyingSecuritySubType field (tag 763).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecuritySubTypeField(FIXFieldBase):
    """"""
    tag: str = "763"
    name: str = "UnderlyingSecuritySubType"
    type: str = "STRING"
    value: str
