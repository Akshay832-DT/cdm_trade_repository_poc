"""
FIX CheckSum field (tag 10).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CheckSumField(FIXFieldBase):
    """"""
    tag: str = "10"
    name: str = "CheckSum"
    type: str = "STRING"
    value: str
