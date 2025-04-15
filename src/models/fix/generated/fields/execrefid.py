"""
FIX ExecRefID field (tag 19).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecRefIDField(FIXFieldBase):
    """"""
    tag: str = "19"
    name: str = "ExecRefID"
    type: str = "STRING"
    value: str
