"""
FIX TotNoStrikes field (tag 422).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNoStrikesField(FIXFieldBase):
    """"""
    tag: str = "422"
    name: str = "TotNoStrikes"
    type: str = "INT"
    value: int
