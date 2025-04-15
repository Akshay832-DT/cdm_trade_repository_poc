"""
FIX TotNoRelatedSym field (tag 393).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TotNoRelatedSymField(FIXFieldBase):
    """"""
    tag: str = "393"
    name: str = "TotNoRelatedSym"
    type: str = "INT"
    value: int
