"""
FIX LastRptRequested field (tag 912).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastRptRequestedField(FIXFieldBase):
    """"""
    tag: str = "912"
    name: str = "LastRptRequested"
    type: str = "BOOLEAN"
    value: bool
