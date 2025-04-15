"""
FIX CollRptID field (tag 908).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollRptIDField(FIXFieldBase):
    """"""
    tag: str = "908"
    name: str = "CollRptID"
    type: str = "STRING"
    value: str
