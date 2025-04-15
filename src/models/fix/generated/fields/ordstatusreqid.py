"""
FIX OrdStatusReqID field (tag 790).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrdStatusReqIDField(FIXFieldBase):
    """"""
    tag: str = "790"
    name: str = "OrdStatusReqID"
    type: str = "STRING"
    value: str
