"""
FIX MDEntryOriginator field (tag 282).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryOriginatorField(FIXFieldBase):
    """"""
    tag: str = "282"
    name: str = "MDEntryOriginator"
    type: str = "STRING"
    value: str
