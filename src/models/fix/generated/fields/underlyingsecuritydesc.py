"""
FIX UnderlyingSecurityDesc field (tag 307).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecurityDescField(FIXFieldBase):
    """"""
    tag: str = "307"
    name: str = "UnderlyingSecurityDesc"
    type: str = "STRING"
    value: str
