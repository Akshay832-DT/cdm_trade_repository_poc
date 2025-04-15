"""
FIX NoMDEntryTypes field (tag 267).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoMDEntryTypesField(FIXFieldBase):
    """"""
    tag: str = "267"
    name: str = "NoMDEntryTypes"
    type: str = "NUMINGROUP"
    value: int
