"""
FIX NoRelatedSym field (tag 146).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoRelatedSymField(FIXFieldBase):
    """"""
    tag: str = "146"
    name: str = "NoRelatedSym"
    type: str = "NUMINGROUP"
    value: int
