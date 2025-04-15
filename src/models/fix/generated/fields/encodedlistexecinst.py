"""
FIX EncodedListExecInst field (tag 353).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedListExecInstField(FIXFieldBase):
    """"""
    tag: str = "353"
    name: str = "EncodedListExecInst"
    type: str = "DATA"
    value: str
