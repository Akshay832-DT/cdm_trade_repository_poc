"""
FIX MDEntryRefID field (tag 280).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryRefIDField(FIXFieldBase):
    """"""
    tag: str = "280"
    name: str = "MDEntryRefID"
    type: str = "STRING"
    value: str
