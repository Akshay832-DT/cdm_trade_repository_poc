"""
FIX QuoteQualifier field (tag 695).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteQualifierField(FIXFieldBase):
    """"""
    tag: str = "695"
    name: str = "QuoteQualifier"
    type: str = "CHAR"
    value: str
