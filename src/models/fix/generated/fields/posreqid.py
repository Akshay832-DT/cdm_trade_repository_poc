"""
FIX PosReqID field (tag 710).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosReqIDField(FIXFieldBase):
    """"""
    tag: str = "710"
    name: str = "PosReqID"
    type: str = "STRING"
    value: str
