"""
FIX SecondaryClOrdID field (tag 526).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecondaryClOrdIDField(FIXFieldBase):
    """"""
    tag: str = "526"
    name: str = "SecondaryClOrdID"
    type: str = "STRING"
    value: str
