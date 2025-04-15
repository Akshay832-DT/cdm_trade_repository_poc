"""
FIX EncodedListExecInstLen field (tag 352).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedListExecInstLenField(FIXFieldBase):
    """"""
    tag: str = "352"
    name: str = "EncodedListExecInstLen"
    type: str = "LENGTH"
    value: int
