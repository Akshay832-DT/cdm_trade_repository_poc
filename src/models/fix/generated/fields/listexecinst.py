"""
FIX ListExecInst field (tag 69).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListExecInstField(FIXFieldBase):
    """"""
    tag: str = "69"
    name: str = "ListExecInst"
    type: str = "STRING"
    value: str
