"""
FIX AllocAccount field (tag 79).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocAccountField(FIXFieldBase):
    """"""
    tag: str = "79"
    name: str = "AllocAccount"
    type: str = "STRING"
    value: str
