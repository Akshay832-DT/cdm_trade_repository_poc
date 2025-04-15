"""
FIX SecureDataLen field (tag 90).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecureDataLenField(FIXFieldBase):
    """"""
    tag: str = "90"
    name: str = "SecureDataLen"
    type: str = "LENGTH"
    value: int
