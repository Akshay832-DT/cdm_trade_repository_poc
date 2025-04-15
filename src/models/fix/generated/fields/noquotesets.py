"""
FIX NoQuoteSets field (tag 296).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoQuoteSetsField(FIXFieldBase):
    """"""
    tag: str = "296"
    name: str = "NoQuoteSets"
    type: str = "NUMINGROUP"
    value: int
