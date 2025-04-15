"""
FIX ExecValuationPoint field (tag 515).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExecValuationPointField(FIXFieldBase):
    """"""
    tag: str = "515"
    name: str = "ExecValuationPoint"
    type: str = "UTCTIMESTAMP"
    value: datetime
