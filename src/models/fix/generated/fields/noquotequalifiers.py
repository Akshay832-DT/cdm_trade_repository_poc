"""
FIX NoQuoteQualifiers field (tag 735).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoQuoteQualifiersField(FIXFieldBase):
    """"""
    tag: str = "735"
    name: str = "NoQuoteQualifiers"
    type: str = "NUMINGROUP"
    value: int
