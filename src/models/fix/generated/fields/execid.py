"""
FIX ExecID field (tag 17).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecIDField(FIXFieldBase):
    """"""
    tag: str = "17"
    name: str = "ExecID"
    type: str = "STRING"
    value: str
