"""
FIX SecureData field (tag 91).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecureDataField(FIXFieldBase):
    """"""
    tag: str = "91"
    name: str = "SecureData"
    type: str = "DATA"
    value: str
