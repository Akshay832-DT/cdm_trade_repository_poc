"""
FIX EncodedAllocText field (tag 361).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedAllocTextField(FIXFieldBase):
    """"""
    tag: str = "361"
    name: str = "EncodedAllocText"
    type: str = "DATA"
    value: str
