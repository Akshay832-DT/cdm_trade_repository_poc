"""
FIX AllocLinkID field (tag 196).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocLinkIDField(FIXFieldBase):
    """"""
    tag: str = "196"
    name: str = "AllocLinkID"
    type: str = "STRING"
    value: str
