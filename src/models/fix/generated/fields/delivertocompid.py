"""
FIX DeliverToCompID field (tag 128).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeliverToCompIDField(FIXFieldBase):
    """"""
    tag: str = "128"
    name: str = "DeliverToCompID"
    type: str = "STRING"
    value: str
