"""
FIX ListID field (tag 66).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListIDField(FIXFieldBase):
    """"""
    tag: str = "66"
    name: str = "ListID"
    type: str = "STRING"
    value: str
