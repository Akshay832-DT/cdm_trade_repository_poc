"""
FIX MDEntryTime field (tag 273).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryTimeField(FIXFieldBase):
    """"""
    tag: str = "273"
    name: str = "MDEntryTime"
    type: str = "UTCTIMEONLY"
    value: time
