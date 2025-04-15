"""
FIX BeginString field (tag 8).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BeginStringField(FIXFieldBase):
    """"""
    tag: str = "8"
    name: str = "BeginString"
    type: str = "STRING"
    value: str
