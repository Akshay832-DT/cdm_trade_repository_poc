"""
FIX RegistID field (tag 513).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistIDField(FIXFieldBase):
    """"""
    tag: str = "513"
    name: str = "RegistID"
    type: str = "STRING"
    value: str
