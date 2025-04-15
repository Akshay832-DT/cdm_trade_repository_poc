"""
FIX ExpireDate field (tag 432).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExpireDateField(FIXFieldBase):
    """"""
    tag: str = "432"
    name: str = "ExpireDate"
    type: str = "LOCALMKTDATE"
    value: date
