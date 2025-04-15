"""
FIX DeskID field (tag 284).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeskIDField(FIXFieldBase):
    """"""
    tag: str = "284"
    name: str = "DeskID"
    type: str = "STRING"
    value: str
