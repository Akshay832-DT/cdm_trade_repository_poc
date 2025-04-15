"""
FIX CollAsgnID field (tag 902).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollAsgnIDField(FIXFieldBase):
    """"""
    tag: str = "902"
    name: str = "CollAsgnID"
    type: str = "STRING"
    value: str
