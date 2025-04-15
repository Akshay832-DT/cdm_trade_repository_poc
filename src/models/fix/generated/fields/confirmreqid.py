"""
FIX ConfirmReqID field (tag 859).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConfirmReqIDField(FIXFieldBase):
    """"""
    tag: str = "859"
    name: str = "ConfirmReqID"
    type: str = "STRING"
    value: str
