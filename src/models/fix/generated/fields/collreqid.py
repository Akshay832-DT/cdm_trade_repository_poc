"""
FIX CollReqID field (tag 894).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollReqIDField(FIXFieldBase):
    """"""
    tag: str = "894"
    name: str = "CollReqID"
    type: str = "STRING"
    value: str
