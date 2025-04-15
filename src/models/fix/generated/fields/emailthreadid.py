"""
FIX EmailThreadID field (tag 164).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EmailThreadIDField(FIXFieldBase):
    """"""
    tag: str = "164"
    name: str = "EmailThreadID"
    type: str = "STRING"
    value: str
