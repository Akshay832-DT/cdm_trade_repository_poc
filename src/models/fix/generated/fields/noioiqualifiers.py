"""
FIX NoIOIQualifiers field (tag 199).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoIOIQualifiersField(FIXFieldBase):
    """"""
    tag: str = "199"
    name: str = "NoIOIQualifiers"
    type: str = "NUMINGROUP"
    value: int
